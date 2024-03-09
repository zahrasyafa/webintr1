import streamlit as st
def page_3():
  st.title("This page use to show rumus matematika ≽^•⩊•^≼")
  st.write('Guys, do you like matematika? Kalau suka kalian sukanya apa? kalau hitung duit kalian suka gak?')
  st.write("Show page from file.MD (Mark Down)")

  with open("alifa.md", "r") as file:
    isi_teks = file.read()
  st.markdown(isi_teks)

  st.write("OHH YAA! Next page show aplikasi hitung persegi panjang!")
  st.write("YOKK DIBUKA GAIS ৻(  •̀ ᗜ •́  ৻)")
