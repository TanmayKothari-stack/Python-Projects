from moviepy.editor import VideoFileClip, AudioFileClip
import os
video = VideoFileClip('Recordings/video.mp4')
audio = AudioFileClip('Recordings/audio.wav')
final = video.set_audio(audio)
final.write_videofile('Recordings/video.mp4')
#os.remove('Recordings/recording.mp4')
#os.remove('Recordings/audio.wav')