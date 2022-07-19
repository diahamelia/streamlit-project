import streamlit as st
import panda as pd

st.header("Alan Jones")
st.subheader("Writer and Developer")
st.write("some descriptive text goes in here")
with st.container():
   image_col, text_col = st.columns(1,2):
   with image_col:
      st.image(image)
   with text_col:
      st.write(text)
with st.container():
   image_col, text_col = st.columns(1,2):
   with image_col:
      st.image(image2)
   with text_col:
      st.write(text2)
