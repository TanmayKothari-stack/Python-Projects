import tkinter as tk
from tkinter import *
# Create the main GUI window
root = tk.Tk()
root.title("Multiple Labels Example")

k = 0
l = 0


for j in range(0, 10):
    label = Label(text="Label + str(i)")
    label.config(fg='red')
    l+= 50
    label.place(x=100, y=l)


root.mainloop()
