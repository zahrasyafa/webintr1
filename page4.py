import streamlit as st
def page_4():
    st.title("Ayo hitung luas persegi panjang!")
    panjang = st.number_input("Panjangnya berapa?",0)
    lebar = st.number_input("Lebarnya berapa?",0)
    hitung = st.button("BANTU HITUNG DONG!")

    if hitung :
        luas = panjang * lebar
        st.write ("Hasilnya adalah ...",luas)
        st.success(f"(˵ •̀ ᴗ - ˵ ) ✧")

    

