# Simplex

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
