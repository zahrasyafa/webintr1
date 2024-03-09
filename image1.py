import streamlit as st
from PIL import Image,ImageFilter
import io



def convert_gambar(image, format) :
    gambar_convert = image.convert("RGB")
    image_bytes = io.BytesIO()
    gambar_convert.save(image_bytes, format = format)
    return image_bytes.getvalue()


def buat_filter(image, jenis_filter):
    if jenis_filter == "BLUR" :
        gambar_filter = image.filter(ImageFilter.BLUR)
    elif jenis_filter == "CONTOUR" :
        gambar_filter = image.filter(ImageFilter.CONTOUR)
    elif jenis_filter == "EMBOSS" :
        gambar_filter = image.filter(ImageFilter.EMBOSS)
    elif jenis_filter == "SMOOTH" :
        gambar_filter = image.filter(ImageFilter.SMOOTH)
    elif jenis_filter == "FIND_EDGES" :
        gambar_filter = image.filter(ImageFilter.FIND_EDGES)
    elif jenis_filter == "EDGE_ENHANCE_MORE" :
        gambar_filter = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    else :
        gambar_filter = image.filter(ImageFilter.SHARPEN)

    return gambar_filter

def main():
    unggah_gambar = st.file_uploader('Choose your image!:', type=['jpg', 'jpeg', 'png'])
    if unggah_gambar is not None :
        gambar = Image.open(unggah_gambar)
        kolom1,kolomtengah, kolom2 = st.columns(3)
        pilih_filter = kolomtengah.selectbox('Choose type of filter', ["BLUR", "CONTOUR", "EMBOSS", "SMOOTH", "FIND_EDGES", "EDGE_ENHANCE_MORE", "SHARPEN"])
        
        kolom1.image(gambar, caption= 'Original image', width=200)
        filtered_image = buat_filter(gambar, pilih_filter.upper())
        kolom2.image(filtered_image, caption= 'Modified image', width=200)
        
        image_bytes = convert_gambar(filtered_image, "PNG")
        kolomtengah.download_button(label="Download your image!", data = image_bytes, file_name = "hasil.png")