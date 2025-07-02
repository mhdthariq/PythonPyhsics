import numpy as np
import matplotlib.pyplot as plt

# --- Physical Constants ---
G = 6.67430e-11                 # Newtonian gravitational constant (m^3 kg^-1 s^-2)
SUN_MASS = 1.989e30             # Mass of the Sun in kg
AU = 1.496e11                   # 1 Astronomical Unit (AU) in meters
TIME_STEP = 60 * 60             # Time step: 1 hour (in seconds)
SIMULATION_STEPS = 24 * 365     # Number of simulation steps: 1 year (in hours)

# --- Initialize Earth's position and velocity ---
# Start at 1 AU on the x-axis
pos_x = AU
pos_y = 0
# Initial velocity is purely in the y-direction
vel_x = 0
vel_y = 29780  # Initial velocity of Earth (29.78 km/s)

# --- Arrays to store position history for plotting ---
x_history = []
y_history = []

# --- Motion Simulation Loop ---
for _ in range(SIMULATION_STEPS):
    # Calculate distance from the sun
    distance_to_sun = np.sqrt(pos_x**2 + pos_y**2)

    # Calculate gravitational acceleration using Newton's law: a = -G*M / r^2
    # We break it down into components by multiplying by (pos / r)
    total_acceleration = -G * SUN_MASS / distance_to_sun**3
    accel_x = total_acceleration * pos_x
    accel_y = total_acceleration * pos_y

    # Update velocity based on acceleration (v = v0 + a*t)
    vel_x += accel_x * TIME_STEP
    vel_y += accel_y * TIME_STEP

    # Update position based on new velocity (p = p0 + v*t)
    pos_x += vel_x * TIME_STEP
    pos_y += vel_y * TIME_STEP

    # Store the new position for plotting
    x_history.append(pos_x)
    y_history.append(pos_y)

# --- Visualization using Matplotlib ---
plt.figure(figsize=(8, 8))
# Plot the Sun at the origin
plt.plot(0, 0, 'yo', markersize=12, label='Sun')
# Plot the Earth's orbital path
plt.plot(np.array(x_history), np.array(y_history), '-b', label="Earth's Orbit")

# Formatting the plot
plt.axis('equal') # Ensure the orbit is not distorted
plt.xlabel("x-position (meters)")
plt.ylabel("y-position (meters)")
plt.title("Earth's Orbit Simulation around the Sun (Newtonian Method)")
plt.legend()
plt.grid(True)
plt.show()
