import tkinter
from tkinter import *
import time
root = Tk()
root.title("Loading")
root.geometry('450x40+450+250')
root.resizable(0,0)

icon = PhotoImage(file='whatsapp.png')
root.iconphoto(False,icon)

load = StringVar()

i = 0
j = 1
def data():
    for i in range(0,110,10):
        global j
        j+=4
        load.set(f"Loading {i}%")
        time.sleep(0.3)
        loader.config(text=load.get(), width=j)
        if i == 100:
            load.set(f"Loading Complete {i}%")
            loader.config(text=load.get())
        root.update_idletasks()
Label(root, font='verdena 12', height=1,bg='lightgrey',width=45).place(x=10, y=10)
loader = Label(root, fg='white', text=load.get() ,font='verdena 12',height=1,bg='green')
loader.place(x=10, y=10)

"""start_btn = Button(root, text="Start", command=data)
start_btn.place(x=30, y=50)"""
data()
time.sleep(1)
root.destroy()
try:
    import chatting.py
except:
    pass
root.mainloop()