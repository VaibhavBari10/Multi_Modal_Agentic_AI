import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

print("Loading dataset...")

# Load CSV dataset
df = pd.read_csv("models/asl_landmarks.csv")

print("Dataset loaded successfully!")
print(f"Dataset shape: {df.shape}")

# Features
X = df.drop("label", axis=1)

# Labels
y = df["label"]

print("\nSplitting dataset...")

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

print("\nCreating RandomForest model...")

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

print("\nTraining started...")

# Train model
model.fit(X_train, y_train)

print("Training completed!")

print("\nMaking predictions...")

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n=================================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("=================================")

# Classification report
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Save model
model_path = "models/asl_model.pkl"

joblib.dump(model, model_path)

print("\n=================================")
print(f"Model saved successfully!")
print(f"Saved at: {model_path}")
print("=================================")