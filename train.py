```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# Define categories of recyclable materials
categories = ['paper', 'plastic', 'metal', 'glass']

# Load processed images and labels
def load_data():
    images = []
    labels = []
    for i, category in enumerate(categories):
        category_images = np.load('data/{}_processed.npy'.format(category))
        images.append(category_images)
        labels.append(np.full(category_images.shape[0], i))  # Assign a label to each image based on its category

    # Concatenate all data
    images = np.concatenate(images)
    labels = np.concatenate(labels)

    return images, labels

# Define the model
def create_model():
    model = Sequential([
        Flatten(input_shape=(100, 100)),  # Input layer
        Dense(128, activation='relu'),  # Hidden layer
        Dense(len(categories), activation='softmax')  # Output layer
    ])

    model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    return model

# Train the model
def train_model(model, images, labels):
    # Split data into training and validation sets
    train_images, val_images, train_labels, val_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

    # Train the model
    model.fit(train_images, train_labels, validation_data=(val_images, val_labels), epochs=10)

    # Save the trained model
    model.save('model.h5')

if __name__ == "__main__":
    images, labels = load_data()
    model = create_model()
    train_model(model, images, labels)
```
