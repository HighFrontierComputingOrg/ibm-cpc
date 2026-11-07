# ADI Alternating Direction Implicit

This example applies the alternating-direction method described by Peaceman
on pages 114–116 of [the 1990 reference](1990-peaceman.pdf) to the same
two-by-three problem used in the SOR example.

Each ADI iteration consists of two sweeps. The first solves a tridiagonal
system across each row, treating the horizontal direction implicitly and the
vertical direction explicitly. The second solves down each column, reversing
those roles. The boundary ring remains fixed, and each line system is solved
with NumPy. For this unit-spaced grid, `time_step` is the ADI
iteration parameter rather than a physical time increment.

## Run

From the repository root:

```sh
.venv/bin/python -m adi.adi
```

The script stops when the largest interior-value change over a complete pair
of sweeps is at most `1e-10`, then prints the grid to three decimal places.
The converged interior values are approximately:

```text
0.416  0.509  0.416
0.155  0.205  0.155
```
