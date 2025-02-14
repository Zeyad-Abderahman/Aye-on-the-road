import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

# Load the trained model
model_path = r"E:\AYE on the road\machine_project.keras"
print(f"Loading model from: {model_path}")
model = load_model(model_path)
print("Model loaded successfully!")

# Prediction function
def predict_frame(frame):
    # Resize to model's input size while preserving aspect ratio
    height, width, _ = frame.shape
    target_size = 100  # Match the size your model was trained on
    scale = target_size / max(height, width)
    new_height, new_width = int(height * scale), int(width * scale)
    resized_frame = cv2.resize(frame, (new_width, new_height))
    
    # Center crop or pad to exact size
    padded_frame = np.zeros((target_size, target_size, 3), dtype=np.uint8)
    pad_h = (target_size - new_height) // 2
    pad_w = (target_size - new_width) // 2
    padded_frame[pad_h:pad_h + new_height, pad_w:pad_w + new_width] = resized_frame

    # Normalize and expand dimensions
    img_array = img_to_array(padded_frame) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction
    prediction = model.predict(img_array)
    return "Closed Eyes" if prediction[0][0] < 0.5 else "Open Eyes"

# GUI and webcam logic
class LivePredictionApp:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source

        # Open the video source
        self.vid = cv2.VideoCapture(self.video_source)

        # Create a canvas for video feed
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH),
                                height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

        # Label for prediction results
        self.prediction_label = Label(window, text="Prediction: ", font=("Arial", 16))
        self.prediction_label.pack()

        # Button to close the app
        self.btn_quit = tk.Button(window, text="Quit", command=self.window.quit)
        self.btn_quit.pack()

        # Start video capture and update loop
        self.update()

    def update(self):
        # Capture frame-by-frame
        ret, frame = self.vid.read()
        if ret:
            # Convert the frame to RGB (Tkinter uses RGB images)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Make prediction
            prediction = predict_frame(frame_rgb)
            self.prediction_label.config(text=f"Prediction: {prediction}")

            # Display the frame
            frame_image = Image.fromarray(frame_rgb)
            frame_tk = ImageTk.PhotoImage(image=frame_image)
            self.canvas.create_image(0, 0, image=frame_tk, anchor=tk.NW)
            self.window.image = frame_tk  # Prevent garbage collection

        # Call this method again after 10ms
        self.window.after(10, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = LivePredictionApp(root, "Live Webcam Eye Detection")
    root.mainloop()
