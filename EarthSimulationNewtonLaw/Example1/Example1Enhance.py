import turtle
import math
import random

# --- Simulation Constants ---
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
TIME_STEP = 3600 * 24  # Time step for calculation (1 day in seconds)
SCALE = 200 / (1.496e11)  # Scale for visualization (pixels per meter)

# --- Celestial Body Class ---
# A general class for any object in space, like a planet or a star.
class CelestialBody:
    def __init__(self, mass, px, py, vx, vy, color, size):
        self.mass = mass
        self.px, self.py = px, py  # Position in meters
        self.vx, self.vy = vx, vy  # Velocity in m/s

        # Setup the turtle for drawing this body
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color(color)
        self.turtle.shapesize(stretch_wid=size, stretch_len=size)
        self.turtle.penup()
        self.turtle.speed(0)

    def calculate_gravity(self, other_body):
        """Calculates the gravitational force exerted by another body."""
        dist_x = other_body.px - self.px
        dist_y = other_body.py - self.py
        distance = math.sqrt(dist_x**2 + dist_y**2)

        # Newton's Law of Universal Gravitation: F = G * (m1*m2) / r^2
        force = G * self.mass * other_body.mass / distance**2

        # Calculate the direction of the force
        theta = math.atan2(dist_y, dist_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, force_x, force_y):
        """Updates the body's velocity and position."""
        # Calculate acceleration: a = F/m
        ax = force_x / self.mass
        ay = force_y / self.mass

        # Update velocity: v = v0 + a*t
        self.vx += ax * TIME_STEP
        self.vy += ay * TIME_STEP

        # Update position: p = p0 + v*t
        self.px += self.vx * TIME_STEP
        self.py += self.vy * TIME_STEP

    def draw(self):
        """Draws the body on the screen at its scaled position."""
        self.turtle.goto(self.px * SCALE, self.py * SCALE)

# --- Helper Functions ---
def draw_stars():
    """Draws a random starfield in the background."""
    star_drawer = turtle.Turtle()
    star_drawer.hideturtle()
    star_drawer.speed(0)
    star_drawer.color("white")
    for _ in range(100):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        star_drawer.penup()
        star_drawer.goto(x, y)
        star_drawer.dot(random.randint(1, 2))

# --- Main Simulation Setup ---
# Screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Newtonian Orbit Simulation")
screen.tracer(0)  # Turn off automatic updates

draw_stars()

# Create celestial bodies with real-world data
sun = CelestialBody(
    mass=1.989e30,      # Mass of the Sun in kg
    px=0, py=0,         # Position at the origin
    vx=0, vy=0,         # Sun is stationary
    color="yellow",
    size=2
)

earth = CelestialBody(
    mass=5.972e24,      # Mass of the Earth in kg
    px=-1.496e11, py=0, # Position at 1 AU on the x-axis
    vx=0, vy=29780,     # Velocity in m/s
    color="blue",
    size=0.8
)
earth.turtle.pendown() # Let Earth draw its orbital path

# --- Animation Loop ---
def animate():
    """The main loop that drives the simulation."""
    # Calculate forces
    gravity_on_earth_fx, gravity_on_earth_fy = earth.calculate_gravity(sun)

    # Update positions
    earth.update_position(gravity_on_earth_fx, gravity_on_earth_fy)
    # Note: In a multi-body simulation, you would also update the sun's position.

    # Draw bodies on screen
    sun.draw()
    earth.draw()

    # Update the screen
    screen.update()

    # Schedule the next frame
    screen.ontimer(animate, 20) # Run again after 20 milliseconds

# --- Start the Simulation ---
animate()
screen.mainloop()
