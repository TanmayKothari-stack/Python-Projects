import cv2
import pyaudio
import requests
import threading
import numpy as np
import time

# ===== CONFIGURATION =====
IP_ADDRESS = "192.168.27.227"  # Replace with your IP webcam address
PORT = "8080"                 # Default port for IP Webcam

# Video stream URL (common endpoints: /video, /videofeed, /video.mjpeg)
VIDEO_URL = f"http://{IP_ADDRESS}:{PORT}/video"

# Audio stream URL (common endpoints: /audio.wav, /audio.aac, /audio)
AUDIO_URL = f"http://{IP_ADDRESS}:{PORT}/audio.wav"

# Audio configuration (adjust based on your webcam's audio settings)
AUDIO_FORMAT = pyaudio.paInt16  # 16-bit audio
CHANNELS = 1                    # 1 for mono, 2 for stereo
SAMPLE_RATE = 44100             # Common sample rate
CHUNK = 1024                    # Audio chunks to read at a time

# ===== VIDEO STREAM =====
def video_stream():
    cap = cv2.VideoCapture(VIDEO_URL)
    
    if not cap.isOpened():
        print("Error: Could not open video stream")
        return
    
    print("Video stream started")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video stream ended")
            break
            
        cv2.imshow('IP Webcam Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# ===== AUDIO STREAM =====
def audio_stream():
    p = pyaudio.PyAudio()
    
    # Open audio stream
    stream = p.open(format=AUDIO_FORMAT,
                    channels=CHANNELS,
                    rate=SAMPLE_RATE,
                    output=True)
    
    print("Audio stream started")
    try:
        with requests.get(AUDIO_URL, stream=True) as r:
            for chunk in r.iter_content(chunk_size=CHUNK):
                stream.write(chunk)
    except Exception as e:
        print(f"Audio stream error: {e}")
    finally:
        print("Audio stream ended")
        stream.stop_stream()
        stream.close()
        p.terminate()

# ===== MAIN =====
if __name__ == "__main__":
    # Start video and audio in separate threads
    video_thread = threading.Thread(target=video_stream)
    audio_thread = threading.Thread(target=audio_stream)
    
    video_thread.start()
    time.sleep(1)  # Small delay to let video initialize
    audio_thread.start()
    
    # Wait for both threads to finish
    video_thread.join()
    audio_thread.join()