# Python Physics Simulations

A comprehensive collection of physics simulations implemented in Python, demonstrating fundamental concepts in mechanics, electromagnetism, orbital dynamics, and complex systems. This educational repository progresses from basic simulations to advanced interactive models.

## Project Overview

This repository contains physics simulations organized into specialized folders, each focusing on different areas of physics. The project includes both basic implementations (often with Indonesian names) and enhanced versions (with English names) that demonstrate improved coding practices and advanced features.

## Folder Structure

### 🌍 [EarthSimulationNewtonLaw](./EarthSimulationNewtonLaw/)

Advanced orbital mechanics simulations using Newton's Law of Universal Gravitation.

**Examples:**

- **Example1**: Basic Earth-Sun orbital system
- **Example2**: Mathematical orbit analysis with matplotlib
- **Example3&4**: Interactive Jupyter notebook with Sun-Earth-Moon system and chaotic three-body dynamics

**Key Physics:** Gravitational forces, orbital mechanics, numerical integration, chaos theory

### ⚡ [LorentzForce](./LorentzForce/)

Electromagnetic force simulations showing charged particle motion in magnetic fields.

**Files:**

- `SimulasiGayaLorentz.py` - Basic Lorentz force simulation _(Indonesian version)_
- `LorentzForceSimulation.py` - Interactive simulation with controls _(Enhanced version)_

**Key Physics:** Electromagnetic forces, cyclotron motion, particle accelerators

### 🌙 [MoonOrbits](./MoonOrbits/)

Earth-Moon orbital system simulations.

**Files:**

- `OrbitBulan.py` - Simple Moon orbit simulation _(Indonesian version)_
- `MoonOrbits.py` - Enhanced with starfield and labels _(Enhanced version)_

**Key Physics:** Circular orbital motion, celestial mechanics, trigonometry

### ⚛️ [ParticleSimulation](./ParticleSimulation/)

Particle motion and collision physics simulations.

**Files:**

- `GerakAcak.py` - Simple random motion _(Indonesian version)_
- `ParticleMotion.py` - Enhanced random motion with multiple particles _(Enhanced version)_
- `SimulasiPartikel.py` - Basic collision simulation _(Indonesian version)_
- `ParticleSimulation.py` - Advanced collision physics _(Enhanced version)_

**Key Physics:** Random motion, elastic collisions, conservation of momentum

### 🪐 [PlanetaryOrbits](./PlanetaryOrbits/)

Solar system simulations with interactive controls.

**Files:**

- `OrbitPlanet.py` - Basic planetary motion _(Indonesian version)_
- `PlanetaryOrbits.py` - Enhanced solar system simulation _(Enhanced version)_

**Key Physics:** Planetary motion, orbital periods, Kepler's laws

### 🌤️ [SimpleWeatherSimulation](./SimpleWeatherSimulation/)

Weather pattern visualization and atmospheric simulation.

**Files:**

- `SimulasiCuaca.py` - Basic weather elements _(Indonesian version)_
- `SimpleWeatherSimulation.py` - Interactive weather patterns _(Enhanced version)_

**Key Physics:** Atmospheric processes, random distributions, environmental science

## Version Progression

### Indonesian Versions (First Implementations)

- Basic functionality with essential physics
- Simple user interfaces
- Educational foundation
- Indonesian comments and variable names

### English Versions (Enhanced Implementations)

- Object-oriented programming
- Advanced user interfaces with controls
- Better visualization and graphics
- Enhanced physics accuracy
- Modern coding practices

### Special Cases

- **EarthSimulationNewtonLaw**: All files are in English, with "Enhance" suffix for improved versions
- **Example3&4**: Combined Jupyter notebook optimized for Google Colab with interactive widget

## Physics Concepts Covered

### Classical Mechanics

- Newton's Laws of Motion
- Gravitational dynamics
- Conservation of energy and momentum
- Orbital mechanics
- Collision physics

