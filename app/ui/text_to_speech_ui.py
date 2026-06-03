import streamlit as st
from tts.text_to_speech import speak


def app():

    st.title("🔊 Text-to-Speech")

    text = st.text_area("Enter text")

    if st.button("Speak"):

        if text.strip():

            speak(text)

            st.success("Speech generated")