import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
# import pandas as pd

# st.write("Favorite Character!")
# df = pd.DataFrame({
#   'number': [1, 2, 3, 4, 5],
#   'name': ['ali','ceros','timbul','esok','mayer'],
#   'age': [19, 92, 67, 35, 16],
#   'book':['bumi series', 'aldebaran', 'hello', 'hujan', 'failure tale']
# })

# df






PAGES = {
  "Page 1" : page_1,
  "Page 2" : page_2,
  "Page 3" : page_3,
  "Page 4" : page_4,
}



st.sidebar.image("AFI.png",width=100)
page = st.sidebar.radio("My Pages!", list(PAGES.keys()))
PAGES[page]()

