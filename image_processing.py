```python
import cv2
import os
import numpy as np

# Define categories of recyclable materials
categories = ['paper', 'plastic', 'metal', 'glass']

# Define standard size to resize images to
standard_size = (100, 100)

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

def process_all_images():
    # Process all images in each category
    for category in categories:
        print("Processing images in category: ", category)
        category_dir = 'data/{}'.format(category)
        image_files = os.listdir(category_dir)

        processed_images = []
        for image_file in image_files:
            image_path = os.path.join(category_dir, image_file)
            processed_image = process_image(image_path)
            processed_images.append(processed_image)

        # Save processed images as numpy array
        np.save('data/{}_processed.npy'.format(category), np.array(processed_images))

if __name__ == "__main__":
    process_all_images()
```

