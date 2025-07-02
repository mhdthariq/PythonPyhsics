import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider, IntSlider, Play, VBox, HBox, jslink
from IPython.display import display
from typing import Tuple

# Konstanta Fisika
G = 6.67430e-11
M_sun = 1.989e30
M_earth = 5.972e24
M_moon = 7.342e22
AU = 1.496e11
MOON_DIST = 384.4e6
EARTH_VEL = 29_780
MOON_VEL = 1022

# Parameter waktu
dt = 900            # Waktu per langkah: 15 menit (dalam detik)
total_days = 120
steps = int((total_days * 24 * 3600) / dt)

# State Vector: [x, y, vx, vy] untuk Sun, Earth, Moon
state = np.array([
    0.0, 0.0, 0.0, 0.0,                             # Sun
    AU, 0.0, 0.0, EARTH_VEL,                        # Earth
    AU + MOON_DIST, 0.0, 0.0, EARTH_VEL + MOON_VEL  # Moon
], dtype='float64')

def grav_acc(x1: float, y1: float, x2: float, y2: float, m2: float) -> Tuple[float, float]:
    dx = x2 - x1
    dy = y2 - y1
    r = np.hypot(dx, dy) + 1e-5  # Hindari div by 0
    r3 = r**3
    return G * m2 * dx / r3, G * m2 * dy / r3

def derivatives(s: np.ndarray) -> np.ndarray:
    x_s, y_s, vx_s, vy_s = s[0:4]
    x_e, y_e, vx_e, vy_e = s[4:8]
    x_m, y_m, vx_m, vy_m = s[8:12]

    # Sun affected by Earth and Moon
    a_s_e = grav_acc(x_s, y_s, x_e, y_e, M_earth)
    a_s_m = grav_acc(x_s, y_s, x_m, y_m, M_moon)
    ax_s = a_s_e[0] + a_s_m[0]
    ay_s = a_s_e[1] + a_s_m[1]

    # Earth affected by Sun and Moon
    a_e_s = grav_acc(x_e, y_e, x_s, y_s, M_sun)
    a_e_m = grav_acc(x_e, y_e, x_m, y_m, M_moon)
    ax_e = a_e_s[0] + a_e_m[0]
    ay_e = a_e_s[1] + a_e_m[1]

    # Moon affected by Sun and Earth
    a_m_s = grav_acc(x_m, y_m, x_s, y_s, M_sun)
    a_m_e = grav_acc(x_m, y_m, x_e, y_e, M_earth)
    ax_m = a_m_s[0] + a_m_e[0]
    ay_m = a_m_s[1] + a_m_e[1]

    return np.array([
        vx_s, vy_s, ax_s, ay_s,
        vx_e, vy_e, ax_e, ay_e,
        vx_m, vy_m, ax_m, ay_m
    ])

def rk4_steps(s: np.ndarray, dt: float) -> np.ndarray:
    k1 = derivatives(s)
    k2 = derivatives(s + 0.5 * dt * k1)
    k3 = derivatives(s + 0.5 * dt * k2)
    k4 = derivatives(s + dt * k3)
    return s + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

# Simulasi RK4
states = []
temp = state.copy()
for _ in range(steps):
    states.append(temp.copy())
    temp = rk4_steps(temp, dt)

states = np.array(states)

# Debug: Cek posisi awal dan akhir
print("Posisi awal Bumi:", states[0][4:6])
print("Posisi akhir Bumi:", states[-1][4:6])
print("Posisi awal Bulan:", states[0][8:10])
print("Posisi akhir Bulan:", states[-1][8:10])

# Fungsi visualisasi
def plot_orbit(i: int, zoom: float = 2.0) -> None:
    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_facecolor("black")

    # Jejak orbit
    if i > 0:
        earth_x = []
        earth_y = []
        moon_x = []
        moon_y = []
        for j in range(i):
            earth_x.append(states[j][4])
            earth_y.append(states[j][5])
            moon_x.append(states[j][8])
            moon_y.append(states[j][9])
        ax.plot(earth_x, earth_y, 'b-', lw=0.8, label='Orbit Bumi')
        ax.plot(moon_x, moon_y, 'gray', lw=0.5, label='Orbit Bulan')

    # Objek saat ini
    current_state = states[i]
    ax.plot(current_state[0], current_state[1], 'yo', markersize=8, label='Matahari')
    ax.plot(current_state[4], current_state[5], 'bo', markersize=6, label='Bumi')
    ax.plot(current_state[8], current_state[9], 'wo', markersize=3, label='Bulan')

    ax.set_xlim(-zoom * AU, zoom * AU)
    ax.set_ylim(-zoom * AU, zoom * AU)
    ax.set_aspect('equal')
    ax.set_title(f'Hari ke-{int(i * dt // (24 * 3600))}', color='white')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
    ax.legend(facecolor='black', labelcolor='white', loc='upper right')
    plt.show()

# Widget Interaktif
play = Play(min=0, max=len(states) - 1, step=1, interval=20, description='▶')
slider = IntSlider(min=0, max=len(states) - 1, step=1, description='Frame')
zoom_slider = FloatSlider(value=2.0, min=0.5, max=5.0, step=0.1, description='Zoom')

# Sinkronisasi play dan slider
jslink((play, 'value'), (slider, 'value'))

controls = HBox([play, slider])
interact_ui = interact(plot_orbit, i=slider, zoom=zoom_slider)
display(VBox([controls, zoom_slider]))
