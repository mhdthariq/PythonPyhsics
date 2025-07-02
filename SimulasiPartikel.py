import tkinter as tk
import random

# Particle Class
class Particle:
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.radius = 3

        # Initial position and velocity
        self.x = random.randint(self.radius, width - self.radius)
        self.y = random.randint(self.radius, height - self.radius)
        self.dx = random.uniform(-2, 2)
        self.dy = random.uniform(-2, 2)

        # Assign a random color
        self.color = random.choice(["red", "orange", "yellow", "green", "cyan", "blue", "magenta", "white"])

        # FIX: create_oval needs 4 coordinates (x1, y1, x2, y2) for the bounding box
        self.id = canvas.create_oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            fill=self.color,
            outline="" # No border for a cleaner look
        )

    def move(self):
        # FIX: Actually move the particle on the canvas
        self.canvas.move(self.id, self.dx, self.dy)

        # Update internal coordinates
        self.x += self.dx
        self.y += self.dy

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Bounce off the edges
        if self.x <= self.radius or self.x >= canvas_width - self.radius:
            self.dx *= -1
        if self.y <= self.radius or self.y >= canvas_height - self.radius:
            self.dy *= -1

# Simulation Class
class ParticleSimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Particle Simulation")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="black")
        self.canvas.pack()

        self.particles = []
        self.num_particles = 100
        self.is_running = False

        self.start_button = tk.Button(root, text="Start", command=self.start_simulation)
        self.start_button.pack(pady=10)

    def create_particles(self):
        # We need to get the canvas size *after* it has been drawn.
        self.canvas.update()
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        for _ in range(self.num_particles):
            particle = Particle(self.canvas, width, height)
            self.particles.append(particle)

    def update(self):
        # If simulation is not running, stop the loop
        if not self.is_running:
            return

        for particle in self.particles:
            particle.move()

        # FIX: Schedule the next update call AFTER the loop to avoid a crash
        self.root.after(10, self.update)

    def start_simulation(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED, text="Running...")

            if not self.particles:
                self.create_particles()

            self.update()

# Run the program
if __name__ == "__main__":
    root = tk.Tk()
    simulation = ParticleSimulation(root)
    root.mainloop()
