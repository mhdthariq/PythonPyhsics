# Example 3 & 4: Interactive Three-Body Systems

This folder contains advanced gravitational simulations implemented in a Jupyter notebook format, demonstrating both the Sun-Earth-Moon system and chaotic three-body dynamics.

## Files

### `Example3andExample4.ipynb`

A comprehensive Jupyter notebook containing two major simulations:

**Example 3: Sun-Earth-Moon System**

- Interactive three-body gravitational simulation
- Realistic astronomical parameters
- Real-time orbit visualization with trails
- Interactive controls for animation and zoom

**Example 4: Chaotic Three-Body Problem**

- Three equal-mass planets in chaotic motion
- Demonstrates sensitive dependence on initial conditions
- Long-term orbital instability visualization
- Advanced chaos theory concepts

## Key Features

### Interactive Controls

- **Play/Pause Animation**: Control simulation timing
- **Frame Slider**: Navigate through simulation steps
- **Zoom Control**: Adjust visualization scale
- **Real-time Updates**: Smooth animation with customizable speed

### Advanced Physics

- **Runge-Kutta 4th Order Integration**: High-precision numerical methods
- **Multi-body Gravitational Forces**: N-body problem implementation
- **Energy Conservation**: Accurate long-term dynamics
- **Realistic Parameters**: Based on actual astronomical data

### Visualization Features

- **Orbital Trails**: Track historical motion paths
- **Black Space Background**: Astronomical appearance
- **Color-coded Objects**: Easy identification of celestial bodies
- **Dynamic Labels**: Real-time information display

## Physics Concepts

### Three-Body Problem

The gravitational interaction between three or more bodies cannot be solved analytically, requiring numerical methods. This simulation demonstrates:

```
F₁₂ = G × (m₁ × m₂) / |r₁₂|² × r̂₁₂
```

Where each body experiences forces from all other bodies simultaneously.

### Chaos Theory

Example 4 demonstrates how small changes in initial conditions can lead to dramatically different long-term behavior - a hallmark of chaotic systems.

### Numerical Integration

Uses Runge-Kutta 4th order method for accurate integration:

```python
def rk4_integrator(pos, vel, dt):
    k1 = derivatives(pos)
    k2 = derivatives(pos + 0.5 * dt * k1)
    k3 = derivatives(pos + 0.5 * dt * k2)
    k4 = derivatives(pos + dt * k3)
    return pos + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
```

## Physical Parameters

### Example 3: Sun-Earth-Moon

```python
G = 6.67430e-11     # Gravitational constant
M_sun = 1.989e30    # Solar mass (kg)
M_earth = 5.972e24  # Earth mass (kg)
M_moon = 7.342e22   # Moon mass (kg)
AU = 1.496e11       # Earth-Sun distance (m)
MOON_DIST = 384.4e6 # Earth-Moon distance (m)
```

### Example 4: Chaotic System

```python
M = 6e24            # Equal planet masses (kg)
dt = 3000           # Time step: 50 minutes
total_time = 120    # Days of simulation
```

## How to Run

### Option 1: Google Colab (Recommended)

1. **Open Google Colab**: Go to [colab.research.google.com](https://colab.research.google.com)
2. **Upload Notebook**: Click "File" → "Upload notebook" → Select `Example3andExample4.ipynb`
3. **Run All Cells**: Click "Runtime" → "Run all" or run cells individually
4. **Interactive Controls**: Use the widgets to control the simulation

### Option 2: Local Jupyter

1. **Install Jupyter**:

   ```bash
   pip install jupyter ipywidgets matplotlib numpy
   ```

2. **Enable Widgets**:

   ```bash
   jupyter nbextension enable --py widgetsnbextension
   ```

3. **Start Jupyter**:

   ```bash
   jupyter notebook Example3andExample4.ipynb
   ```

4. **Run Cells**: Execute each cell in order

### Option 3: JupyterLab

1. **Install JupyterLab**:

   ```bash
   pip install jupyterlab
   ```

2. **Install Widget Extension**:

   ```bash
   jupyter labextension install @jupyter-widgets/jupyterlab-manager
   ```

3. **Launch**:
   ```bash
   jupyter lab Example3andExample4.ipynb
   ```

## Google Colab Setup Instructions

### Step-by-Step Guide:

1. **Access Google Colab**

   - Visit [colab.research.google.com](https://colab.research.google.com)
   - Sign in with your Google account

2. **Upload the Notebook**

   - Click "File" in the menu
   - Select "Upload notebook"
   - Choose `Example3andExample4.ipynb` from your device

3. **Install Required Packages** (if needed)

   ```python
   !pip install ipywidgets matplotlib numpy
   ```

4. **Run the Simulation**

   - Click "Runtime" → "Run all" to execute all cells
   - Or run cells individually by clicking the play button

5. **Interact with Controls**
   - Use the play button to start/stop animation
   - Drag the frame slider to navigate through time
   - Adjust zoom to see different scales
   - Watch the orbital dynamics unfold!

## Educational Objectives

### Understanding Multi-Body Dynamics

- Learn how gravitational forces work in complex systems
- Observe the difference between stable and chaotic motion
- Understand why the three-body problem requires numerical solutions

### Computational Physics Skills

- Experience with numerical integration methods
- Learn about the trade-offs between accuracy and computational speed
- Understand how small errors can accumulate over time

### Interactive Programming

- See how widgets can make scientific simulations more accessible
- Learn about real-time visualization techniques
- Understand the connection between mathematics and visual representation

## Technical Notes

### Performance Considerations

- Simulations use optimized NumPy operations for speed
- Frame rate can be adjusted via the `interval` parameter
- Larger zoom factors require more computation for trail rendering

### Accuracy and Limitations

- RK4 integration provides good accuracy for most timescales
- Very long simulations may show energy drift
- Real astronomical systems have additional factors not modeled here

### Customization Options

- Modify initial conditions to explore different scenarios
- Adjust time steps for different accuracy/speed trade-offs
- Change visualization parameters for different aesthetics

## Related Concepts

### Astronomical Applications

- **Lagrange Points**: Stable points in three-body systems
- **Binary Star Systems**: Two-body orbital dynamics
- **Trojan Asteroids**: Objects sharing planetary orbits
- **Spacecraft Trajectories**: Using gravitational assists

### Mathematical Connections

- **Differential Equations**: Systems of coupled ODEs
- **Vector Calculus**: Force and acceleration calculations
- **Linear Algebra**: State vector representations
- **Chaos Theory**: Sensitivity to initial conditions

This notebook provides an excellent introduction to computational astrophysics and demonstrates how complex physical systems can be studied through simulation and visualization.
