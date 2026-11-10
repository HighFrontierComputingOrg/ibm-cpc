# Sputnik 1 and Doppler tracking

Sputnik 1's launch on October 4, 1957, made its radio beacon an unexpected
source of information about the satellite's motion. William Guier and George
Weiffenbach at the Johns Hopkins Applied Physics Laboratory (APL) studied
the changing frequency of signals from Earth satellites. Their 1958 paper
describes the theoretical analysis of those Doppler signals; a later paper
describes how satellite Doppler measurements could be used for navigation
([sources](#historical-sources)).

The basic measurement is a change in **range rate**: a satellite moving
toward a receiving station makes the received frequency slightly higher,
while one moving away makes it lower. A series of frequency measurements
through a pass therefore traces the satellite's motion along the
station-to-satellite line of sight. It does not directly measure the
satellite's full position or velocity.

## What this example models

The [Python script](sputnik1.py) demonstrates that principle with a deliberately
small straight-line model. It places the receiver at the origin and lets the
satellite pass at constant speed `v`, at a closest distance `r_ca` and time
`t_ca`. The resulting range is

```text
range(t) = sqrt(r_ca^2 + (v * (t - t_ca))^2)
```

Differentiating the range gives its signed rate of change:

```text
range_rate(t) = v^2 * (t - t_ca) / range(t)
```

The script uses the first-order classical Doppler approximation

```text
f_observed(t) = f_0 * (1 - range_rate(t) / c)
```

where `f_0` is the assumed transmitted frequency and `c` is the speed of
light. Before closest approach the range rate is negative and the modeled
frequency is above `f_0`; afterward the range rate is positive and the
frequency is below `f_0`.

This geometry is useful for seeing how a Doppler curve depends on four
parameters: carrier frequency, time of closest approach, minimum range, and
constant speed. It is not a full orbital model. In particular, it leaves out
Earth's rotation and curvature, orbital acceleration, station coordinates,
atmospheric propagation effects, and transmitter-frequency variation.

## Synthetic observations and fitting

The program creates 60 observations over a ten-minute interval from chosen
parameter values, then adds reproducible, zero-mean Gaussian noise with a
15 Hz standard deviation. These are synthetic data, not digitized recordings
from Sputnik 1 or measurements from APL.

`scipy.optimize.curve_fit` then adjusts the four model parameters to minimize
the squared frequency residuals. The initial parameter values are deliberately
approximate. Comparing the fit with the values used to generate the data is a
self-consistency check of this toy model; it is not an estimate of Sputnik
1's actual orbit and does not reproduce the historical orbit-determination
procedure.

## From orbit determination to navigation

Guier and Weiffenbach's early work treated Doppler observations as a way to
learn about a satellite's orbit. The inverse question is also useful: when a
satellite's orbit is known, can its changing Doppler shift help determine a
receiver's position? This principle became the basis of the U.S. Navy's
Transit satellite navigation system. Transit was an important predecessor
to later satellite navigation systems, although it did not work like modern
GPS, which determines position using signals from multiple satellites.

The simple script here illustrates only the range-rate measurement at the
heart of that history. Real orbit determination and navigation require
orbital geometry and a much more complete treatment of the measurements.

## Historical sources

- NASA, [“The Dawn of the Space Age”](https://www.nasa.gov/history/dawn-of-the-space-age/),
  for the date and context of Sputnik 1's launch.
- William H. Guier and George C. Weiffenbach, [“Theoretical Analysis of
  Doppler Radio Signals from Earth Satellites,”](https://doi.org/10.1038/1811525a0)
  *Nature* 181, no. 4622 (1958), 1525–1526.
- William H. Guier and George C. Weiffenbach, [“A Satellite Doppler
  Navigation System,”](https://doi.org/10.1109/JRPROC.1960.287399)
  *Proceedings of the IRE* 48, no. 4 (1960), 507–516.
