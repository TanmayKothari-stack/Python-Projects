import cv2
import numpy as np

file = open("image.txt","rb")
frame = file.read()
#print(frame)
frame = np.frombuffer(frame,dtype=np.uint8)
frame = np.reshape(frame,(480,640,3))
cv2.imshow('image',frame)
cv2.waitKey(0)
cv2.destroyAllWindows()