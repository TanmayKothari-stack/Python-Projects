import socket

user = socket.gethostname()
ip = socket.gethostbyname(user)
print(ip)