from src.downyoutubepy import DownYoutubePy
import streamlit as st
import pandas as pd

import time

# App Title and Mode
st.title('Download Youtube videos and audios')
st.sidebar.header("Mode")

mode = st.sidebar.radio('Select Mode', options=['Vídeo', 'Áudio'])

