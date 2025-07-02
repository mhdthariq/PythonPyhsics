import turtle
import random

# Pengaturan layar
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simulasi Gerak Acak")

# Objek pena
pena = turtle.Turtle()
pena.color("white")
pena.speed(0)
pena.pensize(2)
pena.penup()
pena.goto(0, 0)
pena.pendown()

# Random Particles Function
def gerak_acak(jumlah_langkah=2000, panjang=10):
    for _ in range(jumlah_langkah):
        sudut = random.randint(0, 360)
        pena.setheading(sudut)
        pena.forward(panjang)

# Jalankan Simulasi
gerak_acak()

# Stop Program
pena.hideturtle()
turtle.done()
