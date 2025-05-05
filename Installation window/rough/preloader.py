from tkinter import *
from tkinter import ttk
import time

gui = Tk()
gui.title("Loading")
gui.geometry("500x100")
gui.resizable(0,0)
data = 0
def StartProgress():
    for i in range(5):
        global data
        progress_var["value"] += 20
        stringvar.set(f"Loading {progress_var['value']}")
        label.config(text=stringvar.get() + " %")
        gui.update_idletasks()
        time.sleep(1)
        data+=20
        if data == 100:
            gui.destroy()

# create an instance of progress bar
progress_var = ttk.Progressbar(gui, orient=HORIZONTAL, length=200, mode="determinate")
progress_var.place(x=30, y=20)

# string variable
stringvar = StringVar()
stringvar.set("0%")

# create a label
label = Label(gui, text=stringvar.get(), font=("", 12))
label.place(x=250, y=20)

start_btn = Button(gui, text="Start", command=StartProgress)
start_btn.place(x=30, y=50)

gui.mainloop()
