```python
import cv2
from model import create_model, categories
from image_processing import process_image
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('model.h5')

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Process the captured frame
    processed_frame = process_image(frame)

    # Predict the category of the processed frame
    prediction = model.predict(processed_frame.reshape(1, 100, 100))
    predicted_category = categories[np.argmax(prediction)]

    # Display the resulting frame with predicted category
    cv2.putText(frame, predicted_category, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```

