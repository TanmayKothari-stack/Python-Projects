import tkinter as tk
from tkinter import ttk
import mysql.connector

root = tk.Tk()

root.title("Display Data")

root.geometry("400x280")

trv = ttk.Treeview(root, selectmode='browse')

trv.grid(row=1, column=1, padx=2, pady=2)

trv["columns"] = ("1", "2")
trv["show"] = "headings"
trv.column('1', width='1000', anchor='c')
trv.column('2', width='1000', anchor='c')

trv.heading("1", text='ID')
trv.heading("2", text='CHATS')

conn = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Tanmay1@', database = 'chat_room' )

cursor = conn.cursor()

query = "select * from chat "
cursor.execute(query)
result = cursor.fetchall()
for x in result:
    print(x)

    trv.insert("", 'end', iid=x[0], values=(x[0], x[1]))


root.mainloop()