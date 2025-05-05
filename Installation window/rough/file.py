from pathlib2 import Path
f = open("c:/users/jitendra/My Computer Python/test.txt", "a")
f.replace("Empid","Hello World")
f.close()

f = open("c:/users/jitendra/My Computer Python/test.txt", "r")

print(f.read())