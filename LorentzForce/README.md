# Lorentz Force Simulation

This folder contains simulations demonstrating the Lorentz force acting on charged particles in a magnetic field, showing how electromagnetic forces affect particle motion.

## Files Overview

### Indonesian Version (First Version)
- **SimulasiGayaLorentz.py** - Basic Lorentz force simulation with fixed parameters

### English Version (Enhanced/Improved)
- **LorentzForceSimulation.py** - Interactive Lorentz force simulation with controls *(improved version of SimulasiGayaLorentz.py)*

## Physics Concepts

### Lorentz Force
The Lorentz force describes the force acting on a charged particle moving in electromagnetic fields.

**Mathematical Formula:**
```
F⃗ = q(E⃗ + v⃗ × B⃗)
```

For this simulation (magnetic field only):
```
F⃗ = q(v⃗ × B⃗)
```

**In 2D with B-field perpendicular to screen:**
```
Fx = q · vy · B
Fy = -q · vx · B
```

Where:
- F⃗ = Lorentz force vector
- q = particle charge
- v⃗ = velocity vector (vx, vy)
- B⃗ = magnetic field vector
- B = magnetic field strength

**Acceleration and Motion:**
```
ax = Fx / m = (q · vy · B) / m
ay = Fy / m = (-q · vx · B) / m

vx(t+dt) = vx(t) + ax · dt
vy(t+dt) = vy(t) + ay · dt

x(t+dt) = x(t) + vx · dt
y(t+dt) = y(t) + vy · dt
```

### Circular Motion in Magnetic Field
Charged particles in uniform magnetic fields follow circular paths.

**Cyclotron Frequency:**
```
ωc = qB / m
```

**Radius of Curvature:**
```
r = mv / (qB)
```

Where:
- ωc = cyclotron frequency
- m = particle mass
- r = radius of circular path
- v = particle speed

## Features Comparison

| Feature | Indonesian Version | Enhanced Version |
|---------|-------------------|------------------|
| **Magnetic Field** | Fixed strength (0.1) | Interactive slider control |
| **Particle Count** | Fixed (30 particles) | Adjustable via slider |
| **Controls** | None | Start, Pause, Reset buttons |
| **User Interface** | Basic window | Modern styled controls |
| **Visual Design** | Simple colors | Enhanced styling with themes |
| **Interactivity** | Static simulation | Real-time parameter adjustment |

## Physical Behavior

### Positive vs Negative Charges
- **Positive charges (red)**: Curve in one direction
- **Negative charges (blue)**: Curve in opposite direction
- **Direction**: Determined by right-hand rule

### Magnetic Field Effects
- **Stronger field**: Tighter circular paths
- **Weaker field**: Larger circular paths
- **Zero field**: Straight-line motion
- **Reverse field**: Particles curve in opposite direction

## How to Run

1. **Basic version:**
   ```bash
   python SimulasiGayaLorentz.py
   ```

2. **Enhanced version:**
   ```bash
   python LorentzForceSimulation.py
   ```

## Learning Objectives

- Understand electromagnetic forces on moving charges
- Visualize the relationship between charge, velocity, and magnetic field
- Explore cyclotron motion and its applications
- Learn about particle accelerators and mass spectrometry principles
- Practice implementing electromagnetic physics in simulations

## Real-World Applications

- **Particle Accelerators**: Cyclotrons, synchrotrons
- **Mass Spectrometry**: Separating particles by mass-to-charge ratio
- **Plasma Physics**: Understanding charged particle behavior in plasmas
- **Magnetic Confinement**: Fusion reactors, particle traps
- **Cathode Ray Tubes**: Old TV and monitor technology

## Dependencies

- `tkinter` - For GUI interface
- `random` - For random particle initialization
- `math` - For mathematical calculations

## Interactive Controls (Enhanced Version)

- **B-Field Slider**: Adjust magnetic field strength (-0.5 to 0.5)
- **Particle Count**: Control number of particles (1 to 200)
- **Start/Pause/Reset**: Control simulation state
- **Real-time Updates**: Parameters change simulation immediately