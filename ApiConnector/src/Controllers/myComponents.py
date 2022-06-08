from pydantic import BaseModel
import streamlit as st
import logging
from api import post_data



binary_contents = b'example content'

def button():
     if st.button('Download'):
         st.download_button('Download binary file', binary_contents)
     else:
          logging.info('Falhou')

def apiButton():
    if st.button('Send Api'):
        post_data(5.0)
         #st.download_button('as', post_item(Item))
    else:
          logging.info('Falhou')
