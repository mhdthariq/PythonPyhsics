# Planetary Orbits Simulation

This folder contains simulations of planetary motion in our solar system, demonstrating orbital mechanics and the relationships between different planets' orbital characteristics.

## Files Overview

### Indonesian Version (First Version)
- **OrbitPlanet.py** - Basic planetary orbit simulation with interactive controls

### English Version (Enhanced/Improved)
- **PlanetaryOrbits.py** - Enhanced solar system simulation with advanced controls *(improved version of OrbitPlanet.py)*

## Physics Concepts

### Orbital Motion
The simulations demonstrate planetary motion using circular orbital approximations.

**Mathematical Formula:**
```
x = d · cos(θ)
y = d · sin(θ)
```

Where:
- d = orbital distance from the Sun
- θ = angular position (angle in radians)
- (x, y) = planet's position coordinates

**Angular Velocity:**
```
θ(t) = θ₀ + ωt
ω = angular speed (degrees per frame)
```

### Kepler's Third Law (Simplified)
The relationship between orbital period and distance:
```
T² ∝ r³
```

Where:
- T = orbital period
- r = orbital radius

### Real Planetary Data (Approximated)
- **Mercury**: Closest to Sun, fastest orbit
- **Venus**: Second planet, moderate speed
- **Earth**: Third planet, reference for 1 AU
- **Mars**: Fourth planet, slower orbit

## Features Comparison

| Feature | Indonesian Version | Enhanced Version |
|---------|-------------------|------------------|
| **Planets** | Mercury, Venus, Earth, Mars | All inner planets with accurate colors |
| **Controls** | Individual speed sliders | Advanced control panel |
| **Visual Design** | Basic tkinter interface | Modern styled GUI |
| **Sun** | Central yellow circle | Enhanced solar representation |
| **Interactivity** | Speed adjustment only | Full simulation control |
| **Layout** | Combined window | Separated canvas and controls |

## Orbital Characteristics

### Planet Properties
```
Mercury: distance = 60px,  color = grey,    speed = 1.0 (fastest)
Venus:   distance = 100px, color = #E8B468, speed = 1.0
Earth:   distance = 150px, color = #4A90E2, speed = 1.0
Mars:    distance = 200px, color = #D05F48, speed = 1.0 (slowest)
```

### Speed Relationships
In real solar system:
- **Mercury**: 88 Earth days per orbit
- **Venus**: 225 Earth days per orbit
- **Earth**: 365 days per orbit (reference)
- **Mars**: 687 Earth days per orbit

## How to Run

1. **Basic version:**
   ```bash
   python OrbitPlanet.py
   ```

2. **Enhanced version:**
   ```bash
   python PlanetaryOrbits.py
   ```

## Interactive Controls

### Speed Sliders
- Each planet has individual speed control (0 to 5x)
- Real-time adjustment during simulation
- Independent control allows for custom scenarios

### Simulation Features
- Continuous orbital animation
- Smooth planetary motion
- Visual trail tracking (where implemented)
- Responsive user interface

## Learning Objectives

- Understand relative orbital speeds of planets
- Visualize solar system structure and scale
- Explore the relationship between distance and orbital period
- Practice GUI programming with tkinter
- Learn about planetary characteristics and motion

## Real-World Applications

- **Astronomy Education**: Teaching planetary motion
- **Space Mission Planning**: Understanding orbital mechanics
- **Planetarium Software**: Simulating solar system
- **Navigation**: Understanding celestial mechanics
- **Time Keeping**: Calendar systems based on orbital periods

## Programming Concepts

### Turtle Graphics Integration
- Using turtle graphics within tkinter canvas
- Coordinating multiple moving objects
- Real-time animation with smooth updates

### Event-Driven Programming
- Slider callbacks for speed adjustment
- Animation loops with timer events
- GUI responsiveness during simulation

## Dependencies

- `turtle` - For planetary graphics and animation
- `tkinter` - For GUI interface and controls
- `ttk` - For modern styled widgets
- `math` - For trigonometric calculations

## Educational Value

This simulation demonstrates:
- Basic orbital mechanics principles
- Relative planetary speeds and distances
- Interactive programming concepts
- Solar system structure and organization

The interactive controls allow students to:
- Experiment with different orbital speeds
- Observe planetary alignments
- Understand relative motion concepts
- Explore "what if" scenarios in planetary motion

## Extensions and Improvements

Potential enhancements could include:
- Elliptical orbits instead of circular
- Accurate scale and speed ratios
- Additional planets (outer solar system)
- Moons and asteroid belts
- Real astronomical data integration