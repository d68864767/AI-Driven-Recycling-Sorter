```python
import tkinter as tk
from PIL import Image, ImageTk
from hardware_integration import cap, predicted_category

# Create a new tkinter window
window = tk.Tk()
window.title("AI-Driven Recycling Sorter")

# Create a canvas to display the captured frame
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Function to update the canvas and the label
def update_image():
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to a PIL image
    image = Image.fromarray(frame)
    image = ImageTk.PhotoImage(image)

    # Update the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    canvas.image = image

    # Update the label
    label.config(text="Predicted Category: " + predicted_category)

    # Call this function again after 100ms (for the next frame)
    window.after(100, update_image)

# Create a label to display the predicted category
label = tk.Label(window, text="Predicted Category: ")
label.pack()

# Call the update function once to start the frame updates
update_image()

# Start the tkinter main loop
window.mainloop()
```

