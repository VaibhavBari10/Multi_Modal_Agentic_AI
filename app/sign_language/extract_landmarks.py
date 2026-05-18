import cv2
import mediapipe as mp
import os
import pandas as pd
from tqdm import tqdm

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)

# IMPORTANT:
# Your real dataset path
DATASET_PATH = r"datasets/asl_dataset/asl_alphabet_train/asl_alphabet_train"

data = []
labels = []

print("Starting landmark extraction...")

# Loop through all label folders
for label in os.listdir(DATASET_PATH):

    label_path = os.path.join(DATASET_PATH, label)

    # Skip non-folder files
    if not os.path.isdir(label_path):
        continue

    print(f"\nProcessing class: {label}")

    # Loop through images
    for image_name in tqdm(os.listdir(label_path)):

        image_path = os.path.join(label_path, image_name)

        # Read image
        image = cv2.imread(image_path)

        if image is None:
            continue

        # Convert to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Process hand landmarks
        results = hands.process(image_rgb)

        # If hand detected
        if results.multi_hand_landmarks:

            hand_landmarks = results.multi_hand_landmarks[0]

            landmark_list = []

            # Extract x,y,z
            for lm in hand_landmarks.landmark:
                landmark_list.extend([lm.x, lm.y, lm.z])

            # 21 landmarks × 3 = 63 features
            if len(landmark_list) == 63:
                data.append(landmark_list)
                labels.append(label)

# Create DataFrame
df = pd.DataFrame(data)

# Add labels
df["label"] = labels

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Save CSV
csv_path = "models/asl_landmarks.csv"

df.to_csv(csv_path, index=False)

print("\n=================================")
print("Landmark extraction completed!")
print(f"Dataset saved at: {csv_path}")
print(f"Total samples: {len(df)}")
print("=================================")