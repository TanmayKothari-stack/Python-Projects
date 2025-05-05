import socket
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import filetype

#host = 'localhost'
port = 9999

def sender():
    host = host_entry.get()
    #print(host)
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    print("Waiting for incoming connections...")
    conn,addr = s.accept()
    file = open(filename,'rb')
    #data = file.read()
    file_name = os.path.basename(filename)
    print(file_name)
    #print(data)
    conn.send(f"{file_name}".encode("utf-8"))
    while chunk:= file.read(8192):
        conn.sendall(chunk)
    file.close()

def receiver():
    host = host_entry.get()
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
    
#sender()
#receiver()


def preview_image(image):
    img = Image.open(image)
    img = img.resize((500,150))
    image = ImageTk.PhotoImage(img)
    label.config(text='',image=image,width=500,height=150)
    label.image = image  

def preview_text(text):
    file = open(text,'r')
    data = file.read()
    label.config(image='',text=f'{data}',font='verdena 10',fg='black',width=500,height=7,bg='white')
    label.pack(ipady=10,ipadx=20)
    
root = Tk()
root.title("File Sharing Application")
width = 500
height = 500
root.geometry(f"{width}x{height}")
root.resizable(0,0)

label = Label(root,text='Preview File',font='verdena 15',fg='black',width=500,height=7,bg='white')
label.pack(side='top')

label1 = Frame(root,width=500,height=150,bg='#736aff')
label1.pack(side='bottom')
    
frame = Frame(root,width=500,height=500,bg='cyan')
frame.pack(side='top')

file_entry = Entry(frame,width=35,font='verdena 12',state='readonly')
file_entry.place(x=10,y=10)

def open_file():
    global filename
    filename = filedialog.askopenfilename(title='Select a file')
    file_ext = filename.split(".")[-1]
    #print(file_ext)
    file_entry.config(state='normal')
    file_entry.delete(0,END)
    file_entry.insert(0,filename)
    file_entry.config(state='readonly')

    file_name.config(state='normal')
    file_name.delete(0,END)
    file_name.insert(0,filename.split("/")[-1])
    file_name.config(state='readonly')

    file_type.config(state='normal')
    file_type.delete(0,END)
    kind = filetype.guess(filename)
    if kind:
        file_type.insert(0,kind.mime)
    elif filename.split(".")[-1] == "txt":
        file_type.insert(0,'text')
    elif filename.split(".")[-1] == "msi":
        file_type.insert(0,"application/x-msdownload")
    elif filename.split(".")[-1] == "html":
        file_type.insert(0,"Hypertext Markup Language")
    elif filename.split(".")[-1] == "css":
        file_type.insert(0,"Casscading Style Sheet")
    elif filename.split(".")[-1] == "js":
        file_type.insert(0,"javascript")
    elif filename.split(".")[-1] == "php":
        file_type.insert(0,"HyperText Preprocessor")
    elif filename.split(".")[-1] == "py":
        file_type.insert(0,"application/python")
    elif filename.split(".")[-1] == "jav" or filename.split(".")[-1] == "java":
        file_type.insert(0,"application/java")
    elif filename.split(".")[-1] == "c":
        file_type.insert(0,"application/c language")
    elif filename.split(".")[-1] == "kt":
        file_type.insert(0,"application/kotlin")
    else:
        file_type.insert(0,"other files")
    file_type.config(state='readonly')

    file_size.config(state='normal')
    file_size.delete(0,END)
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        for unit in ['KB','MB']:
            size /= 1024
        file_size.insert(0,f"{size:.2f} {unit}")
    file_size.config(state='readonly')
    
    if filename != "":
        if file_ext in ['jpg','jpeg','png','gif']:
            preview_image(filename)
        elif file_ext in ['txt','csv','log','py','html','css','php','js','jav','java','c','kt']:
            preview_text(filename)
            
        else:
            #file = open(filename,'rb')
            #data = file.read()
            label.config(image='',text=f'No Preview is available',font='verdena 15',fg='black',width=500,height=7,bg='white')
            label.pack(side='top')
    else:      
        label.config(image='',text='Preview File',font='verdena 15',fg='black',bg='white',width=500,height=7) 

file_btn = Button(frame,text='Select File',width=20,height=1,bg='red',fg='white',activebackground='red',activeforeground='white',cursor='hand2',command=open_file)
file_btn.place(x=345,y=10)

Label(frame,text='File Name ',font='verdena 12',bg='cyan').place(x=10,y=50)
file_name = Entry(frame,width=43,font='verdena 12',state='readonly')
file_name.place(x=100,y=50)

Label(frame,text='File Type ',font='verdena 12',bg='cyan').place(x=10,y=100)
file_type = Entry(frame,width=43,font='verdena 12',state='readonly')
file_type.place(x=100,y=100)

Label(frame,text='File Size ',font='verdena 12',bg='cyan').place(x=10,y=150)
file_size = Entry(frame,width=43,font='verdena 12',state='readonly')
file_size.place(x=100,y=150)

#open_file()

Label(label1,text='Host Name',font='verdena 12',bg='#736aff').place(x=10,y=30)
host_entry = Entry(label1,font='verdena 12',width=25)
host_entry.place(x=100,y=30)

send_btn = Button(label1,text='Send',width=20,height=1,bg='#7fff00',fg='white',activebackground='#7fff00',activeforeground='white',cursor='hand2',command=sender)
send_btn.place(x=345,y=30)

recv_btn = Button(label1,text='Receive',width=25,height=1,bg='#cc338b',fg='white',activebackground='#cc33ab',activeforeground='white',cursor='hand2',command=receiver)
recv_btn.place(x=150,y=100)

root.mainloop()



    
