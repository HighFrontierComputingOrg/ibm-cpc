# Numerical examples

This guide covers the Python examples for repeated complex squaring and
matrix inversion with iterative improvement.

## Repeated complex squaring

The [algebra example](algebra.py) reproduces the values in
[Feynman's Table 22-3](https://www.feynmanlectures.caltech.edu/I_22.html).
It demonstrates how rounding and floating-point precision affect repeated
calculations.

### Mathematics

The calculation starts with a complex number close to `10^(i/1024)`, where
`i` is the imaginary unit. In polar form, the ideal value has angle
`theta = ln(10)/1024`, approximately `0.00224861825` radians.

Rather than calculate that ideal value directly, the program uses the nearby
approximation:

| Component | Value |
|---|---:|
| `y0` | `0.00225` |
| `x0` | `sqrt(1 - y0*y0)`, approximately `0.99999747` |
| `z0` | `x0 + i*y0` |

This makes `z0` lie on the unit circle, but its angle is approximately
`0.00225000190` radians—not exactly `ln(10)/1024`. That small difference
becomes more visible after repeated squaring.

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

The program prints each pair before updating it. Its eleven output rows are
therefore `z0` through `z10` (the initial value plus ten updates). Printed
values are rounded to five digits after the decimal point; those rounded
strings are not fed back into the calculation.

Run it from the repository root:

```sh
.venv/bin/python docs/algebra.py
```

The calculation uses Python floating-point arithmetic. Displayed digits are
rounded output, not the internal values used for the next iteration.

## Matrix inversion and iterative improvement

The [inverse example](inverse.py) demonstrates LU decomposition, triangular
solves, matrix inversion by repeated solves, and iterative improvement.
Its numerical example follows the themes of *Computer Solutions of Linear
Algebraic Systems* by George E. Forsythe and Cleve B. Moler (1967). It uses a
six-by-six Hilbert matrix and its exact integer inverse to make finite-
precision errors visible.

### Test matrices

The Hilbert matrix `H` is defined by

```text
H[i, j] = 1 / (i + j - 1),    1 <= i, j <= 6.
```

The program also constructs `T = inverse(H)`, whose entries are integers.
These two matrices make a useful round-trip test:

```text
inverse(T) should reproduce H
inverse(H) should reproduce T
```

The Hilbert matrix is poorly conditioned. Consequently, small floating-point
errors can become large errors in the computed inverse; the discrepancies
are part of the experiment, not evidence that the exact matrices are
inconsistent.

### What the program does

To invert a matrix `A`, the program first factors it once, then solves
`A x = e[j]` for each column `j`, where `e[j]` is the corresponding column
of the identity matrix. The solution vectors become the columns of
`inverse(A)`.

The main routines are:

| Routine | Purpose |
| --- | --- |
| `hil` | Construct the six-by-six Hilbert matrix `H`. |
| `invhil` | Construct the exact integer inverse `T`. |
| `decomp` | Compute an LU factorization with scaled pivot selection. |
| `solve` | Solve a system using the factors and recorded row permutation. |
| `invert` | Factor a matrix and solve for each column of its inverse. |
| `impruv` | Refine a solution by computing a residual and solving for a correction. |

The implementation stores the LU factors together in one array and records
row permutations in `ips`. `invert` reuses the factorization for all six
right-hand sides rather than decomposing the matrix again for every column.

Given an approximate solution `x`, iterative improvement forms the residual
`r = b - A x`, solves `A dx = r` with the existing factors, and updates
`x = x + dx`. The dot-product accumulation used for the residual is promoted
to `float64`; the matrix, right-hand sides, factors, and correction arrays
are `float32`.

The current `impruv` implementation performs a fixed ten correction passes.
It does not currently stop when a convergence tolerance is met or report
the `digits` estimate calculated during the first pass. Treat its output as
a comparison of the fixed-pass result, not as a convergence-certified
answer.

### Reading the output

The program prints six matrices, in this order:

| Output | Meaning |
| --- | --- |
| `Ha` | Computed inverse of `T`, without iterative improvement; compare with `H`. |
| `Hb` | Computed inverse of `T`, with iterative improvement; compare with `H`. |
| `H` | The constructed Hilbert matrix. |
| `Ta` | Computed inverse of `H`, without iterative improvement; compare with `T`. |
| `Tb` | Computed inverse of `H`, with iterative improvement; compare with `T`. |
| `T` | The constructed integer inverse of `H`. |

The first three matrices are printed to eight digits after the decimal point;
the final three use two digits after the decimal point. Formatting only
controls display precision and does not make the calculations more accurate.

### Run and debug

From the repository root, create the shared Python environment and install
project dependencies, including debugger support, as described in the
[top-level setup instructions](../readme.md#python-setup). Then run:

```sh
.venv/bin/python docs/inverse.py
```

To debug it in VS Code, open `docs/inverse.py`, choose **Python: Debug
Current File** in the Run and Debug view, and start debugging. The project
environment must be selected as the Python interpreter; setup and launch
configuration are described in the [top-level README](../readme.md).

## Files

| File | Purpose |
|---|---|
| [`algebra.py`](algebra.py) | Repeated complex-squaring example. |
| [`inverse.py`](inverse.py) | Matrix inversion and iterative-improvement example. |
