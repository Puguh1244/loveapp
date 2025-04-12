import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fungsi untuk membuat gambar love dengan persamaan parametris
def love_curve(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# Inisialisasi Streamlit
st.title("Love Animation with Line")

# Meminta pengguna memasukkan nama
name = st.text_input("Masukkan Nama Anda:", "")

# Menampilkan pesan jika nama dimasukkan
if name:
    st.write(f"Selamat datang, {name}! 💖 Mari nikmati animasi love berikut:")

    # Membuat figure dan axis untuk plot
    fig, ax = plt.subplots()
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_aspect('equal')

    # Membuat garis untuk love
    line, = ax.plot([], [], lw=2)

    # Fungsi untuk update animasi
    def update(frame):
        t = np.linspace(0, 2 * np.pi, 1000)
        x, y = love_curve(t + frame * 0.1)  # Perubahan t untuk animasi
        line.set_data(x, y)

        # Mengubah warna secara acak setiap frame
        color = np.random.choice(['red', 'blue', 'green', 'purple', 'orange', 'yellow'])
        line.set_color(color)
        
        return line,

    # Membuat animasi dengan FuncAnimation
    ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

    # Menampilkan animasi di Streamlit
    st.pyplot(fig)
else:
    st.write("Masukkan nama Anda untuk melihat animasi love!")
