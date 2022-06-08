import streamlit as st
from myComponents import button, apiButton

st.title("Page to send an Api and to download the binnary File")

pages_name = ['Api','Download Binnary File']

page = st.radio('Navigation', pages_name)

if page == 'Api':
    st.subheader('Page to send an Api')
    apiButton()
else:
    st.subheader('Page to download the binnary File')
    button()
