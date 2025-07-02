import turtle
import tkinter as tk
from tkinter import ttk
import math
import random

# --- Main Application Window ---
root = tk.Tk()
root.title("Polished Solar System Simulation")
root.geometry("1300x850") # Adjusted size for better layout
root.configure(bg='#1a1a1a') # Dark background for the main window

# --- Global Simulation State ---
is_paused = True # Start the simulation in a paused state

# --- Functions ---

def toggle_pause():
    """Starts, pauses, or resumes the simulation."""
    global is_paused
    is_paused = not is_paused
    # The button will now toggle between Start, Pause, and Resume
    if is_paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
        # If resuming, call update_simulation to restart the loop
        update_simulation()

def reset_simulation():
    """Resets all planets to their initial positions and angles."""
    for name, data in planets.items():
        data["angle"] = 0 # Reset angle
        planet_turtle = planet_turtles[name]
        label_turtle = planet_labels[name]

        # Recalculate initial position
        x = data["distance"]
        y = 0

        planet_turtle.goto(x, y)

        # Clear and redraw label at initial position
        label_turtle.clear()
        label_turtle.goto(x, y + 15)
        label_turtle.write(name, align="center", font=("Arial", 8, "normal"))

    # A single screen update is needed to show the reset state
    screen.update()


def update_speed(planet_name, value):
    """Updates the speed of a planet and the corresponding value label."""
    speed_value = float(value)
    planets[planet_name]["speed"] = speed_value
    # Update the text of the label to show the numeric speed
    speed_labels[planet_name].config(text=f"{speed_value:.2f}")


def draw_stars():
    """Draws a field of stars in the background for a cosmic feel."""
    star_drawer = turtle.RawTurtle(screen)
    star_drawer.hideturtle()
    star_drawer.penup()
    star_drawer.speed(0)
    for _ in range(200): # More stars
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        # Avoid drawing stars on top of the sun
        if math.sqrt(x**2 + y**2) > 30:
            star_drawer.goto(x, y)
            star_drawer.dot(random.randint(1, 3), "white")

def draw_orbit(t, radius):
    """Draws a circular orbit path."""
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    t.penup()

def update_simulation():
    """The main animation loop for the simulation."""
    if is_paused:
        return # Stop the loop if paused

    for name, data in planets.items():
        planet_turtle = planet_turtles[name]
        label_turtle = planet_labels[name]

        data["angle"] += data["speed"]
        if data["angle"] >= 360:
            data["angle"] -= 360

        angle_rad = math.radians(data["angle"])
        x = data["distance"] * math.cos(angle_rad)
        y = data["distance"] * math.sin(angle_rad)

        # Move the planet body
        planet_turtle.goto(x, y)

        # Move and redraw the label in every frame
        label_turtle.clear()
        label_turtle.goto(x, y + 15)
        label_turtle.write(name, align="center", font=("Arial", 8, "normal"))

    screen.update()
    root.after(15, update_simulation)

# --- Main Frames ---
style = ttk.Style()
style.theme_use('clam') # A modern theme
style.configure("TFrame", background='#1a1a1a')
style.configure("TButton", padding=6, relief="flat", background="#333", foreground="white")
style.map("TButton", background=[('active', '#555')])
style.configure("TLabel", background='#1a1a1a', foreground='white')
style.configure("Horizontal.TScale", background='#1a1a1a')


simulation_frame = ttk.Frame(root, padding=10)
simulation_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

control_panel_frame = ttk.Frame(root, padding=10)
control_panel_frame.pack(side=tk.RIGHT, fill=tk.Y)

# --- Simulation Canvas ---
canvas = tk.Canvas(simulation_frame, width=800, height=800, bg="black", highlightthickness=0)
canvas.pack()

screen = turtle.TurtleScreen(canvas)
screen.setworldcoordinates(-420, -420, 420, 420)
screen.bgcolor("black")
screen.tracer(0)

# --- Draw Static Elements ---
draw_stars()

# Orbit Drawer Turtle
orbit_drawer = turtle.RawTurtle(screen)
orbit_drawer.hideturtle()
orbit_drawer.penup()
orbit_drawer.color("#333")
orbit_drawer.speed(0)

# --- Sun ---
sun = turtle.RawTurtle(screen)
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_wid=2.5, stretch_len=2.5)
sun.penup()

