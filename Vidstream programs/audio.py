from vidstream import *
import threading
import time

receiving = AudioReceiver("169.254.46.255",9999)
sending = AudioSender("169.254.46.255",9999)

t1 = threading.Thread(target=receiving.start_server)
t1.start()

#time.sleep(2)

t2 = threading.Thread(target=sending.start_stream)
t2.start()

while input("")!="STOP":
	continue

receiving.stop_server()
sending.stop_stream()