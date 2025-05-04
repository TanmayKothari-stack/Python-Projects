import cv2
import numpy as np

capture = cv2.VideoCapture(0)
ret,frame = capture.read()
frame = frame.tostring()
with open("image.txt","wb") as file:
    file.write(frame)
