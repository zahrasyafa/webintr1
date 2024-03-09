import streamlit as st
def page_3():
  st.title("This page using for rumus matematika :D")
  st.write("This page use to show rumus matematika ≽^•⩊•^≼")
  st.write("Show page from file.MD (Mark Down)")

  with open("alifa.md", "r") as file:
    isi_teks = file.read()
  st.markdown(isi_teks)

  st.write("OHH YAA! Next page show aplikasi hitung persegi panjang!")
  st.write("YOKK DIBUKA GAIS ৻(  •̀ ᗜ •́  ৻)")
