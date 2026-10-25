# ALP Notes: Simplex and Product-Form Inverse

These notes explain the photographed pages in this folder in original wording.
The scans remain the source for the book's full derivations and notation.
Source: *Advanced Linear-Programming Computing Techniques* (1968), pages
49–82.

## Page index

| Pages | Topics | Scan |
|---|---|---|
| 49 | Composite primal simplex procedure | [page 49](PXL_20261008_155717690.jpg) |
| 50–51 | Pivot updates and the widget-production example | [pages 50–51](PXL_20261008_155728304.jpg) |
| 52–53 | Model equations, variable bounds, and initial tableau | [pages 52–53](PXL_20261008_155736505.jpg) |
| 54–55 | Pricing, pivots, and bound changes in the example | [pages 54–55](PXL_20261008_155745439.jpg) |
| 56–57 | Reading a solution and infeasibility examples | [pages 56–57](PXL_20261008_155755405.jpg) |
| 58–59 | Unboundedness, infeasible starts, and pivoting | [pages 58–59](PXL_20261008_155804243.jpg) |
| 60–61 | Degeneracy | [pages 60–61](PXL_20261008_155812000.jpg) |
| 62–63 | Transition from the simplex example to inverse updates | [pages 62–63](PXL_20261008_155822435.jpg) |
| 64–65 | Elementary column and row transformations | [pages 64–65](PXL_20261008_155831291.jpg) |
| 66–67 | Product form of the inverse | [pages 66–67](PXL_20261008_155839306.jpg) |
| 68–69 | Applying inverse factors and composing transformations | [pages 68–69](PXL_20261008_155849960.jpg) |
| 70–71 | Forward transformation of columns (FTRAN) | [pages 70–71](PXL_20261008_155856317.jpg) |
| 72–73 | Backward transformation of rows (BTRAN) | [pages 72–73](PXL_20261008_155904458.jpg) |
| 74–75 | Reinversion and sparsity-aware pivot selection | [pages 74–75](PXL_20261008_155912128.jpg) |
| 76–77 | Elimination example and pivot-selection counts | [pages 76–77](PXL_20261008_155919446.jpg) |
| 78–79 | Sparse inverse structure and modified elimination | [pages 78–79](PXL_20261008_155928212.jpg) |
| 80–81 | Detailed sparse-reinversion procedure and tradeoffs | [pages 80–81](PXL_20261008_155935106.jpg) |
| 82 | Storage and implementation considerations | [page 82](PXL_20261008_155942188.jpg) |

## 1. Widget-production model

The example models a small factory choosing production and overtime levels.
Its five activities are:

| Variable | Meaning |
|---|---|
| \(x_1\) | Produce unfinished widgets |
| \(x_2\) | Convert unfinished widgets into finished widgets |
| \(x_3\) | Produce finished widgets directly |
| \(x_4\) | Use overtime for labor class L1 |
| \(x_5\) | Use overtime for labor class L2 |

The labor, flow, and contract conditions are

\[
\begin{aligned}
0.5x_1 + 0.6x_3 - x_4 &\le 80,\\
0.25x_1 + 0.5x_2 + 0.6x_3 - x_5 &\le 40,\\
-x_1 + x_2 &\le 0,\\
100 \le x_1 &\le 150.
\end{aligned}
\]

All activity levels are nonnegative, and the overtime activities have upper
bounds \(x_4\le20\) and \(x_5\le10\). The first two inequalities limit the
available hours in the two labor classes. The third ensures the conversion
activity cannot exceed the supply of unfinished widgets. The final condition
is a production contract.

The objective is represented in the tableau as

\[
u_1 - 5.4x_1 - 7.3x_2 - 12.96x_3 + 6x_4 + 9x_5 + 800 = 0,
\]

with \(u_1\) maximized. The coefficients combine the activity's revenues and
costs, including the fixed operating expense. The other tableau rows encode
the capacity, flow, and contract constraints. Slack or bounded variables make
these equations compatible with a basis representation.

The example is valuable because each pivot is small enough to check by hand.
It starts with an initial basis and successively changes which variables are
basic, while tracking both feasibility and objective improvement.

## 2. Primal simplex iteration

For a linear system \(Ax=b\), let \(B\) be the matrix made from the current
basic columns. The current basic values are

\[
\beta = B^{-1}b.
\]

For a candidate entering column \(a_s\), its transformed direction is

