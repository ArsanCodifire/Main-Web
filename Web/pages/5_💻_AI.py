import streamlit as st
import cohere as ai
st.title("Welcome to the AI sector.")

    
token=st.secrets["TOKEN"]
def gen(prompt,mdl):
    co = ai.ClientV2(token)
    response = co.chat(
        model=mdl,
        messages=[{"role": "user", "content": prompt}]
    )
    return response

mdl=st.selectbox("Models",["command-xlarge-nightly","command-medium-nightly"])
if mdl=="command-xlarge-nightly":
    st.write("Slow chatbot")
    st.toast(f"Model selected: '{mdl}'", icon="💻")
elif mdl=="command-medium-nightly":
    st.write("Fast chatbot")
    st.toast(f"Model selected: '{mdl}'", icon="💻")

pr=st.chat_input()
if pr:
    with st.chat_message("user"):
        st.markdown(pr)
    with st.chat_message("assistant"):
        st.markdown(gen(pr,mdl))
        st.toast('You used AI', icon='🎉')
