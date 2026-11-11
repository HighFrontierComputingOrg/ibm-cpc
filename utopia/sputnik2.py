import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

# Synthetic range-rate fitting exercise, not a reconstruction of Sputnik 1
# data or of the historical APL/UNIVAC orbit-determination work.
# --- 1. CONSTANTS & WORLD SETUP ---
GM = 3.986004418e14        # Earth's gravitational parameter (m^3/s^2)
R_EARTH = 6378137.0       # Radius of Earth (meters)
OMEGA_EARTH = 7.292115e-5 # Earth's rotation rate (rad/s)
C = 299792458.0           # Speed of light (m/s)

# Approximate APL latitude/longitude (radians below); note that the station
# function calls use lon_0's default of zero, so lon_station is not applied.
lat_station = np.radians(39.16)
lon_station = np.radians(-76.90)

def get_station_eci(t, lon_0=0.0):
    """Return a spherical-Earth station position rotating about the z-axis."""
    theta = lon_0 + OMEGA_EARTH * t
    x = R_EARTH * np.cos(lat_station) * np.cos(theta)
    y = R_EARTH * np.cos(lat_station) * np.sin(theta)
    z = R_EARTH * np.sin(lat_station)
    return np.array([x, y, z])

def get_station_vel_eci(t, lon_0=0.0):
    """Return the station's velocity from the same z-axis rotation model."""
    theta = lon_0 + OMEGA_EARTH * t
    vx = -R_EARTH * OMEGA_EARTH * np.cos(lat_station) * np.sin(theta)
    vy =  R_EARTH * OMEGA_EARTH * np.cos(lat_station) * np.cos(theta)
    vz = 0.0
    return np.array([vx, vy, vz])

# --- 2. SIMPLIFIED ORBIT MODEL ---
def propagate_orbit(state_0, times):
    """Generate approximate positions and velocities from an initial state.

    This is illustrative rather than a rigorous state propagator: its direct
    coordinate construction and tangential-only velocity are approximations.
    """
    r0, v0 = state_0[:3], state_0[3:]
    pos_rec, vel_rec = [], []

    # Derive two-body quantities from the supplied initial position and speed.
    h = np.cross(r0, v0)
    h_norm = np.linalg.norm(h)
    r0_norm = np.linalg.norm(r0)
    v0_norm = np.linalg.norm(v0)

    # Specific orbital energy gives a; the eccentricity-vector magnitude gives e.
    energy = (v0_norm**2 / 2.0) - (GM / r0_norm)
    a = -GM / (2.0 * energy)
    e_vec = ((v0_norm**2 - GM/r0_norm)*r0 - np.dot(r0, v0)*v0) / GM
    e = np.linalg.norm(e_vec)

    # Keplerian mean motion for this assumed bound two-body orbit.
    n = np.sqrt(GM / a**3)

    # Solve Kepler's equation independently for each elapsed time.
    for t in times:
        dt = t
        M = n * dt
        # Five Newton steps provide the eccentric anomaly for this example.
        E = M
        for _ in range(5):
            E = E - (E - e*np.sin(E) - M) / (1.0 - e*np.cos(E))

        # Standard ellipse coordinates in the orbital plane.
        x_plane = a * (np.cos(E) - e)
        y_plane = a * np.sqrt(1.0 - e**2) * np.sin(E)

        # Approximate plane-to-ECI mapping using normalized initial vectors.
        # These are not an orthonormal perifocal basis, so positions are not a
        # rigorous Keplerian ephemeris for a general initial state.
        pos = (r0 / r0_norm) * x_plane + (v0 / v0_norm) * y_plane
        # This gives only a tangential velocity; eccentric-orbit radial motion
        # is omitted, another reason to treat this propagator as illustrative.
        vel = np.cross(h, pos) / (np.linalg.norm(pos)**2)

        pos_rec.append(pos)
        vel_rec.append(vel)

    return np.array(pos_rec), np.array(vel_rec)

