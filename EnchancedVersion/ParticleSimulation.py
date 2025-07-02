import tkinter as tk
from tkinter import ttk
import random
import math
import itertools

# --- Particle Class ---
# Represents a single particle with physical properties
class Particle:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.radius = random.uniform(4, 12)
        # Mass is proportional to the area of the circle
        self.mass = self.radius ** 2

        # Initial position
        self.x = random.uniform(self.radius, width - self.radius)
        self.y = random.uniform(self.radius, height - self.radius)

        # Initial velocity
        self.dx = random.uniform(-1.5, 1.5)
        self.dy = random.uniform(-1.5, 1.5)

        # Visual properties
        self.color = random.choice(["#ff6b6b", "#f0e68c", "#48dbfb", "#1dd1a1", "#feca57", "#ff9ff3", "#54a0ff"])

        # Create the circle on the canvas
        self.id = canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=self.color,
            outline=""
        )

    def move(self, canvas_width, canvas_height):
        """Updates the particle's position and handles wall collisions."""
        self.canvas.move(self.id, self.dx, self.dy)
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= canvas_width:
            self.dx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= canvas_height:
            self.dy *= -1

# --- Simulation Class ---
# Manages the canvas, UI, and animation loop
class ParticleSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Particle Collision Simulation")
        self.root.configure(bg="#2c3e50")

        # --- UI Setup ---
        control_frame = ttk.Frame(root, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X)

        self.start_button = ttk.Button(control_frame, text="Start", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = ttk.Button(control_frame, text="Pause", command=self.pause_simulation, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # --- Canvas Setup ---
        self.canvas = tk.Canvas(root, width=1000, height=700, bg="#1e272e", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # --- Simulation State ---
        self.particles = []
        self.num_particles = 70
        self.is_running = False
        self.animation_job = None

    def create_particles(self):
        """Clears old particles and creates a new set."""
        self.canvas.delete("all")
        self.particles.clear()
        self.canvas.update_idletasks()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        for _ in range(self.num_particles):
            self.particles.append(Particle(self.canvas, width, height))

    def update(self):
        """The main animation loop."""
        if not self.is_running:
            return

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Move particles and check for collisions
        for p1, p2 in itertools.combinations(self.particles, 2):
            self.handle_collision(p1, p2)

        for particle in self.particles:
            particle.move(width, height)

        self.animation_job = self.root.after(10, self.update)

    def handle_collision(self, p1, p2):
        """Checks for and resolves collisions between two particles."""
        dist_x = p1.x - p2.x
        dist_y = p1.y - p2.y
        distance = math.sqrt(dist_x**2 + dist_y**2)

        if distance <= p1.radius + p2.radius:
            # --- Physics of Elastic Collision ---
            # Normal vector
            nx = dist_x / distance
            ny = dist_y / distance

            # Tangent vector
            tx = -ny
            ty = nx

            # Dot product tangent
            dp_tan1 = p1.dx * tx + p1.dy * ty
            dp_tan2 = p2.dx * tx + p2.dy * ty

            # Dot product normal
            dp_norm1 = p1.dx * nx + p1.dy * ny
            dp_norm2 = p2.dx * nx + p2.dy * ny

            # Conservation of momentum in 1D
            m1 = (dp_norm1 * (p1.mass - p2.mass) + 2 * p2.mass * dp_norm2) / (p1.mass + p2.mass)
            m2 = (dp_norm2 * (p2.mass - p1.mass) + 2 * p1.mass * dp_norm1) / (p1.mass + p2.mass)

            # Update velocities
            p1.dx = tx * dp_tan1 + nx * m1
            p1.dy = ty * dp_tan1 + ny * m1
            p2.dx = tx * dp_tan2 + nx * m2
            p2.dy = ty * dp_tan2 + ny * m2

    def start_simulation(self):
        """Starts or resumes the simulation."""
        if self.is_running:
            return

        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

        if not self.particles:
            self.create_particles()

        self.update()

    def pause_simulation(self):
        """Pauses the simulation."""
        if not self.is_running:
            return
        self.is_running = False
        if self.animation_job:
            self.root.after_cancel(self.animation_job)
            self.animation_job = None
        self.start_button.config(state=tk.NORMAL, text="Resume")
        self.pause_button.config(state=tk.DISABLED)

    def reset_simulation(self):
        """Stops and resets the simulation."""
        self.pause_simulation()
        self.create_particles()
        self.start_button.config(text="Start")


# --- Main Program ---
if __name__ == "__main__":
    root = tk.Tk()
    # Use a modern theme
    style = ttk.Style(root)
    style.theme_use('clam')

    simulation = ParticleSimulation(root)
    root.mainloop()
