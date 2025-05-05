from tkinter import *
from tkinter import filedialog,messagebox
import os
import shutil

root = Tk()
root.title("Installtion")
root.geometry("700x450+300+100")
root.resizable(0,0)
root.config(bg='white')
icon = PhotoImage(file="icon.png")
root.iconphoto(False,icon)

Label(root,text='User Agreement',font='verdena 15 bold',bg='white').place(x=250,y=10)

Label(root,text='''Important points must be remebered while installing this software :-

1. This softawre is an application software which is used for an specific purpose only.

2. The software is made for with an special order for a company.

3. This software is an open source software the written code files are provided inside directory.

4. This software is used within the the boundries of India only.

5. A proper licience is purchased legal while using this software.

######################## Hope this will help you to understand the product #############  ''',font='verdena 12',bg='white').place(x=10,y=100)
def agrees():
	checked = agree.get()
	if checked == 1:
		agree_button.config(state='normal')
		#messagebox.showinfo("Info","Clicked")
	else:
		agree_button.config(state='disable')

def nexter():
	root.destroy()
	next()

def next():
	window = Tk()
	window.title("Installtion")
	window.resizable(0,0)
	window.config(bg='white')
	icon = PhotoImage(file="icon.png")
	window.iconphoto(False,icon)
	window.geometry("700x450+300+100")


	def locate():
		global file
		global file_location_data
		file = "screen_recorder.exe"
		file_location_data = filedialog.askdirectory()
		location.delete(0,'end')
		location.insert(0,file_location_data+f"Screen Recorder/{file}")
		if location.get()!="":
			next_button.config(state='normal')
			install_button.config(state='normal')
		else:
			next_button.config(state='disable')
			install_button.config(state='disable')

	def install():
		try:
			file_loc = location.get()
			loc = file_location_data+"/Screen Recorder/"+file
			if(not os.path.exists(file_loc+"/Screen Recorder")):
				os.mkdir(loc+"/Screen Recorder")
			shutil.copy(file,loc)
			messagebox.showinfo("Sucess","Installtion Complete")
		except Exception as e:
			messagebox.showerror("Error",f"Installtion Failed {e}")

	file_location = Button(window,text='Select File Loctaion',font='verdena 12',bg='white',cursor='hand2',command=locate)
	file_location.place(x=10,y=10)
	location = Entry(window,width=50,font='verdena 12')
	location.place(x=200,y=15)

	next_button = Button(window,text='Next',font='verdena 12',width=10,cursor='hand2',state='disable')
	next_button.place(x=400,y=400)

	install_button = Button(window,text='Install',font='verdena 12',width=10,cursor='hand2',state='disable',command=install)
	install_button.place(x=550,y=400)

	window.mainloop()

frame = Frame(root,width=700,height=100)
frame.place(x=0,y=400)

agree = IntVar()
Checkbutton(frame, text='I accept agreement', font='verdena 12 ' ,variable=agree,onvalue=1,offvalue=0,command=agrees).place(x=10,y=10)

agree_button = Button(frame,text='Next',font='verdena 12',width=10,cursor='hand2',state='disable',command=nexter)
agree_button.place(x=580,y=10)


root.mainloop()
