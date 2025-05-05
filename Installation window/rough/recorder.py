import sounddevice as sd
import soundfile as sf
import os
import time
dur = int(input("Enter a duration in Seconds: "))
#time = dur * 60 * 60



while True:
    fs  = 48000
    myrec = sd.rec(int(dur * fs), samplerate = fs, channels = 2 )

    if time.time() > dur:
        break
    
sd.wait()

sf.write("c:/users/jitendra/My Computer Python/Recorder/test.mp3", myrec, fs)

# path = 'c:/users/jitendra/Recorder.flac'
# dest = 'c:/users/jitendra/My Computer Python/Recorder'
# shutil.move(path, dest)

