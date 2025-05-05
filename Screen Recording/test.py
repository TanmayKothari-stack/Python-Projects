import os
import shutil
import moviepy.editor as mp

path = "Recordings/crackpot.mp4"
video = mp.VideoFileClip(path)
if(os.path.exists(path)):
	video.audio.write_audiofile(path[0:-4]+".mp3")