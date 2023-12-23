```python
import cv2
import os

# Define categories of recyclable materials
categories = ['paper', 'plastic', 'metal', 'glass']

# Create directories for each category if not exist
for category in categories:
    os.makedirs('data/{}'.format(category), exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Wait for user input to save the frame or quit
    key = cv2.waitKey(1)

    if key == ord('q'):
        # Quit if 'q' is pressed
        break
    elif key in [ord(c) for c in categories]:
        # Save the frame to the corresponding category directory if a category key is pressed
        category = chr(key)
        count = len(os.listdir('data/{}'.format(category)))  # Count existing files to avoid overwrite
        cv2.imwrite('data/{}/{}.jpg'.format(category, count), frame)

# When everything done, release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()
```
