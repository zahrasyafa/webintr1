import streamlit as st
import pandas as pd

st.write("Coding Club 2024")
df = pd.DataFrame({
  'number': [1, 2, 3, 4, 5],
  'name': ['ali','ceros','timbul','esok','mayer'],
  'age': [19, 92, 67, 35, 16],
  'book':['bumi series', 'aldebaran', 'hello', 'hujan', 'failure tale']
})

df