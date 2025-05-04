import cv2
import numpy as np
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',database='videocam')
cursor = conn.cursor()
capture = cv2.VideoCapture(0)

def main():
	ret,frame = capture.read()
	reteval,buffer = cv2.imencode(".jpg",frame)
	image_bytes = buffer.tobytes()
	try:
		cursor.execute("delete from video_data ")
		if conn.commit():
			pass
	except:
		pass
	cursor.execute("insert into video_data (video) values(%s) ",(image_bytes.decode('latin1'),))
	if conn.commit():
		pass
	#print(image_bytes)
	cursor.execute("select * from video_data ")
	result = cursor.fetchone()
	res = result[1]#[item[1] for item in result]
	#print(res)
	image_data = res.encode('latin1')
	#print(image_data)
	image = cv2.imdecode(np.frombuffer(image_data,np.uint8),cv2.IMREAD_COLOR)
	height,width, _ = image.shape
	image = image[0:height - int(height*0.2),0:width]
	#print(image)
	cv2.imshow('Image',image)
	cv2.waitKey(1)
	try:
		cursor.execute("delete from video_data ")
		if conn.commit():
			pass
	except:
		pass
while True:
	main()