# --- Planet Data ---
planets = {
    "Mercury": {"distance": 50, "radius": 3.8, "color": "grey", "angle": 0, "speed": 1.6},
    "Venus":   {"distance": 78, "radius": 9.5, "color": "#E8B468", "angle": 0, "speed": 1.2},
    "Earth":   {"distance": 110, "radius": 10, "color": "#4A90E2", "angle": 0, "speed": 1.0},
    "Mars":    {"distance": 152, "radius": 5.3, "color": "#D05F48", "angle": 0, "speed": 0.8},
    "Jupiter": {"distance": 220, "radius": 20, "color": "#D8CA9D", "angle": 0, "speed": 0.43},
    "Saturn":  {"distance": 280, "radius": 18, "color": "#F0E68C", "angle": 0, "speed": 0.32},
    "Uranus":  {"distance": 330, "radius": 14, "color": "#AFDBF5", "angle": 0, "speed": 0.23},
    "Neptune": {"distance": 380, "radius": 13.8, "color": "#3F54BA", "angle": 0, "speed": 0.18}
}

# --- Create Turtles, Labels, Orbits, and UI Controls ---
planet_turtles = {}
planet_labels = {}
sliders = {}
speed_labels = {} # Dictionary to hold the new speed value labels

# --- Control Panel Setup ---
ttk.Label(control_panel_frame, text="Simulation Controls", font=("Helvetica", 18, "bold")).pack(pady=(0, 10))

# Buttons Frame
button_frame = ttk.Frame(control_panel_frame)
button_frame.pack(fill=tk.X, pady=10)
pause_button = ttk.Button(button_frame, text="Start", command=toggle_pause) # Initial text is "Start"
pause_button.pack(side=tk.LEFT, expand=True, padx=5)
reset_button = ttk.Button(button_frame, text="Reset", command=reset_simulation)
reset_button.pack(side=tk.LEFT, expand=True, padx=5)

ttk.Separator(control_panel_frame, orient='horizontal').pack(fill='x', pady=10)

# --- Scrollable Frame for Sliders ---
slider_canvas = tk.Canvas(control_panel_frame, bg='#1a1a1a', highlightthickness=0)
scrollbar = ttk.Scrollbar(control_panel_frame, orient="vertical", command=slider_canvas.yview)
scrollable_frame = ttk.Frame(slider_canvas)

scrollable_frame.bind("<Configure>", lambda e: slider_canvas.configure(scrollregion=slider_canvas.bbox("all")))
slider_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
slider_canvas.configure(yscrollcommand=scrollbar.set)

slider_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


for name, data in planets.items():
    draw_orbit(orbit_drawer, data["distance"])

    t = turtle.RawTurtle(screen)
    t.shape("circle")
    t.color(data["color"])
    t.shapesize(stretch_wid=data["radius"] / 10, stretch_len=data["radius"] / 10)
    t.penup()
    t.goto(data["distance"], 0)
    planet_turtles[name] = t

    # Setup for the label turtle
    label = turtle.RawTurtle(screen)
    label.hideturtle()
    label.penup()
    label.color("white")
    label.goto(data["distance"], data["radius"] + 15)
    planet_labels[name] = label

    # --- UI Controls Setup ---
    planet_control_frame = ttk.Frame(scrollable_frame)
    planet_control_frame.pack(fill=tk.X, pady=4, padx=5)

    # Frame for the planet name and speed value
    label_frame = ttk.Frame(planet_control_frame)
    label_frame.pack(fill=tk.X)
    ttk.Label(label_frame, text=f"{name}").pack(side=tk.LEFT)

    # Add the speed value label
    speed_label = ttk.Label(label_frame, text=f"{data['speed']:.2f}")
    speed_label.pack(side=tk.RIGHT)
    speed_labels[name] = speed_label

    # Add the slider
    slider = ttk.Scale(
        planet_control_frame, from_=0, to=4, orient="horizontal",
        command=lambda val, p_name=name: update_speed(p_name, val)
    )
    slider.set(data["speed"])
    slider.pack(pady=2, fill=tk.X, expand=True)
    sliders[name] = slider

# --- Final Setup ---
# Draw the initial state of the simulation before starting the main loop
reset_simulation()
root.mainloop()
