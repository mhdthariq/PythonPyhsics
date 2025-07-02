# Example 2: Mathematical Orbit Analysis

This example demonstrates mathematical analysis and visualization of planetary orbits using matplotlib for scientific plotting and data analysis.

## Files Overview

### Basic Version
- **Example2.py** - Mathematical orbit simulation with matplotlib plotting

### Enhanced Version (Improved)
- **Example2Enhance.py** - Advanced orbit analysis with enhanced visualization and data export

## Physics Concepts

### Newton's Law of Universal Gravitation
The simulation uses the same gravitational law as Example 1:

```
F = G × (M_sun × m_earth) / r²
```

### Mathematical Integration
Unlike Example 1's real-time visualization, this example focuses on:
- Complete orbital period calculation
- Data collection and analysis
- Scientific plotting and visualization
- Orbital parameter measurement

### Orbit Equations
The simulation solves the differential equation:
```
d²r/dt² = -GM/r² × r̂
```

In component form:
```
d²x/dt² = -GM × x / (x² + y²)^(3/2)
d²y/dt² = -GM × y / (x² + y²)^(3/2)
```

## Physical Parameters

### Simulation Constants
```python
G = 6.67430e-11        # Gravitational constant (m³ kg⁻¹ s⁻²)
M_matahari = 1.989e30  # Solar mass (kg)
AU = 1.496e11          # Astronomical Unit (m)
dt = 3600              # Time step: 1 hour (seconds)
jumlah_langkah = 8760  # Total steps: 1 year (hours)
```

### Initial Conditions
- **Earth position**: (1 AU, 0)
- **Earth velocity**: (0, 29,780 m/s)
- **Simulation duration**: 1 full year (8,760 hours)

## Features Comparison

| Feature | Basic Version | Enhanced Version |
|---------|---------------|------------------|
| **Output** | Single orbit plot | Multiple analysis plots |
| **Data Storage** | Basic arrays | Comprehensive datasets |
| **Visualization** | Simple matplotlib | Advanced scientific plots |
| **Analysis** | Basic orbit shape | Orbital parameters analysis |
| **Export** | Screen display only | Data export capabilities |
| **Measurements** | Visual only | Quantitative analysis |

## Key Differences

### Basic Version (Example2.py)
- Simple position tracking
- Basic matplotlib plotting
- Indonesian comments and labels
- Single orbit visualization
- Minimal data analysis

### Enhanced Version (Example2Enhance.py)
- **Multi-plot analysis**: Position, velocity, energy plots
- **Data export**: CSV files for further analysis
- **Orbital parameters**: Eccentricity, period, semi-major axis
- **Energy conservation**: Verification of physical laws
- **Advanced visualization**: Subplots, annotations, styling

## Mathematical Analysis

### Orbital Parameters Calculated

#### Semi-major axis (a)
```
a = (r_max + r_min) / 2
```

#### Eccentricity (e)
```
e = (r_max - r_min) / (r_max + r_min)
```

#### Orbital Period (T)
```
T = 2π × √(a³/GM)    # Kepler's Third Law
```

#### Orbital Energy (E)
```
E = ½mv² - GMm/r     # Total mechanical energy
```

#### Angular Momentum (L)
```
L = m × |r × v|      # Angular momentum magnitude
```

### Conservation Laws Verification

The simulation verifies:
1. **Energy Conservation**: Total energy remains constant
2. **Angular Momentum Conservation**: L = constant
3. **Kepler's Laws**: Period-distance relationship

## Data Analysis Features

### Position Analysis
- Complete orbital path
- Perihelion and aphelion points
- Orbital shape characterization

### Velocity Analysis
- Speed variations throughout orbit
- Velocity vector changes
- Maximum and minimum speeds

### Energy Analysis
- Kinetic energy variations
- Potential energy changes
- Total energy conservation

## Visualization Outputs

### Basic Plot Elements
- Sun at origin (yellow circle)
- Complete Earth orbit (blue line)
- Grid and axis labels
- Title and legend

### Enhanced Plot Features
- Multiple subplot arrangements
- Time-series data plots
- Energy and momentum graphs
- Statistical analysis displays

## How to Run

1. **Basic version:**
   ```bash
   python Example2.py
   ```

2. **Enhanced version:**
   ```bash
   python Example2Enhance.py
   ```

## Learning Objectives

- Understand mathematical orbit analysis
- Learn scientific data visualization
- Practice matplotlib for physics plots
- Analyze orbital mechanics quantitatively
- Verify conservation laws numerically
- Compare theoretical vs. computational results

## Scientific Applications

### Astronomy and Astrophysics
- Planetary orbit analysis
- Comet and asteroid trajectory studies
- Binary star system analysis
- Exoplanet orbit characterization

### Space Engineering
- Satellite orbit design
- Mission trajectory optimization
- Orbital maneuver planning
- Fuel consumption calculations

## Data Output

The enhanced version can generate:
- **Position data**: x, y coordinates over time
- **Velocity data**: vx, vy components over time
- **Energy data**: Kinetic, potential, total energy
- **Orbital parameters**: a, e, T, L, E
- **Analysis reports**: Statistical summaries

## Mathematical Verification

### Kepler's Third Law Check
```python
T_theoretical = 2 * π * sqrt(a³ / (G * M))
T_simulated = time_for_complete_orbit
relative_error = |T_theoretical - T_simulated| / T_theoretical
```

### Energy Conservation Check
```python
E_initial = 0.5 * m * v₀² - G * M * m / r₀
E_final = 0.5 * m * v_f² - G * M * m / r_f
energy_drift = |E_final - E_initial| / |E_initial|
```

## Dependencies

- `numpy` - Numerical computations and array operations
- `matplotlib.pyplot` - Scientific plotting and visualization
- `math` - Mathematical functions

## Extensions

This example can be extended to include:
- Multiple orbital periods
- Different initial conditions
- Elliptical vs circular orbit comparison
- Perturbation effects
- Multi-body gravitational influences

## Next Steps

This mathematical foundation prepares for:
- Three-body problems (Example 3)
- Interactive parameter studies
- Advanced orbital mechanics
- Chaotic dynamics analysis (Example 4)