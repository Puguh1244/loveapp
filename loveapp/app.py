import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Fungsi untuk membuat gambar love dengan persamaan parametris
def love_curve(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return x, y

# Inisialisasi Streamlit
st.title("SELAMAT DATANG DI WEB INI, KAMU ADALAH ORANG TERSAYANG KARENA TAU WEB INI")

# Meminta pengguna memasukkan nama
name = st.text_input("Masukkan Nama Anda:", "")

# Tombol untuk melanjutkan setelah memasukkan nama
if name:
    # Menampilkan pesan dengan nama
    st.write(f"Halo sayangku {name}, kamu mendapatkan love dari Puguh 💖")

    # Menambahkan tombol untuk melanjutkan
    if st.button("Lihat Animasi"):
        # Membuat figure dan axis untuk plot
        fig, ax = plt.subplots()
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)
        ax.set_aspect('equal')

        # Membuat garis untuk love
        line, = ax.plot([], [], lw=2)

        # Menampilkan animasi secara dinamis
        for frame in range(200):  # Jumlah frame untuk animasi
            t = np.linspace(0, 2 * np.pi, 1000)
            x, y = love_curve(t + frame * 0.1)  # Perubahan t untuk animasi
            line.set_data(x, y)

            # Mengubah warna secara acak setiap frame
            color = np.random.choice(['red', 'blue', 'green', 'purple', 'orange', 'yellow'])
            line.set_color(color)

            # Menggambar ulang grafik
            st.pyplot(fig)

            # Jeda antara frame
            time.sleep(0.05)  # Delay antara frame (50ms)

else:
    st.write("Masukkan nama Anda untuk melihat animasi love!")
