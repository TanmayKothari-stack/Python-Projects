import cv2
import tkinter as tk
from PIL import Image, ImageTk

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(image=frame)
        label.config(image=frame)
        label.image = frame
    window.after(1, update_frame)

# Create Tkinter window
window = tk.Tk()
window.resizable(0,0)
window.title("Live Video")

# Create a label widget to display the video
label = tk.Label(window)
label.pack()

# Create a VideoCapture object to capture frames from the webcam
cap = cv2.VideoCapture(0)

# Start updating the frame
update_frame()

# Run the Tkinter event loop
window.mainloop()

# Release the VideoCapture object
cap.release()
