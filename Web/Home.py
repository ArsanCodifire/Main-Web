import streamlit as st
st.set_page_config(
    page_title="Arsan Codifire",
    page_icon=":computer:"
)
col1, col2 = st.columns(2)
col1.title("Welcome")
col1.write("Hello, I am Arsan Codifire!")
col2.image("https://raw.githubusercontent.com/ArsanCodifire/Main-Web/refs/heads/main/Web/pfp.jpg")
st.subheader("Here are some of my projects:")  
st.write("     1. Base64 Converter")
st.write("     1. Auto-Clicker")
st.sidebar.success("Choose a page above")







