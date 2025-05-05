from winotify import Notification , audio
import os
image_path = os.path.abspath("whatsapp.png")
print(image_path)
toast = Notification(app_id = 'Notification Program',title='Python',msg='Hello World',duration='short',icon=image_path)
toast.set_audio(audio.Default,loop=False)

toast.show()
