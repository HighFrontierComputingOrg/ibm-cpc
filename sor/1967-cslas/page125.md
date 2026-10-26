# Page 125: First SOR Cycle

This page continues the grid example from page 124. It updates the six
interior values in order, using each newly computed value immediately in
later updates in the same SOR pass. Values are rounded to three significant
decimal digits.

Starting with the values from page 124, the update formulas and results are:

| Component | Update | New value |
|---|---|---:|
| \(v_1\) | already updated on page 124 | 0.425 |
| \(v_2\) | \((1 + v_1 + v_5 + v_3)/4\) | 0.533 |
| \(v_3\) | \((1 + v_2 + v_6 + 0)/4\) | 0.408 |
| \(v_4\) | \((v_1 + 0 + 0 + v_5)/4\) | 0.181 |
| \(v_5\) | \((v_2 + v_4 + 0 + v_6)/4\) | 0.204 |
| \(v_6\) | \((v_3 + v_5 + 0 + 0)/4\) | 0.153 |

For example, when computing \(v_2\), the current values are
\(v_1=0.425\), \(v_5=0.300\), and \(v_3=0.400\). The sum is rounded to
three significant digits before division:

\[
v_2 = \frac{1.00 + 0.425 + 0.300 + 0.400}{4}
    \approx \frac{2.13}{4}
    \approx 0.533.
\]

After this cycle, the interior grid is:

| \(v_1=0.425\) | \(v_2=0.533\) | \(v_3=0.408\) |
|---:|---:|---:|
| \(v_4=0.181\) | \(v_5=0.204\) | \(v_6=0.153\) |

The boundary values remain unchanged: 1 along the top and 0 along the other
edges. In SOR, each component is replaced by its new value before calculating
the next component.

The original page image is available in [page125.png](page125.png).
