# import streamlit as st
# from sign_language_ui import app as sign_language_app
# from speech_to_text_ui import app as speech_to_text_app
# from text_to_sign_ui import app as text_to_sign_app
# from agentic_ai_ui import app as agentic_ai_app

# import sys
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# sys.path.append(BASE_DIR)

# from tts.text_to_speech import speak

# # Page config
# st.set_page_config(
#     page_title="Multi-Modal Agentic AI",
#     page_icon="🤖",
#     layout="wide"
# )

# # Sidebar
# st.sidebar.title("Navigation")

# page = st.sidebar.radio(
#     "Go To",
#     [
#         "Home",
#         "Sign Language Detection",
#         "Speech-to-Text",
#         "Text-to-Speech",
#         "Text-to-Sign",
#         "Agentic AI Assistant",
#         "About"
#     ]
# )

# # Home Page
# if page == "Home":

#     st.title("🤖 Multi-Modal Agentic AI System")

#     st.markdown("""
#     ## Features
    
#     ✅ Sign Language Recognition  
#     ✅ Speech Recognition  
#     ✅ Text-to-Speech  
#     ✅ AI-based Communication System  
    
#     ---
    
#     ### Inputs
#     - 🎤 Speech
#     - 📷 Image
#     - 🎥 Video
    
#     ### Outputs
#     - 📝 Text
#     - 🔊 Speech
#     - 🤟 Sign Interpretation
#     """)

# # Sign Language Page
# elif page == "Sign Language Detection":

#     st.title("🤟 Sign Language Detection")

#     sign_language_app()

# # Speech-to-Text Page
# elif page == "Speech-to-Text":

#     st.title("🎤 Speech-to-Text")

#     speech_to_text_app()

# # # Text-to-Speech Page
# # elif page == "Text-to-Speech":

# #     st.title("🔊 Text-to-Speech")

# #     text = st.text_input("Enter text")

# #     if st.button("Speak"):

# #         st.success(f"Speaking: {text}")
        
# # Text-to-Speech Page
# elif page == "Text-to-Speech":

#     st.title("🔊 Text-to-Speech")

#     text = st.text_input("Enter text")

#     if st.button("Speak"):

#         if text.strip() != "":

#             speak(text)

#             st.success("Speech Played Successfully!")

#         else:

#             st.warning("Please enter text.")


# # TEXT TO SIGN PAGE
# elif page == "Text-to-Sign":

#     st.title("🤟 Text-to-Sign")

#     text_to_sign_app()
    
# # Agentic AI Assistant Page    
# elif page == "Agentic AI Assistant":

#     agentic_ai_app()

# # About Page
# elif page == "About":

#     st.title("📘 About Project")

#     st.markdown("""
#     This project is a Multi-Modal Agentic AI System.
    
#     Technologies Used:
#     - Python
#     - OpenCV
#     - MediaPipe
#     - Streamlit
#     - Machine Learning
#     - Text-to-Speech
#     """)


import streamlit as st

from sign_language_ui import app as sign_language_app
from speech_to_text_ui import app as speech_to_text_app
from text_to_sign_ui import app as text_to_sign_app
from text_to_speech_ui import app as text_to_speech_app
from agentic_ai_ui import app as agentic_ai_app
from voice_assistant_ui import app as voice_assistant_app

# Page Configuration
st.set_page_config(
    page_title="Multi-Modal Agentic AI",
    page_icon="🤖",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Sign Language Detection",
        "Speech-to-Text",
        "Text-to-Speech",
        "Text-to-Sign",
        "Agentic AI Assistant",
        "Voice Assistant",
        "About"
    ]
)

# -------------------------
# HOME PAGE
# -------------------------
if page == "Home":

    st.title("🤖 Multi-Modal Agentic AI System")

    st.markdown("""
    ## Features

    ✅ Sign Language Recognition  
    ✅ Speech Recognition  
    ✅ Text-to-Speech  
    ✅ Text-to-Sign Conversion  
    ✅ Agentic AI Assistant  
    ✅ Memory-Aware Conversations  
    ✅ Web Search Agent  
    ✅ Knowledge/RAG Agent  
    ✅ Action Agent  

    ---

    ### Inputs
    - 🎤 Speech
    - 📷 Image
    - 🎥 Video
    - ⌨️ Text

    ### Outputs
    - 📝 Text
    - 🔊 Speech
    - 🤟 Sign Interpretation
    - 🌐 Web Results
    - 🧠 AI Responses
    """)

# -------------------------
# SIGN LANGUAGE DETECTION
# -------------------------
elif page == "Sign Language Detection":

    sign_language_app()

# -------------------------
# SPEECH TO TEXT
# -------------------------
elif page == "Speech-to-Text":

    speech_to_text_app()

# -------------------------
# TEXT TO SPEECH
# -------------------------
elif page == "Text-to-Speech":

    text_to_speech_app()

# -------------------------
# TEXT TO SIGN
# -------------------------
elif page == "Text-to-Sign":

    text_to_sign_app()

# -------------------------
# AGENTIC AI ASSISTANT
# -------------------------
elif page == "Agentic AI Assistant":

    agentic_ai_app()

# -------------------------
# Voice Assistant
# -------------------------
elif page == "Voice Assistant":

    voice_assistant_app()

# -------------------------
# ABOUT PAGE
# -------------------------
elif page == "About":

    st.title("📘 About Project")

    st.markdown("""
    ## Multi-Modal Agentic AI System

    This project combines multiple AI modalities into a single platform.

    ### Modules

    - 🤟 Sign Language Recognition
    - 🎤 Speech Recognition
    - 🔊 Text-to-Speech
    - 🤟 Text-to-Sign Conversion
    - 🧠 Agentic AI Assistant
    - 🌐 Web Search Agent
    - 📚 Knowledge (RAG) Agent
    - 💾 Memory Agent
    - ⚡ Action Agent

    ### Technologies Used

    - Python
    - Streamlit
    - OpenCV
    - MediaPipe
    - TensorFlow
    - Whisper
    - FAISS / ChromaDB
    - LLM APIs
    - WebRTC
    """)