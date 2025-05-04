import socket
import cv2
import numpy as np
import os

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host,port))

capture = cv2.VideoCapture(0)
ret,frame = capture.read()
cv2.imwrite(f"images/image.jpg",frame)

file = open("images/image.jpg","rb")
data = file.read()
s.sendall(data)
s.send("done").encode()
print(data)
file.close()

"""import cv2
import os
"""
"""folder = os.listdir("images")"""
"""if(os.path.exists("images/1.jpg")):
	for files in folder:
			os.remove(f"images/{files}")
"""
"""capture = cv2.VideoCapture(0)
n = 1
try:
	while True:
		
		ret,frame = capture.read()
		cv2.imwrite(f"images/{n}.jpg",frame)
		#os.remove(f"images/{n}.jpg")
		n+=1
		if cv2.waitKey(1) == ord("q"):
			break
except KeyboardInterrupt:
	folder = os.listdir("images")

	for files in folder:
			os.remove(f"images/{files}")
"""