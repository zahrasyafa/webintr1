import streamlit as st
def page_3():
  st.title("Page 3")
  st.write("This page use to show rumus matematika")
  st.write("Show halaman dari file.MD (Mark Down)")

  with open("alifa.md", "r") as file:
    isi_teks = file.read()
  st.markdown(isi_teks)