# IBM CPC

This repository collects small numerical-method examples connected to the
IBM CPC:
<https://www.columbia.edu/cu/computinghistory/cpc.html>.

## Python setup

Python dependencies are declared in [`pyproject.toml`](pyproject.toml).
Create the project environment and install the project and its dependencies
once:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e ".[debug]"
```

Run the Python examples with `.venv/bin/python` so they use the project
environment and its NumPy installation. The `debug` extra installs debugpy
for the Python debugger configuration in `.vscode/launch.json`.

## Projects

### Simplex

The [Python example](simplex/simplex.py) solves Symonds's refinery running
plan, choosing crude-oil operations to maximize profit within supply and
product limits. Six Octave programs demonstrate the Simplex method step by
step, from full-tableau updates to a revised implementation with basis
updates, FTRAN, BTRAN, pricing, and the ratio test.

Run the refinery example from the repository root:

```sh
.venv/bin/python -m simplex.simplex
```

Run an Octave example with:

```sh
octave simplex/1968-alp/smpl1.m
```

Replace `smpl1.m` with `smpl2.m` through `smpl6.m` to explore the later
stages. The [Simplex guide](simplex/readme.md), [Symonds notes](simplex/1955-symonds-chp3.md),
and [ALP source notes](simplex/1968-alp/readme.md) provide more detail and references.

### SOR

See the [SOR guide](sor/readme.md) for an overview of the grid example,
how to run it, and the related source notes.

[`sor/sor.py`](sor/sor.py) currently applies one in-place sweep to a small
two-by-three grid, using a relaxation factor of 1. It keeps the boundary
values fixed, retains full floating-point precision internally, and formats
the displayed grid to three decimal places.

The accompanying [page 123 notes](sor/1967-cslas/page123.md),
[page 124 notes](sor/1967-cslas/page124.md), and
[page 125 notes](sor/1967-cslas/page125.md) summarize the grid model, initial
values, boundary conditions, and first iteration. The page scans are kept
beside the notes.

Run it from the repository root:

```sh
.venv/bin/python sor/sor.py
```

### ADI

[`adi/adi.py`](adi/adi.py) implements the alternating-direction implicit
method on a two-by-three grid for the discrete Laplace equation. Each
iteration alternates implicit row and column solves while keeping the
boundary values fixed. The example uses NumPy and follows the description in
Peaceman's [1990 paper](adi/1990-peaceman.pdf), pages 114–116.

Run it from the repository root:

```sh
.venv/bin/python -m adi.adi
```

See the [ADI guide](adi/readme.md) for more context and details.

### Numerical examples

The [numerical examples guide](docs/readme.md) covers repeated complex
squaring and matrix inversion with iterative improvement.

### CPC emulator POC

See the [CPC folder guide](cpc/readme.md) for an overview of the historical
references, emulator proposal, and related exploratory numerical examples.

## Repository conventions

Python cache directories (`__pycache__/`) are ignored by Git.
