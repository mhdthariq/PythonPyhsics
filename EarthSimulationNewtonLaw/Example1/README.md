# Example 1: Basic Earth-Sun Orbital Simulation

This example demonstrates the fundamental concepts of orbital mechanics using Newton's Law of Universal Gravitation to simulate Earth's orbit around the Sun.

## Files Overview

### Basic Version
- **Example1.py** - Simple Earth-Sun orbit simulation using turtle graphics

### Enhanced Version (Improved)
- **Example1Enhance.py** - Object-oriented design with enhanced visuals and starfield background

## Physics Concepts

### Newton's Law of Universal Gravitation
The simulation is based on the fundamental gravitational law:

```
F = G × (M_sun × m_earth) / r²
```

### Gravitational Acceleration
The acceleration of Earth due to the Sun's gravity:

```
a = F/m = G × M_sun / r²
```

In component form:
```
ax = -G × M_sun × x / r³
ay = -G × M_sun × y / r³
```

Where:
- r = √(x² + y²) = distance from Sun to Earth
- r³ = (x² + y²)^(3/2)

### Numerical Integration (Euler Method)
Position and velocity updates:
```
vx(t+dt) = vx(t) + ax × dt
vy(t+dt) = vy(t) + ay × dt
x(t+dt) = x(t) + vx × dt
y(t+dt) = y(t) + vy × dt
```

## Physical Parameters

### Real Astronomical Values
```python
G = 6.67430e-11    # Gravitational constant (m³ kg⁻¹ s⁻²)
M_sun = 1.989e30   # Solar mass (kg)
AU = 1.496e11      # Astronomical Unit (m)
dt = 3600          # Time step: 1 hour (seconds)
v_earth = 29_780   # Earth's orbital velocity (m/s)
```

### Initial Conditions
- **Earth position**: (1 AU, 0) - starts at maximum distance on x-axis
- **Earth velocity**: (0, 29,780 m/s) - perpendicular to position vector
- **Sun position**: (0, 0) - fixed at origin

## Features Comparison

| Feature | Basic Version | Enhanced Version |
|---------|---------------|------------------|
| **Architecture** | Procedural programming | Object-oriented design |
| **Graphics** | Simple turtle graphics | Enhanced with starfield |
| **Code Organization** | Single script | Modular classes |
| **Visual Effects** | Basic Sun and Earth | Stars, labels, better scaling |
| **Animation** | Continuous loop | Timed animation frames |
| **Celestial Bodies** | Simple circles | CelestialBody class |

## Key Differences

### Basic Version (Example1.py)
- Simple while loop for animation
- Direct turtle manipulation
- Minimal visual elements
- Indonesian comments and variables
- Fixed scaling and colors

### Enhanced Version (Example1Enhance.py)
- **CelestialBody class**: Encapsulates mass, position, velocity, and graphics
- **Helper functions**: `draw_stars()` for background
- **Better organization**: Separated physics from graphics
- **Enhanced visuals**: Starfield background, better scaling
- **Modular design**: Easy to extend for multi-body systems

## Orbital Mechanics Demonstrated

### Circular vs Elliptical Orbits
The simulation can produce different orbit types depending on initial conditions:

- **Circular orbit**: v = √(GM/r) = 29,780 m/s at 1 AU
- **Elliptical orbit**: Different initial velocities create ellipses
- **Escape trajectory**: v > √(2GM/r) ≈ 42,100 m/s at 1 AU

### Conservation Laws
The simulation demonstrates:
1. **Conservation of Energy**: E = ½mv² - GMm/r = constant
2. **Conservation of Angular Momentum**: L = mvr sin(θ) = constant

## How to Run

1. **Basic version:**
   ```bash
   python Example1.py
   ```

2. **Enhanced version:**
   ```bash
   python Example1Enhance.py
   ```

## Learning Objectives

- Understand gravitational force calculations
- Learn basic numerical integration methods
- Visualize orbital motion in real-time
- Practice physics programming with Python
- Compare procedural vs object-oriented approaches
- Explore the relationship between initial conditions and orbital shapes

## Educational Value

This example serves as an introduction to:
- Computational physics
- Orbital mechanics
- Gravitational dynamics
- Scientific programming
- Real-time animation and visualization

The progression from basic to enhanced version demonstrates best practices in scientific software development and code organization.

## Real-World Applications

- Satellite orbit prediction
- Space mission trajectory planning
- Understanding planetary motion
- Asteroid and comet orbit calculations
- Basic astrophysics education

## Dependencies

- `turtle` - For graphics and animation
- `math` - For mathematical calculations
- `random` - For starfield generation (enhanced version)

## Next Steps

This example provides the foundation for more complex simulations like:
- Multi-planet systems (Example 2)
- Earth-Moon-Sun system (Example 3)
- Chaotic three-body problems (Example 4)