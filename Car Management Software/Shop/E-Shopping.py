import tkinter
from tkinter import*
from tkinter import ttk, messagebox,Scrollbar
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import socket
from datetime import datetime
from tkinter import filedialog
import os
import shutil
import matplotlib.pyplot as plt
import numpy as np
import smtplib as s
import webbrowser
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root',password='',database='shopping')
cursor = conn.cursor()


global root
def signup():
	root = Tk()
	root.title("Signup")
	root.geometry("1350x750+0+0")
	root.resizable(0,0)
	root.config(bg='white')
	icon = PhotoImage(file='car.png')
	root.iconphoto(False,icon)

	def submit():
		nm = username.get()
		pwd = password.get()
		eml = email.get()
		secques = security_question.get()
		secans = security_answer.get()

		if nm == "":
			messagebox.showerror("Error","Please write username")
			return False

		if len(nm)< 2:
			messagebox.showerror("Error","Please write username atleast of two characters")
			return False

		if pwd == "":
			messagebox.showerror("Error","Please write Password")
			return False

		if eml == "":
			messagebox.showerror("Error","Please write Email Address")
			return False

		if len(eml) < 12:
			messagebox.showerror("Error","Please write Correct Email Address")
			return False

		if secques == "Select Security Question":
			messagebox.showerror("Error","Please Select Security Question")
			return False

		if secans == "":
			messagebox.showerror("Error","Please write Security Answer")
			return False

		else:
			cursor.execute("select * from account where email =%s",(eml,))
			res = cursor.fetchone()
			if res is not None:
				messagebox.showerror("Error","This Email is already registered please choose the diffrent one")
				
			else:
				cursor.execute("insert into account (name,password,email,security_question,security_answer,device_name) values(%s,%s,%s,%s,%s,%s)",(nm,pwd,eml,secques,secans,socket.gethostname()))

				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Sign Up Sucessfully")
				root.destroy()
				login()


	def reset():
		nm = username
		pwd = password
		eml = email
		secques = security_question
		secans = security_answer

		nm.delete(0,END)
		pwd.delete(0,END)
		eml.delete(0,END)
		secques.set("Select Security Question")
		secans.delete(0,END)

	image = Image.open("background.png")
	image = image.resize((1350,750))
	background_image = ImageTk.PhotoImage(image)
	Label(root,image=background_image,width=1350,height=750).place(x=0,y=0)
	frame = Frame(root,bg='white',width=500,height=650)
	frame.place(x=450,y=30)

	image = Image.open("admin.jpg")
	image = image.resize((50,50))
	user_image = ImageTk.PhotoImage(image)

	Label(frame,image=user_image).place(x=10,y=10)

	Label(frame,text='User Signup Form',font='verdena 15 bold',bg='white').place(x=150,y=20)

	Label(frame,text='User Name',font='verdena 12',bg='white').place(x=10,y=100)
	username = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	username.place(x=150,y=100)

	Label(frame,text='Password',font='verdena 12',bg='white').place(x=10,y=200)
	password = Entry(frame,width=30,font='verdena 12',textvariable=StringVar(),show="*")
	password.place(x=150,y=200)

	Label(frame,text='Email',font='verdena 12',bg='white').place(x=10,y=300)
	email = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	email.place(x=150,y=300)

	Label(frame,text='Security Question',font='verdena 12',bg='white').place(x=10,y=400)
	security_question = Combobox(frame,values=['Select Security Question','Name','Father Name','Company Name'],width=28, font='verdena 12',state='r')
	security_question.place(x=150,y=400)
	security_question.set("Select Security Question")

	Label(frame,text='Security Answer',font='verdena 12',bg='white').place(x=10,y=500)
	security_answer = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	security_answer.place(x=150,y=500)

	submit_button = Button(frame,text='Sign Up',font='verdena 12',bg='green',fg='white',activeforeground='white', width=13,activebackground='green', cursor='hand2',command=submit).place(x=150,y=600)

	reset_button = Button(frame,text='Reset',font='verdena 12',bg='red',fg='white', width=13,activeforeground='white',activebackground='red', cursor='hand2',command=reset).place(x=300,y=600)

	root.mainloop()

############# End of First Window ###############

global root2

def login():
	def user_signup():
		root2.destroy()
		signup()

	def forget_password():
		root2.destroy()
		recover_password()

	def submit():
		eml = email.get()
		pwd = password.get()
		
		if eml == "":
			messagebox.showerror("Error","Please write Email Address")
			return False

		if len(eml) < 12:
			messagebox.showerror("Error","Please write Correct Email Address")
			return False

		if pwd == "":
			messagebox.showerror("Error","Please write Password")
			return False
		else:
			cursor.execute("select * from account where email=%s and password=%s",(eml,pwd))
			res = cursor.fetchone()
			if res is not None:
				cursor.execute("select * from logindata where email=%s and device_name=%s",(eml,socket.gethostname()))
				result = cursor.fetchone()
				if result is None:
					cursor.execute("insert into logindata (email,device_name) values(%s,%s)",(eml,socket.gethostname()))
					if conn.commit():
						pass
					messagebox.showinfo("Sucess","Login Sucessfully")
					root2.destroy()
					dashboard()
				else:
					messagebox.showinfo("Sucess","Login Sucessfully")
					root2.destroy()
					dashboard()

			else:
				messagebox.showerror("Error","Invalid Useremail and Password Try again")


	root2 = Tk()
	root2.title("Login")
	root2.geometry("1350x750+0+0")
	root2.resizable(0,0)
	root2.config(bg='#5453a6')
	icon = PhotoImage(file='car.png')
	root2.iconphoto(False,icon)

	image = Image.open('background1.png')
	image = image.resize((1380,750))
	background_image = ImageTk.PhotoImage(image)
	Label(root2,image=background_image,width=1380,height=750).place(x=0,y=0)

	frame = Frame(root2,width=500,height=450,bg='#5453a6')
	frame.place(x=450,y=150)

	Label(frame,text='Welcome',font='verdena 15 bold', bg='#5453a6',fg='red').place(x=200,y=10)
	image = Image.open('admin.jpg')
	image = image.resize((50,50))
	admin_img = ImageTk.PhotoImage(image)
	Label(frame,image=admin_img).place(x=20,y=70)

	Label(frame,text='User Login', bg='#5453a6', fg='white',font='verdena 15 bold').place(x=200,y=70)
	Label(frame,text='Email',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=170)
	email = Entry(frame,font='verdena 12',width=30,textvariable=StringVar())
	email.place(x=100,y=170)


	Label(frame,text='Password',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=240)
	password = Entry(frame,font='verdena 12',width=30,textvariable=StringVar(),show='*')
	password.place(x=100,y=240)

	Button(frame, text='Forget Password ?',font='verdena 12',width=30,bg='#5453a6',fg='white', activebackground='#5453a6', activeforeground='white', border=0,cursor='hand2',command=forget_password).place(x=100,y=310)

	Button(frame, text='New User ? Signup',font='verdena 12',width=30,bg='#5453a6',fg='white', activebackground='#5453a6', activeforeground='white', border=0,cursor='hand2',command=user_signup).place(x=100,y=340)

	login_data = Button(frame, text='Login',font='verdena 12',width=30,bg='green',fg='white', activebackground='green', activeforeground='white', border=0,cursor='hand2',command=submit).place(x=100,y=390)



	root2.mainloop()

############# End of Second Window ###############

global recover_password
def recover_password():
	root3 = Tk()
	root3.title("Password Recovery")
	root3.geometry("1350x750+0+0")
	root3.resizable(0,0)
	root3.config(bg='#5453a6')
	icon = PhotoImage(file='car.png')
	root3.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root3.destroy()
		profile()

	def dashboard_window():
		root3.destroy()
		dashboard()

	def car_window():
		root3.destroy()
		cars()

	def order_window():
		root3.destroy()
		orders()

	def customer_window():
		root3.destroy()
		customer()

	def customer_contact_window():
		root3.destroy()
		customer_contact()

	def customer_feedback_window():
		root3.destroy()
		customer_feedback()

	def logout_page():
		root3.destroy()
		logout()

	frame1 = Frame(root3,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root3,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)


	def submit():
		eml = email.get()
		secans = security_answer.get()
		pwd = new_password.get()
		if eml == "":
			messagebox.showerror("Error","Please write Email Address")
			return False

		if len(eml) < 12:
			messagebox.showerror("Error","Please write Correct Email Address")
			return False

		if secans == "":
			messagebox.showerror("Error","Please write security answer")
			return False

		if pwd == "":
			messagebox.showerror("Error","Please write Password")
			return False
		else:
			cursor.execute("select * from account where email=%s and security_answer = %s",(eml,secans))
			res = cursor.fetchone()
			if res is not None:
				cursor.execute("update account set password = %s where email=%s ",(pwd,eml))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Password changed sucessfully")
				root6.destroy()
				login()

			else:
				messagebox.showerror("Error","Invalid Security Answer")

	image = Image.open('background2.png')
	image = image.resize((1380,750))
	background_image = ImageTk.PhotoImage(image)
	Label(frame2,image=background_image,width=1380,height=750).place(x=0,y=0)

	frame = Frame(frame2,width=500,height=450,bg='greenyellow')
	frame.place(x=350,y=150)

	Label(frame,text='Welcome',font='verdena 15 bold', bg='greenyellow',fg='red').place(x=200,y=10)
	image = Image.open('admin.jpg')
	image = image.resize((50,50))
	admin_img1 = ImageTk.PhotoImage(image)
	Label(frame,image=admin_img1).place(x=20,y=70)

	Label(frame,text='User Password Recovery', bg='greenyellow', fg='white',font='verdena 15 bold').place(x=120,y=70)
	Label(frame,text='Email',font='verdena 12',bg='greenyellow',fg='white').place(x=20,y=170)
	email = Entry(frame,font='verdena 12',width=30,textvariable=StringVar())
	email.place(x=150,y=170)

	Label(frame,text='Security Answer',font='verdena 12',bg='greenyellow',fg='white').place(x=20,y=240)
	security_answer = Entry(frame,font='verdena 12',width=30,textvariable=StringVar())
	security_answer.place(x=150,y=240)

	Label(frame,text='New Password',font='verdena 12',bg='greenyellow',fg='white').place(x=20,y=310)
	new_password = Entry(frame,font='verdena 12',width=30,textvariable=StringVar(),show='*')
	new_password.place(x=150,y=310)

	login_data = Button(frame, text='Login',font='verdena 12',width=30,bg='green',fg='white', activebackground='green', activeforeground='white', border=0,cursor='hand2',command=submit).place(x=150,y=380)



	root3.mainloop()

############# End of Third Window ###############


