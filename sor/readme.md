# Successive over-relaxation (SOR)

This folder contains a small grid example of an iterative method for solving
the discrete Laplace equation. The Python script performs one in-place sweep
over a two-by-three grid of interior values, using a relaxation factor of 1
(the Gauss-Seidel update).

## Grid and boundary values

The six unknowns are initialized as:

```text
0.400  0.600  0.400
0.100  0.300  0.100
```

The boundary values above the grid are 1; the boundary values along the
other edges are 0. Each interior value is updated to the average of its four
neighbors. The script visits cells from left to right, top to bottom, so
values updated earlier in the sweep are used immediately. Boundary values
stay fixed.

## Run

From the repository root:

```sh
.venv/bin/python sor/sor.py
```

The script performs one sweep and prints the complete grid, including its
boundary ring, to three decimal places. It retains full floating-point
precision during the calculation. For example, its interior values after
the sweep are approximately:

```text
0.425  0.531  0.408
0.181  0.203  0.153
```

The historical page 125 notes round intermediate arithmetic to three
significant digits, so their last digits differ slightly from the script's
full-precision results. The script currently does not repeat sweeps until
convergence or use a relaxation factor other than 1.

## Notes and references

The [`1967-cslas/`](1967-cslas/) folder contains transcriptions and scans of
pages 123–125, covering the grid equations, initial estimates, and first
iteration. The [PDF reference](1955-jacm.pdf) is also stored in this folder.

[1] George Forsythe and Cleve Moler, Computer Solution of Linear Algebraic Systems, Prentice-Hall Series in Automatic Computation (Englewood Cliffs, NJ: Prentice-Hall, 1967).

[2] David M. Young and Charles Warlick, "ORDVAC Solutions of the Dirichlet Problem," Journal of the ACM 2, no. 3 (1955): 137–161.
