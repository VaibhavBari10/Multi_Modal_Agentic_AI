import cv2
import os
import numpy as np
import mediapipe as mp

# Actions
actions = [
    "hello",
    "thanks",
    "yes",
    "no",
    "iloveyou"
]

# Number of videos per action
no_sequences = 30

# Frames per sequence
sequence_length = 30

# Data path
DATA_PATH = "sequence_data"

# MediaPipe
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Create folders
for action in actions:

    for sequence in range(no_sequences):

        os.makedirs(
            os.path.join(DATA_PATH, action, str(sequence)),
            exist_ok=True
        )

# Webcam
cap = cv2.VideoCapture(0)

for action in actions:

    for sequence in range(no_sequences):

        for frame_num in range(sequence_length):

            success, frame = cap.read()

            frame = cv2.flip(frame, 1)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(rgb)

            # Draw landmarks
            if results.multi_hand_landmarks:

                for hand_landmarks in results.multi_hand_landmarks:

                    mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS
                    )

                    landmarks = []

                    for lm in hand_landmarks.landmark:

                        landmarks.extend([
                            lm.x,
                            lm.y,
                            lm.z
                        ])

                    # Save frame landmarks
                    npy_path = os.path.join(
                        DATA_PATH,
                        action,
                        str(sequence),
                        str(frame_num)
                    )

                    np.save(npy_path, landmarks)

            # Display info
            cv2.putText(
                frame,
                f'Collecting: {action}',
                (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f'Sequence: {sequence}',
                (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

            cv2.imshow(
                'Sequence Collection',
                frame
            )

            # Wait before recording
            if frame_num == 0:

                cv2.putText(
                    frame,
                    'STARTING...',
                    (120, 200),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    4
                )

                cv2.imshow(
                    'Sequence Collection',
                    frame
                )

                cv2.waitKey(1000)

            if cv2.waitKey(10) & 0xFF == ord('q'):

                break

cap.release()
cv2.destroyAllWindows()