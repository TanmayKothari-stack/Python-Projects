import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox


import mysql.connector

conn = mysql.connector.connect(host = 'localhost', port=3306, user = 'root', password = '', db = 'ems'

)


if conn.is_connected():
    print("Connection Established")
else:
    print("Connection Failed")

cursor = conn.cursor()

root = Tk()


cursor.execute("select id from ems_data")

tup = cursor.fetchall()


k = [(1,2),(2,3),(3,4)]

out = list(sum(tup, ()))



sid = tk.ttk.Combobox(root, values=out)

sid.pack()



def display():
    cursor.execute("select id from ems_data ")

    tup = cursor.fetchall()
    out = list(sum(tup, ()))
    print(tup[-1])
    sid['values'] += (out[-1], )

Button(root, text="Get", fg="white", bg="red", width=10, font="verdena 12 bold", command=display).pack()




def close():
    root.destroy()

def open():
    root.mainloop()


root.mainloop()


