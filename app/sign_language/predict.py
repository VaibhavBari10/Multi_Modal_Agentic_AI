"""import cv2
import mediapipe as mp
import numpy as np
import joblib

print("Loading trained model...")

# Load trained model
model = joblib.load("models/asl_model.pkl")

print("Model loaded successfully!")

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open webcam
cap = cv2.VideoCapture(0)

# For Windows webcam issues
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("\n=================================")
print("Starting webcam...")
print("Press 'Q' to quit")
print("=================================")

while True:

    success, frame = cap.read()

    if not success:
        print("Failed to read webcam.")
        break

    # Flip frame horizontally
    frame = cv2.flip(frame, 1)

    # Convert BGR → RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand detection
    results = hands.process(rgb_frame)

    predicted_letter = ""

    # If hand detected
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            landmark_list = []

            # Extract x,y,z coordinates
            for lm in hand_landmarks.landmark:
                landmark_list.extend([lm.x, lm.y, lm.z])

            # Ensure correct feature size
            if len(landmark_list) == 63:

                # Convert to numpy array
                features = np.array(landmark_list).reshape(1, -1)

                # Predict gesture
                prediction = model.predict(features)

                predicted_letter = prediction[0]

                # Draw prediction text
                cv2.putText(
                    frame,
                    f"Prediction: {predicted_letter}",
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Show frame
    cv2.imshow("ASL Sign Language Prediction", frame)

    # Quit key
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
cap.release()

# Close windows
cv2.destroyAllWindows()"""


"""import cv2
import mediapipe as mp
import numpy as np
import joblib
import time

print("Loading trained model...")

# Load trained model
model = joblib.load("models/asl_model.pkl")

print("Model loaded successfully!")

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Webcam
cap = cv2.VideoCapture(0)

# Sentence variables
sentence = ""
last_prediction = ""
last_added_time = time.time()

# Cooldown time in seconds
cooldown = 2

print("\n=================================")
print("Press:")
print("Q → Quit")
print("C → Clear Sentence")
print("=================================")

while True:

    success, frame = cap.read()

    if not success:
        print("Webcam error!")
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands
    results = hands.process(rgb_frame)

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

                # Add prediction every cooldown seconds
                current_time = time.time()

                if (
                    predicted_letter != last_prediction
                    or current_time - last_added_time > cooldown
                ):

                    sentence += predicted_letter

                    last_prediction = predicted_letter
                    last_added_time = current_time

                # Draw prediction
                cv2.putText(
                    frame,
                    f"Prediction: {predicted_letter}",
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Display sentence
    cv2.putText(
        frame,
        f"Sentence: {sentence}",
        (10, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # Instructions
    cv2.putText(
        frame,
        "Press C to clear",
        (10, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    cv2.imshow("ASL Sentence Builder", frame)

    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord("q"):
        break

    # Clear sentence
    elif key == ord("c"):
        sentence = ""
        print("Sentence cleared!")

# Cleanup
cap.release()
cv2.destroyAllWindows()"""

import cv2
import mediapipe as mp
import numpy as np
import joblib
import time

from app.tts.text_to_speech import speak

print("Loading trained model...")

# Load trained model
model = joblib.load("models/asl_model.pkl")

print("Model loaded successfully!")

# Initialize MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open webcam
cap = cv2.VideoCapture(0)

# Sentence variables
sentence = ""
last_prediction = ""
last_added_time = time.time()

# Cooldown time
cooldown = 2

print("\n=================================")
print("Controls:")
print("Q → Quit")
print("C → Clear Sentence")
print("S → Speak Sentence")
print("=================================")

while True:

    success, frame = cap.read()

    if not success:
        print("Webcam error!")
        break

    # Flip frame
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame
    results = hands.process(rgb_frame)

    predicted_letter = ""

    # If hand detected
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            landmark_list = []

            # Extract landmarks
            for lm in hand_landmarks.landmark:
                landmark_list.extend([lm.x, lm.y, lm.z])

            # Predict if valid landmarks
            if len(landmark_list) == 63:

                features = np.array(landmark_list).reshape(1, -1)

                prediction = model.predict(features)

                predicted_letter = prediction[0]

                current_time = time.time()

                # Cooldown logic
                if (
                    predicted_letter != last_prediction
                    or current_time - last_added_time > cooldown
                ):

                    sentence += predicted_letter

                    last_prediction = predicted_letter
                    last_added_time = current_time

                # Display prediction
                cv2.putText(
                    frame,
                    f"Prediction: {predicted_letter}",
                    (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # Display sentence
    cv2.putText(
        frame,
        f"Sentence: {sentence}",
        (10, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # Instructions
    cv2.putText(
        frame,
        "Q=Quit | C=Clear | S=Speak",
        (10, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )

    # Show frame
    cv2.imshow("ASL Sign Language To Speech", frame)

    # Keyboard controls
    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord("q"):
        break

    # Clear sentence
    elif key == ord("c"):
        sentence = ""
        print("Sentence cleared!")

    # Speak sentence
    elif key == ord("s"):

        if sentence.strip() != "":

            print(f"Speaking: {sentence}")

            speak(sentence)

# Cleanup
cap.release()
cv2.destroyAllWindows()