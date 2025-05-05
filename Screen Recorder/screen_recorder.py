from tkinter import *
import pyscreenrec
from PIL import Image,ImageTk
import wave
import pyaudio
import threading
import os
#from moviepy.editor import *
rate = 44100
chunk = 1024
channels = 1
format = pyaudio.paInt16
py = pyaudio.PyAudio()
frames = []
is_recording = True
global stream
root = Tk()
root.geometry("500x550+400+50")
root.resizable(0,0)
root.title("Srceen Recorder")
icon = PhotoImage(file='Images/recorder.png')
root.iconphoto(False,icon)
root.config(bg='lightpink')
def thread():
	if start_button['state'] == NORMAL:
		stop_button.config(state='normal')
		start_button.config(state='disable')
		threading.Thread(target=start).start()
	else:
		start_button.config(state='normal')
		stop_button.config(state='disable')
		stop()
def start():
	global recording
	global stream	
	start_button.config(state='disable')
	pause_button.config(state='normal')
	resume_button.config(state='normal')
	stop_button.config(state='normal')
	filename = "Recordings/video"
	rec.start_recording(str(filename+".mp4"),2)
	stream = py.open(rate=rate,frames_per_buffer=chunk,channels=channels,format=format,input=True)
	try:
		del frames[0:]
		while is_recording == True:
			data = stream.read(chunk)
			frames.append(data)
	except:
		pass
def pause():
	rec.pause_recording()
def resume():
	rec.resume_recording()
def stop():
	start_button.config(state='normal')
	pause_button.config(state='disable')
	resume_button.config(state='disable')
	stop_button.config(state='disable')
	if(os.path.exists("Recordings/audio.wav")):
		os.remove("Recordings/audio.wav")
	rec.stop_recording()
	is_recording = False
	filename = 'Recordings/audio.wav'
	sound_file = wave.open(filename,'wb')
	sound_file.setnchannels(1)
	sound_file.setframerate(44100)
	sound_file.setsampwidth(py.get_sample_size(pyaudio.paInt16))
	sound_file.writeframes(b''.join(frames))
	sound_file.close()
	#video = VideoFileClip("Recordings/video.mp4")
	#audio = AudioFileClip("Recordings/audio.wav")
	#final = video.set_audio(audio)
	#final.write_videofile("Recordings/video.mp4")
	#os.remove("Recordings/audio.wav")
	
rec = pyscreenrec.ScreenRecorder()
recorder_image = Image.open('Images/recorder1.png')
image = ImageTk.PhotoImage(recorder_image)
Label(root,text='Srceen Recorder',font='verdena 15 bold',bg='lightpink',fg='white').place(x=180,y=40)
Label(root,image=image).place(x=150,y=100)
start_image = Image.open('Images/start.png')
start_image = start_image.resize((100,100))
image1 = ImageTk.PhotoImage(start_image)
start_button = Button(root,image=image1,borderwidth=0,cursor='hand2',command=thread)
start_button.place(x=200,y=300)
pause_image = Image.open('Images/pause.png')
pause_image = pause_image.resize((50,50))
image2 = ImageTk.PhotoImage(pause_image)
pause_button = Button(root,image=image2,borderwidth=0,cursor='hand2',command=pause,state='disable')
pause_button.place(x=50,y=430)
Label(root,text='Pause',font='verdena 12',fg='white',bg='lightpink').place(x=50,y=490)
resume_image = Image.open('Images/resume.png')
resume_image = resume_image.resize((50,50))
image3 = ImageTk.PhotoImage(resume_image)
resume_button = Button(root,image=image3,borderwidth=0,cursor='hand2',command=resume,state='disable')
resume_button.place(x=230,y=430)
Label(root,text='Resume',font='verdena 12',fg='white',bg='lightpink').place(x=220,y=490)
Stop_image = Image.open('Images/Stop.png')
Stop_image = Stop_image.resize((50,50))
image4 = ImageTk.PhotoImage(Stop_image)
stop_button = Button(root,image=image4,borderwidth=0,cursor='hand2',command=stop,state='disable')
stop_button.place(x=400,y=430)
Label(root,text='Stop',font='verdena 12',fg='white',bg='lightpink').place(x=405,y=490)
root.mainloop()