\[
\alpha = B^{-1}a_s.
\]

The primal procedure repeats four conceptual stages:

1. **Check feasibility and choose a pricing form.** Determine whether the
   current basic values satisfy their bounds. The pricing rule depends on
   that state: a feasible basis uses an improving-objective criterion, while
   an infeasible basis prioritizes reducing infeasibility.
2. **Choose an entering variable.** Price eligible nonbasic columns and
   select one with an improving price. A variable already at its upper bound
   is considered in the direction that moves it back into the feasible
   interval. Columns already in the basis need not be considered.
3. **Perform the ratio test.** Use \(\alpha\) to predict how basic values
   change as the entering variable moves. The first basic variable to reach
   a lower or upper bound determines the pivot row. The entering variable's
   own bounds also limit how far it can move.
4. **Update the basis and values.** Pivot on the selected element, update the
   right-hand side and basis bookkeeping, and record the transformation for
   later use.

If no improving entering column exists while the basis is feasible, the
current solution is optimal. If the basis is infeasible and no priced move
can reduce infeasibility, the model has no feasible solution. If an improving
direction has no limiting bound, the objective is unbounded. A bounded
entering variable can instead reach its opposite bound before any basic
variable leaves; this is a bound flip, not a basis pivot.

The worked tableaux illustrate these decisions, including how a bounded
variable can enter or leave at a bound. For a pivot at row \(r\), if
\(\alpha_r\ne0\), the row-operation coefficients can be written

\[
\eta_r = \frac{1}{\alpha_r},
\qquad
\eta_i = -\frac{\alpha_i}{\alpha_r}\quad(i\ne r).
\]

They make the transformed entering column equal to the \(r\)-th unit vector.
The same coefficients update every basic value and every transformed
tableau column.

## 3. Important edge cases

### Infeasible and unbounded cases

An infeasible starting basis does not by itself mean the model is infeasible:
the algorithm may select moves that reduce the violated bounds. Infeasibility
is concluded only when the pricing and ratio logic show that no permitted
move can repair it.

For an unboundedness test, follow an improving entering direction. If no
basic bound restricts that direction and the entering variable itself has no
limiting bound, the objective can continue improving indefinitely. A finite
upper bound on the entering variable changes this conclusion because the
variable may simply move from one bound to the other.

### Degeneracy

A degenerate pivot occurs when the limiting step length is zero. The basis
changes, but the represented solution does not move. Several consecutive
degenerate pivots are possible, so the objective can remain unchanged for a
while. Pivot rules and careful bookkeeping help avoid cycling; degeneracy is
not evidence that the model has no solution.

### Redundant or inconsistent constraints

Redundant equations can create zero or dependent rows in a tableau. An
inconsistent right-hand side can instead reveal infeasibility. These are
different situations: dependence among constraints is not automatically an
error, but a contradiction prevents any vector from satisfying the system.

## 4. Why maintain an inverse representation?

In a revised simplex implementation, the original constraint matrix is kept
fixed. The algorithm does not repeatedly rewrite every tableau column.
Instead, it maintains the right-hand side \(\beta=B^{-1}b\), transforms only
the columns needed for pricing or a pivot, and records how the basis changes.

This is especially useful for sparse problems. A matrix may be large while
each column contains only a few nonzero entries. Storing and updating a full
dense inverse can destroy that sparsity and waste both memory and arithmetic.
The product-form representation stores a sequence of small pivot
transformations instead.

## 5. Elementary transformations and product form

Suppose basis column \(r\) is replaced by \(a_s\), and compute

\[
\alpha=B^{-1}a_s.
\]

Construct an elementary matrix \(E\) equal to the identity except in column
\(r\), where it contains \(\eta\):

\[
E_{ir} =
\begin{cases}
1/\alpha_r & i=r,\\
-\alpha_i/\alpha_r & i\ne r.
\end{cases}
\]

