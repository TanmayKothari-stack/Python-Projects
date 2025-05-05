import tkinter
from tkinter import *
import PIL
from PIL import ImageTk, Image

root = Tk()

root.title("Image Opening for Python")
root.geometry("1352x690+0+0")
root.resizable(0,0)

image = Image.open('whatsapp.png')
image = image.resize((250, 250))
img = ImageTk.PhotoImage(image)
Label(image=img).pack()

Label(text='Welcome to WhatsApp', font='veredena 25 bold', fg='black').place(x=500, y=400)
Label(text='Read our Privacy Policy. Tap "Agree and continue to accept Terms of Service"', font='veredena 10 bold', fg='black').place(x=450, y=500)

agree = Button(text='Agree and continue', fg='white', bg='green', font='veredena 12', width=55, activebackground='green', activeforeground='white', pady=10)

agree.place(x=450, y=600)

root.mainloop()