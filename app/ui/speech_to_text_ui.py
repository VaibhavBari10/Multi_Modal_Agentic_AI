import streamlit as st
import tempfile

#from app.speech.speech_to_text import transcribe_audio
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from speech.speech_to_text import transcribe_audio


def app():

    st.title("🎤 Speech-to-Text")

    st.markdown("""
    Upload audio file for transcription.
    Supported:
    - WAV
    - MP3
    - M4A
    """)

    uploaded_file = st.file_uploader(
        "Upload Audio",
        type=["wav", "mp3", "m4a"]
    )

    if uploaded_file is not None:

        st.audio(uploaded_file)

        if st.button("Transcribe Audio"):

            with st.spinner("Transcribing..."):

                # Save temp file
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".wav"
                ) as temp_audio:

                    temp_audio.write(uploaded_file.read())

                    temp_path = temp_audio.name

                # Transcribe
                text = transcribe_audio(temp_path)

                st.success("Transcription Complete!")

                st.text_area(
                    "Transcribed Text",
                    text,
                    height=200
                )