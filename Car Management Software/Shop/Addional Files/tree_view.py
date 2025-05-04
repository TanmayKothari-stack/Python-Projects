from tkinter import *
from tkinter import ttk
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root',password='',database='shopping')
cursor = conn.cursor()

root = Tk()
root.title("Tree View")
root.geometry("500x500+350+100")

def data():
	cursor.execute("select * from customer_account ")
	result = cursor.fetchall()
	tree.delete(*tree.get_children())
	for res in result:
		tree.insert('',END, values=res)

xscroll = Scrollbar(root,orient='horizontal')
yscroll = Scrollbar(root,orient='vertical')
xscroll.pack(side='top',fill=X)
yscroll.pack(side='right',fill=Y)

tree = ttk.Treeview(root,columns=('Id','Name','Password','Email','Mobile','State','City'),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
tree.heading('Id',text='Id')
tree.heading('Name',text='Name')
tree.heading('Password',text='Password')
tree.heading('Mobile',text='Mobile')
tree.heading('State',text='State')
tree.heading('City',text='City')
tree['show'] = 'headings'
tree.column('Id',width=10)
tree.pack(fill='both',expand=1)
data()
xscroll.config(command=tree.xview)
yscroll.config(command=tree.yview)

root.mainloop()