from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Bg Image")

img = Image.open("test.jpg")

imgr = img.resize((500, 500))

image= ImageTk.PhotoImage(imgr)

Label(root, image=image).pack()

Label(root, text = "Hello World", fg ="white", bg="red", font="verdena 12 bold" ).place(x=10, y=10)

Entry(root, fg = "black", font="arial 15").place(x=10, y=50)

root.mainloop()