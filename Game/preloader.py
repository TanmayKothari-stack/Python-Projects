import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("900x900")


symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
i = 0
wait = 10000000000

while True:
    i = (i + 1) % len(symbols)
    print('\r\033[K%s loading...' % symbols[i], flush=True, end='')

    l = '\r\033[K%s loading...' % symbols[i]

    time.sleep(0.1)

    messagebox.showinfo("Loading", l)

    if time.time() > wait :
        break

    root.mainloop()