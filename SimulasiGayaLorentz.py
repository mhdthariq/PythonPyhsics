import tkinter as tk
import random

# Screen Size
WIDTH = 800
HEIGHT = 800

# Particle Parameters
RADIUS = 4
PARTICLE_COUNT = 30
MAGNETIC_FIELD = 0.1
TIME_STEP = 0.5

# Particle color based on charge
NEGATIVE_COLOR = "blue"
POSITIVE_COLOR = "red"

# Make the main screen
root = tk.Tk()
root.title("Simulasi Gaya Lorentz")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Particle Initializations
particle_list = []
for _ in range(PARTICLE_COUNT):
    x = random.uniform(100, WIDTH - 100)
    y = random.uniform(100, HEIGHT - 100)
    vx = random.uniform(-5, 5)
    vy = random.uniform(-5, 5)
    charge = random.choice([-1, 1])
    color = NEGATIVE_COLOR if charge < 0 else POSITIVE_COLOR
    particle_list.append([x, y, vx, vy, charge, color])

# Update position and speed
def update():
    canvas.delete("particle")

    for p in particle_list:
        x, y, vx, vy, charge, color = p

        # Lorentz Force (Magnetic Field straight in screen)
        ax = charge * MAGNETIC_FIELD * vy
        ay = -charge * MAGNETIC_FIELD * vx

        # Apply Lorentz Force
        vx += ax * TIME_STEP
        vy += ay * TIME_STEP
        x += vx * TIME_STEP
        y += vy * TIME_STEP

        # Bounce if touch edge screen
        if x < 0 or x > WIDTH:
            vx *= -1
        if y < 0 or y > HEIGHT:
            vy *= -1

        # Save the updated values back to the list
        p[0], p[1], p[2], p[3] = x, y, vx, vy

        # Make particle
        canvas.create_oval(
            x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS,
            fill=color, tags="particle", outline=""
        )

    root.after(20, update)

# Run the simulation
update()

# Start the main loop
root.mainloop()
