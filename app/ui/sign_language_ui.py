import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av
import cv2
import mediapipe as mp
import numpy as np
import joblib
import time

# Load trained model
model = joblib.load("models/asl_model.pkl")

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


class SignLanguageProcessor(VideoProcessorBase):

    def __init__(self):

        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.sentence = ""
        self.last_prediction = ""
        self.last_added_time = time.time()

        self.cooldown = 2

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        # Flip image
        img = cv2.flip(img, 1)

        # Convert to RGB
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process hands
        results = self.hands.process(rgb)

        predicted_letter = ""

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                landmark_list = []

                # Extract landmarks
                for lm in hand_landmarks.landmark:
                    landmark_list.extend([lm.x, lm.y, lm.z])

                if len(landmark_list) == 63:

                    features = np.array(landmark_list).reshape(1, -1)

                    prediction = model.predict(features)

                    predicted_letter = prediction[0]

                    current_time = time.time()

                    # Cooldown logic
                    if (
                        predicted_letter != self.last_prediction
                        or current_time - self.last_added_time > self.cooldown
                    ):

                        self.sentence += predicted_letter

                        self.last_prediction = predicted_letter
                        self.last_added_time = current_time

                    # Prediction text
                    cv2.putText(
                        img,
                        f"Prediction: {predicted_letter}",
                        (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )

                # Draw landmarks
                mp_draw.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        # Display sentence
        cv2.putText(
            img,
            f"Sentence: {self.sentence}",
            (10, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 0, 0),
            2
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


def app():

    st.title("🤟 Live Sign Language Detection")

    st.markdown("""
    ### Controls
    - Show hand signs to webcam
    - AI predicts ASL letters
    - Sentence builds automatically
    """)

    webrtc_streamer(
        key="sign-language",
        video_processor_factory=SignLanguageProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        },
        async_processing=True
    )