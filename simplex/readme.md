# Project Simplex

William Orchard-Hays, Advanced Linear-Programming Computing Techniques (New York: McGraw-Hill, 1968).

Go backward in time, starting in the mid-1960s, and work through a small business problem using linear programming. The widget problem in Chapter 3 of ALP seems ideal. It is solved explicitly in tableau form, takes only four iterations, and every operation is easy to check against the code.

The target is BTRAN, FTRAN, and emulated magnetic tape to maintain the basis inverse as PFI (product form of the inverse) eta columns. At first, the incoming column and pivot row for each iteration are taken as given from Chapter 3 of ALP. This makes the basic mechanics of the revised simplex, FTRAN, and BTRAN easier to see.

## SMPL1: Original Simplex

The Chapter 3 example, worked exactly as it appears in the book. The entire tableau is updated in each iteration. In this example, columns 1 and 4 are unit vectors that do not play a direct role, but they are updated anyway. The revised simplex leaves them untouched.

## SMPL2: Revised Simplex

Chapter 4 of ALP. The full tableau is not updated; the original tableau serves as a constant. Instead, the beta column (the right-hand side) is updated using the basis inverse. New eta vectors are generated for storage on tape. Each eta vector is a column of the basis inverse. The basis inverse is also used to transform incoming columns, with the same effect as the tape-based FTRAN routine.

## SMPL3: Tape-Based FTRAN for Transforming Columns

Tape is emulated by storing pivot-value and eta-column pairs, from left to right, in a matrix. This revised-simplex mechanism approaches the methods used in the late 1950s and early 1960s. Only the right-hand-side beta vector is maintained across iterations; the basis inverse is stored as eta vectors "on tape." The tape and eta columns are read forward.

## SMPL4: Tape-Based BTRAN for Transforming Columns into Prices

Early in each revised-simplex iteration, the updated first-row values for particular columns are needed. These values are the columns' prices. Profit increases when a column with a negative price enters the basis. The updated price of a column is the dot product of that column with the first row of the basis inverse. BTRAN computes these dot products. The first row of the basis inverse is derived from the eta columns on tape, which are read backward—reversing the order used by FTRAN in the previous iteration.

## SMPL5: Pricing and Choosing the Incoming Vector

Until now, the incoming vector was given, so pricing was unnecessary. With BTRAN available, pricing can now be performed to choose the incoming vector.

## SMPL6: Ratio Test and Choosing the Outgoing Vector

Until now, the outgoing vector was given. The incoming column and beta column can now be used to determine the pivot value and, therefore, the outgoing column. First, transform the incoming column from the original tableau using FTRAN. Then, for each relevant row, divide the beta value by the incoming value to find the candidate new beta value. Reject infeasible candidates and choose the smallest remaining ratio. Its row is the pivot row, and its basic variable leaves the basis.

# The Widget Problem in Chapter 3 of ALP

The problem has five activities, x1 through x5, represented by five tableau columns:

- Activity x1 produces unfinished widgets.
- Activity x2 converts unfinished widgets into finished widgets.
- Activity x3 produces finished widgets from scratch.
- Activity x4 uses L1 overtime.
- Activity x5 uses L2 overtime.

The model and tableau have five rows:

- Row 1 is the objective function, recast as an equation. Costs are positive, and revenues are negative.
- Row 2 is the capacity constraint on L1 labor.
- Row 3 is the capacity constraint on L2 labor.
- Row 4 ensures that enough unfinished widgets are produced to allow some to be converted into finished widgets.
- Row 5 represents contractual and policy constraints on unfinished widgets.

The row equations are:

- u1 - 5.4x1 - 7.3x2 - 12.96x3 + 6x4 + 9x5 + 800 = 0
- 0.5x1 + 0.6x3 - x4 <= 80
- 0.25x1 + 0.5x2 + 0.6x3 - x5 <= 40
- -x1 + x2 <= 0
- 100 <= x1 <= 150

All x values are nonnegative, x4 <= 20, and x5 <= 10. The objective is to maximize u1.
