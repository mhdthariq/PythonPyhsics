import turtle
import tkinter as tk
from tkinter import ttk
import math

# --- Main Application Window ---
root = tk.Tk()
root.title("Solar System Simulation")
root.geometry("1000x650") # Give the window a starting size

# --- Simulation Canvas (Left Side) ---
canvas_frame = ttk.Frame(root)
canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(canvas_frame, width=800, height=600)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
screen.bgcolor("black")
screen.tracer(0)  # Turn off automatic screen updates

# --- Controls Panel (Right Side) ---
control_frame = ttk.Frame(root, padding=20)
control_frame.pack(side=tk.RIGHT, fill=tk.Y)

# --- Sun ---
sun = turtle.RawTurtle(screen)
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_wid=1.5, stretch_len=1.5) # Make sun a bit bigger
sun.penup()
sun.goto(0, 0)

# --- Planet Data ---
# Using a dictionary for easier access by name
planets = {
    "Mercury": {"distance": 60, "radius": 4, "color": "grey", "angle": 0, "speed": 1.0},
    "Venus": {"distance": 100, "radius": 6, "color": "#E8B468", "angle": 0, "speed": 1.0},
    "Earth": {"distance": 150, "radius": 8, "color": "#4A90E2", "angle": 0, "speed": 1.0},
    "Mars": {"distance": 200, "radius": 7, "color": "#D05F48", "angle": 0, "speed": 1.0}
}

# --- Functions ---
# Moved function definitions here, before they are called.
def update_speed(planet_name, value):
    """Updates the speed of a planet from its slider."""
    planets[planet_name]["speed"] = float(value)

def update_simulation():
    """The main animation loop for the simulation."""
    for name, t in planet_turtles.items():
        planet_data = planets[name]

        # Update the angle based on the current speed
        planet_data["angle"] += planet_data["speed"]
        if planet_data["angle"] >= 360:
            planet_data["angle"] -= 360

        # Calculate new position using trigonometry
        angle_rad = math.radians(planet_data["angle"])
        x = planet_data["distance"] * math.cos(angle_rad)
        y = planet_data["distance"] * math.sin(angle_rad)

        # Move the planet turtle to the new position
        t.goto(x, y)

    # Update the screen to show the new positions
    screen.update()

    # Schedule this function to run again after a short delay (e.g., 15ms)
    # This creates the animation loop within tkinter's main loop
    root.after(15, update_simulation)


# --- Create Planet Turtles and UI Controls ---
planet_turtles = {}
sliders = {}

# Create a title for the controls
ttk.Label(control_frame, text="Planet Controls", font=("Helvetica", 16, "bold")).pack(pady=(0, 20))

for name, data in planets.items():
    # Create the turtle object for the planet
    t = turtle.RawTurtle(screen)
    t.shape("circle")
    t.color(data["color"])
    t.shapesize(stretch_wid=data["radius"] / 10, stretch_len=data["radius"] / 10)
    t.penup()
    t.goto(data["distance"], 0) # Start at its initial position
    planet_turtles[name] = t

    # Create a frame for each planet's controls for better organization
    planet_control_frame = ttk.Frame(control_frame, padding=5)
    planet_control_frame.pack(fill=tk.X, pady=5)

    # Add a label for the planet name
    ttk.Label(planet_control_frame, text=f"{name} Speed").pack()

    # Create a slider to control the speed
    # Use a lambda function to pass the planet's name to the update function
    slider = ttk.Scale(
        planet_control_frame,
        from_=0,
        to=5,
        orient="horizontal",
        command=lambda val, p_name=name: update_speed(p_name, val)
    )
    slider.set(data["speed"])
    slider.pack(pady=5)
    sliders[name] = slider

# --- Start the Simulation ---
# Call the update function once to begin the loop
update_simulation()

# --- Start the Tkinter Event Loop ---
# This keeps the window open and responsive to user input
root.mainloop()