global dashboard
def dashboard():
	root4 = Tk()
	root4.title("E-Shopping")
	root4.geometry("1350x750+0+0")
	root4.config(bg='lightgrey')
	root4.resizable(0,0)
	icon = PhotoImage(file='car.png')
	root4.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root4.destroy()
		profile()

	def dashboard_window():
		root4.destroy()
		dashboard()

	def car_window():
		root4.destroy()
		cars()

	def order_window():
		root4.destroy()
		orders()

	def customer_window():
		root4.destroy()
		customer()

	def customer_contact_window():
		root4.destroy()
		customer_contact()

	def customer_feedback_window():
		root4.destroy()
		customer_feedback()

	def logout_page():
		root4.destroy()
		logout()

	frame1 = Frame(root4,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root4,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	cursor.execute("select * from account where device_name = %s ",(socket.gethostname(),))
	res = cursor.fetchone()

	def time():
		current_time = datetime.now().strftime('%H:%M:%S')
		time_label.config(text=f'Current Time ({current_time})')
		time_label.after(1000,time)

	def totalcar():
		root4.destroy()
		cars()

	Label(frame2,text=f'Welcome {res[1]}',width=100,font='verdena 12 bold',bg='#5453a6',fg='white',pady=10,padx=80).place(x=0,y=0)

	cursor.execute("select * from cars_data ")
	res1 = cursor.fetchall()

	Button(frame2,text=f'Total cars ({len(res1)})',width=10,font='verdena 12 bold',bg='white',fg='black',pady=10,padx=50,activebackground='white',activeforeground='black',border=0,cursor='hand2',command=totalcar).place(x=20,y=60)

	cursor.execute("select * from customer_account ")
	res2 = cursor.fetchall()

	Button(frame2,text=f'Total Costumers ({len(res2)})',width=10,font='verdena 12 bold',bg='white',fg='black',pady=10,padx=50,activebackground='white',activeforeground='black',border=0,cursor='hand2',command=customer_window).place(x=250,y=60)

	cursor.execute("select * from registred_customers where time=%s ",(datetime.now().strftime("%d/%m/%y"),))
	res3 = cursor.fetchall()
	def today_registration():
		today_registrations()

	Button(frame2,text=f'Today Registration ({len(res3)})',width=10,font='verdena 12 bold',bg='white',fg='black',pady=10,padx=50,activebackground='white',activeforeground='black',border=0,cursor='hand2',command=today_registration).place(x=480,y=60)

	cursor.execute("select * from registred_customers ")
	res4 = cursor.fetchall()
	def total_registration():
		total_registrations()

	Button(frame2,text=f'Total Registrations ({len(res4)})',width=10,font='verdena 12 bold',bg='white',fg='black',pady=10,padx=50,activebackground='white',activeforeground='black',border=0,cursor='hand2',command=total_registration).place(x=710,y=60)

	time_label = Label(frame2,width=10,font='verdena 12 bold',bg='white',fg='black',pady=12,padx=50,activebackground='white',activeforeground='black')
	time_label.place(x=940,y=60)
	time()


	frame3 = Frame(frame2,width=1100,height=700,bg='lightgrey')
	frame3.place(x=10,y=150)
	
	def on_scroll(*args):
	    canvas.yview(*args)
	    canvas.update_idletasks()
	    canvas.config(scrollregion=canvas.bbox("all"))

	
	def update_canvas():
		conn = mysql.connector.connect(host='localhost',user='root',password='',database='shopping')

		cursor = conn.cursor()

		canvas.delete("all")
		
		cursor.execute("select * from customer_login ")
		result = cursor.fetchall()

		y = 20
		for res in result:
			canvas.create_text(20,y,text=f'{res[0]}',font='verdena 12')
			canvas.create_text(200,y,text=f'{res[1]}',font='verdena 12')
			canvas.create_text(400,y,text=f'{res[2]}',font='verdena 12')
			canvas.create_text(650,y,text=f'{res[4]}',font='verdena 12')
			canvas.create_text(850,y,text=f'{res[5]}',font='verdena 12')
			canvas.create_text(1020,y,text=f'{res[6].strftime("%d-%m-%y %H:%M:%S")}',font='verdena 12')
			y+=30

		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.place(x=0,y=100)
		scrollbar.pack(fill='y',side='right')

		canvas.after(1000,update_canvas)

	canvas = Canvas(frame3,width=1100,height=475,bg='white',scrollregion=(0,0,800,600))

	Label(frame3,text='Customer Login Details',font='verdena 12 bold',width=110,bg='#5453a6', fg='white',pady=10).place(x=0,y=0)

	scrollbar = Scrollbar(root4,orient='vertical', width=15,command=on_scroll)
	
	Label(frame3,text='Id',font='verdena 12 bold',width=5,bg='#5453a6', fg='white',pady=10).place(x=0,y=50)

	Label(frame3,text='Name',font='verdena 12 bold',width=25,bg='#5453a6', fg='white',pady=10).place(x=60,y=50)

	Label(frame3,text='Mobile No',font='verdena 12 bold',width=20,bg='#5453a6', fg='white',pady=10).place(x=320,y=50)

	Label(frame3,text='Email',font='verdena 12 bold',width=25,bg='#5453a6', fg='white',pady=10).place(x=530,y=50)

	Label(frame3,text='Customer Id',font='verdena 12 bold',width=15,bg='#5453a6', fg='white',pady=10).place(x=790,y=50)

	Label(frame3,text='Login Time',font='verdena 12 bold',width=15,bg='#5453a6', fg='white',pady=10).place(x=950,y=50)

	update_canvas()

	
############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)


	root4.mainloop()

################ End of Fourth Window ##################



global logout
def logout():
	root5 = Tk()
	root5.title("Logout")
	root5.geometry("1350x750+0+0")
	root5.resizable(0,0)
	root5.config(bg='white')
	icon = PhotoImage(file='car.png')
	root5.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root5.destroy()
		profile()

	def dashboard_window():
		root5.destroy()
		dashboard()

	def car_window():
		root5.destroy()
		cars()

	def order_window():
		root5.destroy()
		orders()

	def customer_window():
		root5.destroy()
		customer()

	def customer_contact_window():
		root5.destroy()
		customer_contact()

	def customer_feedback_window():
		root5.destroy()
		customer_feedback()

	def logout_page():
		root5.destroy()
		logout()

	frame1 = Frame(root5,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root5,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)


	def forget_password():
		root5.destroy()
		recover_password()

	def submit():
		eml = email.get()
		pwd = password.get()
		
		if eml == "":
			messagebox.showerror("Error","Please write Email Address")
			return False

		if len(eml) < 12:
			messagebox.showerror("Error","Please write Correct Email Address")
			return False

		if pwd == "":
			messagebox.showerror("Error","Please write Password")
			return False
		else:
			cursor.execute("select * from account where email=%s and password=%s",(eml,pwd))
			res = cursor.fetchone()
			if res is not None:
				cursor.execute("delete from logindata where email=%s and device_name=%s",(eml,socket.gethostname()))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Logout Sucessfully")
				root5.destroy()
				login()
			else:
				messagebox.showerror("Error","Invalid Useremail and Password Try again")

	image = Image.open('background3.png')
	image = image.resize((1380,750))
	background_image = ImageTk.PhotoImage(image)
	Label(frame2,image=background_image,width=1380,height=750).place(x=0,y=0)

	frame = Frame(frame2,width=500,height=400,bg='maroon')
	frame.place(x=350,y=150)

	image = Image.open('logout.png')
	image = image.resize((50,50))
	logout_img = ImageTk.PhotoImage(image)
	Label(frame,image=logout_img).place(x=20,y=20)

	Label(frame,text='User Logout', bg='maroon', fg='white',font='verdena 15 bold').place(x=200,y=20)
	Label(frame,text='Email',font='verdena 12',bg='maroon',fg='white').place(x=20,y=120)
	email = Entry(frame,font='verdena 12',width=30,textvariable=StringVar())
	email.place(x=100,y=120)

	Label(frame,text='Password',font='verdena 12',bg='maroon',fg='white').place(x=20,y=220)
	password = Entry(frame,font='verdena 12',width=30,textvariable=StringVar(),show='*')
	password.place(x=100,y=220)

	Button(frame, text='Forget Password ?',font='verdena 12',width=30,bg='maroon',fg='white', activebackground='maroon', activeforeground='white', border=0,cursor='hand2',command=forget_password).place(x=100,y=280)

	logout_data = Button(frame, text='Logout',font='verdena 12',width=30,bg='red',fg='white', activebackground='red', activeforeground='white', border=0,cursor='hand2',command=submit).place(x=100,y=320)


	root5.mainloop()

############################ End of Fifth Window #########################

global profile
def profile():
	root6 = Tk()
	root6.title("User Profile")
	root6.geometry("1350x750+0+0")
	root6.resizable(0,0)
	root6.config(bg='white')
	icon = PhotoImage(file='car.png')
	root6.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root6.destroy()
		profile()

	def dashboard_window():
		root6.destroy()
		dashboard()

	def car_window():
		root6.destroy()
		cars()

	def order_window():
		root6.destroy()
		orders()

	def customer_window():
		root6.destroy()
		customer()

	def customer_contact_window():
		root6.destroy()
		customer_contact()

	def customer_feedback_window():
		root6.destroy()
		customer_feedback()

	def logout_page():
		root6.destroy()
		logout()

	frame1 = Frame(root6,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root6,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)


	def submit():
		nm = username.get()
		pwd = password.get()
		eml = email.get()
		secques = security_question.get()
		secans = security_answer.get()
		dvc_nm = device_name.get()

		if nm == "":
			messagebox.showerror("Error","Please write username")
			return False

		if len(nm)< 2:
			messagebox.showerror("Error","Please write username atleast of two characters")
			return False

		if pwd == "":
			messagebox.showerror("Error","Please write Password")
			return False

		if eml == "":
			messagebox.showerror("Error","Please write Email Address")
			return False

		if len(eml) < 12:
			messagebox.showerror("Error","Please write Correct Email Address")
			return False

		if secques == "Select Security Question":
			messagebox.showerror("Error","Please Select Security Question")
			return False

		if secans == "":
			messagebox.showerror("Error","Please write Security Answer")
			return False

		else:
			cursor.execute("select * from account where email =%s",(eml,))
			res = cursor.fetchone()
			if res is not None:
				cursor.execute("update account set name=%s, password=%s,email=%s, security_question=%s,security_answer=%s, device_name=%s",(nm,pwd,eml,secques,secans,socket.gethostname()))
				cursor.execute("update logindata set email=%s,device_name=%s where email=%s ",(eml,socket.gethostname(),eml))
				cursor.execute("update email_sender set email=%s,device_name=%s where email=%s ",(eml,socket.gethostname(),eml))

				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Profile Updated Sucessfully")
				root6.destroy()
				profile()


	def reset():
		nm = username
		pwd = password
		eml = email
		secques = security_question
		secans = security_answer
		dvc_nm = device_name

		nm.delete(0,END)
		pwd.delete(0,END)
		eml.delete(0,END)
		secques.set("Select Security Question")
		secans.delete(0,END)
		dvc_nm.delete(0,END)

	image = Image.open("background4.png")
	image = image.resize((1350,750))
	background_image = ImageTk.PhotoImage(image)
	Label(frame2,image=background_image,width=1350,height=750).place(x=0,y=0)
	frame = Frame(frame2,bg='white',width=500,height=700)
	frame.place(x=350,y=10)

	image = Image.open("admin.jpg")
	image = image.resize((50,50))
	user_image = ImageTk.PhotoImage(image)

	Label(frame,image=user_image).place(x=10,y=10)

	Label(frame,text='User Profile',font='verdena 15 bold',bg='white').place(x=200,y=20)

	Label(frame,text='User Name',font='verdena 12',bg='white').place(x=10,y=100)
	username = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	username.place(x=150,y=100)

	Label(frame,text='Password',font='verdena 12',bg='white').place(x=10,y=200)
	password = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	password.place(x=150,y=200)

	Label(frame,text='Email',font='verdena 12',bg='white').place(x=10,y=300)
	email = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	email.place(x=150,y=300)

	Label(frame,text='Security Question',font='verdena 12',bg='white').place(x=10,y=400)
	security_question = Combobox(frame,values=['Select Security Question','Name','Father Name','Company Name'],width=28, font='verdena 12',state='r')
	security_question.place(x=150,y=400)
	security_question.set("Select Security Question")

	Label(frame,text='Security Answer',font='verdena 12',bg='white').place(x=10,y=500)
	security_answer = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	security_answer.place(x=150,y=500)

	Label(frame,text='Device Name',font='verdena 12',bg='white').place(x=10,y=600)
	device_name = Entry(frame,width=30,font='verdena 12',textvariable=StringVar())
	device_name.place(x=150,y=600)

	submit_button = Button(frame,text='Update',font='verdena 12',bg='green',fg='white',activeforeground='white', width=13,activebackground='green', cursor='hand2',command=submit).place(x=150,y=650)

	reset_button = Button(frame,text='Reset',font='verdena 12',bg='red',fg='white', width=13,activeforeground='white',activebackground='red', cursor='hand2',command=reset).place(x=300,y=650)


	cursor.execute("select * from account where device_name=%s",(socket.gethostname(),))
	res = cursor.fetchone()

	username.insert(0,res[1])
	password.insert(0,res[2])
	email.insert(0,res[3])
	security_question.set(res[4])
	security_answer.insert(0,res[5])
	device_name.insert(0,res[6])


	root6.mainloop()


############################ End of Sixth Window #########################



def customer():
	root7 = Tk()
	root7.title("Customers Details")
	root7.geometry("1350x750+0+0")
	root7.resizable(0,0)
	root7.config(bg='white')
	icon = PhotoImage(file='car.png')
	root7.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root7.destroy()
		profile()

	def dashboard_window():
		root7.destroy()
		dashboard()

	def car_window():
		root7.destroy()
		cars()

	def order_window():
		root7.destroy()
		orders()

	def customer_window():
		root7.destroy()
		customer()

	def customer_contact_window():
		root7.destroy()
		customer_contact()

	def customer_feedback_window():
		root7.destroy()
		customer_feedback()

	def logout_page():
		root7.destroy()
		logout()

	frame1 = Frame(root7,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root7,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)

	
	cursor.execute("select * from account where device_name=%s ",(socket.gethostname(),))
	res = cursor.fetchone()
	Label(frame2,text=f'Welcome {res[1]}', font='verdena 12 bold',width=100, height=2,bg='#5453a6',fg='white',padx=75).place(x=0,y=0)

	frame = Frame(frame2,width=1130, height=300,bg='#5453a6')
	frame.place(x=10,y=50)

	labelframe = LabelFrame(frame,width=850,height=60,bg='#5453a6')
	labelframe.place(x=200,y=20)

	Label(labelframe,text='Select Customers Data', width=15,font='verdena 12 bold',fg='white',bg='#5453a6',padx=20).place(x=0,y=20)
	

	def selected_customer_options(event):

		cmb = customer_options.get()
		if cmb == 'Customer Id':
				cmb = "customer_id"
		if cmb!="Select":
			cursor.execute(f"select {cmb} from customer_account ")
			res = cursor.fetchall()
			list_options = [item[0] for item in res]

			def search():
				search_cust_data = search_data.get()
				if search_cust_data == f"Select Customer {cmb}":
					messagebox.showerror("Error","Please select customer data first")
					return False
				else:
					cursor.execute(f"select * from customer_account where {cmb} = %s ",(search_cust_data,))
					res = cursor.fetchone()
					nm = name
					pwd = password
					eml = email
					mb = mobile
					st = state
					ct = city

					search_enter_data.delete(0,END)
					tree.delete(*tree.get_children())
					nm.delete(0,END)
					pwd.delete(0,END)
					eml.delete(0,END)
					mb.delete(0,END)
					st.delete(0,END)
					ct.delete(0,END)

					search_enter_data.insert(0,search_cust_data)
					tree.insert('',END,values=res)
					nm.insert(0,res[1])
					pwd.insert(0,res[2])
					eml.insert(0,res[3])
					mb.insert(0,res[4])
					st.insert(0,res[5])
					ct.insert(0,res[6])

			search_data = Combobox(labelframe,width=20,font='verdena 12', values=list_options,state='r')
			search_data.place(x=480,y=20)
			search_data.set(f"Select Customer {cmb}")
			search_button = Button(labelframe,text='Search',width=10,font='verdena 12',fg='black',bg='lightyellow',activebackground='lightyellow', cursor="hand2",command=search)
			search_button.place(x=700,y=15)



	customer_options = Combobox(labelframe,width=10,values=['Id','Name','Email','Mobile','State','City','Customer Id'],font='verdena 12',state='r')
	customer_options.place(x=200,y=20)
	customer_options.set("Select")
	customer_options.bind('<<ComboboxSelected>>',selected_customer_options)

	Label(labelframe,text='Search Customer', width=15,font='verdena 12 bold',fg='white',bg='#5453a6').place(x=320,y=20)


	search_enter_data = Entry(labelframe,width=20,font='verdena 12')
	search_enter_data.place(x=480,y=20)

	def search():
		if search_enter_data.get() == "":
			messagebox.showerror("Error","Please Enter Customer Data")
			return False
		else:
			get_data = search_enter_data.get()
			tree.delete(*tree.get_children())
			cursor.execute("select * from customer_account where id=%s or name = %s or email = %s or mobile = %s or state=%s or city=%s or customer_id=%s ",(get_data,get_data,get_data,get_data,get_data,get_data,get_data))
			res = cursor.fetchone()

			name.delete(0,END)
			password.delete(0,END)
			email.delete(0,END)
			mobile.delete(0,END)
			state.delete(0,END)
			city.delete(0,END)

			if res is not None:
				name.insert(0,res[1])
				password.insert(0,res[2])
				email.insert(0,res[3])
				mobile.insert(0,res[4])
				state.insert(0,res[5])
				city.insert(0,res[6])
				tree.insert('',END,values=res)
			else:
				messagebox.showerror("Error","Sorry No Data Found")

	def clear():
		search_enter_data.delete(0,END)
		name.delete(0,END)
		password.delete(0,END)
		email.delete(0,END)
		mobile.delete(0,END)
		state.delete(0,END)
		city.delete(0,END)
		search_tree_data()

	def update():
		if search_enter_data.get() == "":
			messagebox.showerror("Error","Please enter customer Data")
			return False
		if name.get() == "":
			messagebox.showerror("Error","Please enter customer name")
			return False
		if password.get() == "":
			messagebox.showerror("Error","Please enter customer password")
			return False
		if email.get() == "":
			messagebox.showerror("Error","Please enter customer email")
			return False
		if mobile.get() == "":
			messagebox.showerror("Error","Please enter customer mobile number")
			return False
		if state.get() == "":
			messagebox.showerror("Error","Please enter customer state")
			return False
		if city.get() == "":
			messagebox.showerror("Error","Please enter customer city")
			return False

		else:
			msg = messagebox.askquestion("Message","Are you sure want to update your customer data ?")
			if msg == "yes":
				get_data = search_enter_data.get()
				cursor.execute("select * from customer_account where name = %s or email = %s or mobile = %s or state=%s or city=%s ",(get_data,get_data,get_data,get_data,get_data))
				res = cursor.fetchone()
				if res is not None:
					cursor.execute("update customer_account set name=%s, password=%s,email=%s,mobile=%s,state=%s,city=%s where id=%s ",(name.get(),password.get(),email.get(),mobile.get(),state.get(),city.get(),res[0]))

					cursor.execute("update customer_login set name=%s, password=%s,email=%s,mobile=%s where customer_id=%s ",(name.get(),password.get(),email.get(),mobile.get(),res[7]))
					if conn.commit():
						pass

					cursor.execute("update customer_login set name=%s, password=%s,email=%s,mobile=%s where email=%s and password=%s ",(name.get(),password.get(),email.get(),mobile.get(),email.get(),password.get()))

					if conn.commit():
						pass
					messagebox.showinfo("Sucess","Data updated sucessfully")
					name.delete(0,END)
					password.delete(0,END)
					email.delete(0,END)
					mobile.delete(0,END)
					state.delete(0,END)
					city.delete(0,END)
					search_tree_data()

				else:
					messagebox.showerror("Error","Data is not Found so it is not updated")

	def delete_data():
		if search_enter_data.get() == "":
			messagebox.showerror("Error","Please enter customer Data")
			return False
		if name.get() == "":
			messagebox.showerror("Error","Please enter customer name")
			return False
		if password.get() == "":
			messagebox.showerror("Error","Please enter customer password")
			return False
		if email.get() == "":
			messagebox.showerror("Error","Please enter customer email")
			return False
		if mobile.get() == "":
			messagebox.showerror("Error","Please enter customer mobile number")
			return False
		if state.get() == "":
			messagebox.showerror("Error","Please enter customer state")
			return False
		if city.get() == "":
			messagebox.showerror("Error","Please enter customer city")
			return False

		else:
			msg = messagebox.askquestion("Message","Are you sure want to delete your customer data ?")
			if msg == "yes":
				get_data = search_enter_data.get()
				cursor.execute("select * from customer_account where id=%s or name = %s or email = %s or mobile = %s or state=%s or city=%s or customer_id=%s ",(get_data,get_data,get_data,get_data,get_data,get_data,get_data))
				res = cursor.fetchone()
				if res is not None:
					cursor.execute("delete from customer_account where id=%s ",(res[0],))
					if conn.commit():
						pass
					messagebox.showinfo("Sucess","Data delete sucessfully")
				
					name.delete(0,END)
					password.delete(0,END)
					email.delete(0,END)
					mobile.delete(0,END)
					state.delete(0,END)
					city.delete(0,END)
					search_tree_data()

				else:
					messagebox.showerror("Error","Data is not Found so it is not updated")


	search_button = Button(labelframe,text='Search',width=10,font='verdena 12',fg='black',bg='lightyellow',activebackground='lightyellow', cursor="hand2",command=search)
	search_button.place(x=700,y=15)


	Label(frame,text='Customer Details', width=100,bg='#5453a6',fg='white',font='verdena 12 bold').place(x=0,y=100)

	Label(frame,text='Name',fg='White',bg='#5453a6',font='verdena 12').place(x=5,y=150)
	name = Entry(frame,font='verdena 12',width=20,textvariable=StringVar())
	name.place(x=100,y=150)

	Label(frame,text='Password',fg='White',bg='#5453a6',font='verdena 12').place(x=5,y=200)
	password = Entry(frame,font='verdena 12',width=20,textvariable=StringVar())
	password.place(x=100,y=200)

	Label(frame,text='Email',fg='White',bg='#5453a6',font='verdena 12').place(x=5,y=250)
	email = Entry(frame,font='verdena 12',width=20,textvariable=StringVar())
	email.place(x=100,y=250)

	Label(frame,text='Mobile',fg='White',bg='#5453a6',font='verdena 12').place(x=400,y=150)
	mobile = Entry(frame,font='verdena 12',width=20,textvariable=StringVar())
	mobile.place(x=500,y=150)

	Label(frame,text='State',fg='White',bg='#5453a6',font='verdena 12').place(x=400,y=200)
	state = Entry(frame,font='verdena 12',width=20,textvariable=StringVar())
	state.place(x=500,y=200)

	Label(frame,text='City/Address',fg='White',bg='#5453a6',font='verdena 12').place(x=400,y=250)
	city = Entry(frame,font='verdena 12',width=20,textvariable=StringVar())
	city.place(x=500,y=250)

	clear_button = Button(frame,text='Clear', width=10,fg='White',bg='Blue',font='verdena 12',activebackground='Blue',activeforeground='white',cursor='hand2',command=clear).place(x=800,y=150)

	update_button = Button(frame,text='Update', width=10,fg='White',bg='orange',font='verdena 12',activebackground='orange',activeforeground='white',cursor='hand2',command=update).place(x=800,y=200)

	delete_button = Button(frame,text='Delete', width=10,fg='White',bg='red',font='verdena 12',activebackground='red',activeforeground='white',cursor='hand2',command=delete_data).place(x=800,y=250)

	frame3 = Frame(frame2,width=1130,height=370,bg='white')
	frame3.place(x=10,y=385)

	Label(frame2,text='All Customers Details',bg='white',width=110,font='verdena 12 bold',padx=12).place(x=10,y=360)

	def search_tree_data():
		cursor.execute("select * from customer_account ")
		tree.delete(*tree.get_children())
		result = cursor.fetchall()
		for res in result:
			tree.insert('',END,values=res)

	def onclick_tree_data(event):
		try:
			item = tree.focus()
			values = tree.item(item,'values')

			search_enter_data.delete(0,END)
			name.delete(0,END)
			password.delete(0,END)
			email.delete(0,END)
			mobile.delete(0,END)
			state.delete(0,END)
			city.delete(0,END)

			search_enter_data.insert(0,values[1])
			name.insert(0,values[1])
			password.insert(0,values[2])
			email.insert(0,values[3])
			mobile.insert(0,values[4])
			state.insert(0,values[5])
			city.insert(0,values[6])
		except:
			pass

	yscroll = Scrollbar(frame3,orient='vertical')
	yscroll.pack(side='right',fill='y')

	tree = ttk.Treeview(frame3, height=15,columns=('Id','Name','Password','Email','Mobile','State','City','Customer Id'),yscrollcommand=yscroll.set)
	tree.heading('Id',text='Id')
	tree.heading('Name',text='Name')
	tree.heading('Password',text='Password')
	tree.heading('Email',text='Email')
	tree.heading('Mobile',text='Mobile')
	tree.heading('State',text='State')
	tree.heading('City',text='City/Address')
	tree.heading('Customer Id',text='Customer Id')

	tree['show'] = 'headings'
	tree.column('Id',width=10)
	tree.column('Password',width=100)
	tree.column('Mobile',width=100)
	tree.column('State',width=150)
	tree.column('City',width=260)
	tree.column('Customer Id',width=100)
	tree.pack(fill='both',expand=1)

	yscroll.config(command=tree.yview)

	search_tree_data()
	tree.bind('<ButtonRelease-1>',onclick_tree_data)

	root7.mainloop()

############################ End of Seventh Window #########################

def cars():
	root8 = Tk()
	root8.title("Cars")
	root8.geometry("1350x750+0+0")
	root8.resizable(0,0)
	root8.config(bg='white')
	icon = PhotoImage(file='car.png')
	root8.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root8.destroy()
		profile()

	def dashboard_window():
		root8.destroy()
		dashboard()

	def car_window():
		root8.destroy()
		cars()

	def order_window():
		root8.destroy()
		orders()

	def customer_window():
		root8.destroy()
		customer()

	def customer_contact_window():
		root8.destroy()
		customer_contact()

	def customer_feedback_window():
		root8.destroy()
		customer_feedback()

	def logout_page():
		root8.destroy()
		logout()

	frame1 = Frame(root8,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root8,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)

	cursor.execute("select * from account where device_name=%s ",(socket.gethostname(),))
	res = cursor.fetchone()
	Label(frame2,text=f'Welcome {res[1]}', font='verdena 12 bold',width=100, height=2,bg='#5453a6',fg='white',padx=75).place(x=0,y=0)

	labelframe1 = LabelFrame(frame2,width=1120,height=50,bg='#5453a6')
	labelframe1.place(x=20,y=50)

	def selected_customer_options(event):
		cmb = search_cars_dropdown.get()

		if cmb!="Select Cars Data":
			if cmb == "Car Id":
				cmb = 'id'
			if cmb == "Car Name":
				cmb = 'name'
			if cmb=='Car Price':
				cmb = 'car_price'
			if cmb=='Model Date':
				cmb = 'model_date'
			if cmb =='Car Type':
				cmb='car_type'
			if cmb=='Car Capicity':
				cmb = 'car_capicity'
			if cmb == 'Car Brand':
				cmb = 'car_brand'
			if cmb == 'Car Features':
				cmb='car_features'

			cursor.execute(f"select {cmb} from cars_data")
			res = cursor.fetchall()

			list_options = [item[0] for item in res]

			def dropdown_data_fetch(event):
				selected_data = car_data_dropdown.get()

				if selected_data!=f"Select Car {cmb}":
					search_enter_data.delete(0,'end')
					search_enter_data.insert(0,selected_data)

				else:
					messagebox.showerror("Error",'Please select car data')
					return False
				

			car_data_dropdown = Combobox(labelframe1, width=30,font='verdena 12',values=list_options,state='r')
			car_data_dropdown.set(f"Select Car {cmb}")
			car_data_dropdown.place(x=630,y=10)
			car_data_dropdown.bind('<<ComboboxSelected>>',dropdown_data_fetch)

			def search():
				get_data = car_data_dropdown.get()
				if get_data == f"Select Car {cmb}":
					messagebox.showerror("Error","Please select car data")
					return False
				else:
					car_id.delete(0,'end')
					car_name.delete(0,'end')
					car_price.delete(0,'end')
					model_date.delete(0,'end')
					car_type.set("Select Car Type")
					car_capicity.set("Select Car Capicity")
					car_brand.set("Select Car Brand")
					car_features.set("Select Car Features")

					image = Image.open('car.jpg')
					image = image.resize((50,50))
					car_image = ImageTk.PhotoImage(image)

					car_img1.config(image=car_image)
					car_img1.image = car_image

					car_img2.config(image=car_image)
					car_img2.image = car_image

					car_img3.config(image=car_image)
					car_img3.image = car_image

					car_img4.config(image=car_image)
					car_img4.image = car_image

					car_img5.config(image=car_image)
					car_img5.image = car_image

					car_img6.config(image=car_image)
					car_img6.image = car_image										

					cursor.execute("select * from cars_data where id=%s or name=%s or car_price=%s or model_date=%s or car_type=%s or car_capicity=%s or car_brand=%s or car_features=%s ",(get_data,get_data,get_data,get_data,get_data,get_data,get_data,get_data))
					res = cursor.fetchone()
					if res is not None:
						car_id.insert(0,res[0])
						car_name.insert(0,res[1])
						car_price.insert(0,res[2])
						model_date.insert(0,res[3])
						car_type.set(res[4])
						car_capicity.set(res[5])
						car_brand.set(res[6])
						car_features.set(res[7])

						if car_features.get() == "1. Air Condional + Top Roof Open" or car_features.get()=="2. Car Controlling Through Phone" or car_features.get() == "4. Feature 1 and Feature 2" or car_features.get() == "5. Feature 2 and Feature 3" or car_features.get() == "6. Feature 1 and Feature 3" :
							car_features.config(width=28)

						if res[8]!="" or res[9]!="" or res[10]!="" or res[11]!="" or res[12]!="" or res[13]!="" :
							image1 = Image.open(res[8])
							image1 = image1.resize((50,50))
							car_imge1 = ImageTk.PhotoImage(image1)

							car_img1.config(image=car_imge1)
							car_img1.image = car_imge1

							image2 = Image.open(res[9])
							image2 = image2.resize((50,50))
							car_imge2 = ImageTk.PhotoImage(image2)


							car_img2.config(image=car_imge2)
							car_img2.image = car_imge2

							image3 = Image.open(res[10])
							image3 = image3.resize((50,50))
							car_imge3 = ImageTk.PhotoImage(image3)

							car_img3.config(image=car_imge3)
							car_img3.image = car_imge3

							image4 = Image.open(res[11])
							image4 = image4.resize((50,50))
							car_imge4 = ImageTk.PhotoImage(image4)

							car_img4.config(image=car_imge4)
							car_img4.image = car_imge4

							image5 = Image.open(res[12])
							image5 = image5.resize((50,50))
							car_imge5 = ImageTk.PhotoImage(image5)

							car_img5.config(image=car_imge5)
							car_img5.image = car_imge5

							image6 = Image.open(res[13])
							image6 = image6.resize((50,50))
							car_imge6 = ImageTk.PhotoImage(image6)

							car_img6.config(image=car_imge6)
							car_img6.image = car_imge6

						save_button.config(state='disable')
						update_button.config(state='normal')
						delete_button.config(state='normal')

						car_image1.config(state='normal')
						car_image2.config(state='normal')
						car_image3.config(state='normal')
						car_image4.config(state='normal')
						car_image5.config(state='normal')
						car_image6.config(state='normal')

					else:
						messagebox.showerror("Error","Sorry No Data Found")

			search_button = Button(labelframe1,text='Search', width=10,font='verdena 12',bg='lightyellow',cursor='hand2',activebackground='lightyellow',command=search)
			search_button.place(x=950,y=5)

	Label(labelframe1,text='Select Cars Data',font='verdena 12 bold',bg='#5453a6',fg='white').place(x=20,y=10)
	search_cars_dropdown = Combobox(labelframe1,width=25,font='verdena 12',values=['Car Id','Car Name','Car Price','Model Date','Car Type','Car Capicity','Car Brand','Car Features'],state='r')
	search_cars_dropdown.set("Select Cars Data")
	search_cars_dropdown.place(x=170,y=10)
	search_cars_dropdown.bind('<<ComboboxSelected>>',selected_customer_options)

	Label(labelframe1,text='Search Cars',font='verdena 12 bold',fg='white',bg='#5453a6').place(x=500,y=10)
	search_enter_data = Entry(labelframe1,width=30,font='verdena 12')
	search_enter_data.place(x=630,y=10)

	def search():
		get_data = search_enter_data.get()
		if search_enter_data.get() == "":
			messagebox.showerror("Error","Please enter car data")
			return False
		else:
			car_id.delete(0,'end')
			car_name.delete(0,'end')
			car_price.delete(0,'end')
			model_date.delete(0,'end')
			car_type.set("Select Car Type")
			car_capicity.set("Select Car Capicity")
			car_brand.set("Select Car Brand")
			car_features.set("Select Car Features")

			image = Image.open('car.jpg')
			image = image.resize((50,50))
			car_image = ImageTk.PhotoImage(image)

			car_img1.config(image=car_image)
			car_img1.image = car_image

			car_img2.config(image=car_image)
			car_img2.image = car_image

			car_img3.config(image=car_image)
			car_img3.image = car_image

			car_img4.config(image=car_image)
			car_img4.image = car_image

			car_img5.config(image=car_image)
			car_img5.image = car_image

			car_img6.config(image=car_image)
			car_img6.image = car_image										

			cursor.execute("select * from cars_data where id=%s or name=%s or car_price=%s or model_date=%s or car_type=%s or car_capicity=%s or car_brand=%s or car_features=%s ",(get_data,get_data,get_data,get_data,get_data,get_data,get_data,get_data))
			res = cursor.fetchone()
			if res is not None:
				car_id.insert(0,res[0])
				car_name.insert(0,res[1])
				car_price.insert(0,res[2])
				model_date.insert(0,res[3])
				car_type.set(res[4])
				car_capicity.set(res[5])
				car_brand.set(res[6])
				car_features.set(res[7])
				if car_features.get() == "1. Air Condional + Top Roof Open" or car_features.get()=="2. Car Controlling Through Phone" or car_features.get() == "4. Feature 1 and Feature 2" or car_features.get() == "5. Feature 2 and Feature 3" or car_features.get() == "6. Feature 1 and Feature 3" :
					car_features.config(width=28)

				if res[8]!="" or res[9]!="" or res[10]!="" or res[11]!="" or res[12]!="" or res[13]!="" :
					image1 = Image.open(res[8])
					image1 = image1.resize((50,50))
					car_imge1 = ImageTk.PhotoImage(image1)

					car_img1.config(image=car_imge1)
					car_img1.image = car_imge1

					image2 = Image.open(res[9])
					image2 = image2.resize((50,50))
					car_imge2 = ImageTk.PhotoImage(image2)


					car_img2.config(image=car_imge2)
					car_img2.image = car_imge2

					image3 = Image.open(res[10])
					image3 = image3.resize((50,50))
					car_imge3 = ImageTk.PhotoImage(image3)

					car_img3.config(image=car_imge3)
					car_img3.image = car_imge3

					image4 = Image.open(res[11])
					image4 = image4.resize((50,50))
					car_imge4 = ImageTk.PhotoImage(image4)

					car_img4.config(image=car_imge4)
					car_img4.image = car_imge4

					image5 = Image.open(res[12])
					image5 = image5.resize((50,50))
					car_imge5 = ImageTk.PhotoImage(image5)

					car_img5.config(image=car_imge5)
					car_img5.image = car_imge5

					image6 = Image.open(res[13])
					image6 = image6.resize((50,50))
					car_imge6 = ImageTk.PhotoImage(image6)

					car_img6.config(image=car_imge6)
					car_img6.image = car_imge6

				save_button.config(state='disable')
				update_button.config(state='normal')
				delete_button.config(state='normal')

				car_image1.config(state='normal')
				car_image2.config(state='normal')
				car_image3.config(state='normal')
				car_image4.config(state='normal')
				car_image5.config(state='normal')
				car_image6.config(state='normal')

			else:
				messagebox.showerror("Error","Sorry No Data Found")

	search_button = Button(labelframe1,text='Search', width=10,font='verdena 12',bg='lightyellow',cursor='hand2',activebackground='lightyellow',command=search)
	search_button.place(x=950,y=5)

	labelframe2 = LabelFrame(frame2,width=1120,height=350,bg='#5453a6')
	labelframe2.place(x=20,y=100)

	Label(labelframe2,text='Car Details',fg='white',font='verdena 12 bold',bg='#5453a6').place(x=500,y=10)

	Label(labelframe2,text='Car Id',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=50)
	car_id = Entry(labelframe2,width=20,font='verdena 12')
	car_id.place(x=120,y=50)

	Label(labelframe2,text='Car Name',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=100)
	car_name = Entry(labelframe2,width=20,font='verdena 12')
	car_name.place(x=120,y=100)

	Label(labelframe2,text='Car Price',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=150)
	car_price = Entry(labelframe2,width=20,font='verdena 12')
	car_price.insert(0,"₹")
	car_price.place(x=120,y=150)
	
	Label(labelframe2,text='Model Date',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=200)
	model_date = Entry(labelframe2,width=20,font='verdena 12')
	model_date.place(x=120,y=200)

	
	cursor.execute("select * from car_type_values where not value = '' ")
	result = cursor.fetchall()

	cartype = [item[1] for item in result]


	Label(labelframe2,text='Car Type',font='verdena 12',bg='#5453a6',fg='white').place(x=400,y=50)
	car_type = Combobox(labelframe2,width=20,font='verdena 12',values=cartype,state='r')
	car_type.place(x=500,y=50)
	car_type.set("Select Car Type")

	Label(labelframe2,text='Car Capicity',font='verdena 12',bg='#5453a6',fg='white').place(x=400,y=100)
	car_capicity = Combobox(labelframe2,width=20,font='verdena 12',values=['4','6','8'],state='r')
	car_capicity.place(x=500,y=100)
	car_capicity.set("Select Car Capicity")

	cursor.execute("select * from car_brand_values where not value = '' ")
	result = cursor.fetchall()

	carbrand = [item[1] for item in result]

	Label(labelframe2,text='Car Brand',font='verdena 12',bg='#5453a6',fg='white').place(x=400,y=150)
	car_brand = Combobox(labelframe2,width=20,font='verdena 12',values=carbrand,state='r')
	car_brand.place(x=500,y=150)
	car_brand.set("Select Car Brand")

	cursor.execute("select * from car_feature_values ")
	result = cursor.fetchall()
	carfeature = [item[1] for item in result]

	Label(labelframe2,text='Car Features',font='verdena 12',bg='#5453a6',fg='white').place(x=400,y=200)
	car_features = Combobox(labelframe2,width=20,font='verdena 12',values=carfeature,state='r')
	car_features.place(x=500,y=200)
	car_features.set("Select Car Features")
	def onclick_features(event):

		features = car_features.get()
		if features!="Select Car Features":
			if features == "1. Air Condional + Top Roof Open" or features == "2. Car Controlling Through Phone" or features == "4. Feature 1 and Feature 2" or features == "5. Feature 2 and Feature 3" or features == "6. Feature 1 and Feature 3":
				car_features.config(width=28)
			else:
				car_features.config(width=20)				

	car_features.bind('<<ComboboxSelected>>',onclick_features)

	image = Image.open('car.jpg')
	image = image.resize((50,50))
	car_image = ImageTk.PhotoImage(image)

	
	car_img1 = Label(labelframe2,image=car_image)
	car_img1.place(x=750,y=50)
	car_img2 = Label(labelframe2,image=car_image)
	car_img2.place(x=850,y=50)
	car_img3 = Label(labelframe2,image=car_image)
	car_img3.place(x=950,y=50)

	car_img4 = Label(labelframe2,image=car_image)
	car_img4.place(x=750,y=150)
	car_img5 = Label(labelframe2,image=car_image)
	car_img5.place(x=850,y=150)
	car_img6 = Label(labelframe2,image=car_image)
	car_img6.place(x=950,y=150)

	car_images = ['','','','','','']

	def open_image1():
		try:
			global folder1
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG File","*.png"),("JPG File","*.jpg")))
			img = Image.open(filename)
			img = img.resize((50,50))
			image = ImageTk.PhotoImage(img)
			car_img1.config(image=image)
			car_img1.image = image

			images = (Image.open(filename))
			folder1 = f"car_images/{filename.split("/")[-1]}"
			images.save(folder1)

			car_images[0] = folder1

		except Exception as e:
			pass

	def open_image2():
		try:
			global folder2
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG File","*.png"),("JPG File","*.jpg")))
			img = Image.open(filename)
			img = img.resize((50,50))
			image = ImageTk.PhotoImage(img)
			car_img2.config(image=image)
			car_img2.image = image

			images = (Image.open(filename))
			folder2 = f"car_images/{filename.split("/")[-1]}"
			images.save(folder2)

			car_images[1] = folder2

			

		except:
			pass


	def open_image3():
		try:
			global folder3
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG File","*.png"),("JPG File","*.jpg")))
			img = Image.open(filename)
			img = img.resize((50,50))
			image = ImageTk.PhotoImage(img)
			car_img3.config(image=image)
			car_img3.image = image

			images = (Image.open(filename))
			folder3 = f"car_images/{filename.split("/")[-1]}"
			images.save(folder3)

			car_images[2] = folder3


		except:
			pass

	def open_image4():
		try:
			global folder4
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG File","*.png"),("JPG File","*.jpg")))
			img = Image.open(filename)
			img = img.resize((50,50))
			image = ImageTk.PhotoImage(img)
			car_img4.config(image=image)
			car_img4.image = image

			images = (Image.open(filename))
			folder4 = f"car_images/{filename.split("/")[-1]}"
			images.save(folder4)

			car_images[3] = folder4

		except:
			pass

	def open_image5():
		try:
			global folder5
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG File","*.png"),("JPG File","*.jpg")))
			img = Image.open(filename)
			img = img.resize((50,50))
			image = ImageTk.PhotoImage(img)
			car_img5.config(image=image)
			car_img5.image = image

			images = (Image.open(filename))
			folder5 = f"car_images/{filename.split("/")[-1]}"
			images.save(folder5)

			car_images[4] = folder5


		except:
			pass

	def open_image6():
		try:
			global folder6
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG File","*.png"),("JPG File","*.jpg")))
			img = Image.open(filename)
			img = img.resize((50,50))
			image = ImageTk.PhotoImage(img)
			car_img6.config(image=image)
			car_img6.image = image

			images = (Image.open(filename))
			folder6 = f"car_images/{filename.split("/")[-1]}"
			images.save(folder6)

			car_images[5] = filename.split("/")[-1]


		except:
			pass

	car_image1 = Button(labelframe2,text='Select Car Image 1',bg='mediumblue',font='verdena 12',fg='white',cursor='hand2',command=open_image1,activebackground='mediumblue',activeforeground='white',state='disable')
	car_image1.place(x=550,y=250)

	car_image2 = Button(labelframe2,text='Select Car Image 2',bg='mediumblue',font='verdena 12',fg='white',cursor='hand2',command=open_image2,activebackground='mediumblue',activeforeground='white',state='disable')
	car_image2.place(x=750,y=250)

	car_image3 = Button(labelframe2,text='Select Car Image 3',bg='mediumblue',font='verdena 12',fg='white',cursor='hand2',command=open_image3,activebackground='mediumblue',activeforeground='white',state='disable')
	car_image3.place(x=950,y=250)

	car_image4 = Button(labelframe2,text='Select Car Image 4',bg='mediumblue',font='verdena 12',fg='white',cursor='hand2',command=open_image4,activebackground='mediumblue',activeforeground='white',state='disable')
	car_image4.place(x=550,y=300)

	car_image5 = Button(labelframe2,text='Select Car Image 5',bg='mediumblue',font='verdena 12',fg='white',cursor='hand2',command=open_image5,activebackground='mediumblue',activeforeground='white',state='disable')
	car_image5.place(x=750,y=300)

	car_image6 = Button(labelframe2,text='Select Car Image 6',bg='mediumblue',font='verdena 12',fg='white',cursor='hand2',command=open_image6,activebackground='mediumblue',activeforeground='white',state='disable')
	car_image6.place(x=950,y=300)

	def save():
		cnm = car_name.get()
		cpr = car_price.get()
		md = model_date.get()
		ctp = car_type.get()
		cap = car_capicity.get()
		brd = car_brand.get()
		feature = car_features.get()



		if cnm == "":
			messagebox.showerror("Error","Please write car name")
			return False
		if cpr=="" or cpr=="₹":
			messagebox.showerror("Error","Please write car price")
			return False
		if md == "" or len(md) < 3:
			messagebox.showerror("Error","Please write car model date")
			return False
		if ctp == "Select Car Type":
			messagebox.showerror("Error","Please select car type")
			return False
		if cap=="Select Car Capicity":
			messagebox.showerror("Error","Please select car capicity")
			return False
		if brd=="Select Car Brand":
			messagebox.showerror("Error","Please select car brand")
			return False
		if feature=="Select Car Features":
			messagebox.showerror("Error","Please select car features")
			return False

		try:
			open_image1()
			open_image2()
			open_image3()
			open_image4()
			open_image5()
			open_image6()
				
		except:
			messagebox.showerror("Error","Please select image file")
		
		else:
			#cursor.execute("select * from cars_data where name=%s ",(cnm,))
			#res = cursor.fetchone()
			#if res is not None:
				#messagebox.showerror("Error","This car is already present")

			#else:
				cursor.execute("insert into cars_data (name,car_price,model_date,car_type,car_capicity,car_brand,car_features,car_image1,car_image2, car_image3, car_image4, car_image5, car_image6,device_name,time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(cnm,cpr,md,ctp,cap,brd,feature,folder1, folder2, folder3, folder4, folder5, folder6,socket.gethostname(),datetime.now().strftime("%d-%m-%y %H:%M:%S")))

				if conn.commit():
					pass
				car_name.delete(0,'end')
				car_price.delete(0,'end')
				car_price.insert(0,"₹")
				model_date.delete(0,'end')
				car_type.set("Select Car Type")
				car_capicity.set("Select Car Capicity")
				car_brand.set("Select Car Brand")
				car_features.set("Select Car Features")

				image = Image.open('car.jpg')
				image = image.resize((50,50))
				car_image = ImageTk.PhotoImage(image)

				car_img1.config(image=car_image)
				car_img1.image = car_image

				car_img2.config(image=car_image)
				car_img2.image = car_image

				car_img3.config(image=car_image)
				car_img3.image = car_image

				car_img4.config(image=car_image)
				car_img4.image = car_image

				car_img5.config(image=car_image)
				car_img5.image = car_image

				car_img6.config(image=car_image)
				car_img6.image = car_image										

				messagebox.showinfo("Sucess","Data inserted sucessfully")




	def update():
		cid = car_id.get()
		cnm = car_name.get()
		cpr = car_price.get()
		md = model_date.get()
		ctp = car_type.get()
		cap = car_capicity.get()
		brd = car_brand.get()
		feature = car_features.get()

		cursor.execute("select * from cars_data where id=%s ",(cid,))
		res = cursor.fetchone()

		if car_images[0] == "":
			car_images[0] = (res[8])

		if car_images[1] == "":
			car_images[1] = (res[9])

		if car_images[2] == "":
			car_images[2] = (res[10])

		if car_images[3] == "":
			car_images[3] = (res[11])

		if car_images[4] == "":
			car_images[4] = (res[12])

		if car_images[5] == "":
			car_images[5] = (res[13])
	
		
			
		if cid == "":
			messagebox.showerror("Error","Please write car id")
			return False
		if cnm == "":
			messagebox.showerror("Error","Please write car name")
			return False
		if cpr=="" or cpr=="₹":
			messagebox.showerror("Error","Please write car price")
			return False
		if md == "" or len(md) < 3:
			messagebox.showerror("Error","Please write car model date")
			return False
		if ctp == "Select Car Type":
			messagebox.showerror("Error","Please select car type")
			return False
		if cap=="Select Car Capicity":
			messagebox.showerror("Error","Please select car capicity")
			return False
		if brd=="Select Car Brand":
			messagebox.showerror("Error","Please select car brand")
			return False
		if feature=="Select Car Features":
			messagebox.showerror("Error","Please select car features")
			return False



		else:
			cursor.execute("select * from cars_data where id=%s ",(cid,))
			res = cursor.fetchone()

			
			
			if res is not None:
				cursor.execute("update cars_data set name=%s,car_price=%s,model_date=%s,car_type=%s,car_capicity=%s,car_brand=%s,car_features=%s,car_image1=%s, car_image2=%s, car_image3=%s, car_image4=%s, car_image5=%s, car_image6=%s where id=%s ",(cnm,cpr,md,ctp,cap,brd,feature, car_images[0], car_images[1], car_images[2], car_images[3], car_images[4], car_images[5],res[0]))
				if conn.commit():
					pass
				car_id.delete(0,'end')
				car_name.delete(0,'end')
				car_price.delete(0,'end')
				car_price.insert(0,"₹")
				model_date.delete(0,'end')
				car_type.set("Select Car Type")
				car_capicity.set("Select Car Capicity")
				car_brand.set("Select Car Brand")
				car_features.set("Select Car Features")
				car_features.config(width=20)

				image = Image.open('car.jpg')
				image = image.resize((50,50))
				car_image = ImageTk.PhotoImage(image)

				car_img1.config(image=car_image)
				car_img1.image = car_image

				car_img2.config(image=car_image)
				car_img2.image = car_image

				car_img3.config(image=car_image)
				car_img3.image = car_image

				car_img4.config(image=car_image)
				car_img4.image = car_image

				car_img5.config(image=car_image)
				car_img5.image = car_image

				save_button.config(state='normal')
				update_button.config(state='disable')
				delete_button.config(state='disable')

				car_image1.config(state='disable')
				car_image2.config(state='disable')
				car_image3.config(state='disable')
				car_image4.config(state='disable')
				car_image5.config(state='disable')
				car_image6.config(state='disable')


				car_img6.config(image=car_image)
				car_img6.image = car_image										

				messagebox.showinfo("Sucess","Data updated sucessfully")

			else:
				messagebox.showerror("Error","Sorry data is not updated")

	def delete():
		cid = car_id.get()
		cnm = car_name.get()
		cpr = car_price.get()
		md = model_date.get()
		ctp = car_type.get()
		cap = car_capicity.get()
		brd = car_brand.get()
		feature = car_features.get()

		if cid == "":
			messagebox.showerror("Error","Please write car id")
			return False
		if cnm == "":
			messagebox.showerror("Error","Please write car name")
			return False
		if cpr=="" or cpr=="₹":
			messagebox.showerror("Error","Please write car price")
			return False
		if md == "" or len(md) < 3:
			messagebox.showerror("Error","Please write car model date")
			return False
		if ctp == "Select Car Type":
			messagebox.showerror("Error","Please select car type")
			return False
		if cap=="Select Car Capicity":
			messagebox.showerror("Error","Please select car capicity")
			return False
		if brd=="Select Car Brand":
			messagebox.showerror("Error","Please select car brand")
			return False
		if feature=="Select Car Features":
			messagebox.showerror("Error","Please select car features")
			return False

		else:
			cursor.execute("select id from cars_data where id=%s ",(cid,))
			res = cursor.fetchone()
			if res is not None:
				msg = messagebox.askquestion("Message","Are you sure want to delete the car data ?")
				if msg == "yes":
					cursor.execute("delete from cars_data where id=%s ",(res[0],))
					if conn.commit():
						pass
					car_id.delete(0,'end')
					car_name.delete(0,'end')
					car_price.delete(0,'end')
					car_price.insert(0,"₹")
					model_date.delete(0,'end')
					car_type.set("Select Car Type")
					car_capicity.set("Select Car Capicity")
					car_brand.set("Select Car Brand")
					car_features.set("Select Car Features")
					car_features.config(width=20)

					image = Image.open('car.jpg')
					image = image.resize((50,50))
					car_image = ImageTk.PhotoImage(image)

					car_img1.config(image=car_image)
					car_img1.image = car_image

					car_img2.config(image=car_image)
					car_img2.image = car_image

					car_img3.config(image=car_image)
					car_img3.image = car_image

					car_img4.config(image=car_image)
					car_img4.image = car_image

					car_img5.config(image=car_image)
					car_img5.image = car_image

					save_button.config(state='normal')
					update_button.config(state='disable')
					delete_button.config(state='disable')

					car_image1.config(state='disable')
					car_image2.config(state='disable')
					car_image3.config(state='disable')
					car_image4.config(state='disable')
					car_image5.config(state='disable')
					car_image6.config(state='disable')


					car_img6.config(image=car_image)
					car_img6.image = car_image										

					messagebox.showinfo("Sucess","Data delete sucessfully")

			else:
				messagebox.showerror("Error","Sorry data is not delete")

	def clear():
		car_id.delete(0,'end')
		car_name.delete(0,'end')
		car_price.delete(0,'end')
		car_price.insert(0,"₹")
		model_date.delete(0,'end')
		car_type.set("Select Car Type")
		car_capicity.set("Select Car Capicity")
		car_brand.set("Select Car Brand")
		car_features.set("Select Car Features")
		car_features.config(width=20)									


		image = Image.open('car.jpg')
		image = image.resize((50,50))
		car_image = ImageTk.PhotoImage(image)

		car_img1.config(image=car_image)
		car_img1.image = car_image

		car_img2.config(image=car_image)
		car_img2.image = car_image

		car_img3.config(image=car_image)
		car_img3.image = car_image

		car_img4.config(image=car_image)
		car_img4.image = car_image

		car_img5.config(image=car_image)
		car_img5.image = car_image

		save_button.config(state='normal')
		update_button.config(state='disable')
		delete_button.config(state='disable')

		car_image1.config(state='disable')
		car_image2.config(state='disable')
		car_image3.config(state='disable')
		car_image4.config(state='disable')
		car_image5.config(state='disable')
		car_image6.config(state='disable')


		car_img6.config(image=car_image)
		car_img6.image = car_image	


	save_button = Button(labelframe2,text='Save', width=10,bg='steelblue',fg='white',font='verdena 12',cursor='hand2',activebackground='steelblue',activeforeground='white',command=save)
	save_button.place(x=20,y=300)

	update_button = Button(labelframe2,text='Update', width=10,bg='greenyellow',fg='white',font='verdena 12',cursor='hand2',activebackground='greenyellow',activeforeground='white',command=update,state='disable')
	update_button.place(x=150,y=300)

	delete_button = Button(labelframe2,text='Delete', width=10,bg='red',fg='white',font='verdena 12',cursor='hand2',activebackground='red',activeforeground='white',command=delete,state='disable')
	delete_button.place(x=280,y=300)

	clear_button = Button(labelframe2,text='Clear', width=10,bg='blue',fg='white',font='verdena 12',cursor='hand2',activebackground='blue',activeforeground='white',command=clear)
	clear_button.place(x=410,y=300)	

	frame3 = Frame(frame2,width=1120,height=280,bg='#5453a6')
	frame3.place(x=20,y=450)

	def graph():

		def vertical_bar_graph():
			conn = mysql.connector.connect(host='localhost',user='root',password='',database='shopping')
			cursor = conn.cursor()

			
			carsdata = []

			cursor.execute("select * from car_brand_values ")
			result = cursor.fetchall()
			data = [item[1] for item in result]
			
			query = "select count(*) from cars_data where car_brand = %s"
			
			for i in data:
				cursor = conn.cursor()
				cursor.execute(query, (i,))
				result = cursor.fetchall()

				cardata = [item[0] for item in result]
				carsdata.append(cardata[0])


			x = data
			y = carsdata
			plt.figure(figsize=(8,5))

			plt.bar(x,y,color='orange')
			plt.plot(x,y,marker='o', markersize=12,markerfacecolor='greenyellow',label='Available Cars')

			plt.xlabel('Car Brands')
			plt.ylabel('Available cars data')

			plt.get_current_fig_manager().window.geometry("+350+50")
			plt.get_current_fig_manager().window.title("Cars Statistics")
			plt.title("Car Statistics")


			plt.legend()
			plt.show()

		def horizintal_bar_graph():

			carsdata = []

			cursor = conn.cursor()

			cursor.execute("select * from car_brand_values")
			result = cursor.fetchall()
			data = [item[1] for item in result]

			for i in data:
				cursor = conn.cursor()
				cursor.execute("select count(*) from cars_data where car_brand=%s ",(i,))
				result = cursor.fetchall()
				cardata = [item[0] for item in result]
				carsdata.append(cardata[0])

			x = data
			y = carsdata

			plt.barh(x,y,color='#e41b17')

			plt.xlabel('Car Brands')
			plt.ylabel('Available cars data')

			plt.get_current_fig_manager().window.geometry("1100x550+200+50")
			plt.get_current_fig_manager().window.title("Cars Statistics")
			plt.title("Car Statistics")

			plt.show()

			pass

		def double_bar_graph():
			
			cursor = conn.cursor()

			cursor.execute("select * from car_brand_values ")
			result = cursor.fetchall()
			data = [item[1] for item in result]

			carsdata = []

			for i in data:
				cursor = conn.cursor()
				cursor.execute("select count(*) from cars_data where car_brand = %s ",(i,))
				result = cursor.fetchall()
				cardata = [item[0] for item in result]
				carsdata.append(cardata[0])

			x = data
			y = carsdata
			colors = ['#e30b5d','blue']
			plt.bar(x,y,color=colors)

			plt.xlabel('Car Brands')
			plt.ylabel('Available cars data')

			plt.get_current_fig_manager().window.geometry("1100x550+200+50")
			plt.get_current_fig_manager().window.title("Cars Statistics")
			plt.title("Car Statistics")

			plt.show()
			pass

		def pie_chart_graph():
			
			cursor = conn.cursor()

			cursor.execute("select * from car_brand_values ")
			result = cursor.fetchall()
			data = [item[1] for item in result]

			carsdata = []

			for i in data:
				cursor = conn.cursor()
				cursor.execute("select count(*) from cars_data where car_brand = %s ",(i,))
				result = cursor.fetchall()
				cardata = [item[0] for item in result]
				carsdata.append(cardata[0])

			x = data
			y = carsdata
			plt.figure(figsize=(8,5))

			plt.pie(y,labels=x,autopct='%2.0f%%', colors=['red','green','blue','yellow','steelblue','greenyellow','maroon'],textprops={'color':'black'})

			plt.xlabel('Car Brands')
			plt.ylabel('Available cars data')

			plt.get_current_fig_manager().window.geometry("+350+50")
			plt.get_current_fig_manager().window.title("Cars Statistics")
			plt.title("Car Statistics")


			
			plt.show()
			pass


		root = Toplevel(root8)
		root.geometry("1120x150+220+490")
		root.resizable(0,0)
		root.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root.iconphoto(False,icon)

		Label(root,text='View Statistics In Diffrent Types Of graphs',font='verdena 15 bold',fg='white',bg='#5453a6').place(x=350,y=10)

		Button(root,text='Vertical Bar Graph',font='verdena 12',bg='orange', fg='white',width=25,height=3,cursor='hand2',activebackground='orange',activeforeground='white',command=vertical_bar_graph).place(x=50,y=50)

		Button(root,text='Hozizontal Bar Graph',font='verdena 12',bg='#e41b17', fg='white',width=25,height=3,cursor='hand2',activebackground='#e41b17',activeforeground='white',command=horizintal_bar_graph).place(x=300,y=50)

		Button(root,text='Double Bar Graph',font='verdena 12',bg='#e30b5d', fg='white',width=25,height=3,cursor='hand2',activebackground='#e30b5d',activeforeground='white',command=double_bar_graph).place(x=550,y=50)


		Button(root,text='Pie Chart Graph',font='verdena 12',bg='darkblue', fg='white',width=20,height=3,cursor='hand2',activebackground='darkblue',activeforeground='white',command=pie_chart_graph).place(x=800,y=50)


		root.mainloop()


	def all_cars():
		webbrowser.open("localhost/shop/load.html")
		'''root1 = Toplevel(root8)
		root1.geometry("1130x620+210+80")
		root1.title("All cars data")
		root1.resizable(0,0)
		icon = PhotoImage(file='car.png')
		root1.iconphoto(False,icon)

		def on_scrollX(*args):
			canvas.xview(*args)
			canvas.update_idletasks()
			canvas.config(scrollregion = canvas.bbox("all"))


		def on_scrollY(*args):
			canvas.yview(*args)
			canvas.update_idletasks()
			canvas.config(scrollregion = canvas.bbox("all"))

		
		Label(root1,text='All Cars Details', width=100,bg='#5453a6',font='verdena 15 bold',fg='white',pady=12).pack()

		scrollbarX = Scrollbar(root1,orient='horizontal',command=on_scrollX)		
		scrollbarY = Scrollbar(root1,orient='vertical',command=on_scrollY)

		canvas = Canvas(root1,width=1090,height=480, bg='#5453a6',scrollregion=(0,0,600,800))
		on_scrollX()

		Label(root1,text='Car Id', width=10, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=10,y=60)

		Label(root1,text='Car Name', width=10, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=120,y=60)

		Label(root1,text='Car Price', width=10, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=230,y=60)

		Label(root1,text='Model Date', width=10, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=340,y=60)

		Label(root1,text='Car Type', width=10, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=450,y=60)

		Label(root1,text='Car Capicity', width=10, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=560,y=60)

		Label(root1,text='Car Brand', width=20, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=670,y=60)

		Label(root1,text='Additional Features', width=20, height=2,font='verdena 12 bold',bg='#5453a6',fg='white').place(x=880,y=60)

		def update_canvas():
			conn = mysql.connector.connect(host='localhost',user='root',password='',database='shopping')
			cursor = conn.cursor()
			canvas.delete("all")

			cursor.execute("select * from cars_data ")
			result = cursor.fetchall()

			
			y = 20

			for res in result:


				cid = canvas.create_text(10,y,text=res[0],font='verdena 11',fill='white')
				canvas.create_text(130,y,text=res[1],font='verdena 11',fill='white')
				canvas.create_text(270,y,text=res[2],font='verdena 11',fill='white')
				canvas.create_text(380,y,text=res[3],font='verdena 11',fill='white')
				canvas.create_text(480,y,text=res[4],font='verdena 11',fill='white')
				canvas.create_text(590,y,text=f'{res[5]}  Seater',font='verdena 11',fill='white')
				canvas.create_text(740,y,text=res[6],font='verdena 11',fill='white')
				if(res[7] == "All of above"):
					canvas.create_text(1130,y,text=f'Air Condional + Top Roof Open \\ Car Controlling Through Phone \\ Wireless Charging',font='verdena 11',fill='white')

				if(res[7] == "1. Air Condional + Top Roof Open"):
					canvas.create_text(960,y,text=f'Air Condional + Top Roof Open',font='verdena 11',fill='white')

				if(res[7] == "2. Car Controlling Through Phone"):
					canvas.create_text(960,y,text=f'Car Controlling Through Phone',font='verdena 11',fill='white')

				if(res[7] == "3. Wireless Charging "):
					canvas.create_text(960,y,text=f'Wireless Charging',font='verdena 11',fill='white')



				if(res[7] == "4. Feature 1 and Feature 2"):
					canvas.create_text(960,y,text=f'Air Condional + Top Roof Open and Car Controlling Through Phone',font='verdena 11',fill='white')

				if(res[7] == "5. Feature 2 and Feature 3"):
					canvas.create_text(960,y,text=f'Car Controlling Through Phone and Wireless Charging',font='verdena 11',fill='white')

				if(res[7] == "6. Feature 1 and Feature 3"):
					canvas.create_text(1040,y,text=f'Air Condional + Top Roof Open and Wireless Charging',font='verdena 11',fill='white')

				if res[7] == "No Additional Features" :
					canvas.create_text(960,y,text=f'{res[7]}',font='verdena 11',fill='white')


				y+=50
			canvas.after(1000,update_canvas)



		canvas.configure(xscrollcommand=scrollbarX.set,yscrollcommand=scrollbarY.set)
		scrollbarX.pack(fill='x',side='bottom')		
		scrollbarY.pack(fill='y',side='right')
		canvas.place(x=10,y=110)

		update_canvas()


		root1.mainloop()'''


	def bookedcar():
		root8.destroy()
		booked_cars()

	Label(frame3,text='Additional Features',font='verdena 15 bold',bg='#5453a6',fg='white').place(x=450,y=10)

	Button(frame3,text='Booked Cars/Registered Cars',font='verdena 12',bg='#adf802', fg='white',width=30,height=2,cursor='hand2',activebackground='#adf802',activeforeground='white',command=bookedcar).place(x=20,y=50)

	Button(frame3,text='View Statistics',font='verdena 12',bg='MediumVioletRed', fg='white',width=30,height=2,cursor='hand2',activebackground='MediumVioletRed',activeforeground='white',command=graph).place(x=400,y=50)

	Button(frame3,text='View All Cars',font='verdena 12',bg='#ff7722', fg='white',width=30,height=2,cursor='hand2',activebackground='#ff7722',activeforeground='white',command=all_cars).place(x=780,y=50)


	def add_car_type():
		root2 = Toplevel(root8)
		root2.geometry("1120x85+220+480")
		root2.resizable(0,0)
		root2.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root2.iconphoto(False,icon)

		Label(root2,text='Add Car Type',font='verdena 15 bold',bg='#5453a6',fg='white').pack()
		car = Entry(root2,width=95,font='verdena 12')
		car.place(x=50,y=50)

		def add_cars_type():
			if(car.get() == ""):
				messagebox.showerror("Error","Please write car type")
				return False

			else:
				cursor.execute("select * from car_type_values where value = %s ",(car.get(),))
				res = cursor.fetchone()
				if res is not None:
					messagebox.showinfo("Message","This car type is already present")					
				else:
					cursor.execute("insert into car_type_values(value) values(%s) ",(car.get(),))
					if conn.commit():
						pass
					messagebox.showinfo("Sucess","Car type added sucessfully")
					root2.destroy()
					root8.destroy()
					cars()

		Button(root2,text='Add',font='verdena 12', width=10,bg='green',fg='white',cursor='hand2',activebackground='green',activeforeground='white',command=add_cars_type).place(x=1000,y=45)
		root2.mainloop()


	def add_car_brand():
		root3 = Toplevel(root8)
		root3.geometry("1120x85+220+480")
		root3.resizable(0,0)
		root3.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root3.iconphoto(False,icon)
		Label(root3,text='Add Car Brand',font='verdena 15 bold',bg='#5453a6',fg='white').pack()
		car = Entry(root3,width=95,font='verdena 12')
		car.place(x=50,y=50)

		def add_cars_brand():
			if(car.get() == ""):
				messagebox.showerror("Error","Please write car brand")
				return False

			else:
				cursor.execute("select * from car_brand_values where value = %s ",(car.get(),))
				res = cursor.fetchone()
				if res is not None:
					messagebox.showinfo("Message","This car brand is already present")					
				else:
					cursor.execute("insert into car_brand_values(value) values(%s) ",(car.get(),))
					if conn.commit():
						pass
					messagebox.showinfo("Sucess","Car brand added sucessfully")
					root3.destroy()
					root8.destroy()
					cars()

		Button(root3,text='Add',font='verdena 12', width=10,bg='MediumBlue',fg='white',cursor='hand2',activebackground='MediumBlue',activeforeground='white',command=add_cars_brand).place(x=1000,y=45)

		root3.mainloop()


	def add_car_feature():
		root4 = Toplevel(root8)
		root4.geometry("1120x85+220+480")
		root4.resizable(0,0)
		root4.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root4.iconphoto(False,icon)
		Label(root4,text='Add Car Feature',font='verdena 15 bold',bg='#5453a6',fg='white').pack()
		car = Entry(root4,width=95,font='verdena 12')
		car.place(x=50,y=50)

		def add_cars_features():
			if(car.get() == ""):
				messagebox.showerror("Error","Please write car feature")
				return False

			else:
				cursor.execute("select * from car_feature_values where value = %s ",(car.get(),))
				res = cursor.fetchone()
				if res is not None:
					messagebox.showinfo("Message","This car feature is already present")					
				else:
					cursor.execute("insert into car_feature_values(value) values(%s) ",(car.get(),))
					if conn.commit():
						pass
					messagebox.showinfo("Sucess","Car feature added sucessfully")
					root4.destroy()
					root8.destroy()
					cars()

		Button(root4,text='Add',font='verdena 12', width=10,bg='#e71534',fg='white',cursor='hand2',activebackground='#e71534',activeforeground='white',command=add_cars_features).place(x=1000,y=45)

		root4.mainloop()



	def remove_car_type():
		root5 = Toplevel(root8)
		root5.geometry("1120x85+220+480")
		root5.resizable(0,0)
		root5.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root5.iconphoto(False,icon)

		cursor.execute("select * from car_type_values ")
		result = cursor.fetchall()
		data = [item[1] for item in result]

		Label(root5,text='Remove Car Type',font='verdena 15 bold',bg='#5453a6',fg='white').pack()
		car = Combobox(root5,width=95,font='verdena 12', values=data,state='r')
		car.set("Select Car Type")
		car.place(x=50,y=50)

		def remove_cars_type():
			if(car.get() == "Select Car Type"):
				messagebox.showerror("Error","Please select car type")
				return False

			else:
				cursor.execute("delete from car_type_values where value=%s ",(car.get(),))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Car type removed sucessfully")
				root5.destroy()
				root8.destroy()
				cars()

		Button(root5,text='Remove',font='verdena 12', width=10,bg='indianred',fg='white',cursor='hand2',activebackground='indianred',activeforeground='white',command=remove_cars_type).place(x=1000,y=45)
		root5.mainloop()


	def remove_car_brand():
		root6 = Toplevel(root8)
		root6.geometry("1120x85+220+480")
		root6.resizable(0,0)
		root6.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root6.iconphoto(False,icon)
		Label(root6,text='Remove Car Brand',font='verdena 15 bold',bg='#5453a6',fg='white').pack()

		cursor.execute("select * from car_brand_values ")
		result = cursor.fetchall()
		data = [item[1] for item in result]

		car = Combobox(root6,width=95,font='verdena 12', values=data,state='r')
		car.set("Select Car Brand")	
		car.place(x=50,y=50)

		def remove_cars_brand():
			if(car.get() == "Select Car Brand"):
				messagebox.showerror("Error","Please select car brand")
				return False

			else:
				cursor.execute("delete from car_brand_values where value=%s ",(car.get(),))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Car brand removed sucessfully")
				root6.destroy()
				root8.destroy()
				cars()
		Button(root6,text='Remove',font='verdena 12', width=10,bg='darkred',fg='white',cursor='hand2',activebackground='darkred',activeforeground='white',command=remove_cars_brand).place(x=1000,y=45)

		root6.mainloop()


	def remove_car_feature():
		root7 = Toplevel(root8)
		root7.geometry("1120x85+220+480")
		root7.resizable(0,0)
		root7.config(bg='#5453a6')
		icon = PhotoImage(file='car.png')
		root7.iconphoto(False,icon)
		Label(root7,text='Remove Car Feature',font='verdena 15 bold',bg='#5453a6',fg='white').pack()

		cursor.execute("select * from car_feature_values ")
		result = cursor.fetchall()
		data = [item[1] for item in result]

		car = Combobox(root7,width=95,font='verdena 12', values=data,state='r')
		car.set("Select Car Feature")	
		car.place(x=50,y=50)


		def remove_cars_features():
			if(car.get() == "Select Car Feature"):
				messagebox.showerror("Error","Please select car feature")
				return False

			else:
				cursor.execute("delete from car_feature_values where value=%s ",(car.get(),))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Car feature removed sucessfully")
				root7.destroy()
				root8.destroy()
				cars()
		Button(root7,text='Remove',font='verdena 12', width=10,bg='firebrick',fg='white',cursor='hand2',activebackground='firebrick',activeforeground='white',command=remove_cars_features).place(x=1000,y=45)

		root7.mainloop()



	Button(frame3,text='Add Car Type',font='verdena 12',bg='green', fg='white',width=30,height=2,cursor='hand2',activebackground='green',activeforeground='white',command=add_car_type).place(x=20,y=120)

	Button(frame3,text='Add Car Brand',font='verdena 12',bg='MediumBlue', fg='white',width=30,height=2,cursor='hand2',activebackground='MediumBlue',activeforeground='white',command=add_car_brand).place(x=400,y=120)

	Button(frame3,text='Add Car Feature',font='verdena 12',bg='#e71534', fg='white',width=30,height=2,cursor='hand2',activebackground='#e71534',activeforeground='white',command=add_car_feature).place(x=780,y=120)



	Button(frame3,text='Remove Car Type',font='verdena 12',bg='indianred', fg='white',width=30,height=2,cursor='hand2',activebackground='indianred',activeforeground='white',command=remove_car_type).place(x=20,y=190)

	Button(frame3,text='Remove Car Brand',font='verdena 12',bg='darkred', fg='white',width=30,height=2,cursor='hand2',activebackground='darkred',activeforeground='white',command=remove_car_brand).place(x=400,y=190)

	Button(frame3,text='Remove Car Feature',font='verdena 12',bg='firebrick', fg='white',width=30,height=2,cursor='hand2',activebackground='firebrick',activeforeground='white',command=remove_car_feature).place(x=780,y=190)
	
	root8.mainloop()


############################ End of Eighth Window #########################


def booked_cars():
	root9 = Tk()
	root9.title("Registered Cars")
	root9.geometry("1350x750+0+0")
	root9.resizable(0,0)
	root9.config(bg='white')
	icon = PhotoImage(file='car.png')
	root9.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root9.destroy()
		profile()

	def dashboard_window():
		root9.destroy()
		dashboard()

	def car_window():
		root9.destroy()
		cars()

	def order_window():
		root9.destroy()
		orders()

	def customer_window():
		root9.destroy()
		customer()

	def customer_contact_window():
		root9.destroy()
		customer_contact()

	def customer_feedback_window():
		root9.destroy()
		customer_feedback()

	def logout_page():
		root9.destroy()
		logout()

	frame1 = Frame(root9,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root9,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)

	cursor.execute("select * from account where device_name=%s ",(socket.gethostname(),))
	res = cursor.fetchone()
	Label(frame2,text=f'Welcome {res[1]}', font='verdena 12 bold',width=100, height=2,bg='#5453a6',fg='white',padx=75).place(x=0,y=0)

	labelframe1 = LabelFrame(frame2,width=1140,height=50,bg='#5453a6')
	labelframe1.place(x=5,y=50)

	def selected_data(event):
		global search_button
		data = selected_customer_options.get()
		if data == "Proof Id":
			data = 'proofid'
		Label(labelframe1,text='Search Customers Data',font='verdena 9 bold',bg='#5453a6',fg='white').place(x=330,y=10)

		cursor.execute(f"select {data} from registred_customers ")
		res = cursor.fetchall()
		listoptions = [item[0] for item in res]
		searched_options_data = Combobox(labelframe1,font='verdena 9',width=20,values=listoptions,state='r')
		searched_options_data.place(x=480,y=10)

		if data == "proofid":
			data = 'Proof Id'
		searched_options_data.set(f'Select Customers {data}')

		def search():
			search_car_button.config(state='disable')
			save_final_data.config(state='disable')
			update_final_data.config(state='normal')
			delete_final_data.config(state='normal')
			print_final_data.config(state='normal')

			sod = searched_options_data.get()
			if sod == f"Select Customers {data}":
				messagebox.showerror('Error','Please select customer data')
				return False

			cnm = customer_name
			ceml = customer_email
			cmb = customer_mobile
			cgn = customer_gender
			cadd = customer_address
			cdob = customer_dob
			cdor = customer_dor
			cnational = customer_nationality
			cptype = customer_ptype
			cpid = customer_pid
			cid = customer_id

			crid = car_id
			crnm = car_name
			crprice = car_price
			cr_brand = car_brand
			cr_mdl_date = car_model_date
			cr_nmb = car_number

			cursor.execute(f"select * from registred_customers where id = %s or name=%s or mobile=%s or email=%s or proofid=%s ",(sod,sod,sod,sod,sod))
			res = cursor.fetchone()

			if res is not None:
				cnm.delete(0,'end')
				ceml.delete(0,'end')
				cmb.delete(0,'end')
				cgn.set('Select Gender')
				cadd.delete(1.0,'end')
				cdob.delete(0,'end')
				cdor.delete(0,'end')
				cnational.delete(0,'end')
				cptype.set('Select Proof Type')
				cpid.delete(0,'end')
				cid.delete(0,'end')
				image = Image.open('user.png')
				image = image.resize((50,50))
				image = ImageTk.PhotoImage(image)
				customer_image.config(image=image)
				customer_image.image = image

				image1 = Image.open(res[13])
				if car_image_data[0] == '':
					car_image_data[0] = res[13]

				image1 = image1.resize((50,50))
				image1 = ImageTk.PhotoImage(image1)
				car_image.config(image=image1)
				car_image.image = image1

				crid.delete(0,'end')
				crnm.delete(0,'end')
				crprice.delete(0,'end')
				cr_brand.delete(0,'end')
				cr_mdl_date.delete(0,'end')
				cr_nmb.delete(0,'end')

				cnm.insert(0,res[1])
				ceml.insert(0,res[2])
				cmb.insert(0,res[3])
				cgn.set(res[4])
				cadd.insert(END,res[5])
				cdob.insert(0,res[6])
				cdor.insert(0,res[7])
				cnational.insert(0,res[8])
				cptype.set(res[9])
				cpid.insert(0,res[10])
				cid.insert(0,res[11])
				image = Image.open(res[12])
				image = image.resize((50,50))
				image = ImageTk.PhotoImage(image)
				customer_image.config(image=image)
				customer_image.image = image

				image1 = Image.open(res[13])
				image1 = image1.resize((50,50))
				image1 = ImageTk.PhotoImage(image1)
				car_image.config(image=image1)
				car_image.image = image1	
				crid.insert(0,res[14])
				crnm.insert(0,res[15])
				crprice.insert(0,res[16])
				cr_brand.insert(0,res[17])
				cr_mdl_date.insert(0,res[18])
				cr_nmb.insert(0,res[19])
			else:
				messagebox.showerror('Error','Sorry no data is found')
				root9.destroy()
				booked_cars()

		search_button = Button(labelframe1,text='Search',font='verdena 9',bg='lightblue', fg='white',width=7,cursor='hand2',activebackground='lightblue',activeforeground='white',command=search)
		search_button.place(x=650,y=8)

	Label(labelframe1,text='Select Customers Data',font='verdena 9 bold',bg='#5453a6',fg='white').place(x=10,y=10)
	selected_customer_options = Combobox(labelframe1,font='verdena 9',width=20, height=1,values=['Id','Name','Mobile','Email','Proof Id'],state='r')
	selected_customer_options.place(x=160,y=10)
	selected_customer_options.set('Select Data')
	selected_customer_options.bind('<<ComboboxSelected>>',selected_data)

	Label(labelframe1,text='Search Customers Data',font='verdena 9 bold',bg='#5453a6',fg='white').place(x=330,y=10)

	def search():
		search_car_button.config(state='disable')
		save_final_data.config(state='disable')
		update_final_data.config(state='normal')
		delete_final_data.config(state='normal')
		print_final_data.config(state='normal')

		scd = searched_customer_data.get()

		if scd == "":
			messagebox.showerror('Error','Please write customer data')
			return False

		cnm = customer_name
		ceml = customer_email
		cmb = customer_mobile
		cgn = customer_gender
		cadd = customer_address
		cdob = customer_dob
		cdor = customer_dor
		cnational = customer_nationality
		cptype = customer_ptype
		cpid = customer_pid
		cid = customer_id

		crid = car_id
		crnm = car_name
		crprice = car_price
		cr_brand = car_brand
		cr_mdl_date = car_model_date
		cr_nmb = car_number

		cursor.execute("select * from registred_customers where id= %s or name=%s or email=%s or mobile=%s or proofid=%s or customer_id=%s or car_number=%s ",(scd,scd,scd,scd,scd,scd,scd))
		res = cursor.fetchone()

		if res is not None:

			cnm.delete(0,'end')
			ceml.delete(0,'end')
			cmb.delete(0,'end')
			cgn.set('Select Gender')
			cadd.delete(1.0,'end')
			cdob.delete(0,'end')
			cdor.delete(0,'end')
			cnational.delete(0,'end')
			cptype.set('Select Proof Type')
			cpid.delete(0,'end')
			cid.delete(0,'end')
			image = Image.open('user.png')
			image = image.resize((50,50))
			image = ImageTk.PhotoImage(image)
			customer_image.config(image=image)
			customer_image.image = image

			crid.delete(0,'end')
			crnm.delete(0,'end')
			crprice.delete(0,'end')
			cr_brand.delete(0,'end')
			cr_mdl_date.delete(0,'end')
			cr_nmb.delete(0,'end')

			cnm.insert(0,res[1])
			ceml.insert(0,res[2])
			cmb.insert(0,res[3])
			cgn.set(res[4])
			cadd.insert(END,res[5])
			cdob.insert(0,res[6])
			cdor.insert(0,res[7])
			cnational.insert(0,res[8])
			cptype.set(res[9])
			cpid.insert(0,res[10])
			cid.insert(0,res[11])
			image = Image.open(res[12])
			image = image.resize((50,50))
			image = ImageTk.PhotoImage(image)
			customer_image.config(image=image)
			customer_image.image = image

			customer_images_data[0] = res[12]

			image1 = Image.open(res[13])
			if car_image_data[0] == '':
				car_image_data[0] = res[13]

			image1 = image1.resize((50,50))
			image1 = ImageTk.PhotoImage(image1)
			car_image.config(image=image1)
			car_image.image = image1

			crid.insert(0,res[14])
			crnm.insert(0,res[15])
			crprice.insert(0,res[16])
			cr_brand.insert(0,res[17])
			cr_mdl_date.insert(0,res[18])
			cr_nmb.insert(0,res[19])

		else:
			messagebox.showerror('Error','Sorry no data is found')

	searched_customer_data = Entry(labelframe1,font='verdena 9',width=20)
	searched_customer_data.place(x=480,y=10)


	search_customer_button = Button(labelframe1,text='Search',font='verdena 9',bg='lightblue', fg='white',width=7,cursor='hand2',activebackground='lightblue',activeforeground='white',command=search)
	search_customer_button.place(x=650,y=8)

	Label(labelframe1,text='Select Car Data',font='verdena 9 bold',bg='#5453a6',fg='white').place(x=750,y=10)

	cursor.execute("select name from cars_data ")
	result = cursor.fetchall()
	listoptions = [item[0] for item in result]

	searched_car_data = Combobox(labelframe1,font='verdena 9',width=20,values=listoptions,state='r')
	searched_car_data.place(x=860,y=10)
	searched_car_data.set("Select Car Name")

	car_image_data = ['']

	def search_cars():
		try:
			if search_customer_button['state'] == "normal":
				#print("Hello")
				search_customer_button.config(state='disable')
				search_button.config(state='disable')
				selected_customer_options.config(state='r')
		except:
			pass
		scd = searched_car_data.get()
		if scd == "Select Car Name":
			messagebox.showerror('Error','Please select car name')
			return False

		crid = car_id
		crnm = car_name
		crprice = car_price
		cr_brand = car_brand
		cr_mdl_date = car_model_date
		cr_img = car_image

		cursor.execute(f"select * from cars_data where name = %s ",(scd,))
		res = cursor.fetchone()

		if res is not None:
			crid.delete(0,'end')
			crnm.delete(0,'end')
			crprice.delete(0,'end')
			cr_brand.delete(0,'end')
			cr_mdl_date.delete(0,'end')

			crid.insert(0,res[0])
			crnm.insert(0,res[1])
			crprice.insert(0,res[2])
			cr_brand.insert(0,res[6])
			cr_mdl_date.insert(0,res[3])
			car_image_data[0] = res[8]

			image = Image.open(res[8])
			image = image.resize((50,50))
			image = ImageTk.PhotoImage(image)

			cr_img.config(image=image)
			cr_img.image = image
		else:
			messagebox.showerror('Error','Sorry no data is found')

	search_car_button = Button(labelframe1,text='Search',font='verdena 9',bg='lightblue', fg='white',width=7,cursor='hand2',activebackground='lightblue',activeforeground='white',command=search_cars)
	search_car_button.place(x=1050,y=8)


	frame3 = Frame(frame2,width=1140,height=630,bg='#5453a6')
	frame3.place(x=5,y=100)

	Label(frame3,text='Customer Details',font='verdena 15 bold',bg='#5453a6',fg='white').place(x=150,y=20)

	Label(frame3,text='Customer Name',font='verdena 12',fg='white',bg='#5453a6').place(x=20,y=70)

	Label(frame3,text='Customer Email',font='verdena 12',fg='white',bg='#5453a6').place(x=20,y=120)

	Label(frame3,text='Customer Mobile',font='verdena 12',fg='white',bg='#5453a6').place(x=20,y=170)

	Label(frame3,text='Customer Gender',font='verdena 12',fg='white',bg='#5453a6').place(x=20,y=220)

	Label(frame3,text='Customer Address',font='verdena 12',fg='white',bg='#5453a6').place(x=20,y=300)

	customer_name = Entry(frame3,width=20,font='verdena 12')
	customer_name.place(x=160,y=70)

	customer_email = Entry(frame3,width=20,font='verdena 12')
	customer_email.place(x=160,y=120)

	customer_mobile = Entry(frame3,width=20,font='verdena 12')
	customer_mobile.place(x=160,y=170)

	customer_gender = Combobox(frame3,width=18,font='verdena 12',values=['Male','Female'],state='r')
	customer_gender.place(x=160,y=220)
	customer_gender.set('Select Gender')

	customer_address = Text(frame3,width=20, height=5,font='verdena 12',pady=10,padx=10)
	customer_address.place(x=160,y=270)

	Label(frame3,text='Customer D.O.B',font='verdena 12',fg='white',bg='#5453a6').place(x=400,y=70)

	Label(frame3,text='Customer D.O.R',font='verdena 12',fg='white',bg='#5453a6').place(x=400,y=120)

	Label(frame3,text='Customer Nationality',font='verdena 12',fg='white',bg='#5453a6').place(x=400,y=170)

	Label(frame3,text='Customer Proof Type',font='verdena 12',fg='white',bg='#5453a6').place(x=400,y=220)

	Label(frame3,text='Customer Proof Id',font='verdena 12',fg='white',bg='#5453a6').place(x=400,y=270)

	Label(frame3,text='Customer Id',font='verdena 12',fg='white',bg='#5453a6').place(x=400,y=320)

	customer_dob = Entry(frame3,width=15,font='verdena 12')
	customer_dob.place(x=555,y=70)

	customer_dor = Entry(frame3,width=15,font='verdena 12')
	customer_dor.place(x=555,y=120)
	customer_dor.insert(0,datetime.now().strftime("%d/%m/%y"))

	customer_nationality = Entry(frame3,width=15,font='verdena 12')
	customer_nationality.place(x=555,y=170)

	customer_ptype = Combobox(frame3,width=13,font='verdena 12',values=['Adhar card','Pan card','ATM card','Debit card','Credit card','Passport'],state='r')
	customer_ptype.place(x=555,y=220)
	customer_ptype.set('Select Proof Type')

	customer_pid = Entry(frame3,width=15,font='verdena 12')
	customer_pid.place(x=555,y=270)

	customer_id = Entry(frame3,width=15,font='verdena 12')
	customer_id.place(x=555,y=320)

	customer_images_data = ['']

	def open_image():
		try:
			global customer_folder
			filename = filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=[('PNG Files','*png'),('JPG Files','*.jpg'),('JPEG Files','*jpeg')])
			image = Image.open(filename)
			image = image.resize((50,50))
			image = ImageTk.PhotoImage(image)
			customer_image.config(image=image)
			customer_image.image = image
			customer_folder = "customer_images/"+filename.split("/")[-1]
			customer_images_data[0] = customer_folder
			shutil.copy(filename,customer_folder)
			#messagebox.showinfo('info',customer_folder)

		except:
			pass

	image = Image.open('user.png')
	image = image.resize((50,50))
	image = ImageTk.PhotoImage(image)
	customer_image = Button(frame3,image=image,cursor='hand2',command=open_image)
	customer_image.place(x=20,y=5)

	Label(frame3,text='Cars Details',font='verdena 15 bold',bg='#5453a6',fg='white').place(x=850,y=20)

	Label(frame3,text='Car Id',font='verdena 12',bg='#5453a6',fg='white').place(x=750,y=70)

	Label(frame3,text='Car Name',font='verdena 12',bg='#5453a6',fg='white').place(x=750,y=120)

	Label(frame3,text='Car Price',font='verdena 12',bg='#5453a6',fg='white').place(x=750,y=170)

	Label(frame3,text='Car Brand',font='verdena 12',bg='#5453a6',fg='white').place(x=750,y=220)

	Label(frame3,text='Car Model',font='verdena 12',bg='#5453a6',fg='white').place(x=750,y=270)

	Label(frame3,text='Car Number',font='verdena 12',bg='#5453a6',fg='white').place(x=750,y=320)

	carimage = Image.open('car.jpg')
	carimage = carimage.resize((50,50))
	carimage = ImageTk.PhotoImage(carimage)

	car_image = Label(frame3,image=carimage)
	car_image.place(x=750,y=5)

	car_id = Entry(frame3,font='verdena 12',width=20)
	car_id.place(x=850,y=70)

	car_name = Entry(frame3,font='verdena 12',width=20)
	car_name.place(x=850,y=120)

	car_price = Entry(frame3,font='verdena 12',width=20)
	car_price.place(x=850,y=170)
	car_price.insert(0,'₹')

	car_brand = Entry(frame3,font='verdena 12',width=20)
	car_brand.place(x=850,y=220)


	car_model_date = Entry(frame3,font='verdena 12',width=20)
	car_model_date.place(x=850,y=270)

	car_number = Entry(frame3,font='verdena 12',width=20)
	car_number.place(x=850,y=320)

	def save():

		cnm = customer_name.get()
		ceml = customer_email.get()
		cmb = customer_mobile.get()
		cgn = customer_gender.get()
		cadd = customer_address.get(1.0,'end')
		cdob = customer_dob.get()
		cdor = customer_dor.get()
		cnational = customer_nationality.get()
		cptype = customer_ptype.get()
		cpid = customer_pid.get()
		cid = customer_id.get()

		crid = car_id.get()
		crnm = car_name.get()
		crprice = car_price.get()
		cr_brand = car_brand.get()
		cr_mdl_date = car_model_date.get()
		cr_nmb = car_number.get()

		if cnm == "":
			messagebox.showerror('Error','Please write customer name')
			return False

		if len(cnm) < 2:
			messagebox.showerror('Error','Please write correct customer name')
			return False

		if ceml == "":
			messagebox.showerror('Error','Please write customer email')
			return False

		if len(ceml) < 12:
			messagebox.showerror('Error','Please write correct email address')
			return False

		if cmb == "":
			messagebox.showerror('Error','Please write customer mobile number')
			return False

		if len(cmb) < 10:
			messagebox.showerror('Error','Please write correct mobile number')
			return False

		if len(cmb) > 10:
			messagebox.showerror('Error','Please write correct mobile number')
			return False

		if cgn == "Select Gender":
			messagebox.showerror('Error','Please select customer gender')
			return False

		if cadd == "":
			messagebox.showerror('Error','Please write customer address')
			return False

		if len(cadd) < 5:
			messagebox.showerror('Error','Please write correct address')
			return False

		if cdob == "":
			messagebox.showerror('Error','Please write customer date of birth')
			return False

		try:
			if int(cdor.split("/")[-1]) - int(cdob.split("/")[-1]) <= 0:
				pass

			elif int(cdor.split("/")[-1]) - int(cdob.split("/")[-1]) < 18:
				messagebox.showerror('Error','This customer is below the citizen age')
				return False
		except:
			messagebox.showerror("Error","Something went wrong")

		if cdor == "":
			messagebox.showerror('Error','Please write customer date of registration')
			return False

		if cnational == "":
			messagebox.showerror('Error','Please write customer nationality')
			return False

		if cptype == "Select Proof Type":
			messagebox.showerror('Error','Please select customer proof type')
			return False

		if cpid == "":
			messagebox.showerror('Error','Please write customer proof id')
			return False

		if len(cpid) < 2:
			messagebox.showerror('Error','Please write correct proof id')
			return False

		if cid == "":
			messagebox.showerror('Error','Please write customer id')
			return False

		if len(cid) < 9 or len(cid) > 9:
			messagebox.showerror('Error','Please write correct customer id')
			return False

		if crid == "":
			messagebox.showerror('Error','Please write car id')
			return False

		if crnm == "":
			messagebox.showerror('Error','Please write car name')
			return False

		if len(crnm) < 2:
			messagebox.showerror('Error','Please write correct car name')
			return False

		if crprice == "":
			messagebox.showerror('Error','Please write car price')
			return False

		if cr_brand == "":
			messagebox.showerror('Error','Please write car brand name')
			return False

		if cr_mdl_date == "":
			messagebox.showerror('Error','Please write car model date')
			return False

		if cr_nmb == "":
			messagebox.showerror('Error','Please write car number')
			return False

		if len(cr_nmb) < 12 or len(cr_nmb) > 12 :
			messagebox.showerror('Error','Please write correct car number')
			return False

		try:
			open_image()
		except:
			pass

		else:
			cursor.execute("select * from registred_customers where email=%s or mobile=%s or proofid=%s or customer_id=%s or car_number=%s ",(ceml,cmb,cpid,cid,cr_nmb))
			res = cursor.fetchone()

			if res is None:
				cursor.execute("select * from cars_data where id=%s",(crid,))
				res1 = cursor.fetchone()

				cursor.execute("insert into registred_customers (name,email,mobile,gender,address,dob,dor,nationality,prooftype,proofid,customer_id,customer_photo,car_image,car_id,car_name,car_price,car_brand,model_date,car_number,time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(cnm,ceml,cmb,cgn,cadd,cdob,cdor,cnational,cptype,cpid,cid,
					customer_folder,car_image_data[0],crid,crnm,crprice,cr_brand,cr_mdl_date,cr_nmb,datetime.now().strftime("%d/%m/%y")))
				if conn.commit():
					pass

				cursor.execute("insert into reserve_cars_data (name,car_price,model_date,car_type,car_capicity,car_brand,car_features,car_image1,car_image2, car_image3, car_image4, car_image5, car_image6,device_name,time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(res1[1],res1[2],res1[3],res1[4],res1[5],res1[6],res1[7],res1[8], res1[9], res1[10], res1[11], res1[12], res1[13],socket.gethostname(),datetime.now().strftime("%d-%m-%y %H:%M:%S")))

				if conn.commit():
					pass

				cursor.execute("delete from cars_data where id=%s ",(crid,))
				
				if conn.commit():
					pass

				cursor.execute("delete from reserve_customers_data where email=%s ",(ceml,))
				
				if conn.commit():
					pass	

				cnm = customer_name.delete(0,'end')
				ceml = customer_email.delete(0,'end')
				cmb = customer_mobile.delete(0,'end')
				cgn = customer_gender.set('Select Gender')
				cadd = customer_address.delete(1.0,'end')
				cdob = customer_dob.delete(0,'end')
				customer_dor.delete(0,'end')

				cdor = customer_dor.insert(0,datetime.now().strftime("%d/%m/%y"))
				cnational = customer_nationality.delete(0,'end')
				cptype = customer_ptype.set('Select Proof Type')
				cpid = customer_pid.delete(0,'end')
				cid = customer_id.delete(0,'end')

				crid = car_id.delete(0,'end')
				crnm = car_name.delete(0,'end')
				crprice = car_price.delete(0,'end')

				crprice = car_price.insert(0,'₹')
				cr_brand = car_brand.delete(0,'end')
				cr_mdl_date = car_model_date.delete(0,'end')
				cr_nmb = car_number.delete(0,'end')

				image = Image.open('user.png')
				image = image.resize((50,50))
				image = ImageTk.PhotoImage(image)

				customer_image.config(image=image)
				customer_image.image = image

				image1 = Image.open('car.jpg')
				image1 = image1.resize((50,50))
				image1 = ImageTk.PhotoImage(image1)

				car_image.config(image=image1)
				car_image.image = image1

				searched_car_data.set("Select Car Name")

				messagebox.showinfo('Sucess','Customer registred sucessfully')
				clear()

			else:
				messagebox.showerror('Error','This customer is already registred please choose diffrent one ')
				return False

	def update():
		
		cnm = customer_name.get()
		ceml = customer_email.get()
		cmb = customer_mobile.get()
		cgn = customer_gender.get()
		cadd = customer_address.get(1.0,'end')
		cdob = customer_dob.get()
		cdor = customer_dor.get()
		cnational = customer_nationality.get()
		cptype = customer_ptype.get()
		cpid = customer_pid.get()
		cid = customer_id.get()

		crid = car_id.get()
		crnm = car_name.get()
		crprice = car_price.get()
		cr_brand = car_brand.get()
		cr_mdl_date = car_model_date.get()
		cr_nmb = car_number.get()

		if cnm == "":
			messagebox.showerror('Error','Please write customer name')
			return False

		if len(cnm) < 2:
			messagebox.showerror('Error','Please write correct customer name')
			return False

		if ceml == "":
			messagebox.showerror('Error','Please write customer email')
			return False

		if len(ceml) < 12:
			messagebox.showerror('Error','Please write correct email address')
			return False

		if cmb == "":
			messagebox.showerror('Error','Please write customer mobile number')
			return False

		if len(cmb) < 10:
			messagebox.showerror('Error','Please write correct mobile number')
			return False

		if len(cmb) > 10:
			messagebox.showerror('Error','Please write correct mobile number')
			return False

		if cgn == "Select Gender":
			messagebox.showerror('Error','Please select customer gender')
			return False

		if cadd == "":
			messagebox.showerror('Error','Please write customer address')
			return False

		if len(cadd) < 5:
			messagebox.showerror('Error','Please write correct address')
			return False

		if cdob == "":
			messagebox.showerror('Error','Please write customer date of birth')
			return False
		try:
			if int(cdor.split("/")[-1]) - int(cdob.split("/")[-1]) <= 0:
				pass

			elif int(cdor.split("/")[-1]) - int(cdob.split("/")[-1]) < 18:
				messagebox.showerror('Error','This customer is below the citizen age')
				return False
		except:
			messagebox.showerror('Error','Something went wrong')
			return False		

		if cdor == "":
			messagebox.showerror('Error','Please write customer date of registration')
			return False

		if cnational == "":
			messagebox.showerror('Error','Please write customer nationality')
			return False

		if cptype == "Select Proof Type":
			messagebox.showerror('Error','Please select customer proof type')
			return False

		if cpid == "":
			messagebox.showerror('Error','Please write customer proof id')
			return False

		if len(cpid) < 2:
			messagebox.showerror('Error','Please write correct proof id')
			return False

		if cid == "":
			messagebox.showerror('Error','Please write customer id')
			return False

		if len(cid) < 9 or len(cid) > 9:
			messagebox.showerror('Error','Please write correct customer id')
			return False


		if crid == "":
			messagebox.showerror('Error','Please write car id')
			return False

		if crnm == "":
			messagebox.showerror('Error','Please write car name')
			return False

		if len(crnm) < 2:
			messagebox.showerror('Error','Please write correct car name')
			return False

		if crprice == "":
			messagebox.showerror('Error','Please write car price')
			return False

		if cr_brand == "":
			messagebox.showerror('Error','Please write car brand name')
			return False

		if cr_mdl_date == "":
			messagebox.showerror('Error','Please write car model date')
			return False

		if cr_nmb == "":
			messagebox.showerror('Error','Please write car number')
			return False

		if len(cr_nmb) < 12 or len(cr_nmb) > 12 :
			messagebox.showerror('Error','Please write correct car number')
			return False

		else:
			cursor.execute("select * from registred_customers where customer_id=%s ",(cid,))
			res = cursor.fetchone()

			customer_images_data[0] = res[12]

			if res is not None:
				cursor.execute("update registred_customers set name=%s,email=%s,mobile=%s,gender=%s,address=%s,dob=%s,dor=%s,nationality=%s,prooftype=%s,proofid=%s,customer_id=%s,customer_photo=%s,car_image=%s,car_id=%s,car_name=%s,car_price=%s,car_brand=%s,model_date=%s,car_number=%s where customer_id=%s ",(cnm,ceml,cmb,cgn,cadd,cdob,cdor,cnational,cptype,cpid,cid,
					customer_images_data[0],car_image_data[0],crid,crnm,crprice,cr_brand,cr_mdl_date,cr_nmb,cid))

				if conn.commit():
					pass

				cursor.execute("update customer_account set name=%s,email=%s,mobile=%s where customer_id=%s ",(cnm,ceml,cmb,res[11]))

				if conn.commit():
					pass

				cursor.execute("update customer_login set name=%s,email=%s,mobile=%s where customer_id=%s ",(cnm,ceml,cmb,res[11]))

				if conn.commit():
					pass

				cnm = customer_name.delete(0,'end')
				ceml = customer_email.delete(0,'end')
				cmb = customer_mobile.delete(0,'end')
				cgn = customer_gender.set('Select Gender')
				cadd = customer_address.delete(1.0,'end')
				cdob = customer_dob.delete(0,'end')
				customer_dor.delete(0,'end')


				cdor = customer_dor.insert(0,datetime.now().strftime("%d/%m/%y"))
				cnational = customer_nationality.delete(0,'end')
				cptype = customer_ptype.set('Select Proof Type')
				cpid = customer_pid.delete(0,'end')
				cid = customer_id.delete(0,'end')

				crid = car_id.delete(0,'end')
				crnm = car_name.delete(0,'end')
				car_price.delete(0,'end')

				crprice = car_price.insert(0,'₹')
				cr_brand = car_brand.delete(0,'end')
				cr_mdl_date = car_model_date.delete(0,'end')
				cr_nmb = car_number.delete(0,'end')

				image = Image.open('user.png')
				image = image.resize((50,50))
				image = ImageTk.PhotoImage(image)

				customer_image.config(image=image)
				customer_image.image = image

				image1 = Image.open('car.jpg')
				image1 = image1.resize((50,50))
				image1 = ImageTk.PhotoImage(image1)

				car_image.config(image=image1)
				car_image.image = image1

				searched_car_data.set("Select Car Name")		

				messagebox.showinfo('Sucess','Customer data updated sucessfully')
				
				clear()


			else:
				messagebox.showerror('Error','Sorry this customer is not present data is not updated')
				return False

	def delete():
		cnm = customer_name.get()
		ceml = customer_email.get()
		cmb = customer_mobile.get()
		cgn = customer_gender.get()
		cadd = customer_address.get(1.0,'end')
		cdob = customer_dob.get()
		cdor = customer_dor.get()
		cnational = customer_nationality.get()
		cptype = customer_ptype.get()
		cpid = customer_pid.get()
		cid = customer_id.get()

		crid = car_id.get()
		crnm = car_name.get()
		crprice = car_price.get()
		cr_brand = car_brand.get()
		cr_mdl_date = car_model_date.get()
		cr_nmb = car_number.get()

		if cnm == "":
			messagebox.showerror('Error','Please write customer name')
			return False

		if len(cnm) < 2:
			messagebox.showerror('Error','Please write correct customer name')
			return False

		if ceml == "":
			messagebox.showerror('Error','Please write customer email')
			return False

		if len(ceml) < 12:
			messagebox.showerror('Error','Please write correct email address')
			return False

		if cmb == "":
			messagebox.showerror('Error','Please write customer mobile number')
			return False

		if len(cmb) < 10:
			messagebox.showerror('Error','Please write correct mobile number')
			return False

		if len(cmb) > 10:
			messagebox.showerror('Error','Please write correct mobile number')
			return False

		if cgn == "Select Gender":
			messagebox.showerror('Error','Please select customer gender')
			return False

		if cadd == "":
			messagebox.showerror('Error','Please write customer address')
			return False

		if len(cadd) < 5:
			messagebox.showerror('Error','Please write correct address')
			return False

		if cdob == "":
			messagebox.showerror('Error','Please write customer date of birth')
			return False

		if cdor == "":
			messagebox.showerror('Error','Please write customer date of registration')
			return False

		try:
			if int(cdor.split("/")[-1]) - int(cdob.split("/")[-1]) <= 0:
				pass

			elif int(cdor.split("/")[-1]) - int(cdob.split("/")[-1]) < 18:
				messagebox.showerror('Error','This customer is below the citizen age')
				return False
		except:
			messagebox.showerror("Error","Something went wrong")

		if cnational == "":
			messagebox.showerror('Error','Please write customer nationality')
			return False

		if cptype == "Select Proof Type":
			messagebox.showerror('Error','Please select customer proof type')
			return False

		if cpid == "":
			messagebox.showerror('Error','Please write customer proof id')
			return False

		if len(cpid) < 2:
			messagebox.showerror('Error','Please write correct proof id')
			return False

		if cid == "":
			messagebox.showerror('Error','Please write customer id')
			return False

		if len(cid) < 9 or len(cid) > 9:
			messagebox.showerror('Error','Please write correct customer id')
			return False

		if crid == "":
			messagebox.showerror('Error','Please write car id')
			return False

		if crnm == "":
			messagebox.showerror('Error','Please write car name')
			return False

		if len(crnm) < 2:
			messagebox.showerror('Error','Please write correct car name')
			return False

		if crprice == "":
			messagebox.showerror('Error','Please write car price')
			return False

		if cr_brand == "":
			messagebox.showerror('Error','Please write car brand name')
			return False

		if cr_mdl_date == "":
			messagebox.showerror('Error','Please write car model date')
			return False

		if cr_nmb == "":
			messagebox.showerror('Error','Please write car number')
			return False

		if len(cr_nmb) < 12 or len(cr_nmb) > 12 :
			messagebox.showerror('Error','Please write correct car number')
			return False

		else:
			msg = messagebox.askquestion('Message','Are you really want to delete your customer data')
			if msg == "yes":
				cursor.execute("select * from registred_customers where customer_id=%s ",(cid,))
				res = cursor.fetchone()
				
				customer_images_data[0] = res[12]

				if res is not None:
					cursor.execute("select * from reserve_cars_data where name=%s ",(crnm,))
					res1 = cursor.fetchone()

					cursor.execute("insert into cars_data (name,car_price,model_date,car_type,car_capicity,car_brand,car_features,car_image1,car_image2, car_image3, car_image4, car_image5, car_image6,device_name,time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(res1[1],res1[2],res1[3],res1[4],res1[5],res1[6],res1[7],res1[8], res1[9], res1[10], res1[11], res1[12], res1[13],socket.gethostname(),datetime.now().strftime("%d-%m-%y %H:%M:%S")))

					if conn.commit():
						pass

					cursor.execute("insert into reserve_customers_data (name,email,mobile,gender,address,dob,dor,nationality,prooftype,proofid,customer_id,customer_photo,car_image,car_id,car_name,car_price,car_brand,model_date,car_number) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ",(cnm,ceml,cmb,cgn,cadd,cdob,cdor,cnational,cptype,cpid,cid,
						customer_images_data[0],car_image_data[0],crid,crnm,crprice,cr_brand,cr_mdl_date,cr_nmb))

					if conn.commit():
						print()

					cursor.execute("delete from registred_customers where id=%s ",(res[0],))
					if conn.commit():
						pass
	
					cursor.execute("delete from reserve_cars_data where name=%s ",(res1[1],))
					if conn.commit():
						pass

					customer_name.delete(0,'end')
					customer_email.delete(0,'end')
					customer_mobile.delete(0,'end')
					customer_gender.set('Select Gender')
					customer_address.delete(1.0,'end')
					customer_dob.delete(0,'end')
					customer_dor.delete(0,'end')

					customer_dor.insert(0,datetime.now().strftime("%d/%m/%y"))
					customer_nationality.delete(0,'end')
					customer_ptype.set('Select Proof Type')
					customer_pid.delete(0,'end')
					customer_id.delete(0,'end')

					car_id.delete(0,'end')
					car_name.delete(0,'end')
					car_price.delete(0,'end')

					car_price.insert(0,'₹')
					car_brand.delete(0,'end')
					car_model_date.delete(0,'end')
					car_number.delete(0,'end')

					image = Image.open('user.png')
					image = image.resize((50,50))
					image = ImageTk.PhotoImage(image)

					customer_image.config(image=image)
					customer_image.image = image

					image1 = Image.open('car.jpg')
					image1 = image1.resize((50,50))
					image1 = ImageTk.PhotoImage(image1)

					car_image.config(image=image1)
					car_image.image = image1

					searched_car_data.set("Select Car Name")

					messagebox.showinfo('Sucess','Customer data delete sucessfully')
					clear()

				else:
					messagebox.showerror('Error','Sorry this customer is not present data is not deleted')
					return False
	def clear():
		cnm = customer_name.delete(0,'end')
		ceml = customer_email.delete(0,'end')
		cmb = customer_mobile.delete(0,'end')
		cgn = customer_gender.delete(0,'end')
		cadd = customer_address.delete(1.0,'end')
		cdob = customer_dob.delete(0,'end')
		cdor = customer_dor.delete(0,'end')

		cdor = customer_dor.insert(0,datetime.now().strftime("%d/%m/%y"))
		cnational = customer_nationality.delete(0,'end')
		cptype = customer_ptype.delete(0,'end')
		cpid = customer_pid.delete(0,'end')
		cid = customer_id.delete(0,'end')

		crid = car_id.delete(0,'end')
		crnm = car_name.delete(0,'end')
		crprice = car_price.delete(0,'end')

		crprice = car_price.insert(0,'₹')
		cr_brand = car_brand.delete(0,'end')
		cr_mdl_date = car_model_date.delete(0,'end')
		cr_nmb = car_number.delete(0,'end')

		image = Image.open('user.png')
		image = image.resize((50,50))
		image = ImageTk.PhotoImage(image)

		customer_image.config(image=image)
		customer_image.image = image

		image1 = Image.open('car.jpg')
		image1 = image1.resize((50,50))
		image1 = ImageTk.PhotoImage(image1)

		car_image.config(image=image1)
		car_image.image = image1

		save_final_data.config(state='normal')
		update_final_data.config(state='disable')
		delete_final_data.config(state='disable')
		print_final_data.config(state='disable')
		search_customer_button.config(state='normal')
		selected_customer_options.config(state='r')
		search_car_button.config(state='normal')
		search_button.config(state='normal')

		cursor.execute("select name from cars_data ")
		result = cursor.fetchall()
		listoptions = [item[0] for item in result]
		searched_car_data.config(values=listoptions)

		searched_car_data.set("Select Car Name")

	def print_data():	
		cnm = customer_name.get()
		ceml = customer_email.get()
		cmb = customer_mobile.get()
		cgn = customer_gender.get()
		cadd = customer_address.get(1.0,'end')
		cdob = customer_dob.get()
		cdor = customer_dor.get()
		cnational = customer_nationality.get()
		cptype = customer_ptype.get()
		cpid = customer_pid.get()
		cid = customer_id.get()

		crid = car_id.get()
		crnm = car_name.get()
		crprice = car_price.get()
		cr_brand = car_brand.get()
		cr_mdl_date = car_model_date.get()
		cr_nmb = car_number.get()

		data = f'''
		\t\t    Customer Bill\n\n

		 \t\tCustomer Name - {cnm}		

		 \t\tCustomer Email - {ceml}

		 \t\tCustomer Mobile - {cmb}

		 \t\tCustomer Address - {cadd}

		 \t\tCustomer Date of birth - {cdob}

		 \t\tCustomer Date of product - {cdor}

		 \t\tCustomer Nationality - {cnational}

		 \t\tCustomer Proof Type - {cptype}

		 \t\tCustomer Proof ID - {cpid}

		 \t\tCustomer ID - {cid}

		 \t\tProduct Name - {crnm}

		 \t\tProduct Price - {'RS' + ' ' + crprice[1:]}

		 \t\tProduct Brand - {cr_brand}

		 \t\tProduct Model Date/Year - {cr_mdl_date}

		 \t\tProduct Number - {cr_nmb}


		''';


		file = open(f"customer_bills/{cnm}"+'.txt','w')
		file.write(data)
		file.close()
		system = os.startfile(f'customer_bills\\{cnm}.txt','print')


	save_final_data = Button(frame3,text='Save',font='verdena 12',fg='white',bg='green',activeforeground='white',activebackground='green',width=10,cursor='hand2',command=save)
	save_final_data.place(x=50,y=420)

	update_final_data = Button(frame3,text='Update',font='verdena 12',fg='white',bg='yellow',activeforeground='white',activebackground='yellow',width=10,cursor='hand2',state='disable',command=update)
	update_final_data.place(x=250,y=420)

	delete_final_data = Button(frame3,text='Delete',font='verdena 12',fg='white',bg='red',activeforeground='white',activebackground='red',width=10,cursor='hand2',state='disable',command=delete)
	delete_final_data.place(x=450,y=420)

	clear_final_data = Button(frame3,text='Clear/Reset',font='verdena 12',fg='white',bg='blue',activeforeground='white',activebackground='blue',width=10,cursor='hand2',command=clear)
	clear_final_data.place(x=650,y=420)

	print_final_data = Button(frame3,text='Print',font='verdena 12',fg='white',bg='orangered',activeforeground='white',activebackground='orangered',width=10,cursor='hand2',state='disable',command=print_data)
	print_final_data.place(x=850,y=420)

	def graph():
		cursor = conn.cursor()

		maledata = []
		femaledata = []

		cursor.execute("select * from car_brand_values ")
		result = cursor.fetchall()
		data = [item[1] for item in result]
		for i in data:
			cursor.execute("select count(*) from registred_customers where car_brand = %s and gender='Male' ",(i,))
			result = cursor.fetchall()
			person = [item[0] for item in result]
			maledata.append(person[0])

		for j in data:
			cursor.execute("select count(*) from registred_customers where car_brand = %s and gender = 'Female' ",(j,))
			result = cursor.fetchall()
			person = [item[0] for item in result]
			femaledata.append(person[0])

		x = np.arange(len(data))

		male = maledata
		female = femaledata

		plt.bar(x - 0.2,male,width=0.6,label='Male')
		plt.bar(x + 0.4,female,width=0.6,label='Female')

		plt.title('Customers Data')
		plt.xlabel('Car Brand')
		plt.ylabel('Car Data')

		plt.xticks(x,data)
		plt.legend(loc='upper left')

		plt.get_current_fig_manager().window.geometry("1110x550+210+70")
		plt.get_current_fig_manager().window.title("Customer Statistics Data")

		plt.show()

	Button(frame3,text='View Customers Statistics',font='verdena 12',fg='white',bg='#e41b17',width=25,height=2,activebackground='#e41b17',activeforeground='white',cursor='hand2',command=graph).place(x=20,y=550)

	root9.mainloop()

############################ End of Nineth Window #########################

def customer_contact():

	root10 = Tk()
	root10.title("Customer Contact")
	root10.geometry("1350x750+0+0")
	root10.resizable(0,0)
	root10.config(bg='white')
	icon = PhotoImage(file='car.png')
	root10.iconphoto(False,icon)

	def admin_hover(event):
		admin_button['background'] = 'mediumblue'
	def admin_unhover(event):
		admin_button['background'] = '#5453a6'

	def dashboard_hover(event):
		dashboard_button['background'] = 'mediumblue'
	def dashboard_unhover(event):
		dashboard_button['background'] = '#5453a6'

	def product_hover(event):
		product_button['background'] = 'mediumblue'
	def product_unhover(event):
		product_button['background'] = '#5453a6'

	def order_hover(event):
		order_button['background'] = 'mediumblue'
	def order_unhover(event):
		order_button['background'] = '#5453a6'

	def customer_hover(event):
		customer_button['background'] = 'mediumblue'
	def customer_unhover(event):
		customer_button['background'] = '#5453a6'

	def customer_contact_hover(event):
		customer_contact_button['background'] = 'mediumblue'
	def customer_contact_unhover(event):
		customer_contact_button['background'] = '#5453a6'

	def customer_feedback_hover(event):
		customer_feedback_button['background'] = 'mediumblue'
	def customer_feedback_unhover(event):
		customer_feedback_button['background'] = '#5453a6'

	def logout_button_hover(event):
		logout_button['background'] = 'mediumblue'
	def logout_button_unhover(event):
		logout_button['background'] = '#5453a6'

	def admin_profile():
		root10.destroy()
		profile()

	def dashboard_window():
		root10.destroy()
		dashboard()

	def car_window():
		root10.destroy()
		cars()

	def order_window():
		root10.destroy()
		orders()

	def customer_window():
		root10.destroy()
		customer()

	def customer_contact_window():
		root10.destroy()
		customer_contact()

	def customer_feedback_window():
		root10.destroy()
		customer_feedback()

	def logout_page():
		root10.destroy()
		logout()

	frame1 = Frame(root10,width=200,height=750,bg='#5453a6')
	frame1.place(x=0,y=0)
	frame2 = Frame(root10,width=1200,height=750,bg='lightgrey')
	frame2.place(x=200,y=0)

	admin_button = Button(frame1, text='Admin Profile',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=admin_profile)
	admin_button.place(x=30,y=30)
	image = Image.open('admin.jpg')
	img = image.resize((20,20))
	admin_img = ImageTk.PhotoImage(img)
	Label(frame1,image=admin_img).place(x=20,y=30)

	admin_button.bind('<Enter>',admin_hover)
	admin_button.bind('<Leave>',admin_unhover)

	
	dashboard_button = Button(frame1, text='Dashboard',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=dashboard_window)
	dashboard_button.place(x=30,y=100)
	image = Image.open('dashboard.png')
	img = image.resize((20,20))
	dashboard_img = ImageTk.PhotoImage(img)
	Label(frame1,image=dashboard_img).place(x=20,y=100)

	dashboard_button.bind('<Enter>',dashboard_hover)
	dashboard_button.bind('<Leave>',dashboard_unhover)

	product_button = Button(frame1, text='Cars',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=car_window)
	product_button.place(x=30,y=170)
	image = Image.open('car.png')
	img = image.resize((20,20))
	product_img = ImageTk.PhotoImage(img)
	Label(frame1,image=product_img).place(x=20,y=170)

	product_button.bind('<Enter>',product_hover)
	product_button.bind('<Leave>',product_unhover)

	
	order_button = Button(frame1, text='Orders',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=order_window)
	order_button.place(x=30,y=240)

	image = Image.open('order.png')
	img = image.resize((20,20))
	order_img = ImageTk.PhotoImage(img)
	Label(frame1,image=order_img).place(x=20,y=240)


	order_button.bind('<Enter>',order_hover)
	order_button.bind('<Leave>',order_unhover)

	
	customer_button = Button(frame1, text='Customers',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_window)
	customer_button.place(x=30,y=310)
	image = Image.open('customer.png')
	img = image.resize((20,20))
	customer_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_img).place(x=20,y=310)

	customer_button.bind('<Enter>',customer_hover)
	customer_button.bind('<Leave>',customer_unhover)

	customer_contact_button = Button(frame1, text='Contact To Customer',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_contact_window)
	customer_contact_button.place(x=50,y=380)

	image = Image.open('customer_contact.png')
	img = image.resize((20,20))
	customer_contact_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_contact_img).place(x=20,y=380)

	customer_contact_button.bind('<Enter>',customer_contact_hover)
	customer_contact_button.bind('<Leave>',customer_contact_unhover)

	
	customer_feedback_button = Button(frame1, text='Customer Feedback',width=18,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=customer_feedback_window)
	customer_feedback_button.place(x=50,y=450)

	image = Image.open('customer_feedback.png')
	img = image.resize((20,20))
	customer_feedback_img = ImageTk.PhotoImage(img)
	Label(frame1,image=customer_feedback_img).place(x=20,y=450)

	customer_feedback_button.bind('<Enter>',customer_feedback_hover)
	customer_feedback_button.bind('<Leave>',customer_feedback_unhover)

	logout_button = Button(frame1, text='Logout',width=20,height=1,font='verdena 10',bg='#5453a6',fg='white',border=0, activebackground='#5453a6',activeforeground='white',cursor='hand2',command=logout_page)
	logout_button.place(x=30,y=520)

	image = Image.open('logout.png')
	img = image.resize((20,20))
	logout_button_img = ImageTk.PhotoImage(img)
	Label(frame1,image=logout_button_img).place(x=20,y=520)

	logout_button.bind('<Enter>',logout_button_hover)
	logout_button.bind('<Leave>',logout_button_unhover)

	############################# Credits ########################

	Label(text='Develeoper Product',font='verdena 7',bg='#5453a6',fg='white').place(x=10,y=600)

	cursor.execute("select * from account where device_name=%s ",(socket.gethostname(),))
	res = cursor.fetchone()
	Label(frame2,text=f'Welcome {res[1]}', font='verdena 12 bold',width=100, height=2,bg='#5453a6',fg='white',padx=75).place(x=0,y=0)

	labelframe1 = LabelFrame(frame2,width=1140,height=650,bg="#5453a6")
	labelframe1.place(x=10,y=50)

	Label(labelframe1,text="Conatct to customers email address",font='verdena 15 bold',bg='#5453a6',fg='white').place(x=400,y=20)

	Label(labelframe1,text='Select Customer Data',font='verdena 12 bold',bg='#5453a6',fg='white').place(x=20,y=70)

	cid = ['']

	def selected_customer_options(event):
		data = selected_customer_data.get()
		if data == "Customer Id":
			data = "customer_id"

		cursor.execute(f"select {data} from customer_login ")
		result = cursor.fetchall()
		listoptions = [item[0] for item in result]
		selected_customer = Combobox(labelframe1,font='verdena 12',values=listoptions, width=30,state='r')
		selected_customer.place(x=630,y=70)
		if data == "customer_id":
			data = "Customer Id"
		selected_customer.set(f"Select customer {data}")

		if data == "Id":
			selected_customer.set(f"Select customer by {data}")

		def search():
			selected_data = selected_customer.get()
			ceml = customer_email

			cursor.execute("select email,id from customer_login where id =%s or name=%s or mobile=%s or email=%s or customer_id=%s ",(selected_data,selected_data,selected_data,selected_data,selected_data))
			res = cursor.fetchone()

			ceml.delete(0,'end')
			ceml.insert(0,res[0])
			cid[0] = res[1]


		search_button = Button(labelframe1,text='Search', font='verdena 12',bg='lightyellow',width=15,activebackground='lightyellow',cursor='hand2',command=search)
		search_button.place(x=950,y=63)


	selected_customer_data = Combobox(labelframe1,font='verdena 12',values=['Id','Name','Email','Mobile','Customer Id'],state='r')
	selected_customer_data.place(x=200,y=70)
	selected_customer_data.set("Select customer data")
	selected_customer_data.bind('<<ComboboxSelected>>',selected_customer_options)

	Label(labelframe1,text='Enter Customer Data',font='verdena 12 bold',fg='white',bg='#5453a6').place(x=450,y=70)

	inserted_customer_data = Entry(labelframe1,width=30,font='verdena 12')
	inserted_customer_data.place(x=630,y=70)


	def search():
		inserted_data = inserted_customer_data.get()
		ceml = customer_email

		if inserted_data == "":
			messagebox.showerror("Error","Please write customer data")
			return False

		cursor.execute("select email,id from customer_login where id =%s or name=%s or mobile=%s or email=%s or customer_id=%s ",(inserted_data,inserted_data,inserted_data,inserted_data,inserted_data))
		res = cursor.fetchone()

		ceml.delete(0,'end')
		ceml.insert(0,res[0])
		cid[0] = res[1]

	search_button = Button(labelframe1,text='Search', font='verdena 12',bg='lightyellow',width=15,activebackground='lightyellow',cursor='hand2',command=search)
	search_button.place(x=950,y=63)

	Label(labelframe1,text='Customer Email',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=150)

	customer_email = Entry(labelframe1,width=100,font='verdena 12')
	customer_email.place(x=200,y=150)

	Label(labelframe1,text='Email Subject',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=250)

	email_title = Entry(labelframe1,width=100,font='verdena 12')
	email_title.place(x=200,y=250)

	Label(labelframe1,text='Email Content',font='verdena 12',bg='#5453a6',fg='white').place(x=20,y=350)

	email_content = Text(labelframe1,width=97, height=10,font='verdena 12',pady=15,padx=15)
	email_content.place(x=200,y=350)

	def send():
		ceml = customer_email.get()
		etl = email_title.get()
		econ = email_content.get(1.0,"end")

		if ceml == "":
			messagebox.showerror("Error","Please write customer email")
			return False

		if len(ceml) < 12:
			messagebox.showerror("Error","Please write proper email address")
			return False

		if etl == "":
			messagebox.showerror("Error","Please write email subject")
			return False

		if econ == "":
			messagebox.showerror("Error","Please write email content ")
			return False

		if len(econ) < 2:
			messagebox.showerror("Error","Please write proper email content")
			return False

		else:
			cursor.execute("select name from customer_login where email=%s and id=%s ",(ceml,cid[0]))
			res = cursor.fetchone()

			if res is not None:

				try:
					connection = s.SMTP("smtp.gmail.com",587)
				except:
					messagebox.showerror("Error","No network connection is found")
					return False
				try:	
					connection.starttls()
					cursor.execute("select email,password from email_sender where device_name=%s ",(socket.gethostname(),))
					res = cursor.fetchone()
					if res is not None:
						user = res[0]
						password = res[1]
					else:
						messagebox.showerror("Error","User email is not registred please registred first")
						return False

					connection.login(user=user,password=password)
					connection.sendmail(sender,ceml,f"Subject: {etl}\n\n{econ}")
					connection.quit()
					customer_email.delete(0,'end')
					email_title.delete(0,'end')
					email_content.delete(1.0,'end')

				except:
					messagebox.showerror("Error","Network error")
					return False

				cursor.execute("insert into email_data (name,email,title,content,datetime) values(%s,%s,%s,%s,%s) ",(res[0],ceml,etl,econ,datetime.now().strftime("%d/%m/%y %H/%M/%S")))
				if conn.commit():
					pass

				messagebox.showinfo("Sucess","Email sent sucessfully")

			else:
				messagebox.showerror("Error","Sorry customer data is not found")

	send_button = Button(labelframe1,text='Send',bg='lightgreen',fg='white',font='verdena 12',width=15,activebackground='lightgreen',activeforeground='white',cursor='hand2',command=send)
	send_button.place(x=100,y=600)

	def reset():
		customer_email.delete(0,'end')
		email_title.delete(0,'end')
		email_content.delete(1.0,'end')

	reset_button = Button(labelframe1,text='Reset',bg='red',fg='white',font='verdena 12',width=15,activebackground='red',activeforeground='white',cursor='hand2',command=reset)
	reset_button.place(x=500,y=600)

	customer_mail_button = Button(labelframe1,text='View All',bg='blue',fg='white',font='verdena 12',width=15,activebackground='blue',activeforeground='white',cursor='hand2')
	customer_mail_button.place(x=900,y=600)

	image = Image.open('settings.png')
	image = image.resize((20,20))
	image = ImageTk.PhotoImage(image)

	def settings():
		root = Toplevel(root10)
		root.title("Email Settings")
		root.geometry("1000x250+300+100")
		root.resizable(0,0)
		icon = PhotoImage(file='car.png')
		root.iconphoto(False,icon)

		labelframe = LabelFrame(root,width=980,height=230,bg="#5453a6")
		labelframe.place(x=10,y=10)

		Label(root,text='User Email Settings',font='verdena 15 bold',bg='#5453a6',fg='white').place(x=400,y=15)

		Label(labelframe,text='User Email',font='verdena 12 bold',bg='#5453a6',fg='white').place(x=10,y=50)

		Label(labelframe,text='User Password',font='verdena 12 bold',bg='#5453a6',fg='white').place(x=10,y=120)

		email = Entry(labelframe,width=85,font='verdena 12')
		email.place(x=150,y=50)

		password = Entry(labelframe,width=85,font='verdena 12')
		password.place(x=150,y=120)

		cursor.execute("select email,password from email_sender where device_name=%s ",(socket.gethostname(),))
		res = cursor.fetchone()


		def save():
			eml = email.get()
			pwd = password.get()

			cursor.execute("select * from email_sender where device_name=%s ",(socket.gethostname(),))
			res = cursor.fetchone()
			if res is not None:
				cursor.execute("update email_sender set email=%s,password=%s where device_name=%s ",(eml,pwd,socket.gethostname()))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Email updated sucessfully")
				root.destroy()
			else:
				cursor.execute("insert into email_sender (email,password,device_name) values(%s,%s,%s) ",(eml,pwd,socket.gethostname()))
				if conn.commit():
					pass
				messagebox.showinfo("Sucess","Email registred sucessfully")
				root.destroy()

		save_button = Button(labelframe,text='Save',bg='green',fg='white',font='verdena 12',width=15,activebackground='green',activeforeground='white',cursor='hand2',command=save)
		save_button.place(x=250,y=170)

		def reset():
			email.delete(0,'end')
			password.delete(0,'end')

		reset_button = Button(labelframe,text='Reset',bg='red',fg='white',font='verdena 12',width=15,activebackground='red',activeforeground='white',cursor='hand2',command=reset)
		reset_button.place(x=550,y=170)

		if res is not None:
			save_button.config(text='Update')
			email.insert(0,res[0])
			password.insert(0,res[1])

		else:
			save_button.config(text='Save')


		root.mainloop()

	Button(labelframe1,image=image,cursor='hand2',command=settings).place(x=1100,y=20)

	root10.mainloop()

############################ End of Tenth Window #########################



def customer_feedback():
	webbrowser.open("Web data/feedback.php")

############################ End of Eleventh Window #########################


def today_registrations():	
	webbrowser.open("Web data/today_registration.php")

############################ End of Twelveth Window #########################


def total_registrations():	
	webbrowser.open("Web data/total_registrations.php")

############################ End of Thirteenth Window #########################


def orders():	
	webbrowser.open("Web data/orders.php")

############################ End of Fourteenth Window #########################


def checkip():
	cursor.execute("select * from logindata where device_name = %s ",(socket.gethostname(),))
	res = cursor.fetchone()
	if res is not None:
		dashboard()
	else:
		login()

checkip()
