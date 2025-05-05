from moviepy.editor import VideoFileClip, AudioFileClip

# Load the video and audio clips
video_clip = VideoFileClip("test.mp4")
audio_clip = AudioFileClip("test.mp3")

# Set the audio of the video clip to the loaded audio clip
video_clip = video_clip.set_audio(audio_clip)

# Write the merged video to a file
video_clip.write_videofile("output_video.mp4")

# Close the video and audio clips
video_clip.close()
audio_clip.close()
