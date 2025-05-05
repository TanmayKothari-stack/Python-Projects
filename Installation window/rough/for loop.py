import tkinter
from tkinter import *
root = Tk()
l = ['A','B','C','D','E']
y = 0
for i in l:
	print(i)
	y = y+50
	Label(root,text=f'{i}',fg='white',bg='green',font='verdena 12').place(x=10,y=y)
root.mainloop()