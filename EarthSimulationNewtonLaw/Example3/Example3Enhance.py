import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider, Play, VBox, HBox, jslink
from IPython.display import display
from typing import Tuple, Optional

# Physical Constants
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³/kg·s²
MASS_SUN = 1.989e30                   # kg
MASS_EARTH = 5.972e24                 # kg
MASS_MOON = 7.342e22                  # kg
ASTRONOMICAL_UNIT = 1.496e11          # meters (Earth-Sun distance)
EARTH_MOON_DISTANCE = 384.4e6         # meters
EARTH_ORBITAL_VELOCITY = 29_780       # m/s
MOON_ORBITAL_VELOCITY = 1022          # m/s

# Simulation Parameters
TIME_STEP = 900                       # seconds (15 minutes per step)
SIMULATION_DAYS = 120                 # total simulation period
TOTAL_STEPS = int((SIMULATION_DAYS * 24 * 3600) / TIME_STEP)

# Initial State Vector: [x, y, velocity_x, velocity_y] for Sun, Earth, Moon
initial_state = np.array([
    # Sun at origin (stationary initially)
    0.0, 0.0, 0.0, 0.0,
    # Earth at 1 AU from Sun, moving perpendicular to radius
    ASTRONOMICAL_UNIT, 0.0, 0.0, EARTH_ORBITAL_VELOCITY,
    # Moon relative to Earth, moving in same direction as Earth plus orbital velocity
    ASTRONOMICAL_UNIT + EARTH_MOON_DISTANCE, 0.0, 0.0, EARTH_ORBITAL_VELOCITY + MOON_ORBITAL_VELOCITY
], dtype='float64')

def calculate_gravitational_acceleration(x1: float, y1: float, x2: float, y2: float, mass2: float) -> Tuple[float, float]:
    """
    Calculate gravitational acceleration of object 1 due to object 2

    Parameters:
    x1, y1: position of object 1
    x2, y2: position of object 2
    mass2: mass of object 2

    Returns:
    tuple: (acceleration_x, acceleration_y)
    """
    distance_x = x2 - x1
    distance_y = y2 - y1
    distance = np.hypot(distance_x, distance_y) + 1e-5  # Small value to prevent division by zero
    distance_cubed = distance**3

    acceleration_x = GRAVITATIONAL_CONSTANT * mass2 * distance_x / distance_cubed
    acceleration_y = GRAVITATIONAL_CONSTANT * mass2 * distance_y / distance_cubed

    return acceleration_x, acceleration_y

def calculate_derivatives(current_state: np.ndarray) -> np.ndarray:
    """
    Calculate derivatives for the three-body system (Sun-Earth-Moon)

    Parameters:
    current_state: array containing [x, y, vx, vy] for each body

    Returns:
    numpy array: derivatives [vx, vy, ax, ay] for each body
    """
    # Extract positions and velocities for each body
    sun_x, sun_y, sun_vx, sun_vy = current_state[0:4]
    earth_x, earth_y, earth_vx, earth_vy = current_state[4:8]
    moon_x, moon_y, moon_vx, moon_vy = current_state[8:12]

    # Calculate Sun's acceleration (affected by Earth and Moon)
    sun_accel_from_earth = calculate_gravitational_acceleration(sun_x, sun_y, earth_x, earth_y, MASS_EARTH)
    sun_accel_from_moon = calculate_gravitational_acceleration(sun_x, sun_y, moon_x, moon_y, MASS_MOON)
    sun_acceleration_x = sun_accel_from_earth[0] + sun_accel_from_moon[0]
    sun_acceleration_y = sun_accel_from_earth[1] + sun_accel_from_moon[1]

    # Calculate Earth's acceleration (affected by Sun and Moon)
    earth_accel_from_sun = calculate_gravitational_acceleration(earth_x, earth_y, sun_x, sun_y, MASS_SUN)
    earth_accel_from_moon = calculate_gravitational_acceleration(earth_x, earth_y, moon_x, moon_y, MASS_MOON)
    earth_acceleration_x = earth_accel_from_sun[0] + earth_accel_from_moon[0]
    earth_acceleration_y = earth_accel_from_sun[1] + earth_accel_from_moon[1]

    # Calculate Moon's acceleration (affected by Sun and Earth)
    moon_accel_from_sun = calculate_gravitational_acceleration(moon_x, moon_y, sun_x, sun_y, MASS_SUN)
    moon_accel_from_earth = calculate_gravitational_acceleration(moon_x, moon_y, earth_x, earth_y, MASS_EARTH)
    moon_acceleration_x = moon_accel_from_sun[0] + moon_accel_from_earth[0]
    moon_acceleration_y = moon_accel_from_sun[1] + moon_accel_from_earth[1]

    return np.array([
        sun_vx, sun_vy, sun_acceleration_x, sun_acceleration_y,
        earth_vx, earth_vy, earth_acceleration_x, earth_acceleration_y,
        moon_vx, moon_vy, moon_acceleration_x, moon_acceleration_y
    ])

