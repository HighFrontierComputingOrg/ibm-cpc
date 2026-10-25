# Repeated Complex Squaring

This example reproduces the values in [Feynman's Table 22-3](https://www.feynmanlectures.caltech.edu/I_22.html) using three implementations:

- [Python](algebra.py)
- [Fortran IV-style source](algebra.for)
- [TOPS-10 MACRO-10 source](algebra.mac)

The purpose is to compare the same numerical process across languages and
machine environments, and to observe how rounding and floating-point
precision affect repeated calculations.

## Mathematics

The calculation starts with a complex number close to `10^(i/1024)`, where
`i` is the imaginary unit. In polar form, the ideal value has angle
`theta = ln(10)/1024`, approximately `0.00224861825` radians.

### Starting value

Rather than calculate that ideal value directly, each program uses the
nearby approximation:

| Component | Value |
|---|---:|
| `y0` | `0.00225` |
| `x0` | `sqrt(1 - y0*y0)`, approximately `0.99999747` |
| `z0` | `x0 + i*y0` |

This makes `z0` lie on the unit circle, but its angle is approximately
`0.00225000190` radians—not exactly `ln(10)/1024`. That small difference
becomes more visible after repeated squaring.

### Repeated squaring

Write the current value as `zn = xn + i*yn`. Squaring it gives the next
value:

| Next component | Update |
|---|---|
| `x(n+1)` | `xn*xn - yn*yn` |
| `y(n+1)` | `2*xn*yn` |

Equivalently, `z(n+1) = zn*zn`, so after `n` updates,
`zn = z0^(2^n)`. Each update doubles the angle. After ten updates, the
ideal sequence reaches `10^i`; the program's approximate starting value
produces a nearby result.

The programs print each pair before updating it. Their eleven output rows
are therefore `z0` through `z10` (the initial value plus ten updates).
Printed values are rounded to five digits after the decimal point; those
rounded strings are not fed back into the calculation.

## Run the examples

### Python

From the repository root:

```sh
.venv/bin/python algebra/algebra.py
```

### Fortran

The source uses fixed-form, older Fortran syntax. With `gfortran`:

```sh
gfortran -std=legacy -o /tmp/algebra-fortran algebra/algebra.for
GFORTRAN_STDIN_UNIT=6 GFORTRAN_STDOUT_UNIT=5 /tmp/algebra-fortran
```

The program writes to Fortran unit 5. These environment settings map unit 5
to standard output and unit 6 to standard input for the local run. Unit
number conventions differ across runtimes and TOPS-10, so adjust them for
the target environment as needed.

The earlier Raspberry Pi workflow also uses `gdb` and the VS Code Modern
Fortran extension for debugging. On macOS, the system security configuration
may prevent `gdb` from attaching.

### MACRO-10

[`algebra.mac`](algebra.mac) is intended for a TOPS-10 environment; it is
not directly runnable with the Python or Fortran commands above. It uses
TOPS-10 monitor calls such as `OUTCHR` to print one character at a time.
Its `PRFLT` routine prints a value smaller than one with five digits after
the decimal point.

## Comparing results

The implementations share the recurrence, but their initial values,
arithmetic formats, and output routines are not identical. In particular:

- Python and Fortran calculate `x0` from `sqrt(1 - y*y)`.
- MACRO-10 starts from a decimal constant for `x0`.
- The MACRO-10 source uses double-floating-point operations (`DFMP` and
  `DFSB`); it should not be described as a single-precision implementation.
- Python and Fortran print five digits after the decimal point, while the
  MACRO-10 output routine explicitly extracts five fractional digits.

Small differences in the initial approximation or intermediate precision
are amplified by repeated squaring. A divergence in later rows is therefore
a useful prompt to inspect initialization, operation precision, rounding,
and formatting; by itself, it does not identify which factor caused the
difference.

The displayed digits are rounded output, not the internal values used for
the next iteration.

## Fortran and TOPS-10 notes

The Fortran source uses a `WRITE` unit and a separate `FORMAT` statement.
In `WRITE (5, 10)`, `5` is the unit number and `10` identifies the format
statement. The runtime decides how unit numbers map to the terminal.

The MACRO-10 source keeps values in accumulators, performs the recurrence
with floating-point instructions, then converts each value to text for
terminal output. `OUTCHR` sends one character to the TOPS-10 monitor; the
printing routine repeats this for the sign, decimal point, and digits.

## Files

| File | Purpose |
|---|---|
| [`algebra.py`](algebra.py) | Python reference implementation |
| [`algebra.for`](algebra.for) | Fixed-form Fortran implementation |
| [`algebra.mac`](algebra.mac) | TOPS-10 MACRO-10 implementation |
