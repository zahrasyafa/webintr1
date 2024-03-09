import streamlit as st
from PIL import Image,ImageFilter

unggah_gambar = st.file_uploader('Choose your image!:', type=['jpg', 'jpeg', 'png'])
if unggah_gambar is not None :
    gambar = Image.open(unggah_gambar)
    st.image(gambar, caption= 'original image', width=200)
    gambar_filter = apply