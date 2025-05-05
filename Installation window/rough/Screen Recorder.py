import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

import sounddevice as sd
import soundfile as sf
import os
import shutil
import keyboard
import time
start = int(input("Enter a duration in Seconds: "))
#time = dur * 60 * 60



while True:
    fs  = 48000
    myrec = sd.rec(int(start * fs), samplerate = fs, channels = 2 )

    if time.time() > start:
        break
    
sd.wait()

sf.write("c:/users/jitendra/My Computer Python/Recorder/test.mp3", myrec, fs)

# path = 'c:/users/jitendra/Recorder.flac'
# dest = 'c:/users/jitendra/My Computer Python/Recorder'
# shutil.move(path, dest)




width = GetSystemMetrics(0)
height  = GetSystemMetrics(1)

dim = (width, height)

f = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter("c:/users/jitendra/My Computer Python/Recorder/test.mp4", f , 30.0, dim)

now_start_time = time.time()

#start = int(input("Enter Time Do You Want To Record: "))

start = start*2+start

end_time = now_start_time + start

while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)

    output.write(frame)

    ctime = time.time()

    if ctime > end_time:
        break
    
output.release()

print("----END----")
