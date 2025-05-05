import socket
from tkinter import filedialog
import os
host = 'localhost'
port = 9999
def receiver():
    s = socket.socket()
    s.connect((host,port))
    data = s.recv(1024).decode("utf-8")
    #print(data)
    if not os.path.exists("downloads/"):
        os.mkdir("downloads/")
    file = open(f"downloads/{data}",'wb')
    while True:
        data = s.recv(8192)
        if not data:
            break
        file.write(data)
         
    file.close()
    #print(data)
    
receiver()
