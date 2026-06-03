"""import streamlit as st
from sign_dictionary import SIGN_MAP


def animate_sign(text):

    words = text.lower().split()

    for word in words:

        if word in SIGN_MAP:

            st.image(
                SIGN_MAP[word],
                caption=word
            )

        else:

            st.warning(
                f"No sign animation found for: {word}"
            )"""


import streamlit as st
import sys
import os

# =========================
# PATH SETUP
# =========================

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(CURRENT_DIR)

# =========================
# IMPORT SIGN MAP
# =========================

from sign_dictionary import SIGN_MAP


def animate_sign(text):

    # Convert text to lowercase
    words = text.lower().split()

    # Check empty input
    if len(words) == 0:

        st.warning("Please enter some text.")

        return

    # Show animations
    for word in words:

        if word in SIGN_MAP:

            st.subheader(f"🤟 {word}")

            sign_path = SIGN_MAP[word]

            # Check file exists
            if os.path.exists(sign_path):

                # GIF support
                if sign_path.endswith(".gif"):

                    st.image(
                        sign_path,
                        caption=word,
                        use_container_width=True
                    )

                # MP4 support
                elif sign_path.endswith(".mp4"):

                    video_file = open(sign_path, "rb")

                    video_bytes = video_file.read()

                    st.video(video_bytes)

                else:

                    st.error(
                        f"Unsupported file format for {word}"
                    )

            else:

                st.error(
                    f"File not found: {sign_path}"
                )

        else:

            st.warning(
                f"No sign animation found for: {word}"
            )