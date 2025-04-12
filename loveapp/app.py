import streamlit as st
import time

# Judul aplikasi
st.title("HALO KAKAK ❤️")

# Input nama
nama = st.text_input("Masukkan nama kakak:")

if nama:
    st.write(f"Salam dari puguh untukmu,Aku sayang kamu, {nama} 💖")

    # Animasi Hati
    st.markdown("<h1 style='text-align: center;'>❤️❤️❤️</h1>", unsafe_allow_html=True)

    # Efek animasi hati
    for _ in range(5):
        time.sleep(1)
        st.markdown("<h1 style='text-align: center;'>❤️</h1>", unsafe_allow_html=True)
        time.sleep(1)
        st.markdown("<h1 style='text-align: center;'>❤️❤️❤️</h1>", unsafe_allow_html=True)
