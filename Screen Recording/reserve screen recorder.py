from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyscreenrec
import wave
import pyaudio
import moviepy.editor
import threading
from pygame import mixer
import cv2
from PIL import Image,ImageTk
import os
import shutil
import ffmpeg as fm
import time
import moviepy.editor as mp

mixer.init()

root = Tk()
root.title("Syscam Screen Recorder")
root.iconphoto(False,PhotoImage(file="images/icon.png"))
root.config(bg="#454545")
root.geometry("1370x700+0+0")
root.resizable(0,0)

heading = Frame(root,width=1370,height=50,bg='darkorange')
heading.pack(fill=X)

Label(heading,text='System Camera Screen Recorder',font='verdena 15 bold',bg='darkorange',fg='white').pack()


video_files_frame = Frame(root,width=500,height=500,bg='#52595d')
video_files_frame.place(x=0,y=60)

scroll = Scrollbar(video_files_frame)

video_files = Listbox(video_files_frame,width=80,height=30,bg='#52595d',fg='white',border=0,selectbackground='steelblue',cursor='hand2',yscrollcommand=scroll.set)
scroll.config(command=video_files.yview)
scroll.pack(side='right',fill='y')
video_files.pack()


files_data = "Recordings/"
file_data = os.listdir(files_data)
n = 0
for data in file_data:
	if data.split(".")[-1] == "mp4":
		video_files.insert(0,data)
		video_files.insert(0,"\n\n")
		n+=1
Label(root,text=f'Total Recordings: {n}',width=40,bg='#52595d',fg='white',font='verdena 12 bold').place(x=10,y=550)

video_player_frame = Frame(root,width=870,height=480,bg='#52595d')
video_player_frame.place(x=500,y=60)
video_player_name = Label(root,text='',font='verdena 12 bold',width=870,height=1,bg='blue',fg='white')
video_player_name.pack(fill='x')

is_recording = True
def play_video():
	global video_player_label
	data = video_files.get(ACTIVE)
	#messagebox.showinfo("Info",data)

	if(not os.path.exists("Recordings/"+data[0:-4]+".mp3")):
		video = mp.VideoFileClip("Recordings/"+data)
		video.audio.write_audiofile("Recordings/"+data[0:-4]+".mp3")

		mixer.music.load("Recordings/"+data[0:-4]+".mp3")
		mixer.music.play()

	else:
		mixer.music.load("Recordings/"+data[0:-4]+".mp3")
		mixer.music.play()

	def thread():
		threading.Thread(target=video_cap).start()
		video_play.config(state='disable')
		video_pause.config(state='normal')
		video_stop.config(state='normal')

	def thread1():
		threading.Thread(target=resume_video).start()

	video_player_name.config(text=data[0:-4])
	#messagebox.showinfo("Info",data[6:])
	capture = cv2.VideoCapture("Recordings/"+data)
	def video_cap():
		try:
			while is_recording == True:
				global stop_video
				global frame
				global ret
				ret,frame = capture.read()
				if ret:
					#cv2.imshow("Image",frame)
					#cv2.waitKey(1)
					frame = cv2.resize(frame,(870,480))					
					data = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
					data = Image.fromarray(data)
					#player_image = data.resize((870,480))
					player_image = ImageTk.PhotoImage(image=data)
					time.sleep(0.005)
					video_player_label.config(image=player_image)
					video_player_label.image = player_image
					#video_player_frame.after(1,video_cap)
		except Exception as e:
			messagebox.showerror('Error',e)
			pass

	video_player_label = Label(video_player_frame,bg='#52595d',width=870,height=480)
	video_player_label.place(x=0,y=0)

	def pause_video():
		global video_player_label
		global frame
		global is_recording
		is_recording = False
		video_player_label1 = Label(video_player_frame,bg='#52595d',width=870,height=480,compound='left')
		video_player_label1.place(x=0,y=0)
		try:
			data = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
			data = Image.fromarray(data)
			player_image = data.resize((870,480))
			player_image = ImageTk.PhotoImage(image=player_image)
			video_player_label1.config(image=player_image)
			video_player_label1.image = player_image
			mixer.music.pause()
			video_resume.config(state='normal')
			video_pause.config(state='disable')
		except:
			root.destroy()
	def resume_video():
		global video_player_label
		global is_recording
		is_recording = True
		thread()
		video_player_label = Label(video_player_frame,bg='#52595d',width=870,height=480,compound='left')
		video_player_label.place(x=0,y=0)
		video_pause.config(state='normal')
		video_resume.config(state='disable')
		mixer.music.unpause()


	def stop_video():
		video_player_frame.destroy()
		video_player_label.destroy()
		video_play.config(state='normal')
		video_pause.config(state='disable')
		video_resume.config(state='disable')
		video_stop.config(state='disable')
		mixer.music.stop()
		create_frame()

	def create_frame():
		global video_player_frame
		video_player_frame = Frame(root,width=870,height=480,bg='#52595d')
		video_player_frame.place(x=500,y=60)
		video_play.config(state='normal')

		video_player_label = Label(video_player_frame,bg='#52595d',width=870,height=480,compound='left')
		video_player_label.place(x=0,y=0)

	video_pause = Button(root,image=pause_video_button_image,font='verdena 12',fg='white',cursor='hand2',state='disable',border=0,command=pause_video)
	video_pause.place(x=600,y=545)


	video_resume = Button(root,image=resume_video_button_image,font='verdena 12',fg='white',cursor='hand2',state='disable',border=0,command=resume_video)
	video_resume.place(x=700,y=545)


	video_stop = Button(root,image=stop_video_button_image,font='verdena 12',fg='white',cursor='hand2',state='disable',border=0,command=stop_video)
	video_stop.place(x=800,y=545)

	thread()

