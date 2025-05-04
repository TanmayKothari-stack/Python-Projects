from tkinter import *
from tkinter.ttk import Combobox
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',database='shopping')
cursor = conn.cursor()

root = Tk()
root.title("List Data")
root.geometry("500x500+400+50")

def delete_option():
	if combobox.get()!="Select Id":
		select_index = combobox.current()
		if select_index!= -1:
			del options[select_index]
			combobox.set("Select Id")
			combobox['values'] = options

cursor.execute("select id from customer_account")
result = cursor.fetchall()
options = [item[-1] for item in result]
combobox = Combobox(root,values=options,state='r')
combobox.set("Select Id")
combobox.place(x=200,y=20)
delete_button = Button(root,text='Delete Option',command=delete_option)
delete_button.place(x=100,y=20)
root.mainloop()