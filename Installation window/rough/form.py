import tkinter as tk
from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host = "localhost", user="root", password="Tanmay1@", db = "tanmay")

cursor = conn.cursor()

root = Tk()

root.title("Insert Data")

frame = tk.Frame(root, bg="#5453a6")

fn = tk.Label(frame, text="First Name", font=('arial', 12), bg="#5453a6")
entry_fn = tk.Entry(frame)

ln = tk.Label(frame, text="Last Name", font=('arial', 12), bg="#5453a6")
entry_ln = tk.Entry(frame)

em = tk.Label(frame, text="Email", font=('arial', 12), bg="#5453a6")
entry_em = tk.Entry(frame)

ag = tk.Label(frame, text="Age", font=('arial', 12), bg="#5453a6")

entry_ag = tk.Entry(frame)


def data():
    fn_data = entry_fn.get()
    ln_data = entry_ln.get()
    em_data = entry_em.get()
    ag_data = entry_ag.get()

    sqli = "select count(*) from userdata "
    cursor.execute(sqli)
    total = cursor.fetchall()
    for n in total:
        n = n
    raw = list(n)
    format = str(raw)
    print(format[1])
    if(format[1] == '1' or format[1] > '1'):

        sql = "select firstname from userdata"
        cursor.execute(sql)
        result = cursor.fetchall()
        for x in result:
            x = x
            #print(x)
        dis = list(x)
        def convert(tup):
            str = ''.join(tup)
            return str
        data = convert(dis)
        if(data == fn_data):
            print("Failed To Insert The Data Into Database")
        if(format[1] == '0' or format[1] > '0' and data!= fn_data):
            qry = "insert into userdata (firstname, lastname, email, age) values (%s, %s, %s, %s) "
            values = (fn_data, ln_data, em_data, ag_data)
            exe = cursor.execute(qry, values)
            conn.commit()
            print("Data Inserted Into Database")

btn_in = tk.Button(root, text="Insert", font=('arial', 14), bg="red", command=data)

fn.grid(row=0, column=0)
entry_fn.grid(row=0, column=1, pady=10, padx=10)

ln.grid(row=1, column=0)
entry_ln.grid(row=1, column=1, pady=10, padx=10)

em.grid(row=2, column=0)
entry_em.grid(row=2, column=1, pady=10, padx=10)

ag.grid(row=3, column=0)
entry_ag.grid(row=3, column=1, pady=10, padx=10)

btn_in.grid(row=4, column=0, pady=10, padx=10)

frame.grid(row=0, column=0)

root.mainloop()

#sql = "create table userdata (id int(11) not null auto_increment, primary key(`id`), firstname varchar(100), lastname varchar(100), email varchar(100), age varchar(100) ) "
#exe = cursor.execute(sql)
#conn.commit()
#print("Data Inserted Into Database")



