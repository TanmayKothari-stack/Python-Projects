from tkinter import *
import soundfile as sf
import pyaudio
import threading
import numpy as np

root = Tk()
root.title("Voice Recorder")
root.geometry("100x100")
root.resizable(0,0)
rate = 44100
chunk = 1024
channels = 1
format = pyaudio.paInt16
py = pyaudio.PyAudio()
frames = []
is_recording = True
global stream
def start():
	global stream
	stream = py.open(rate=rate,frames_per_buffer=chunk,channels=channels,format=format,input=True)
	while is_recording == True:
		data = stream.read(chunk)
		frames.append(np.frombuffer(data,dtype=np.int16))
def stop():
	is_recording = False
	stream.stop_stream()
	stream.close()
	py.terminate()

	save()
def save():
	filename = 'Recordings/recording.wav'
	sf.write(filename,np.concatenate(frames),rate)
def thread():
	if start_button['state'] == NORMAL:
		stop_button.config(state='normal')
		start_button.config(state='disable')
		threading.Thread(target=start).start()
	else:
		start_button.config(state='normal')
		stop_button.config(state='disable')
		stop()


start_button = Button(root,text='Start',command=thread)
start_button.place(x=50,y=20)
stop_button = Button(root,text='Save',command=thread,state='disable')
stop_button.place(x=50,y=50)
root.mainloop() 