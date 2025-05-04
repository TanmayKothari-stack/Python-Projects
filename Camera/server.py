import socket
import cv2
import numpy as np

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
s.listen(1)
client,addr = s.accept()
print(addr, "Connteced")
file = open("images/image1.jpg","wb")
file_bytes = b""
done = False
data = client.recv(1024)
print(data)
while not done:
	if data == data.decode:
		done = True
	else:
		file_bytes+=data
file.write(file_bytes)
file.close()
"""import cv2
import os
"""
#frames = []
"""while True:
	folder = os.listdir("images")
	for file in folder:
		image = cv2.imread(f"images/{file}")
		#frames.append(image)

	#for frame in frames:
		if file.split(".")[-1] == "jpg":
			cv2.imshow("image",image)
			#del frame[0:]
			try:
				os.remove(f"images/{file}")
			except:
				pass
			quit = cv2.waitKey(1)
			if quit == ord("q"):
				break

for files in folder:
	os.remove(f"images/{files}")
			
cv2.destroyAllWindows()"""