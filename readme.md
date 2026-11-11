# IBM CPC

This repository explores the numerical methods and computing history around
the IBM Card-Programmed Electronic Calculator (CPC). Its examples are small
enough to inspect and run, but illustrate important ideas in linear algebra:
optimizing a constrained plan, solving a grid equation iteratively, and
seeing how finite-precision arithmetic affects a calculation.

The projects are related by their historical setting, not by a single
software application. The Simplex and grid examples are independent
demonstrations; the CPC emulator is a design proposal, not a working
emulator. Historical papers, manuals, transcriptions, and scans are kept
alongside the code so the examples can be compared with their sources. For
background on the machine, see the [Columbia IBM CPC history
page](https://www.columbia.edu/cu/computinghistory/cpc.html).

## Projects

### Simplex: planning under constraints

The [refinery example](simplex/simplex.py) turns a running-plan problem into
linear programming: choose how much of each crude-oil operation to run while
respecting crude supplies and product limits, and maximize profit. Product
limits are ceilings, so the best plan may leave some demand unmet if making
more would not be profitable.

Run the Python model from the repository root:

```sh
.venv/bin/python -m simplex.simplex
```

Six [Octave examples](simplex/1968-alp/) build the Simplex algorithm in
stages—from updating a full tableau to revised-simplex techniques such as
pricing, FTRAN, BTRAN, and the ratio test. Run the first stage with
`octave simplex/1968-alp/smpl1.m`; replace `smpl1.m` with `smpl2.m` through
`smpl6.m` to explore the rest. The [Simplex guide](simplex/readme.md) and
[source notes](simplex/1968-alp/readme.md) provide more detail. The model
comes from the refinery-planning work documented in
[Symonds's Chapter 3 notes](simplex/1955-symonds-chp3.md).

### SOR and ADI: solving a grid equation

[SOR](sor/sor.py) and [ADI](adi/adi.py) use the same small discrete Laplace
problem: find interior grid values consistent with fixed boundary values.
This makes them a useful pair to compare. SOR updates one cell at a time,
reusing values as it sweeps across the grid, with a relaxation factor
controlling the update. ADI instead alternates row and column sweeps, solving
each line implicitly. Both approximate the steady-state solution, but take
different routes through the underlying linear system.

Run either example from the repository root:

```sh
.venv/bin/python sor/sor.py
.venv/bin/python -m adi.adi
```

The [SOR guide](sor/readme.md) explains the grid, relaxation factor, and
historical worked example. The [ADI guide](adi/readme.md) introduces the
alternating-direction method and links it to Peaceman's
[1990 retrospective](adi/1990-peaceman.pdf).

### UTOPIA: satellite range-rate tracking, navigation, and geodesy

The [Utopia examples](utopia/) explore how a satellite's line-of-sight
range-rate changes its received radio frequency, connecting the Sputnik
era's satellite tracking work with the later Transit navigation system. The
examples use synthetic data and simplified models; they are demonstrations
of the measurement and fitting ideas, not reconstructions of Sputnik 1's
recorded signal or actual orbit. See the [Utopia guide](utopia/readme.md) for
the equations, historical background, and sources.

Run either example from the repository root:

```sh
.venv/bin/python utopia/sputnik1.py
.venv/bin/python utopia/sputnik2.py
```

### Numerical examples: precision and stability

The [numerical examples guide](cpc/msc/readme.md) covers two further
experiments. Repeated complex squaring shows how a tiny difference in the
starting value becomes visible through repeated arithmetic. Matrix inversion
and iterative improvement use a Hilbert matrix to make finite-precision
error—and the effect of refining a computed solution—easier to observe.
These are standalone numerical examples, not components of the emulator
proposal.

### CPC emulator proof of concept

The [CPC folder](cpc/) contains historical machine manuals and a
[proof-of-concept design](cpc/cpc-emulator-poc.md) for a small behavioral
model. The proposal focuses on the CPC's card-driven workflow, decimal
arithmetic, control panel, and storage. It is not implemented, and does not
aim to reproduce the complete machine or its timing.
