import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard

actions = np.array([
    "hello",
    "thanks",
    "yes",
    "no",
    "iloveyou"
])

label_map = {
    label: num
    for num, label in enumerate(actions)
}

DATA_PATH = "sequence_data"

sequences = []
labels = []

# Load sequences
for action in actions:

    for sequence in range(30):

        window = []

        for frame_num in range(30):

            npy_path = os.path.join(
                DATA_PATH,
                action,
                str(sequence),
                f"{frame_num}.npy"
            )

            res = np.load(npy_path)

            window.append(res)

        sequences.append(window)

        labels.append(label_map[action])
        
X = np.array(sequences)

y = to_categorical(labels).astype(int)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.05
)

log_dir = os.path.join("Logs")

tb_callback = TensorBoard(
    log_dir=log_dir
)

model = Sequential()

model.add(
    LSTM(
        64,
        return_sequences=True,
        activation='relu',
        input_shape=(30, 63)
    )
)

model.add(
    LSTM(
        128,
        return_sequences=True,
        activation='relu'
    )
)

model.add(
    LSTM(
        64,
        return_sequences=False,
        activation='relu'
    )
)

model.add(Dense(64, activation='relu'))

model.add(Dense(32, activation='relu'))

model.add(Dense(actions.shape[0], activation='softmax'))

model.compile(
    optimizer='Adam',
    loss='categorical_crossentropy',
    metrics=['categorical_accuracy']
)

model.fit(
    X_train,
    y_train,
    epochs=200,
    callbacks=[tb_callback]
)

model.save("models/lstm_sign_model.h5")