# Successive over-relaxation (SOR)

A small example of an iterative method for the harmonic boundary value problem repeatedly sweeps a two-by-three grid of interior values until the grid stops changing, demonstrating iterative convergence on a solution. Though in many senses successive over-relaxation is a very simple approach, it is linear algebra at heart, with Ax=b, an A matrix and a vector of solution variables x. One thing in this case is that there is no time variable involved, the solution is at a point in time. It is a static system without dynamics, nothing is changing in time, and this is helpful as a kind of simplest and most straightforward introduction. It does have a bit of complexity of its own in that it has a tuning parameter, and it is quite sensitive to this tuning parameter. It is easy to see this in action, and this makes it a helpful introductory example for seeing the role of alternate approaches. Historically this was one of the questionable things, there was clear evidence of people questioning, "Okay, SOR is fine, but how do you get this tuning parameter correct?" It can easily be observed that this is an important practical question. If it is done right, it performs well. If done wrong, it is at a disadvantage. 

The extraordinary thing is that it can reach a solution vector x without directly handling the A matrix at all. There are simply no direct operations on the A matrix. It is true that the A matrix enters indirectly and that its structure, nature, and values of course matter, but somewhat indirectly. There are no operations on the rows and columns of A. This is one of the senses in which it is simple linear algebra, in that there are no matrix decompositions. Matrix decomposition does not enter in at all. This is starkly different from both Simplex and ADI, where operations on the A matrix are direct and explicit. Looking at SOR, it becomes evident from the literature that the A matrix does actually come to play more important roles. There is a certain property that David Young identified in the A matrix that is very important for SOR, and there is a certain structure, the so called red-black structure of the A matrix, that also becomes important. In the initial "just get it working" phase, however, these do not enter in. They are just glimmers on the horizon of what is to come, and it is straightforward to reach a SOR solution vector without ever directly dealing with the A matrix.

This is an entry point into the world of the A matrix. If asked what linear algebra is, it is the A matrix and Ax=b, or even Ax=0 in some cases. Linear algebra is about the A matrix. With SOR, initially, it is minimally and indirectly about the A matrix, which is quite curious and interesting for learning, even at the entry level of a small grid problem. In David Young's 1955 paper, though there is no direct appearance of the A matrix, its eigenvalues do appear. The whole question about the tuning parameter, or omega, is really a question about the eigenvalues. Here things become a bit hazy, there are eigenvalues of a matrix that are critical for the tuning parameter, but this matrix's exact relationship to the A matrix is a bit obscure. In any case, linear algebra in a nutshell is the A matrix, and the A matrix is partially equivalent to some special values. Anywhere with an A matrix or eigenvalues is linear algebra, and the german term eigenvalues makes things much more mysterious than they need to be. They are special values, which is the translation of eigen, meaning special or singular, the characteristic values of the A matrix. These singular values contain critical information encoded in the A matrix. It cannot be all there is to it, of course, but much of the critical information of the A matrix is in its singular values, and in the SOR context the topic of choosing the tuning parameter omega enters here.

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

The script compares the grid after each sweep as formatted to three decimal
places. It stops when that displayed grid matches the previous one, reports
the number of sweeps, and prints the complete grid including its boundary
ring. Full floating-point precision is retained during the calculation;
rounding is only used for the convergence check and display. For example,
the converged interior values are approximately:

```text
0.416  0.509  0.416
0.155  0.205  0.155
```

The historical page 125 notes round intermediate arithmetic to three
significant digits, so their last digits differ slightly from the script's
full-precision results. The script uses a relaxation factor of 1.

## Notes and references

The [`1967-cslas/`](1967-cslas/) folder contains transcriptions and scans of
pages 123–125, covering the grid equations, initial estimates, and first
iteration. The [PDF reference](1955-jacm.pdf) is also stored in this folder.

[1] George Forsythe and Cleve Moler, Computer Solution of Linear Algebraic Systems, Prentice-Hall Series in Automatic Computation (Englewood Cliffs, NJ: Prentice-Hall, 1967).

[2] David M. Young and Charles Warlick, "ORDVAC Solutions of the Dirichlet Problem," Journal of the ACM 2, no. 3 (1955): 137–161.
