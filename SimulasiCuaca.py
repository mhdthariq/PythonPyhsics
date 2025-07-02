import turtle
import random

# Screen Settings
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("lightblue")
screen.title("Simulasi Cuaca Sederhana")

# Turtle in each element
sun = turtle.Turtle()
cloud = turtle.Turtle()
raindrop = turtle.Turtle()

# Turnoff animation
sun.speed(0)
cloud.speed(0)
raindrop.speed(0)

# Create Sun Function
def create_sun():
    sun.penup()
    sun.goto(-300, 200)
    sun.pendown()
    sun.color("yellow")
    sun.begin_fill()
    sun.circle(50)
    sun.end_fill()

# Create Cloud in (x, y) position Function
def create_cloud(x, y):
    cloud.penup()
    cloud.goto(x, y)
    cloud.pendown()
    cloud.color("white")
    cloud.begin_fill()
    for _ in range(2):
        cloud.circle(30, 180)
        cloud.forward(60)
    cloud.end_fill()

# Create Raindrop in (x, y) position Function
def create_raindrop(x, y):
    raindrop.penup()
    raindrop.goto(x, y)
    raindrop.pendown()
    raindrop.color("blue")
    raindrop.shape("triangle")
    raindrop.setheading(270)  # Set the heading to point downwards
    raindrop.shapesize(0.2, 0.5)
    raindrop.stamp()

# Simulate wind (random cloud and raindrop)
def simulate_wind():
    # Cloud
    for _ in range(20):
        x = random.randint(-350, 350)
        y = random.randint(50, 200)
        create_cloud(x, y)

    # Raindrop
    for _ in range(20):
        x = random.randint(-350, 350)
        y = random.randint(50, 100)
        create_raindrop(x, y)

# Start the Simulation
create_sun()
simulate_wind()

# Click to close screen
screen.exitonclick()
