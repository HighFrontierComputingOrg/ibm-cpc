# Matrix inversion and iterative improvement

This Python example demonstrates the core operations behind direct solution
of linear systems: LU decomposition, triangular solves, matrix inversion by
repeated solves, and iterative improvement.

The numerical example follows the themes of *Computer Solutions of Linear
Algebraic Systems* by George E. Forsythe and Cleve B. Moler (1967). It uses a
six-by-six Hilbert matrix and its exact integer inverse to make finite-
precision errors visible.

## The test matrices

The Hilbert matrix `H` is defined by

```text
H[i, j] = 1 / (i + j - 1),    1 <= i, j <= 6.
```

The program also constructs `T = inverse(H)`, whose entries are integers. These
two matrices make a useful round-trip test:

```text
inverse(T) should reproduce H
inverse(H) should reproduce T
```

The Hilbert matrix is poorly conditioned. Consequently, small floating-point
errors can become large errors in the computed inverse; the discrepancies are
part of the experiment, not evidence that the exact matrices are inconsistent.

## What the program does

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

### Iterative improvement

Given an approximate solution `x`, the program forms the residual
`r = b - A x`, solves `A dx = r` with the existing factors, and updates
`x = x + dx`. In the Python implementation, the dot-product
accumulation used for the residual is promoted to `float64`; the matrix,
right-hand sides, factors, and correction arrays are `float32`.

The current `impruv` implementation performs a fixed ten correction passes.
It does not currently stop when a convergence tolerance is met or report the
`digits` estimate calculated during the first pass. Treat its output as a
comparison of the fixed-pass result, not as a convergence-certified answer.

## Reading the output

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

## Run the Python version

From the repository root, create the shared Python environment and install
project dependencies, including the debugger support, as described in the
[top-level setup instructions](../readme.md#python-setup). Then run:

```sh
.venv/bin/python inverse/inverse.py
```

To debug it in VS Code, open `inverse/inverse.py`, choose **Python: Debug
Current File** in the Run and Debug view, and start debugging. The project
environment must be selected as the Python interpreter; setup and launch
configuration are described in the [top-level README](../readme.md).

## Files

- [`inverse.py`](inverse.py) — NumPy implementation.
