# IBM CPC

https://www.columbia.edu/cu/computinghistory/cpc.html 


# Simplex

William Orchard-Hays, Advanced Linear-Programming Computing Techniques (New York: McGraw-Hill, 1968). The widget problem in Chapter 3 of ALP seems ideal. It is solved explicitly in tableau form, takes only four iterations, and every operation is easy to check against the code. The target is BTRAN, FTRAN, and emulated magnetic tape to maintain the basis inverse as PFI (product form of the inverse) eta columns. At first, the incoming column and pivot row for each iteration are taken as given from Chapter 3 of ALP. This makes the basic mechanics of the revised simplex, FTRAN, and BTRAN easier to see.

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

# ADI Alternating Direction Implicit
