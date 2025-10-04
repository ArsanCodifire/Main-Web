import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Discord Stats", page_icon=":robot:")

def embed_iframe(url, width=350, height=500, radius=20):
    components.html(f"""
    <div style="overflow:hidden; border-radius:{radius}px; width:{width}px; height:{height}px; border:1px solid #ccc; margin-bottom:10px;">
        <iframe src="{url}" width="100%" height="100%" style="border:none;"></iframe>
    </div>
    """, height=height+10)

embed_iframe("https://pygamer-b24o.onrender.com")
embed_iframe("https://pytools-pm6d.onrender.com")
embed_iframe("https://pymedia.onrender.com")