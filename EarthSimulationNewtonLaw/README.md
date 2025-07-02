# Earth Simulation using Newton's Law

This folder contains multiple examples demonstrating orbital mechanics using Newton's Law of Universal Gravitation. Each example builds upon the previous one, showing progressively more complex simulations of celestial body motion.

## Folder Structure

### Example 1 - Basic Earth-Sun System

- **Example1.py** - Basic orbit simulation using turtle graphics
- **Example1Enhance.py** - Enhanced version with object-oriented design and stars _(improved version)_

### Example 2 - Mathematical Orbit Analysis

- **Example2.py** - Mathematical orbit simulation using matplotlib
- **Example2Enhance.py** - Enhanced version with advanced visualization _(improved version)_

### Example 3 & 4 - Interactive Three-Body Systems (Jupyter Notebook)

- **Example3andExample4.ipynb** - Combined notebook with both Sun-Earth-Moon system and chaotic three-body dynamics
  - Example 3: Interactive Sun-Earth-Moon system with realistic parameters
  - Example 4: Chaotic three-planet system demonstrating chaos theory
  - Interactive controls with play/pause, frame navigation, and zoom
  - Optimized for Google Colab with step-by-step instructions

## Physics Concepts

### Newton's Law of Universal Gravitation

All simulations are based on Newton's fundamental law:

```
F = G × (m₁ × m₂) / r²
```

Where:

- F = gravitational force between two objects
- G = gravitational constant (6.67430 × 10⁻¹¹ m³ kg⁻¹ s⁻²)
- m₁, m₂ = masses of the two objects
- r = distance between the centers of the objects

### Force and Acceleration

From Newton's second law:

```
F = ma
a = F/m = (G × M) / r² × (r̂)
```

In component form:

```
aₓ = -G × M × x / r³
aᵧ = -G × M × y / r³
```

Where r³ = (x² + y²)^(3/2)

### Numerical Integration

Position and velocity updates using Euler's method:

```
v(t+dt) = v(t) + a(t) × dt
r(t+dt) = r(t) + v(t) × dt
```

For more accurate simulations, Runge-Kutta 4th order method is used:

```
k₁ = f(t, y)
k₂ = f(t + dt/2, y + dt×k₁/2)
k₃ = f(t + dt/2, y + dt×k₂/2)
k₄ = f(t + dt, y + dt×k₃)
y(t+dt) = y(t) + dt/6 × (k₁ + 2k₂ + 2k₃ + k₄)
```

## Example Progression

### Example 1: Earth-Sun System

**Purpose**: Basic orbital mechanics demonstration

**Key Concepts**:

- Single planet orbiting a central star
- Circular/elliptical orbit formation
- Real-time visualization with turtle graphics

**Physical Parameters**:

- Earth mass: 5.972 × 10²⁴ kg
- Sun mass: 1.989 × 10³⁰ kg
- Earth orbital velocity: 29,780 m/s
- Earth-Sun distance: 1 AU (1.496 × 10¹¹ m)

### Example 2: Mathematical Analysis

**Purpose**: Orbit plotting and analysis

**Key Concepts**:

- Complete orbital paths visualization
- Matplotlib for scientific plotting
- Orbital period calculation
- Energy conservation analysis

### Example 3: Three-Body Problem

**Purpose**: Sun-Earth-Moon system

**Key Concepts**:

- Multi-body gravitational interactions
- Barycentric motion
- Interactive parameter control
- Complex orbital dynamics

**Additional Parameters**:

- Moon mass: 7.342 × 10²² kg
- Earth-Moon distance: 384,400 km
- Moon orbital velocity: 1,022 m/s

### Example 4: Chaotic Dynamics

**Purpose**: Three-planet chaotic system

**Key Concepts**:

- Sensitive dependence on initial conditions
- Chaotic motion in gravitational systems
- Long-term orbital stability
- Complex multi-body interactions

## Features Comparison

| Feature            | Basic Versions       | Enhanced Versions         |
| ------------------ | -------------------- | ------------------------- |
| **Graphics**       | Simple visualization | Enhanced with backgrounds |
| **Code Structure** | Procedural           | Object-oriented design    |
| **Interactivity**  | Limited              | Interactive controls      |
| **Accuracy**       | Euler integration    | RK4 integration           |
| **Visual Effects** | Basic shapes         | Stars, trails, labels     |
| **User Interface** | None/Basic           | Modern widgets            |

## Real Physical Constants Used

```python
G = 6.67430e-11     # Gravitational constant (m³ kg⁻¹ s⁻²)
M_sun = 1.989e30    # Solar mass (kg)
M_earth = 5.972e24  # Earth mass (kg)
M_moon = 7.342e22   # Moon mass (kg)
AU = 1.496e11       # Astronomical Unit (m)
```

## Learning Objectives

- Understand Newton's Law of Universal Gravitation
- Learn numerical integration methods
- Explore orbital mechanics and celestial dynamics
- Practice scientific programming and visualization
- Understand multi-body gravitational systems
- Explore chaotic dynamics in physics

## Real-World Applications

- **Satellite Orbit Prediction**: GPS, communication satellites
- **Space Mission Planning**: Trajectory calculations
- **Planetary Science**: Understanding planetary formation
- **Asteroid Tracking**: Near-Earth object monitoring
- **Binary Star Systems**: Stellar dynamics
- **Galaxy Formation**: Large-scale structure evolution

## Dependencies

- `turtle` - Real-time orbit visualization
- `numpy` - Numerical computations
- `matplotlib` - Scientific plotting
- `ipywidgets` - Interactive controls (Example 3 & 4)
- `IPython` - Jupyter notebook integration

## How to Run

1. **For turtle graphics examples:**

   ```bash
   python Example1/Example1.py
   python Example1/Example1Enhance.py
   ```

2. **For matplotlib examples:**

   ```bash
   python Example2/Example2.py
   python Example2/Example2Enhance.py
   ```

3. **For interactive examples (Jupyter recommended):**

   ```bash
   jupyter notebook Example3/Example3.py
   jupyter notebook Example4/Example4.py
   ```

4. **For the combined Jupyter notebook (Example 3 & 4):**

   **Option A: Google Colab (Recommended)**

   - Go to [colab.research.google.com](https://colab.research.google.com)
   - Upload `Example3and4/Example3andExample4.ipynb`
   - Run all cells and interact with the widgets

   **Option B: Local Jupyter**

   ```bash
   pip install jupyter ipywidgets matplotlib numpy
   jupyter nbextension enable --py widgetsnbextension
   jupyter notebook Example3and4/Example3andExample4.ipynb
   ```

## Mathematical Background

### Orbital Velocity

For circular orbits:

```
v = √(GM/r)
```

### Orbital Period

Kepler's Third Law:

```
T² = (4π²/GM) × r³
```

### Energy Conservation

Total energy in gravitational system:

```
E = ½mv² - GMm/r
```

### Escape Velocity

Minimum velocity to escape gravitational field:

```
v_escape = √(2GM/r)
```

This collection provides a comprehensive introduction to computational orbital mechanics and gravitational physics simulation.
