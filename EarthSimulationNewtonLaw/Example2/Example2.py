import numpy as np
import matplotlib.pyplot as plt

# Konstanta Fisika
G = 6.67430e-11             # Gravitasi Newton (m^3 kg^-1 s^-2)
M_matahari = 1.989e30       # Massa Matahari dalam kg
AU = 1.496e11               # Jarak satu Astronomical Unit (AU) dalam meter
dt = 60 * 60                # Waktu per langkah: 1 jam (dalam detik)
jumlah_langkah = 24 * 365   # Jumlah langkah simulasi: 1 tahun (dalam jam)

# Inisialisasi posisi dan kecepatan bumi
x = AU
y = 0
vx = 0
vy = 29_780     # Kecepatan awal bumi (29.78 m/s)

# Array untuk menyimpan posisi
x_posisi = []
y_posisi = []

# Simulasi gerak
for _ in range(jumlah_langkah):
    r = np.sqrt(x**2 + y**2)
    a = -G * M_matahari / r**3
    ax = a * x
    ay = a * y
    vx += ax * dt
    vy += ay * dt

    x += vx * dt
    y += vy * dt

    x_posisi.append(x)
    y_posisi.append(y)

# Visualisasi
plt.figure(figsize=(8, 8))
plt.plot(0, 0, 'yo', markersize=12, label='Matahari')  # Titik pusat
plt.plot(np.array(x_posisi), np.array(y_posisi), '-b', label='Orbit Bumi')
plt.axis('equal')
plt.xlabel("x (meter)")
plt.ylabel("y (meter)")
plt.title("Simulasi Orbit Bumi Mengelilingi Matahari (Metode Newton)")
plt.legend()
plt.grid(True)
plt.show()