Then \(E\alpha=e_r\). If \(B'\) is the basis after the replacement, its
inverse is

\[
(B')^{-1}=E B^{-1}.
\]

The full tableau need not be rebuilt to apply this pivot: multiply the
current transformed right-hand side and any required transformed columns by
\(E\). After successive pivots with factors \(E_1,\ldots,E_k\), the updated
basis inverse is

\[
B_k^{-1}=E_kE_{k-1}\cdots E_1B_0^{-1}.
\]

The factor order matters. To transform a column, apply the first recorded
factor, then the second, continuing forward through the pivot history. Each
factor is represented compactly by its pivot row and eta column rather than
by storing a full matrix.

The row-update counterpart uses transformations on the other side of the
matrix. Row operations are useful for the pricing calculations; column
operations update the right-hand side and candidate columns. The two views
are linked by transpose identities, which also explain why their traversal
orders differ.

## 6. FTRAN: transform a column

Given a structural column \(a_j\), FTRAN computes its coordinates in the
current basis:

\[
\alpha_j=B^{-1}a_j.
\]

With a product-form inverse, begin with \(a_j\) and apply the stored eta
factors in pivot order:

\[
a_j^{(0)}=a_j,\qquad a_j^{(t)}=E_ta_j^{(t-1)}.
\]

The final vector is the transformed column. The same operation is needed for
the right-hand side when updating \(\beta\). It is normally unnecessary to
materialize \(B^{-1}\) itself.

The cost depends on the number of factors and their nonzero structure. As the
factor list grows, transformations become more expensive and may accumulate
roundoff. This motivates periodically rebuilding the inverse representation
from the current basis.

## 7. BTRAN: transform a pricing row

Pricing can be expressed using a row vector \(f^T\). BTRAN computes

\[
\pi^T=f^TB^{-1}.
\]

The resulting row can be dotted with original columns to obtain their
transformed prices. In the ordinary objective-pricing case,
\(f^T=c_B^T\), so the reduced cost of a nonbasic column is

\[
\bar c_j=c_j-\pi^Ta_j.
\]

When feasibility restoration is in progress, the pricing form \(f\) can
instead encode which basic bounds are violated. Thus BTRAN is the common
mechanism for turning a row pricing rule into prices for all candidate
columns.

Because \(B^{-1}=E_k\cdots E_1B_0^{-1}\), multiplying a row on the right
applies the factors in reverse pivot order. FTRAN reads the product forward
for column vectors; BTRAN reads it backward for row vectors. Confusing these
orders produces incorrect prices even when each individual eta factor is
correct.

## 8. Reinversion and sparse pivoting

Product form is economical for a sequence of pivots, but it is not free:
each additional factor increases future FTRAN and BTRAN work. Reinversion
starts again from the current basis and creates a fresh inverse
representation, discarding or replacing the accumulated factor history.
The right time to reinvert balances the cost of rebuilding against the cost
and numerical drift of continuing to apply old factors.

Sparse reinversion seeks pivot choices that keep intermediate matrices sparse.
The pages describe ordering candidate pivots by the number of nonzero
elements they would create, while respecting rows and columns already used.
The central tradeoff is:

- A numerically valid pivot may create many new nonzeros and cause fill-in.
- A sparse pivot reduces storage and arithmetic, but should not be chosen at
  the expense of numerical reliability.
- Row and column incidence counts can cheaply estimate fill-in before
  constructing the full updated matrix.
- Reordering and partitioning the matrix into structural blocks can make
  storage and pivot searches more efficient.

The practical sparse-inversion procedure keeps track of which rows and
columns are still available, counts their nonzero entries, selects a pivot
that balances fill-in against usability, updates the remaining matrix, and
repeats. If a sparse path is exhausted, the method can relax its selection
criteria rather than treating that as proof that the original matrix is
singular.

Storage constraints matter too. Implementations may keep row and column
incidence lists, use searches to reconstruct one list from the other, or
spill transformation data to auxiliary storage. Such choices change the
tradeoff between memory, data movement, arithmetic, and precision; they do
not change the mathematical goal of applying the current basis inverse.

## 9. Connection to the examples in this repository

The `smpl*.m` programs gradually implement the ideas summarized above:

| Program | Focus |
|---|---|
| [`smpl1.m`](../smpl1.m) | Update the complete tableau at each pivot |
| [`smpl2.m`](../smpl2.m) | Keep the original tableau and update the right-hand side using an explicit inverse |
| [`smpl3.m`](../smpl3.m) | Store pivot and eta data, then perform forward column transforms |
| [`smpl4.m`](../smpl4.m) | Add backward row transformation for pricing |
| [`smpl5.m`](../smpl5.m) | Use prices to choose an entering column |
| [`smpl6.m`](../smpl6.m) | Add a ratio test to choose the leaving row |

The progression isolates the mechanics: first verify pivots in a full
tableau, then separate the basis transformation, record its factors, use
them in both directions, and finally automate entering and leaving
selection.
