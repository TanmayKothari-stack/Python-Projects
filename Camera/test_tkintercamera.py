import tkinter
from tkinter import *
from PIL import Image,ImageTk
import cv2
import numpy as np
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',database='videocam')
cursor = conn.cursor()

def main():
	ret,frame = caputre.read()
	if ret:
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
		cursor.execute("select * from video_data ")
		result = cursor.fetchone()
		res = result[1]#[item[1] for item in result]
		#print(res)
		image_data = res.encode('latin1')
		#print(image_data)
		image = cv2.imdecode(np.frombuffer(image_data,np.uint8),cv2.IMREAD_COLOR)
		frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		frame = Image.fromarray(frame)
		image = ImageTk.PhotoImage(image=frame)
		label.config(image=image)
		label.image = image
	root.after(10,main)

root = Tk()
root.title("Video Camera")
root.geometry("500x500+400+50")
root.resizable(0,0)

caputre = cv2.VideoCapture(0)
label = Label(root)
label.pack()
main()
root.mainloop()