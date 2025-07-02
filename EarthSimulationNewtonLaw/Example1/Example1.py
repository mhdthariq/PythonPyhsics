import turtle
import math

# Konstanta
G = 6.67430e-11    # Konstanta gravitasi (m^3 kg^-1 s^-2)
SM = 1.989e30      # Massa matahari (kg)
AU = 1.496e11      # Jarak rata-rata matahari ke bumi (m)
dt = 60 * 60       # Interval waktu (1 jam dalam detik)
skala = 250 / AU   # Skala visualisasi (AU -> piksel)

# Inisialisasi posisi dan kecepatan bumi
x = AU
y = 0
vx = 0
vy = 29_780     # Kecepatan awal bumi (29.78 m/s)

# Turtle setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simulasi Orbit Bumi berdasarkan Hukum Newton Bagian 1")
screen.tracer(0)

# Gambar Matahari
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.penup()
sun.goto(0, 0)
sun.stamp()
sun.hideturtle()

# Gambar Bumi
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.penup()
earth.goto(x * skala, y * skala)
earth.pendown()

# Simulasi orbit bumi
while True:
    # Hitung jarak dan percepatan
    r = math.sqrt(x**2 + y**2)
    a = -G * SM / r**3
    ax = a * x
    ay = a * y

    # Update kecepatan
    vx += ax * dt
    vy += ay * dt

    # Update posisi
    x += vx * dt
    y += vy * dt

    # Update tampilan turtle
    earth.goto(x * skala, y * skala)
    screen.update()
