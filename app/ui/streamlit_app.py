import streamlit as st
from sign_language_ui import app as sign_language_app
from speech_to_text_ui import app as speech_to_text_app

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(BASE_DIR)

from tts.text_to_speech import speak

# Page config
st.set_page_config(
    page_title="Multi-Modal Agentic AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Sign Language Detection",
        "Speech-to-Text",
        "Text-to-Speech",
        "About"
    ]
)

# Home Page
if page == "Home":

    st.title("🤖 Multi-Modal Agentic AI System")

    st.markdown("""
    ## Features
    
    ✅ Sign Language Recognition  
    ✅ Speech Recognition  
    ✅ Text-to-Speech  
    ✅ AI-based Communication System  
    
    ---
    
    ### Inputs
    - 🎤 Speech
    - 📷 Image
    - 🎥 Video
    
    ### Outputs
    - 📝 Text
    - 🔊 Speech
    - 🤟 Sign Interpretation
    """)

# Sign Language Page
elif page == "Sign Language Detection":

    st.title("🤟 Sign Language Detection")

    sign_language_app()

# Speech-to-Text Page
elif page == "Speech-to-Text":

    st.title("🎤 Speech-to-Text")

    speech_to_text_app()

# # Text-to-Speech Page
# elif page == "Text-to-Speech":

#     st.title("🔊 Text-to-Speech")

#     text = st.text_input("Enter text")

#     if st.button("Speak"):

#         st.success(f"Speaking: {text}")
        
# Text-to-Speech Page
elif page == "Text-to-Speech":

    st.title("🔊 Text-to-Speech")

    text = st.text_input("Enter text")

    if st.button("Speak"):

        if text.strip() != "":

            speak(text)

            st.success("Speech Played Successfully!")

        else:

            st.warning("Please enter text.")

# About Page
elif page == "About":

    st.title("📘 About Project")

    st.markdown("""
    This project is a Multi-Modal Agentic AI System.
    
    Technologies Used:
    - Python
    - OpenCV
    - MediaPipe
    - Streamlit
    - Machine Learning
    - Text-to-Speech
    """)