# CPC Emulator: Minimal Python POC Design

## Goal

Build a small, inspectable emulator that demonstrates the defining workflow
of the IBM Card-Programmed Electronic Calculator (CPC): an externally
configured control panel directs a decimal arithmetic unit, data moves through
numbered storage, and cards provide input and output.

This is a behavioral teaching model, not a cycle-accurate hardware
simulation. The design is grounded in two local sources:

- [*The IBM Card-Programmed Electronic Calculator* (1951)](cpc-overview.pdf),
  a short overview of the machine.
- [*Card-Programmed Electronic Calculator: Model A1 Using Machine Types
  412–418, 605, 527, and 941: Principles of Operation* (October 1954)](cpc-principles.pdf),
  a detailed operational manual.

The 1954 manual should be the primary reference for machine behavior; the
1951 article supplies historical context and an overview.

Useful starting points in the 1954 manual (printed page numbers):

| Pages | POC-relevant details |
|---|---|
| 11–12 | Card reading stages, machine-cycle sequence, component specifications |
| 17–20 | Control-panel roles and program-advance operation |
| 23–25 | Read-in/calculation/print example, program levels, and A/B/C exits |
| 29–35 | Basic arithmetic operations, selector behavior, multiply and divide |
| 40–48 | 941 register banks, register codes, read-in, read-out, and clear |

The manual has front matter, so its PDF page index differs from its printed
page numbers.

## What the source suggests the model should preserve

- **Separate control and data.** The arithmetic unit is configured by a
  plugboard control panel. The panel selects operations and their order; it
  is not a unified, addressable program-memory array like that of a modern
  stored-program computer.
- **Decimal arithmetic.** The machine works with signed decimal digits.
  Arithmetic capacity is wider than its ordinary storage values: the scan
  describes a 13-position counter and multiple smaller storage units.
- **Distinct storage and I/O paths.** The diagrams distinguish arithmetic
  storage, counters, card entry, printing, and punched-card output, connected
  by channels.
- **Sequencing is explicit.** Program steps can be repeated or selected by
  control wiring. The 605 has 60 program levels, with A, B, and C exits per
  level; program-pickup signals activate sets of exits. Input and output are
  operations in the machine's workflow, not implicit host-language reads
  and prints.
- **Cards pass through staged reads.** The 412 reads control/selector
  information at one station and data fields at another. The manual's
  example separates card feed, second and third readings, calculation,
  counter readout, and 941 readout across machine cycles. The POC can
  abstract physical feed timing while preserving these stages in its trace.
- **Storage is a separate machine.** A 941 contains 16 registers, each
  holding a signed 10-position number. Read-in and read-out are addressed by
  register code and use channels connecting the 941 and 412.
- **Arithmetic is wider than ordinary stored values.** The 605 counter has
  13 positions. The manual describes multiplication of an 8-position value
  by a 5-position value to produce a 13-position product, and division of a
  13-position dividend by an 8-position divisor to produce a 5-position
  quotient.
- **There are different speeds.** Card and electromechanical operations are
  much slower than the electronic arithmetic. The POC should expose this
  distinction conceptually, without trying to emulate physical timing.

The manuals describe substantially more hardware than this POC will model:
hundreds of panel hubs, specialized storage units, arithmetic timing
circuits, real card-feed interlocks, and auxiliary equipment. Those details
should not be mistaken for implemented behavior.

## POC boundary

### Include

1. Separate 412, 605, and 941 behavioral components.
2. Signed decimal values with distinct 605 counter and 941 register widths.
3. A separately defined control-panel configuration with program levels and
   A/B/C exits.
4. A machine-cycle loop that models card-reading stages, calculation, and
   result availability.
5. Explicit card input and output, initially represented by text records
   rather than physical punched-card images.
6. A trace that reports the machine cycle, card-read stage, active program
   level/exit, operation, affected component, and result.
7. Defined behavior for invalid control wiring, malformed card data,
   divide-by-zero, and arithmetic overflow.

### Defer

- Transistor, tube, relay, pulse, or real-time simulation.
- Graphical plugboard wiring.
- A faithful physical 80-column card layout and punched-hole encoding.
- Every operation or special-purpose circuit shown in the article.
- Auxiliary storage-unit models and parallel operation.
- Operating-system, assembler, or general-purpose programming-language
  compatibility.
- Claims of bit-for-bit or cycle-accurate equivalence to the historical
  machine.

## Proposed architecture

Keep the emulator split into a small number of parts:

| Part | Responsibility |
|---|---|
| `Machine` | Coordinate machine cycles and stop/error state |
| `CardUnit412` | Advance cards through abstract read stations and expose fields |
| `Calculator605` | Hold counter/factor state and perform decimal arithmetic |
| `Storage941` | Hold 16 individually addressed signed 10-position registers |
| `ControlPanel` | Map program-level exits and selectors to component actions |
| `CardUnit527` | Optionally collect summary-punch output |
| `Trace` | Emit a readable record of each cycle and state transition |

Keep configured panel wiring distinct from both the machine's data state and
the card data. This separation is the most important architectural
constraint in the POC.

### State model

```text
MachineState
  machine_cycle: integer
  active_program_level: integer
  active_exits: set of A/B/C
  card_position: reader stage
  calculator_counter: signed decimal value (up to 13 digit positions)
  factor_storage: named decimal values
  storage_941: 16 signed decimal registers (10 positions each)
  input_card_position: integer
  output_records: list of card/print records
  stopped: boolean
```

