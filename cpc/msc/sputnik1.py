import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# This straight-line model illustrates range-rate Doppler shift; it is not a
# full orbital model or a reconstruction of APL's historical computation.
def sputnik_doppler_model(t, f_0, t_ca, r_ca, v):
    """
    Model received frequency for a constant-speed, straight-line pass.

    The receiver is treated as stationary at the origin. ``r_ca`` is the
    minimum range, reached at ``t_ca``; ``v`` is the satellite's constant
    speed relative to the receiver.

    Parameters are time in seconds, carrier frequency in hertz, closest-
    approach time in seconds, minimum range in meters, and speed in meters
    per second, respectively.
    """
    c = 299792458.0  # Speed of light in meters per second

    # Pythagorean geometry gives the line-of-sight range at each time.
    slant_range = np.sqrt(r_ca**2 + (v * (t - t_ca))**2)

    # This derivative is negative while approaching and positive while receding.
    range_rate = (v**2 * (t - t_ca)) / slant_range

    # First-order classical Doppler approximation; positive range rate lowers
    # the received frequency, while negative range rate raises it.
    f_observed = f_0 * (1.0 - range_rate / c)
    return f_observed

# Generate repeatable synthetic observations, not measurements recovered
# from Sputnik 1 or archival APL tracking data.
np.random.seed(42)
true_f0 = 20.005e6      # Assumed carrier frequency for this example (Hz)
true_t_ca = 300.0       # Chosen closest-approach time (seconds)
true_r_ca = 900.0e3     # Chosen minimum range (meters)
true_v = 7800.0         # Chosen constant relative speed (meters per second)

# Sample the modeled pass at 60 evenly spaced times over ten minutes.
time_data = np.linspace(0, 600, 60)
# Add Gaussian noise with a 15 Hz standard deviation to the model frequencies.
clean_frequencies = sputnik_doppler_model(time_data, true_f0, true_t_ca, true_r_ca, true_v)
noise = np.random.normal(0, 15, size=time_data.shape)
observed_frequencies = clean_frequencies + noise

# Fit the four model parameters, starting from an intentionally rough guess.
# This least-squares demonstration is not a reproduction of APL's method.
initial_guess = [20.000e6, 250.0, 500.0e3, 7000.0]
estimated_params, covariance = curve_fit(
    sputnik_doppler_model,
    time_data,
    observed_frequencies,
    p0=initial_guess
)

est_f0, est_t_ca, est_r_ca, est_v = estimated_params

# Compare fitted parameters with the known values used to generate the data.
print("=== FIT TO SYNTHETIC DOPPLER OBSERVATIONS ===")
print(f"Fitted Carrier Frequency: {est_f0/1e6:.5f} MHz (Input: {true_f0/1e6:.5f} MHz)")
print(f"Fitted Closest-Approach Time: {est_t_ca:.2f} sec (Input: {true_t_ca:.2f} sec)")
print(f"Fitted Minimum Range: {est_r_ca/1000:.2f} km (Input: {true_r_ca/1000:.2f} km)")
print(f"Fitted Relative Speed: {est_v:.2f} m/s (Input: {true_v:.2f} m/s)")

# Plot the noisy synthetic observations and their fitted model.
fit_frequencies = sputnik_doppler_model(time_data, *estimated_params)

plt.figure(figsize=(10, 6))
plt.scatter(time_data, observed_frequencies / 1e6, color='red', alpha=0.6, label='Synthetic observations')
plt.plot(time_data, fit_frequencies / 1e6, color='navy', linewidth=2, label='Fitted Doppler model')
plt.title('Fitting a Synthetic Doppler Pass', fontsize=14, fontweight='bold')
plt.xlabel('Time Elapsed (Seconds)', fontsize=12)
plt.ylabel('Observed Frequency (MHz)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.show()
