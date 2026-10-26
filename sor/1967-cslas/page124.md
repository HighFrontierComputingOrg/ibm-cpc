# Page 124: SOR

This page continues an example of the SOR method for solving a linear system.
It begins with a guess for every unknown and repeatedly replaces individual
values using equations from the system.

## Uniqueness exercise

The page first refers to an earlier system and asks the reader to establish
that it has only one solution. Its suggested argument is to suppose there are
two solutions, \(w\) and \(y\), and consider their difference
\(z=w-y\). Since both satisfy the same system, subtracting their equations
gives a homogeneous system for \(z\), with zero right-hand sides. Showing that
this system forces \(z=0\) proves that \(w=y\), so there cannot be two distinct
solutions.

## Grid and initial values

For the iterative example, the unknowns are arranged in two rows of three:

| \(v_1=0.400\) | \(v_2=0.600\) | \(v_3=0.400\) |
|---:|---:|---:|
| \(v_4=0.100\) | \(v_5=0.300\) | \(v_6=0.100\) |

The diagram also shows fixed boundary values around this grid. The three
values along the top are 1; the left and right boundary values beside the two
rows are 0; and the three values along the bottom are 0. The six interior
values are starting estimates, not yet the final solution.

The example processes the components in numerical order, \(v_1\) through
\(v_6\). At each step, it solves the corresponding equation for the component
being updated. Values already updated during the current pass are used
immediately; values later in the order still have their previous values.
This in-place use of the newest available values is the distinguishing
feature of the SOR iteration.

## First update

The first unknown, \(v_1\), is at the upper-left of the interior grid. Its
equation relates it to the boundary value above it (1), the boundary value to
its left (0), and its two interior neighbors \(v_2\) and \(v_4\):

\[
4v_1 - 1 - 0 - v_2 - v_4 = 0.
\]

Rearranging gives

\[
v_1 = \frac{1 + 0 + v_2 + v_4}{4}.
\]

At this first step, \(v_2\) and \(v_4\) have not yet been updated, so the
initial values \(v_2=0.600\) and \(v_4=0.100\) are substituted:

\[
v_1 = \frac{1 + 0 + 0.600 + 0.100}{4}
     = \frac{1.700}{4}
     = 0.425.
\]

Thus the first pass replaces \(v_1=0.400\) with \(v_1=0.425\). The page notes
that the arithmetic is carried out with three-decimal floating-point values;
the next updates continue in the stated left-to-right, top-to-bottom order.

The original page image is available in [page124.png](page124.png).
