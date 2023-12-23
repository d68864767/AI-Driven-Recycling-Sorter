```python
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Define categories of recyclable materials
categories = ['paper', 'plastic', 'metal', 'glass']

# Define standard size to resize images to
standard_size = (100, 100)

# Load the trained model
model = load_model('model.h5')

def process_image(image_path):
    # Load image
    img = cv2.imread(image_path)

    # Resize image to standard size
    img = cv2.resize(img, standard_size)

    # Convert image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Normalize pixel values to [0, 1] range
    img = img / 255.0

    return img

def predict_category(image_path):
    # Process image
    img = process_image(image_path)

    # Add an extra dimension for batch size
    img = np.expand_dims(img, axis=0)

    # Predict category
    prediction = model.predict(img)
    predicted_category = categories[np.argmax(prediction)]

    return predicted_category

if __name__ == "__main__":
    # Test the model on a new image
    image_path = 'test.jpg'  # Replace with your image path
    predicted_category = predict_category(image_path)
    print("Predicted category: ", predicted_category)
```

