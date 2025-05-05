import cv2 
import os

ques = input("Type a question: ")

if(ques == "Hello How Are You" or ques == "hi" or ques == "hello"):
    print("Hello how can be I service")
elif(ques == "Write a Html code for create a form" or ques == "how to create html form"):
    print("Here is a code\n")
    file = open('test.html')
    read = file.read()
    print(read)
elif(ques == "open html"):
    print("Opning HTML\n")
    os.system("test.html")
elif(ques == "open image"):
    print("Opning Image\n")
    open = os.system("test.jpg")
elif(ques == "play a song"):
    print("Playing Song")
    open = os.system("test.mp3")
elif(ques == "write a php code"):
    print("Here is A code\n")
    open = open("test.php")
    read = open.read()
    print(read)