# --- 3. FREQUENCY RESIDUALS FOR THE RANGE-RATE FIT ---
def range_rate_frequency_residuals(state_guess, times, observed_freqs, f0_guess):
    """Return predicted-minus-observed frequencies for a candidate state."""
    pos_sat, vel_sat = propagate_orbit(state_guess, times)
    residuals = []

    for i, t in enumerate(times):
        r_st = get_station_eci(t)
        v_st = get_station_vel_eci(t)

        # Relative vectors
        rho = pos_sat[i] - r_st
        rho_norm = np.linalg.norm(rho)
        v_rel = vel_sat[i] - v_st

        # Project relative velocity along the station-to-satellite line of sight.
        range_rate = np.dot(rho, v_rel) / rho_norm

        # First-order frequency-shift model driven by range rate; f0 is fixed.
        f_pred = f0_guess * (1.0 - range_rate / C)
        residuals.append(f_pred - observed_freqs[i])

    return np.array(residuals)

# --- 4. SYNTHETIC DATA AND STATE FIT ---
# Chosen input state for this simulation, not historical Sputnik 1 elements.
true_pos = np.array([4500.0e3, 5200.0e3, 2000.0e3]) # ECI meters
true_vel = np.array([-5200.0,  3800.0,  3000.0])   # ECI m/s
true_state = np.concatenate([true_pos, true_vel])
true_f0 = 20.005e6

times = np.linspace(0, 900, 45) # 45 samples spanning a synthetic 15-minute arc

# Generate synthetic frequencies with the same approximate model used in fitting.
pos_sat_true, vel_sat_true = propagate_orbit(true_state, times)
observed_freqs = []
for i, t in enumerate(times):
    rho = pos_sat_true[i] - get_station_eci(t)
    range_rate = np.dot(rho, vel_sat_true[i] - get_station_vel_eci(t)) / np.linalg.norm(rho)
    # Unseeded Gaussian noise means each run uses a different noisy data set.
    observed_freqs.append(true_f0 * (1.0 - range_rate / C) + np.random.normal(0, 8.0))

# Deliberately different optimizer start, not a historical APL initial guess.
blind_state_guess = np.array([4000.0e3, 5000.0e3, 1500.0e3, -4800.0, 4200.0, 2500.0])

# Fit six initial-state components while holding the carrier frequency fixed.
result = least_squares(
    range_rate_frequency_residuals,
    blind_state_guess,
    args=(times, observed_freqs, true_f0),
)
est_state = result.x

# --- 5. REPORT TWO ORBITAL METRICS ---
def state_to_elements(state):
    r, v = state[:3], state[3:]
    r_mag, v_mag = np.linalg.norm(r), np.linalg.norm(v)
    h = np.cross(r, v)
    h_mag = np.linalg.norm(h)

    # This helper reports only semi-major axis and inclination, not all six
    # classical orbital elements.
    a = 1.0 / (2.0/r_mag - v_mag**2/GM)
    i = np.degrees(np.arccos(h[2] / h_mag))

    return a, i

true_a, true_i = state_to_elements(true_state)
est_a, est_i = state_to_elements(est_state)

print("=== RECONSTRUCTED ORBITAL METRICS ===")
print(f"Estimated Semi-Major Axis: {est_a/1000:.2f} km (True: {true_a/1000:.2f} km)")
print(f"Estimated Orbit Inclination: {est_i:.2f}° (True: {true_i:.2f}°)")

# Plot synthetic observations and model predictions. These legacy labels do
# not indicate historical transcriptions or a UNIVAC computation.
plt.figure(figsize=(9, 5))
plt.plot(times, np.array(observed_freqs)/1e6, 'ro', label='Station Transcriptions')
initial_residuals = range_rate_frequency_residuals(
    blind_state_guess, times, observed_freqs, true_f0
)
# Adding predicted-minus-observed residuals back to observations gives predictions.
plt.plot(times, (observed_freqs + initial_residuals)/1e6, 'k--', label='Initial Wrong Guess Track')
final_residuals = range_rate_frequency_residuals(
    est_state, times, observed_freqs, true_f0
)
plt.plot(times, (observed_freqs + final_residuals)/1e6, 'b-', linewidth=2, label='UNIVAC Reconstructed Path')
plt.ylabel("Frequency (MHz)")
plt.xlabel("Time Passed (Seconds)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
