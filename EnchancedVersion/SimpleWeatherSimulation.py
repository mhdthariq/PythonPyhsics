import turtle
import random

# --- Screen Setup ---
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#87CEEB") # Start with a sky blue background
screen.title("Dynamic Weather Simulation")
screen.tracer(0) # Turn off automatic screen updates for manual control

# --- Global Weather State ---
is_raining = False
ground_level = -250

# --- Object-Oriented Design ---

class Cloud:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.x = random.randint(-450, 450)
        self.y = random.randint(150, 250)
        self.speed = random.uniform(0.5, 1.5)
        self.turtle.goto(self.x, self.y)

    def draw(self):
        """Draws a multi-part cloud."""
        self.turtle.color("white")
        self.turtle.begin_fill()
        self.turtle.circle(20)
        self.turtle.end_fill()

        self.turtle.forward(25)

        self.turtle.begin_fill()
        self.turtle.circle(25)
        self.turtle.end_fill()

        self.turtle.forward(25)

        self.turtle.begin_fill()
        self.turtle.circle(20)
        self.turtle.end_fill()

    def move(self):
        """Moves the cloud across the screen and wraps around."""
        self.x += self.speed
        if self.x > 450:
            self.x = -450 # Wrap around to the left side
        self.turtle.clear()
        self.turtle.goto(self.x, self.y)
        self.draw()

class Raindrop:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.shape("triangle")
        self.turtle.color("#1E90FF") # DodgerBlue
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.setheading(270) # Point downwards
        self.turtle.shapesize(0.5, 0.2, 1) # Long and thin
        self.is_active = False

    def fall(self):
        """Moves the raindrop down and checks for ground collision."""
        if self.is_active:
            self.turtle.forward(10)
            if self.turtle.ycor() < ground_level:
                self.reset()

    def drop(self, x, y):
        """Activates a raindrop from a specific location."""
        if not self.is_active:
            self.is_active = True
            self.turtle.goto(x, y)
            self.turtle.showturtle()

    def reset(self):
        """Hides the raindrop and marks it as inactive."""
        self.is_active = False
        self.turtle.hideturtle()

# --- Setup Simulation Elements ---
# Sun
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.speed(0)
sun.goto(-300, 200)
sun.color("yellow")
sun.begin_fill()
sun.circle(50)
sun.end_fill()

# Ground
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.speed(0)
ground.goto(-400, ground_level)
ground.color("#228B22") # ForestGreen
ground.begin_fill()
for _ in range(2):
    ground.forward(800)
    ground.right(90)
    ground.forward(50)
    ground.right(90)
ground.end_fill()

# Create a pool of objects
num_clouds = 5
num_raindrops = 50
clouds = [Cloud() for _ in range(num_clouds)]
raindrops = [Raindrop() for _ in range(num_raindrops)]

# --- Main Animation Loop ---
def animate():
    global is_raining

    # Move all clouds
    for cloud in clouds:
        cloud.move()

    # If it's raining, make raindrops fall
    if is_raining:
        # Randomly drop new rain from clouds
        if random.randint(1, 5) == 1:
            active_cloud = random.choice(clouds)
            # Find an inactive raindrop to recycle
            for drop in raindrops:
                if not drop.is_active:
                    drop.drop(active_cloud.x + 25, active_cloud.y)
                    break # Drop one at a time

        # Move all active raindrops
        for drop in raindrops:
            drop.fall()

    # Update the screen
    screen.update()

    # Schedule the next animation frame
    screen.ontimer(animate, 50)

def change_weather():
    """Toggles the weather between sunny and rainy."""
    global is_raining
    is_raining = not is_raining

    if is_raining:
        screen.bgcolor("#696969") # DimGray
    else:
        screen.bgcolor("#87CEEB") # SkyBlue
        # Reset all raindrops when it stops raining
        for drop in raindrops:
            drop.reset()

    # Schedule the next weather change
    screen.ontimer(change_weather, 10000) # Change weather every 10 seconds


# --- Start the Simulation ---
animate()
change_weather() # Start the weather cycle
screen.mainloop()
