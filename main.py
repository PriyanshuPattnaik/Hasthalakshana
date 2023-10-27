import streamlit as st

PAGES = {
    "About Me": "about_me.py",
    "Image to Text": "image_to_text.py",
    "Image to Speech": "image_to_speech.py",
}

st.set_page_config(layout="wide", page_icon="https://static.thenounproject.com/png/497-200.png")

st.sidebar.header("Welcome to an app for the specially abled")
st.sidebar.markdown("Used CNN algorithm")

page = st.sidebar.radio("", list(PAGES.keys()))

with open(PAGES[page]) as f:
    code = compile(f.read(), PAGES[page], 'exec')
    exec(code)