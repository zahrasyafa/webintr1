import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from page5 import page_5
from page6 import page_6
from image1 import main
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
  "About Me" : page_1,
  "Page 1" : page_2,
  "Page 2" : page_3,
  "Page 3" : page_4,
  "Movie list" : page_5,
  "Novel Recomendations!" : page_6,
  "Convert your image" : main,
}


st.sidebar.image("AFI.png",width=100)
page = st.sidebar.radio("My Pages!", list(PAGES.keys()))
PAGES[page]()

st.markdown(
    """

        <style>
        [data-tesrid="stActionButtonIcon"]{
             display : none;
        }
              [data-testid="baseButton-header"]{
        }

        <style>
        """
)