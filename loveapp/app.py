import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# Fungsi bentuk love
def love_shape(t):
    x = 16 * np.sin(t)**3
    y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
    return x, y

st.set_page_config(page_title="Hai sayangku 💖", layout="centered")

st.title("kamu adalah orang tersayang karena  tahu web ini 💕")

nama = st.text_input("Masukkan namamu dulu ya :)")

if nama:
    if st.button("Masuk dan lihat kejutan ❤️"):
        st.write(f"Halo sayangku **{nama}**, ikan hiu makan tomat, minta whatsappnya dong cantik **Puguh** 💘")
        placeholder = st.empty()

        # Animasi terus-menerus
        t = np.linspace(0, 2 * np.pi, 1000)
        while True:
            fig, ax = plt.subplots()
            x, y = love_shape(t)
            color = np.random.choice(['red', 'hotpink', 'deeppink', 'magenta', 'crimson', 'orange'])

            ax.plot(x, y, color=color, linewidth=4)
            ax.set_facecolor("black")
            ax.axis("off")

            # Tampilkan ke streamlit
            placeholder.pyplot(fig)
            plt.close(fig)
            time.sleep(0.2)
