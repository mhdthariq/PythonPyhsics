import turtle
import tkinter as tk
from tkinter import ttk
import math
import random

# --- Main Application Window ---
root = tk.Tk()
root.title("Enhanced Earth-Moon Orbit Simulation")
root.geometry("1000x700")
root.configure(bg='#1a1a1a')

# --- Global Simulation State ---
is_paused = True # Start paused

# --- Simulation Data ---
moon_data = {
    "orbit_radius": 150,
    "angle": 0,
    "speed": 1.0, # Initial speed
    "turtle": None,
    "label": None
}

# --- Functions ---

def toggle_pause():
    """Starts, pauses, or resumes the simulation."""
    global is_paused
    is_paused = not is_paused
    pause_button.config(text="Resume" if is_paused else "Pause")
    if not is_paused:
        update_simulation()

def reset_simulation():
    """Resets the moon to its starting position."""
    moon_data["angle"] = 0
    x = moon_data["orbit_radius"]
    y = 0
    moon_data["turtle"].goto(x, y)
    moon_data["label"].clear()
    moon_data["label"].goto(x, y + 20)
    moon_data["label"].write("Moon", align="center", font=("Arial", 10, "normal"))
    screen.update()

def update_speed(value):
    """Updates the moon's speed from the slider and updates the label."""
    speed_value = float(value)
    moon_data["speed"] = speed_value
    speed_label.config(text=f"{speed_value:.2f}")

def draw_stars():
    """Draws a field of stars in the background."""
    star_drawer = turtle.RawTurtle(screen)
    star_drawer.hideturtle()
    star_drawer.penup()
    star_drawer.speed(0)
    for _ in range(150):
        x = random.randint(-350, 350)
        y = random.randint(-350, 350)
        if math.sqrt(x**2 + y**2) > 40: # Avoid stars on Earth
            star_drawer.goto(x, y)
            star_drawer.dot(random.randint(1, 3), "white")

def draw_orbit():
    """Draws the moon's orbital path."""
    orbit_drawer = turtle.RawTurtle(screen)
    orbit_drawer.hideturtle()
    orbit_drawer.penup()
    orbit_drawer.color("#444")
    orbit_drawer.goto(0, -moon_data["orbit_radius"])
    orbit_drawer.pendown()
    orbit_drawer.circle(moon_data["orbit_radius"])

def update_simulation():
    """The main animation loop."""
    if is_paused:
        return

    # Update angle based on speed
    moon_data["angle"] += moon_data["speed"]
    if moon_data["angle"] >= 360:
        moon_data["angle"] -= 360

    # Calculate new position
    theta = math.radians(moon_data["angle"])
    x = moon_data["orbit_radius"] * math.cos(theta)
    y = moon_data["orbit_radius"] * math.sin(theta)

    # Move moon and its label
    moon_data["turtle"].goto(x, y)
    moon_data["label"].clear()
    moon_data["label"].goto(x, y + 20)
    moon_data["label"].write("Moon", align="center", font=("Arial", 10, "normal"))

    screen.update()
    root.after(20, update_simulation)

# --- UI Styling and Frames ---
style = ttk.Style()
style.theme_use('clam')
style.configure("TFrame", background='#1a1a1a')
style.configure("TButton", padding=6, relief="flat", background="#333", foreground="white")
style.map("TButton", background=[('active', '#555')])
style.configure("TLabel", background='#1a1a1a', foreground='white')
style.configure("Horizontal.TScale", background='#1a1a1a')

simulation_frame = ttk.Frame(root, padding=10)
simulation_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

control_panel = ttk.Frame(root, padding=20)
control_panel.pack(side=tk.RIGHT, fill=tk.Y)

# --- Simulation Canvas Setup ---
canvas = tk.Canvas(simulation_frame, width=600, height=600, bg="black", highlightthickness=0)
canvas.pack()
screen = turtle.TurtleScreen(canvas)
screen.setworldcoordinates(-300, -300, 300, 300)
screen.bgcolor("black")
screen.tracer(0)

# --- Draw Static Elements ---
draw_stars()
draw_orbit()

# --- Earth ---
earth = turtle.RawTurtle(screen)
earth.shape("circle")
earth.color("deepskyblue")
earth.shapesize(stretch_wid=2.5, stretch_len=2.5)

# --- Moon ---
moon = turtle.RawTurtle(screen)
moon.shape("circle")
moon.color("lightgray")
moon.shapesize(stretch_wid=0.8, stretch_len=0.8)
moon.penup()
moon_data["turtle"] = moon

# --- Moon Label ---
moon_label = turtle.RawTurtle(screen)
moon_label.hideturtle()
moon_label.penup()
moon_label.color("white")
moon_data["label"] = moon_label

# --- Control Panel Widgets ---
ttk.Label(control_panel, text="Simulation Controls", font=("Helvetica", 18, "bold")).pack(pady=(0, 20))

button_frame = ttk.Frame(control_panel)
button_frame.pack(fill=tk.X, pady=10)
pause_button = ttk.Button(button_frame, text="Start", command=toggle_pause)
pause_button.pack(side=tk.LEFT, expand=True, padx=5)
reset_button = ttk.Button(button_frame, text="Reset", command=reset_simulation)
reset_button.pack(side=tk.LEFT, expand=True, padx=5)

ttk.Separator(control_panel, orient='horizontal').pack(fill='x', pady=20)

# Speed Control
speed_control_frame = ttk.Frame(control_panel)
speed_control_frame.pack(fill=tk.X)
ttk.Label(speed_control_frame, text="Moon Speed").pack(side=tk.LEFT)
speed_label = ttk.Label(speed_control_frame, text=f"{moon_data['speed']:.2f}")
speed_label.pack(side=tk.RIGHT)

speed_slider = ttk.Scale(control_panel, from_=0.1, to=5, orient="horizontal", command=update_speed)
speed_slider.set(moon_data["speed"])
speed_slider.pack(pady=5, fill=tk.X, expand=True)

# --- Final Setup and Main Loop ---
reset_simulation() # Set initial positions
root.mainloop()
