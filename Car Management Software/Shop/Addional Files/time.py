import datetime
import tkinter as tk

def update_time():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)


root = tk.Tk()
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='white')
time_label.place(x=0,y=0)
update_time()

root.mainloop()
