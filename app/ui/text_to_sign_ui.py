import streamlit as st

# from app.sign_animation.animator import animate_sign

import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

sys.path.append(PROJECT_ROOT)

from sign_animation.animator import animate_sign


def app():

    st.title("🤟 Text to Sign Language")

    st.markdown("""
    Convert text into sign language animation.
    """)

    user_text = st.text_input(
        "Enter text"
    )

    if st.button("Generate Sign Animation"):

        if user_text.strip() != "":

            animate_sign(user_text)