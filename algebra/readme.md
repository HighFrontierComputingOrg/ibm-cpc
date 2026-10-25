# Repeated Complex Squaring

This Python example reproduces the values in
[Feynman's Table 22-3](https://www.feynmanlectures.caltech.edu/I_22.html).

It demonstrates how rounding and floating-point precision affect repeated
calculations.

## Mathematics

The calculation starts with a complex number close to `10^(i/1024)`, where
`i` is the imaginary unit. In polar form, the ideal value has angle
`theta = ln(10)/1024`, approximately `0.00224861825` radians.

### Starting value

Rather than calculate that ideal value directly, the program uses the nearby
approximation:

| Component | Value |
|---|---:|
| `y0` | `0.00225` |
| `x0` | `sqrt(1 - y0*y0)`, approximately `0.99999747` |
| `z0` | `x0 + i*y0` |

This makes `z0` lie on the unit circle, but its angle is approximately
`0.00225000190` radians—not exactly `ln(10)/1024`. That small difference
becomes more visible after repeated squaring.

### Repeated squaring

Write the current value as `zn = xn + i*yn`. Squaring it gives the next
value:

| Next component | Update |
|---|---|
| `x(n+1)` | `xn*xn - yn*yn` |
| `y(n+1)` | `2*xn*yn` |

Equivalently, `z(n+1) = zn*zn`, so after `n` updates,
`zn = z0^(2^n)`. Each update doubles the angle. After ten updates, the
ideal sequence reaches `10^i`; the program's approximate starting value
produces a nearby result.

The program prints each pair before updating it. Its eleven output rows are
therefore `z0` through `z10` (the initial value plus ten updates). Printed
values are rounded to five digits after the decimal point; those rounded
strings are not fed back into the calculation.

## Run the example

From the repository root:

```sh
.venv/bin/python algebra/algebra.py
```

The calculation uses Python floating-point arithmetic. Its displayed digits
are rounded output, not the internal values used for the next iteration.

## Files

| File | Purpose |
|---|---|
| [`algebra.py`](algebra.py) | Python reference implementation |
