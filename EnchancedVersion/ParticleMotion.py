import turtle
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Enhanced Particle Motion Simulation")
# Turn off automatic screen updates for smoother animation
screen.tracer(0)

# --- Simulation Parameters ---
num_particles = 30
particles = []
colors = ["white", "cyan", "magenta", "yellow", "lightgreen", "orange", "red"]

# --- Create Particles ---
for _ in range(num_particles):
    particle = turtle.Turtle()
    particle.shape("circle")
    particle.shapesize(0.2) # Make particles smaller
    particle.color(random.choice(colors))
    particle.penup()
    particle.speed(0)
    particles.append(particle)

# --- Animation Function ---
def move_particles():
    """
    Moves each particle one random step and schedules the next update.
    """
    for p in particles:
        # Determine a random angle and distance for each step
        angle = random.randint(0, 360)
        distance = random.randint(1, 5)

        p.setheading(angle)
        p.forward(distance)

    # Update the screen to show all particle movements at once
    screen.update()

    # Schedule this function to run again after a short delay (in milliseconds)
    screen.ontimer(move_particles, 20)

# --- Run the Simulation ---
move_particles()

# --- Keep the window open ---
# mainloop() keeps the window running and responsive.
screen.mainloop()
