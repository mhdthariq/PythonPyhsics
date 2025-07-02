import turtle
import math

# Screen settings
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Moon and Earth Orbit Simulation")
screen.tracer(0)

# Earth
earth = turtle.Turtle()
earth.shape("circle")
earth.color("deepskyblue")
earth.shapesize(1.5)
earth.penup()
earth.goto(0, 0)
earth.stamp()  # Earth stays in place
earth.hideturtle()

# Moon
moon = turtle.Turtle()
moon.shape("circle")
moon.color("lightgray")
moon.shapesize(0.7)
moon.penup()
moon.goto(100, 0)
moon.pendown()

# Orbit Parameter
orbit_radius = 100
angle = 0
delta_angle = 0.5  # Angle increment per frame

# Function to update moon position
def update_position():
    global angle
    angle += delta_angle
    theta = math.radians(angle)
    x = orbit_radius * math.cos(theta)
    y = orbit_radius * math.sin(theta)
    moon.goto(x, y)

    screen.update()
    screen.ontimer(update_position, 20)  # Repeat the update_position function every 20 milliseconds

# Start Simulation
update_position()

# Start GUI
screen.mainloop()