Use exact decimal arithmetic rather than binary floating-point. Represent
sign, decimal digits, and decimal-point position explicitly, or use Python's
`decimal.Decimal` with explicit precision and rounding rules. Do not infer
one universal fixed scale: the control-panel wiring and operation determine
where the decimal point is placed and how a result is adjusted. Keep those
rules in the operation configuration.

The 13-position counter and 16 ten-position 941 registers are documented
starting values for this machine profile. Other machine types and format
details should be configurable or marked as assumptions.

## Control-panel program representation

Represent a simplified panel setup as structured Python data, not as
executable Python source. Program levels and exits must remain separate from
the actions wired to them. For example:

```python
panel = {
    "program_levels": {
        1: {"A": [{"component": "605", "action": "read_factor", "source": "card.field_a"}]},
        2: {"A": [{"component": "605", "action": "multiply"}]},
        3: {"A": [{"component": "941", "action": "read_out", "register": 1}]},
    },
    "selectors": {
        "operation_code": {
            "X76": "multiply",
            "X78": "divide",
            "digit_1_column_80": "add",
            "digit_2_column_80": "subtract",
        }
    },
}
```

This is an abstract representation of the panel's connections, not a
transcription of physical sockets. A card code and selector configuration
can choose which operation a program exit triggers. Program-pickup signals
activate the relevant A/B/C exits. Do not present the configuration as a
modern instruction stream fetched from memory.

Initial panel actions:

| Action | Effect |
|---|---|
| `read_factor` | Transfer a selected card field into calculator factor storage |
| `read_in_941` | Store a selected value in a specified 941 register |
| `add` / `subtract` | Apply the selected factor to the 605 counter |
| `multiply` / `divide` | Perform the selected calculator operation |
| `counter_read_out` | Make a counter result available to printing, counting, or storage |
| `read_out_941` | Transfer a specified 941 register to an output channel |
| `print` | Format a result for a line printer |
| `summary_punch` | Queue a result for the 527 summary punch |
| `repeat` | Re-enable a configured set of program-level exits for a bounded repeat |
| `stop` | Stop the behavioral machine |

## Vertical slice

The first demonstration should process a card with two decimal factors,
multiply them, and write the result:

1. A card enters the 412 and passes through an abstract second-reading
   stage, where the configuration detects card-control fields.
2. At the third-reading stage, selected card fields are transferred to the
   605 factor storage.
3. The active 605 program level issues the configured multiply action.
4. The 605 produces a result in its counter; the trace marks it available
   for readout.
5. A later configured action reads the counter result and sends it to the
   printer output.
6. The trace shows each card stage, active exit, transfer, and calculation.

Then add a multi-card version with bounded program repeat and 941 register
read-in/read-out. This tests sequencing and storage channels without needing
a full card-image emulator.

## Observable execution

Provide a single entry point such as:

```sh
python3 cpc/run.py examples/multiply_cards.json examples/input.txt
```

The POC should print a concise trace to the terminal and write result records
to a specified output file. A trace line might show:

```text
cycle=4 stage=CALCULATE level=2 exit=A op=MULTIPLY counter=0000000000012
```

The exact formatting is a design choice; it should make decimal width,
operation order, and state changes easy to inspect.

## Error policy

Fail explicitly, with the current step and operation in the error message,
for:

- An unknown operation or register.
- Missing or malformed input records.
- Division by zero.
- A value that exceeds the selected digit capacity.
- A repeat range that is invalid or that would exceed a configured execution
  limit.

Do not silently coerce an invalid value to zero, continue after arithmetic
failure, or let a repeat loop run forever.

## Suggested Python file layout

```text
cpc/
    __init__.py
    machine.py
    calculator605.py
    control_panel.py
    card_unit412.py
    storage941.py
    card_unit527.py
    trace.py
    run.py
examples/
    multiply_cards.json
    input.txt
tests/
    test_calculator605.py
    test_control_panel.py
    test_card_unit412.py
    test_storage941.py
    test_machine.py
```

Keep this separate from `simplex/` and `sor/`: those are numerical examples,
while `cpc/` would be the machine-model POC.

## Test plan

1. Decimal add, subtract, multiply, and divide, including sign, decimal-point
   placement, rounding, and divide-by-zero.
2. The 605's 13-position counter and 941's 16 ten-position registers enforce
   their separate limits.
3. Program pickup activates only the wired A/B/C exits for a selected level.
4. A card field is not consumed until its configured reading stage.
5. The 605 calculation result becomes readable at its modeled result stage.
6. 941 read-in and read-out target only the selected register.
7. Bounded program repeat processes every card once and terminates.
8. Missing card fields, invalid wiring, and arithmetic overflow fail
   explicitly.
9. The vertical-slice example produces the expected result and a complete
   cycle trace.

## Implementation order

1. Define exact decimal values and the documented 605/941 digit limits.
2. Implement and test the 605 arithmetic operations and decimal adjustment.
3. Model the 412 card stages and field selection at a behavioral level.
4. Represent 605 program levels and A/B/C exits as separate control-panel
   wiring data.
5. Add addressed 941 storage and channel transfers.
6. Run the multiply-card vertical slice with a cycle-by-cycle trace.
7. Add bounded repeat, printer output, and optional summary-punch output.
8. Revisit details against the operating manual as more machine behaviors
   are added.

## Success criteria

The POC is successful if a reader can follow a small card-driven calculation
from card field selection through panel-controlled machine cycles to decimal
output, see state after each transition, and understand which historical
features are represented versus simplified.
