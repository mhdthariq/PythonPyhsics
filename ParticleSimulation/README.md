# Particle Simulation

This folder contains simulations of particle motion and collisions, demonstrating fundamental physics concepts like random motion and elastic collisions.

## Files Overview

### Indonesian Versions (First Version)
- **GerakAcak.py** - Simple random motion simulation using turtle graphics
- **SimulasiPartikel.py** - Basic particle collision simulation with tkinter

### English Versions (Enhanced/Improved)
- **ParticleMotion.py** - Enhanced random motion with multiple particles *(improved version of GerakAcak.py)*
- **ParticleSimulation.py** - Advanced particle collision simulation with physics *(improved version of SimulasiPartikel.py)*

## Physics Concepts

### 1. Random Motion (Brownian Motion)
**GerakAcak.py** and **ParticleMotion.py** simulate random particle movement.

**Mathematical Formula:**
```
θ = random(0, 360°)
x = x₀ + d·cos(θ)
y = y₀ + d·sin(θ)
```

Where:
- θ = random angle
- d = step distance
- (x₀, y₀) = previous position
- (x, y) = new position

### 2. Elastic Collision Physics
**SimulasiPartikel.py** and **ParticleSimulation.py** implement collision detection and response.

**Collision Detection:**
```
distance = √[(x₁ - x₂)² + (y₁ - y₂)²]
collision = distance ≤ (r₁ + r₂)
```

**Elastic Collision Response:**
```
Normal vector: n⃗ = (x₁ - x₂, y₁ - y₂) / distance
Tangent vector: t⃗ = (-ny, nx)

Velocity components:
v₁n = v⃗₁ · n⃗
v₁t = v⃗₁ · t⃗
v₂n = v⃗₂ · n⃗
v₂t = v⃗₂ · t⃗

New normal velocities (conservation of momentum):
v₁n' = (v₁n(m₁ - m₂) + 2m₂v₂n) / (m₁ + m₂)
v₂n' = (v₂n(m₂ - m₁) + 2m₁v₁n) / (m₁ + m₂)

Final velocities:
v⃗₁' = v₁t · t⃗ + v₁n' · n⃗
v⃗₂' = v₂t · t⃗ + v₂n' · n⃗
```

## Features Comparison

| Feature | Indonesian Version | Enhanced Version |
|---------|-------------------|------------------|
| **Random Motion** | Single particle, basic trail | Multiple particles, colors, smooth animation |
| **Collision Physics** | Basic bouncing | Full elastic collision with momentum conservation |
| **User Interface** | Simple start button | Advanced controls, pause/resume, reset |
| **Visual Effects** | Basic circles | Color-coded particles, modern UI styling |
| **Performance** | Standard rendering | Optimized with animation timers |

## How to Run

1. **For basic versions:**
   ```bash
   python GerakAcak.py
   python SimulasiPartikel.py
   ```

2. **For enhanced versions:**
   ```bash
   python ParticleMotion.py
   python ParticleSimulation.py
   ```

## Learning Objectives

- Understand random motion and its applications in physics
- Learn about conservation of momentum in elastic collisions
- Explore particle systems and their behaviors
- Practice implementing physics simulations in Python
- Compare different approaches to the same physical phenomena

## Dependencies

- `turtle` - For graphics rendering (GerakAcak.py, ParticleMotion.py)
- `tkinter` - For GUI interface (SimulasiPartikel.py, ParticleSimulation.py)
- `random` - For random number generation
- `math` - For mathematical calculations