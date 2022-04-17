from src.downyoutubepy import DownYoutubePy
import streamlit as st
import pandas as pd
import os
#import time

# App Title and Mode
st.sidebar.header('Type')
option = st.sidebar.radio('', options=['audio', 'video'])

st.title('Download Youtube {}'.format(option))

url = st.text_input('Youtube Url', key='url', value='')
a = st.button('Download', key='download')
if option and url:
    app = DownYoutubePy()
    save_path = 'D:\\Google Drive\\Mp3'
    if option == 'audio':
        app.ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{ 'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '128'}],
        'outtmpl': save_path + '/%(title)s.%(ext)s',}
    elif option == 'video':
        app.ydl_opts = {'format': 'bestvideo+bestaudio', 'postprocessors': [{ 'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
        'outtmpl': save_path + '/%(title)s.%(ext)s',}

    app.url = url
    app.typefile = option
    app.download()
    st.text('Finish')