play_video_button_image = Image.open("images/play-button.png")
play_video_button_image = play_video_button_image.resize((50,50))
play_video_button_image = ImageTk.PhotoImage(image=play_video_button_image)

video_play = Button(root,image=play_video_button_image,font='verdena 12',bg='#454545',fg='white',activebackground='#454545',cursor='hand2',border=0,command=play_video)
video_play.place(x=500,y=545)

pause_video_button_image = Image.open("images/pause-button.png")
pause_video_button_image = pause_video_button_image.resize((50,50))
pause_video_button_image = ImageTk.PhotoImage(image=pause_video_button_image)

video_pause = Button(root,image=pause_video_button_image,font='verdena 12',fg='white',cursor='hand2',state='disable',border=0)
video_pause.place(x=600,y=545)

resume_video_button_image = Image.open("images/resume-button.png")
resume_video_button_image = resume_video_button_image.resize((50,50))
resume_video_button_image = ImageTk.PhotoImage(image=resume_video_button_image)

video_resume = Button(root,image=resume_video_button_image,font='verdena 12',fg='white',cursor='hand2',state='disable',border=0)
video_resume.place(x=700,y=545)

stop_video_button_image = Image.open("images/stop-button.png")
stop_video_button_image = stop_video_button_image.resize((50,50))
stop_video_button_image = ImageTk.PhotoImage(image=stop_video_button_image)

video_stop = Button(root,image=stop_video_button_image,font='verdena 12',fg='white',cursor='hand2',state='disable',border=0)
video_stop.place(x=800,y=545)


def face_cam():
	win = Toplevel(root)
	win.iconphoto(False,PhotoImage(file='images/icon.png'))
	win.geometry("250x200+900+100")
	win.resizable(0,0)
	capture = cv2.VideoCapture(0)
	def video_cap():
		ret,frame = capture.read()
		if ret:
			#cv2.imshow('Image',frame)
			frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
			frame = Image.fromarray(frame)
			image = ImageTk.PhotoImage(image=frame)
			label.config(image=image)
			label.image = image
			win.after(10,video_cap)

	label = Label(win,width=870,height=32)
	label.pack(fill='both',expand=1)
	video_cap()


control_frame = Frame(root,width=1370,height=100,bg='#454545')
control_frame.place(x=0,y=600)

def start_rec():
	pass

def pause_rec():
	pass

def resume_rec():
	pass

def stop_rec():
	pass

start_button_image = Image.open("images/start.png")
start_button_image = start_button_image.resize((50,50))
start_button_image = ImageTk.PhotoImage(image=start_button_image)

start_button = Button(control_frame,image=start_button_image,bg='#454545',cursor='hand2',border=0,activebackground='#454545',command=start_rec)
start_button.place(x=20,y=10)

pause_button_image = Image.open("images/pause.png")
pause_button_image = pause_button_image.resize((50,50))
pause_button_image = ImageTk.PhotoImage(image=pause_button_image)

pause_button = Button(control_frame,image=pause_button_image,bg='#454545',cursor='hand2',border=0,activebackground='#454545',command=pause_rec)
pause_button.place(x=120,y=10)

resume_button_image = Image.open("images/play.png")
resume_button_image = resume_button_image.resize((50,50))
resume_button_image = ImageTk.PhotoImage(image=resume_button_image)

resume_button = Button(control_frame,image=resume_button_image,bg='#454545',cursor='hand2',border=0,activebackground='#454545',command=resume_rec)
resume_button.place(x=220,y=10)

stop_button_image = Image.open("images/stop.png")
stop_button_image = stop_button_image.resize((50,50))
stop_button_image = ImageTk.PhotoImage(image=stop_button_image)

stop_button = Button(control_frame,image=stop_button_image,bg='#454545',cursor='hand2',border=0,activebackground='#454545',command=stop_rec)
stop_button.place(x=320,y=10)

root.mainloop()