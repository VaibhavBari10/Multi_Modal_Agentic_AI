import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model

# Load trained model
model = load_model(
    "models/lstm_sign_model.h5"
)

# Actions
actions = np.array([
    "hello",
    "thanks",
    "yes",
    "no",
    "iloveyou"
])

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Variables
sequence = []
sentence = []

threshold = 0.8

predicted_action = ""
confidence = 0.0

# Open webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():

    success, frame = cap.read()

    if not success:
        break

    # Flip image
    frame = cv2.flip(frame, 1)

    # Convert to RGB
    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Process hands
    results = hands.process(rgb)

    # If hand detected
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = []

            # Extract landmarks
            for lm in hand_landmarks.landmark:

                landmarks.extend([
                    lm.x,
                    lm.y,
                    lm.z
                ])

            # Add frame to sequence
            sequence.append(landmarks)

            # Keep only last 30 frames
            sequence = sequence[-30:]

            # Predict when sequence full
            if len(sequence) == 30:

                prediction = model.predict(
                    np.expand_dims(sequence, axis=0),
                    verbose=0
                )[0]

                predicted_action = actions[
                    np.argmax(prediction)
                ]

                confidence = prediction[
                    np.argmax(prediction)
                ]

                # Confidence check
                if confidence > threshold:

                    # Avoid duplicate words
                    if len(sentence) > 0:

                        if predicted_action != sentence[-1]:

                            sentence.append(
                                predicted_action
                            )

                    else:

                        sentence.append(
                            predicted_action
                        )

    # Keep only last 5 words
    sentence = sentence[-5:]

    # Prediction text
    cv2.putText(
        frame,
        f"Prediction: {predicted_action}",
        (10, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Confidence text
    cv2.putText(
        frame,
        f"Confidence: {confidence:.2f}",
        (10, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    # Top rectangle
    cv2.rectangle(
        frame,
        (0, 0),
        (640, 40),
        (245, 117, 16),
        -1
    )

    # Sentence display
    cv2.putText(
        frame,
        ' '.join(sentence),
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    # Show window
    cv2.imshow(
        "Dynamic Sign Language AI",
        frame
    )

    # Quit
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()

cv2.destroyAllWindows()