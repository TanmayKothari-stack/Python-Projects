import pyaudio
import wave
import threading
from tkinter import *

root = Tk()
root.title("Voice Recorder")
root.resizable(0,0)
def thread():
	threading.Thread(target=start).start()


def start():
	global stream
	global audio
	global frames
	audio = pyaudio.PyAudio()
	stream = audio.open(frames_per_buffer=1024,rate=44100,channels=1,format=pyaudio.paInt16,input=True)
	frames = []
	while True:
		data = stream.read(1024)
		frames.append(data)

def stop():
	stream.stop_stream()
	stream.close()
	audio.terminate()

	sound_file = wave.open('Recordings/audio.wav','wb')
	sound_file.setnchannels(1)
	sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
	sound_file.setframerate(44100)
	sound_file.writeframes(b''.join(frames))
	sound_file.close()

Button(root,text='Start',command=thread).place(x=100,y=10)
Button(root,text='Stop',command=stop).place(x=100,y=100)


root.mainloop()