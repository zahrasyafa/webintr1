import streamlit as st
# import pandas as pd

# st.write("Favorite Character!")
# df = pd.DataFrame({
#   'number': [1, 2, 3, 4, 5],
#   'name': ['ali','ceros','timbul','esok','mayer'],
#   'age': [19, 92, 67, 35, 16],
#   'book':['bumi series', 'aldebaran', 'hello', 'hujan', 'failure tale']
# })

# df


def page_1():
  st.title("Page 1")
  st.write("This page use to introduction")
def page_2():
  st.title("Page 2")
  st.write("This page use to show youtube video")
def page_3():
  st.title("Page 3")
  st.write("This page use to show rumus matematika")

PAGES = {
  "Page 1" : page_1,
  "Page 2" : page_2,
  "Page 3" : page_3,
}

page = st.sidebar.radio("My Pages!", list(PAGES.keys()))
PAGES[page]()

 