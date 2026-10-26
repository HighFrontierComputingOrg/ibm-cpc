# Page 123: Grid System for the Iteration

This page sets up the linear system used in the SOR example on page 124. It
models values on a rectangular grid,
with interior unknowns \(v_1,\ldots,v_6\) and prescribed boundary values.

## Grid and boundary conditions

For the illustrated case, \(N=1\), there are six interior grid points in two
rows of three:

```text
          1       1       1
       +-----------------------+
     0 |   v1      v2      v3  | 0
       |                       |
     0 |   v4      v5      v6  | 0
       +-----------------------+
          0       0       0
```

The top boundary values are 1. The left and right boundary values beside the
interior rows, and the bottom boundary values, are 0. Each interior point is
related to its four neighboring points: its coefficient is 4, and each
neighbor contributes with coefficient -1. Boundary-neighbor terms are moved
to the right-hand side.

## Six-equation system

Applying that rule at each interior point gives:

\[
\begin{aligned}
4v_1 - v_2 - v_4 &= 1, \\
-v_1 + 4v_2 - v_3 - v_5 &= 1, \\
-v_2 + 4v_3 - v_6 &= 1, \\
-v_1 + 4v_4 - v_5 &= 0, \\
-v_2 - v_4 + 4v_5 - v_6 &= 0, \\
-v_3 - v_5 + 4v_6 &= 0.
\end{aligned}
\]

The first three equations have right-hand side 1 because those grid points
touch the top boundary. The remaining equations have right-hand side 0.
Equivalently, the coefficient matrix has diagonal entries 4 and entries -1
for neighboring interior points; all other entries are zero.

## Larger grids

The page contrasts this six-unknown example with a much larger grid that
could be handled by a computer. It describes choosing \(N=34\) to obtain
roughly fifteen thousand grid points, while noting that the number of
interior unknowns is

\[
n=(3N-1)(4N-1).
\]

Although the corresponding matrix is large, it is sparse: every equation
involves only a point and its immediate neighbors, so each row has at most
five nonzero coefficients. This is why an iterative method can be useful
instead of treating the system as a dense matrix.

The original page image is available in [page123.png](page123.png).
