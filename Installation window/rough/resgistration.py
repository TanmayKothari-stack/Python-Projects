import tkinter as tk
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
#import mysql.connector

#conn = mysql.connector.connect(host = 'localhost', port='3306', user = 'root', password = 'mysql')

#cursor = conn.cursor()


root = Tk()
root.title("Registration Form")
root.config(bg='#5453a6')
root.geometry("500x900+400+0")
root.resizable(0,0)

#Design Part

def name_placeholder(event):
    if name_entry.get() == 'Name':
        name_entry.delete(0,END)

def pass_placeholder(event):
    if pass_entry.get() == 'Password':
        pass_entry.delete(0, END)
        pass_entry.config(show='*')

def conpass_placeholder(event):
   if conpass_entry.get() == 'Conform Password':
        conpass_entry.delete(0, END)
        conpass_entry.config(show='*')

def onhover(event):
    submit['background'] = 'magenta'
def onunhover(event):
    submit['background'] = 'deeppink'

def email_placeholder(event):
    if email_entry.get() == 'Email':
        email_entry.delete(0, END)

def submit():
    nm = name_entry.get()
    ps = pass_entry.get()
    cnps = conpass_entry.get()
    em = email_entry.get()
    if nm == "" or nm == "Name" or ps == "" or ps == "Password" or cnps == "" or cnps == "Conform Password" or cnps!= ps or em == "" or em == "Email" :
        messagebox.showerror('Error', "Data Is Missing Please Try Again")
    #else:
        #sql = "select name from tan where name = %s or email = %s "
        #dta = cursor.execute(sql, (nm, em))
        #res = cursor.fetchone()
        #if res!= None:
            #messagebox.showerror('Error', 'Data Already Exits #Please Try Again or choose diffrent one data')
       # else:
            #query = "insert into user_data (name, password, #conpassword, email) values(%s, %s, %s, %s) ";
            #values = (nm, ps, cnps, em)

            #cursor.execute(query, values)

            #if conn.commit():
                #print("Data Insetred Into Database")
    else:
        messagebox.showinfo('Sucess', 'Registration Sucessfull')


Label(root, text="Regisration Form", bg='#64e9a6', font='arial 20 bold', fg='white').pack(side=TOP, fill=X)

Label(root, text="Regisration Details", bg='deeppink', font='arial 14 bold', fg='white').pack(side=TOP, fill=X)

frame = LabelFrame(root, width=1200, height=500, bd=0, bg='#5453a6', fg='white', font='arial 12', )

frame.place(x = 0, y = 100)

Label(frame, text='Name', font='verdana 12', bd=0, bg='#5453a6', fg='white').place(x=10, y=12)

name = StringVar()

name_entry = Entry(frame, textvariable=name, font='arial 20', fg='magenta2', bg='white', width='22')

name_entry.place(x=120, y=10)

name_entry.insert(0,'Name')

name_entry.bind('<FocusIn>', name_placeholder)

Label(frame, text='Password', font='verdana 12', bd=0, bg='#5453a6', fg='white').place(x=10, y=82)

password = StringVar()

pass_entry = Entry(frame, font='arial 20', fg='magenta2', bg='white', width='22')

pass_entry.place(x=120, y=80)

pass_entry.insert(0,'Password')

pass_entry.bind('<FocusIn>', pass_placeholder)

Label(frame, text='Conform Password', font='verdana 8', bd=0, bg='#5453a6', fg='white').place(x=10, y=152)


conpassword = StringVar()

conpass_entry = Entry(frame, font='arial 20', fg='magenta2', bg='white', width='22')

conpass_entry.place(x=120, y=150)

conpass_entry.insert(0,'Conform Password')

conpass_entry.bind('<FocusIn>', conpass_placeholder)

Label(frame, text='Email', font='verdana 12', bd=0, bg='#5453a6', fg='white').place(x=10, y=222)

email = StringVar()

email_entry = Entry(frame, font='arial 20', fg='magenta2', bg='white', width='22')

email_entry.place(x=120, y=220)

email_entry.insert(0, 'Email')

email_entry.bind('<FocusIn>', email_placeholder)



submit = Button(frame, text='Submit', font='verdana 12', fg='white', bg='deeppink', width=30, height=1, cursor='hand2', command=submit)

submit.place(x= 120, y= 350)


submit.bind('<Enter>', onhover)
submit.bind('<Leave>', onunhover)


root.mainloop()
