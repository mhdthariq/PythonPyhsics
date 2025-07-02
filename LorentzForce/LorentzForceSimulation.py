import tkinter as tk
from tkinter import ttk
import random

# --- Particle Class ---
# Encapsulates the properties and behavior of a single particle.
class Particle:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.radius = 4

        # --- Physical Properties ---
        self.x = random.uniform(self.radius, width - self.radius)
        self.y = random.uniform(self.radius, height - self.radius)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.charge = random.choice([-1, 1])

        # --- Visual Properties ---
        color = "blue" if self.charge < 0 else "red"

        # Create the visual representation on the canvas
        self.id = self.canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=color,
            outline=""
        )

    def update(self, magnetic_field, time_step, width, height):
        """Calculates forces, updates velocity, and moves the particle."""
        # --- Lorentz Force Calculation (B-field is perpendicular to the screen) ---
        # F_x = q * v_y * B
        # F_y = -q * v_x * B
        # a = F/m (we assume mass m=1 for simplicity)
        ax = self.charge * self.vy * magnetic_field
        ay = -self.charge * self.vx * magnetic_field

        # --- Update Velocity (Integration) ---
        self.vx += ax * time_step
        self.vy += ay * time_step

        # --- Update Position ---
        # We move the object on the canvas instead of deleting and redrawing
        self.canvas.move(self.id, self.vx * time_step, self.vy * time_step)
        self.x += self.vx * time_step
        self.y += self.vy * time_step

        # --- Boundary Collision Check ---
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.vx *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.vy *= -1

# --- Simulation Class ---
# Manages the UI, canvas, and the main animation loop.
class LorentzSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Lorentz Force Simulation")
        self.root.configure(bg="#2c3e50")

        # --- Simulation State ---
        self.particles = []
        self.is_running = False
        self.animation_job = None

        # --- UI Setup ---
        self.setup_controls()

        # --- Canvas Setup ---
        self.canvas = tk.Canvas(root, bg="black", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def setup_controls(self):
        """Creates the control panel with sliders and buttons."""
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.pack(side=tk.TOP, fill=tk.X)

        # --- Buttons ---
        self.start_button = ttk.Button(control_frame, text="Start", command=self.start_simulation)
        self.start_button.pack(side=tk.LEFT, padx=5)
        self.pause_button = ttk.Button(control_frame, text="Pause", command=self.pause_simulation, state=tk.DISABLED)
        self.pause_button.pack(side=tk.LEFT, padx=5)
        self.reset_button = ttk.Button(control_frame, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # --- Magnetic Field Slider ---
        ttk.Label(control_frame, text="B-Field:").pack(side=tk.LEFT, padx=(15, 0))
        self.b_field_var = tk.DoubleVar(value=0.1)
        self.b_field_slider = ttk.Scale(control_frame, from_=-0.5, to=0.5, variable=self.b_field_var, orient=tk.HORIZONTAL)
        self.b_field_slider.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        # --- Particle Count Slider ---
        ttk.Label(control_frame, text="Particles:").pack(side=tk.LEFT, padx=(15, 0))
        self.particle_count_var = tk.IntVar(value=50)
        self.particle_count_slider = ttk.Scale(control_frame, from_=1, to=200, variable=self.particle_count_var, orient=tk.HORIZONTAL)
        self.particle_count_slider.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    def create_particles(self):
        """Clears the canvas and creates a new set of particles."""
        self.canvas.delete("all")
        self.particles.clear()
        self.canvas.update_idletasks() # Ensure canvas has its size
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        for _ in range(self.particle_count_var.get()):
            self.particles.append(Particle(self.canvas, width, height))

    def update_loop(self):
        """The core animation loop that updates every particle."""
        if not self.is_running:
            return

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        magnetic_field = self.b_field_var.get()
        time_step = 0.5 # Kept constant for stability

        for p in self.particles:
            p.update(magnetic_field, time_step, width, height)

        self.animation_job = self.root.after(15, self.update_loop)

    def start_simulation(self):
        if self.is_running:
            return
        self.is_running = True
        self.start_button.config(state=tk.DISABLED, text="Resume")
        self.pause_button.config(state=tk.NORMAL)
        if not self.particles:
            self.create_particles()
        self.update_loop()

    def pause_simulation(self):
        if not self.is_running:
            return
        self.is_running = False
        if self.animation_job:
            self.root.after_cancel(self.animation_job)
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def reset_simulation(self):
        self.pause_simulation()
        self.create_particles()
        self.start_button.config(text="Start")

# --- Main Program Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')

    app = LorentzSimulation(root)
    root.mainloop()