### Electromagnetism

- Lorentz force
- Charged particle motion
- Magnetic field effects
- Cyclotron frequency

### Complex Systems

- Three-body problems
- Chaotic dynamics
- Multi-particle systems
- Statistical mechanics

### Computational Physics

- Numerical integration (Euler, Runge-Kutta)
- Real-time simulation
- Interactive visualization
- Data analysis and plotting

## Mathematical Foundations

### Newton's Law of Universal Gravitation

```
F = G × (m₁ × m₂) / r²
```

### Lorentz Force

```
F⃗ = q(E⃗ + v⃗ × B⃗)
```

### Elastic Collision

```
v₁' = ((m₁-m₂)v₁ + 2m₂v₂)/(m₁+m₂)
v₂' = ((m₂-m₁)v₂ + 2m₁v₁)/(m₁+m₂)
```

### Orbital Motion

```
v = √(GM/r)  (circular orbit)
T² ∝ r³     (Kepler's Third Law)
```

## Dependencies

### Core Libraries

- `numpy` - Numerical computations
- `matplotlib` - Scientific plotting
- `turtle` - Graphics and animation
- `tkinter` - GUI interfaces
- `random` - Random number generation
- `math` - Mathematical functions

### Advanced Features

- `ipywidgets` - Interactive controls (Jupyter)
- `IPython` - Notebook integration
- `typing` - Type hints
- `jupyter` - Notebook environment (for Example3&4)

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mhdthariq/PythonPyhsics.git
   cd PythonPhysics
   ```

2. **Install dependencies:**

   ```bash
   pip install numpy matplotlib ipywidgets
   ```

3. **Run simulations:**

   ```bash
   # Basic simulations
   python ParticleSimulation/GerakAcak.py

   # Enhanced simulations
   python ParticleSimulation/ParticleMotion.py

   # Interactive simulations (Jupyter recommended)
   jupyter notebook EarthSimulationNewtonLaw/Example3/Example3.py

   # Combined Jupyter notebook (Google Colab recommended)
   # Upload EarthSimulationNewtonLaw/Example3and4/Example3andExample4.ipynb to Google Colab
   ```

## Educational Goals

### Learning Progression

1. **Basic Physics**: Start with simple simulations
2. **Programming Skills**: Progress to object-oriented designs
3. **Advanced Concepts**: Explore complex multi-body systems
4. **Research Methods**: Analyze chaotic and statistical behavior

### Skills Developed

- Physics simulation programming
- Numerical methods and integration
- Scientific visualization
- Interactive application development
- Mathematical modeling
- Data analysis and interpretation

## Real-World Applications

### Space and Astronomy

- Satellite orbit prediction
- Mission trajectory planning
- Planetary motion analysis
- Asteroid tracking

### Engineering

- Particle accelerator design
- Electromagnetic device simulation
- Mechanical system analysis
- Weather prediction models

### Research

- Chaos theory studies
- Complex system analysis
- Computational physics methods
- Educational software development

## Contributing

This project serves as an educational resource. Contributions that enhance learning value are welcome:

- Additional physics simulations
- Improved documentation
- Better visualization techniques
- Performance optimizations
- Educational exercises and problems

## Usage Notes

### Best Practices

1. Start with basic versions to understand core concepts
2. Progress to enhanced versions for advanced features
3. Use Jupyter notebooks for interactive simulations
4. Experiment with different parameters to explore physics

### Performance Considerations

- Large particle counts may slow simulations
- Complex three-body systems require significant computation
- Real-time graphics may limit simulation speed
- Consider reducing visual quality for faster physics

## License

This educational project is designed for learning and teaching physics through computational methods. Please maintain attribution when using or modifying the code.

---

**Author:** Muhammad Thariq Arya Putra Sembiring
**Purpose:** Educational physics simulation and computational learning
**Level:** Beginner to Advanced
**Language:** Python 3.13.5