def runge_kutta_4th_order_step(current_state: np.ndarray, time_step: float) -> np.ndarray:
    """
    Perform one step of 4th order Runge-Kutta integration

    Parameters:
    current_state: current state vector
    time_step: time step size

    Returns:
    numpy array: new state after one integration step
    """
    k1 = calculate_derivatives(current_state)
    k2 = calculate_derivatives(current_state + 0.5 * time_step * k1)
    k3 = calculate_derivatives(current_state + 0.5 * time_step * k2)
    k4 = calculate_derivatives(current_state + time_step * k3)

    return current_state + (time_step / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

# Run the simulation using RK4 integration
simulation_states = []
current_state = initial_state.copy()

print(f"Running simulation for {SIMULATION_DAYS} days with {TOTAL_STEPS} time steps...")
print(f"Time step: {TIME_STEP/60:.1f} minutes")

for step in range(TOTAL_STEPS):
    simulation_states.append(current_state.copy())
    current_state = runge_kutta_4th_order_step(current_state, TIME_STEP)

    # Progress indicator
    if step % (TOTAL_STEPS // 10) == 0:
        progress = (step / TOTAL_STEPS) * 100
        print(f"Progress: {progress:.0f}%")

simulation_states = np.array(simulation_states)

# Validation: Check initial and final positions
print("\n=== Simulation Results ===")
initial_earth_pos = simulation_states[0]
final_earth_pos = simulation_states[-1]
initial_moon_pos = simulation_states[0]
final_moon_pos = simulation_states[-1]

print(f"Initial Earth position: ({initial_earth_pos[4]/ASTRONOMICAL_UNIT:.3f} AU, {initial_earth_pos[5]/ASTRONOMICAL_UNIT:.3f} AU)")
print(f"Final Earth position: ({final_earth_pos[4]/ASTRONOMICAL_UNIT:.3f} AU, {final_earth_pos[5]/ASTRONOMICAL_UNIT:.3f} AU)")
print(f"Initial Moon position: ({initial_moon_pos[8]/ASTRONOMICAL_UNIT:.3f} AU, {initial_moon_pos[9]/ASTRONOMICAL_UNIT:.3f} AU)")
print(f"Final Moon position: ({final_moon_pos[8]/ASTRONOMICAL_UNIT:.3f} AU, {final_moon_pos[9]/ASTRONOMICAL_UNIT:.3f} AU)")

# Calculate and display orbital periods
earth_x_positions = []
earth_y_positions = []
for i in range(len(simulation_states)):
    earth_x_positions.append(simulation_states[i][4])
    earth_y_positions.append(simulation_states[i][5])
earth_x_array = np.array(earth_x_positions)
earth_y_array = np.array(earth_y_positions)
earth_distance_from_sun = np.sqrt(earth_x_array**2 + earth_y_array**2)
print(f"Earth orbital distance variation: {np.std(earth_distance_from_sun)/ASTRONOMICAL_UNIT:.6f} AU")

def plot_orbital_animation(frame_index: int, zoom_factor: float = 2.0, show_trails: bool = True, trail_length: Optional[int] = None) -> None:
    """
    Create animated plot of the three-body system

    Parameters:
    frame_index: current animation frame
    zoom_factor: zoom level for the plot
    show_trails: whether to show orbital trails
    trail_length: length of trails to show (None for full trails)
    """
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor("black")

    # Determine trail start index
    if trail_length is None or not show_trails:
        trail_start = 0
    else:
        trail_start = max(0, frame_index - trail_length)

    # Plot orbital trails
    if show_trails and frame_index > 1:
        # Earth orbit trail
        earth_trail_x = []
        earth_trail_y = []
        for j in range(trail_start, frame_index):
            earth_trail_x.append(simulation_states[j][4])
            earth_trail_y.append(simulation_states[j][5])
        ax.plot(earth_trail_x, earth_trail_y,
                'cyan', linewidth=1.2, alpha=0.7, label='Earth Orbit')

        # Moon orbit trail
        moon_trail_x = []
        moon_trail_y = []
        for j in range(trail_start, frame_index):
            moon_trail_x.append(simulation_states[j][8])
            moon_trail_y.append(simulation_states[j][9])
        ax.plot(moon_trail_x, moon_trail_y,
                'lightgray', linewidth=0.8, alpha=0.6, label='Moon Orbit')

    # Plot current positions of celestial bodies
    current_frame_state = simulation_states[frame_index]
    ax.plot(current_frame_state[0], current_frame_state[1],
            'yellow', marker='o', markersize=12, label='Sun')
    ax.plot(current_frame_state[4], current_frame_state[5],
            'blue', marker='o', markersize=8, label='Earth')
    ax.plot(current_frame_state[8], current_frame_state[9],
            'white', marker='o', markersize=4, label='Moon')

    # Set plot limits and appearance
    plot_limit = zoom_factor * ASTRONOMICAL_UNIT
    ax.set_xlim(-plot_limit, plot_limit)
    ax.set_ylim(-plot_limit, plot_limit)
    ax.set_aspect('equal')

    # Calculate current day
    current_day = frame_index * TIME_STEP / (24 * 3600)
    ax.set_title(f'Three-Body System Simulation - Day {current_day:.1f}',
                color='white', fontsize=14, pad=20)

    # Customize plot appearance
    ax.tick_params(colors='white', labelsize=10)
    ax.set_xlabel('Distance (m)', color='white', fontsize=12)
    ax.set_ylabel('Distance (m)', color='white', fontsize=12)

    for spine in ax.spines.values():
        spine.set_edgecolor('white')

    # Add legend
    ax.legend(facecolor='black', labelcolor='white', loc='upper right',
              framealpha=0.8, fontsize=10)

    # Add grid for better visualization
    ax.grid(True, color='gray', alpha=0.3, linestyle='--', linewidth=0.5)

    plt.tight_layout()
    plt.show()

# Create interactive widgets for animation control
animation_play_button = Play(
    min=0,
    max=len(simulation_states) - 1,
    step=1,
    interval=50,  # milliseconds between frames
    description='Play Animation'
)

frame_slider = IntSlider(
    min=0,
    max=len(simulation_states) - 1,
    step=1,
    description='Frame:'
)

zoom_control = FloatSlider(
    value=2.0,
    min=0.5,
    max=5.0,
    step=0.1,
    description='Zoom Level:'
)

trail_length_control = IntSlider(
    value=500,
    min=10,
    max=2000,
    step=50,
    description='Trail Length:'
)

# Link play button with frame slider
jslink((animation_play_button, 'value'), (frame_slider, 'value'))

# Create control panel layout
animation_controls = HBox([animation_play_button, frame_slider])
display_controls = HBox([zoom_control, trail_length_control])

# Create interactive animation
def interactive_animation(frame_index: int, zoom_factor: float, trail_length: int) -> None:
    plot_orbital_animation(frame_index, zoom_factor, True, trail_length)

animation_interface = interact(
    interactive_animation,
    frame_index=frame_slider,
    zoom_factor=zoom_control,
    trail_length=trail_length_control
)

# Display all controls
print("\n=== Interactive Animation Controls ===")
print("Use the controls below to explore the three-body simulation:")
display(VBox([animation_controls, display_controls]))

# Additional analysis functions
def calculate_system_energy(state_index: int) -> float:
    """Calculate total energy of the system at a given time step"""
    state = simulation_states[state_index]

    # Kinetic energy
    kinetic_energy = 0.5 * (
        MASS_SUN * (state[2]**2 + state[3]**2) +
        MASS_EARTH * (state[6]**2 + state[7]**2) +
        MASS_MOON * (state[10]**2 + state[11]**2)
    )

    # Potential energy
    sun_earth_dist = np.hypot(state[4] - state[0], state[5] - state[1])
    sun_moon_dist = np.hypot(state[8] - state[0], state[9] - state[1])
    earth_moon_dist = np.hypot(state[8] - state[4], state[9] - state[5])

    potential_energy = -(
        GRAVITATIONAL_CONSTANT * MASS_SUN * MASS_EARTH / sun_earth_dist +
        GRAVITATIONAL_CONSTANT * MASS_SUN * MASS_MOON / sun_moon_dist +
        GRAVITATIONAL_CONSTANT * MASS_EARTH * MASS_MOON / earth_moon_dist
    )

    return kinetic_energy + potential_energy

# Energy conservation check
initial_energy = calculate_system_energy(0)
final_energy = calculate_system_energy(-1)
energy_conservation_error = abs((final_energy - initial_energy) / initial_energy) * 100

print("\n=== Energy Conservation Analysis ===")
print(f"Initial system energy: {initial_energy:.3e} J")
print(f"Final system energy: {final_energy:.3e} J")
print(f"Energy conservation error: {energy_conservation_error:.6f}%")

if energy_conservation_error < 0.1:
    print("✓ Excellent energy conservation!")
elif energy_conservation_error < 1.0:
    print("✓ Good energy conservation")
else:
    print("⚠ Poor energy conservation - consider smaller time step")
