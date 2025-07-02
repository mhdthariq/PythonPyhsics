import turtle
import math
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Earth-Moon Orbit Simulation with Stars")
screen.tracer(0) # Turn off automatic updates

# --- Function to Draw Stars ---
def draw_stars():
    """Draws a field of stars in the background."""
    star_drawer = turtle.Turtle()
    star_drawer.hideturtle()
    star_drawer.penup()
    star_drawer.speed(0)
    star_drawer.color("white")
    for _ in range(150): # Number of stars
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        # Avoid drawing stars too close to the center
        if math.sqrt(x**2 + y**2) > 40:
            star_drawer.goto(x, y)
            star_drawer.dot(random.randint(1, 3)) # Star size

# --- Draw the background elements ---
draw_stars()

# --- Earth Turtle ---
earth = turtle.Turtle()
earth.shape("circle")
earth.color("deepskyblue")
earth.shapesize(2.5)
earth.penup()
# The earth is at the center, so we don't need to move it,
# but we stamp its shape so other turtles can draw over it.
earth.stamp()
earth.hideturtle()

# --- Earth Label ---
earth_label = turtle.Turtle()
earth_label.hideturtle()
earth_label.penup()
earth_label.color("white")
earth_label.goto(0, -45) # Position the label just below the Earth
earth_label.write("Earth", align="center", font=("Arial", 12, "normal"))


# --- Moon Turtle ---
moon = turtle.Turtle()
moon.shape("circle")
moon.color("lightgray")
moon.shapesize(0.8)
moon.penup()
moon.goto(150, 0) # Initial position
moon.pendown() # Moon will leave a trail for its orbit

# --- Moon Label ---
moon_label = turtle.Turtle()
moon_label.hideturtle()
moon_label.penup()
moon_label.color("white")

# --- Orbit Parameters ---
orbit_radius = 150
angle = 0
speed = 1.0 # Angle increment per frame

# --- Animation Function ---
def update_simulation():
    """Updates the moon's position and schedules the next update."""
    global angle

    # Update the angle to move the moon
    angle += speed
    if angle >= 360:
        angle -= 360

    # Calculate the new position using trigonometry
    theta = math.radians(angle)
    x = orbit_radius * math.cos(theta)
    y = orbit_radius * math.sin(theta)

    # Move the moon to its new position
    moon.goto(x, y)

    # Move and redraw the moon's label
    moon_label.clear()
    moon_label.goto(x, y + 15) # Position label slightly above the moon
    moon_label.write("Moon", align="center", font=("Arial", 10, "normal"))

    # Manually update the screen to show the new frame
    screen.update()

    # Schedule this function to run again after 20 milliseconds
    screen.ontimer(update_simulation, 20)

# --- Start the Simulation ---
update_simulation()

# --- Keep the Window Open ---
screen.mainloop()
