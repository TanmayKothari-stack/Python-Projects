from winotify import Notification , audio
import os
import time
import threading
def notification():
    image_path = os.path.abspath("whatsapp.png")
    print(image_path)
    toast = Notification(app_id = 'Notification Program',title='Python',msg='Hello World',duration='long',icon=image_path)
    toast.set_audio(audio.LoopingAlarm,loop=True)

    toast.show()

def loop():
    while True:
        notification()
        time.sleep(27)
        
notification_thread = threading.Thread(target=loop)
notification_thread.start()

