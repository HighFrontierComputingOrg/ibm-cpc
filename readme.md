# IBM CPC

This repository collects small numerical-method examples connected to the
IBM CPC computing history project:
<https://www.columbia.edu/cu/computinghistory/cpc.html>.

## Projects

### SOR

[`sor/sor.py`](sor/sor.py) currently applies one in-place sweep to a small
two-by-three grid, using a relaxation factor of 1. It keeps the boundary
values fixed, retains full floating-point precision internally, and formats
the displayed grid to three decimal places.

The accompanying [page 123 notes](sor/page123.md),
[page 124 notes](sor/page124.md), and [page 125 notes](sor/page125.md)
summarize the grid model, initial values, boundary conditions, and first
iteration. The page scans are kept beside the notes.

Run it from the repository root:

```sh
python3 sor/sor.py
```

### Simplex

The six Octave programs in [`simplex/`](simplex/) build from a complete
tableau update to a revised simplex implementation with basis updates, stored
pivot transformations, FTRAN, BTRAN, pricing, and a ratio test.

Run an example from the repository root:

```sh
octave simplex/smpl1.m
```

Replace `smpl1.m` with `smpl2.m` through `smpl6.m` to run the other stages.
The [simplex guide](simplex/readme.md) describes the programs. Detailed
[source notes and page index](simplex/alp/readme.md) cover the worked model,
pivot rules, product-form inverse, and sparse reinversion; the photographed
pages are stored in `simplex/alp/`.

### ADI

The [ADI folder](adi/) is reserved for alternating-direction implicit
examples; it currently contains only a short placeholder.

### CPC emulator POC

A draft design for a minimal Python emulator, based primarily on the 1954
operating manual and informed by the 1951 overview, is in the
[CPC emulator POC design](docs/cpc-emulator-poc.md). The emulator itself has
not been implemented yet.

## Repository conventions

Python cache directories (`__pycache__/`) are ignored by Git.
