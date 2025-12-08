import streamlit as st
import os
st.set_page_config(
    page_title="Arsan Codifire",
    page_icon=":computer:"
)
current_folder = os.path.dirname(os.path.abspath(__file__))
local_image_path = os.path.join(current_folder, "pfp.jpg")
github_url = "https://raw.githubusercontent.com/ArsanCodifire/Main-Web/main/Web/pfp.jpg"

col1, col2 = st.columns(2)
col1.title("Welcome")
col1.write("Hello, I am Arsan Codifire!")
col2.image("pfp.jpg")
st.subheader("Here are some of my projects:")  
st.write("     1. Base64 Converter")
st.write("     1. Auto-Clicker")
st.sidebar.success("Choose a page above")








