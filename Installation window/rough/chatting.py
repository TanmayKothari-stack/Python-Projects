import tkinter
from tkinter import*
import PIL
from PIL import ImageTk, Image
import mysql.connector
conn = mysql.connector.connect(host = 'localhost', user='root', password = '', db='chat_room')

cursor = conn.cursor()
import tkinter
from tkinter import *
from tkinter import ttk, Checkbutton, RADIOBUTTON, Text, messagebox, ttk, Scrollbar
import PIL
from PIL import ImageTk, Image
import random
import smtplib
from plyer import notification
import socket
import threading
import time

global agrees
def agrees():
	try:
		global root2
		root2 = Tk()
		root2.title('Whatsapp')
		root2.geometry("1352x690+0+0")
		root2.resizable(0,0)
		root2.resizable(1,1)
		root2.resizable(0,0)
		icon = PhotoImage(file='whatsapp.png')
		root2.iconphoto(False,icon)

		def check():
			if email.get() == "":
				messagebox.showerror("Error","Please Write your Email Address")
				root2.destroy()
				agrees()
				return False
			if len(email.get()) < 12:
				messagebox.showerror("Error","Please write correct Email Address")
				root2.destroy()
				agrees()
				return False
			if email.get().isdigit():
				messagebox.showerror("Error","Please Write Only Characters")
				root2.destroy()
				agrees()
			else:

				try:
					connection = smtplib.SMTP("smtp.gmail.com",587)
					connection.ehlo()
					connection.starttls()
					connection.login(user='sushmakotnalatanmaykothari@gmail.com',password="lgyqsmaukiphyaqe")

					global body
					subject = "WhatsApp"
					body = random.randint(000000, 999999)
					if body <= 99999:
						body = 978525

					msg = f"subject:{subject}\n\n Your OTP Number {body}"

					reciver = email.get() #'sushmakothari593@gmail.com']

					#connection.sendmail("sushmakotnalatanmaykothari@gmail.com", reciver,msg)

					connection.close()
					notification.notify(title="WhatsApp Verification",message=f"Your Whatsapp OTP number {body}",app_icon="whatsapp.ico",timeout=10)
					global emaildata
					emaildata = email.get()
					root2.destroy()
					verify()
				except:
					messagebox.showerror("Error","Please connect to your Internet")

		Label(root2, text='Enter Your Email', font='veredena 25 bold', fg='black').place(x=500, y=20)

		Label(root2, text='WhatsApp Needs To verify your account', font='veredena 15', fg='black', padx=15).place(x=500, y=100)
		global email
		email = Entry(root2, fg='black', font='veredena 15', width=30)
		email.place(x=520, y=150)
		Next = Button(root2, text='Next', fg='white', bg='green', font='veredena 12', width=55, activebackground='green', activeforeground='white', pady=10, command=check)

		Next.place(x=450, y=600)
	except:
		#messagebox.showerror("Error","Something went wrong")
		print()
############### End of Second Window #############


def verify():
	try:
		global root3
		root3 = Tk()
		root3.title('Whatsapp')
		root3.geometry("1352x690+0+0")
		root3.resizable(0,0)
		root3.resizable(1,1)
		root3.resizable(0,0)
		icon = PhotoImage(file='whatsapp.png')
		root3.iconphoto(False,icon)

		def sign():
			root3.destroy()
		def verfication():
			if otp.get() == "":
				messagebox.showerror("Error","Please Write OTP number")
				root3.destroy()
				verify()
				return False
			if len(otp.get()) > 6 or len(otp.get()) < 6:
				messagebox.showerror("Error", "Please write correct otp number")
				root3.destroy()
				verify()
				return False
			if not otp.get().isdigit():
				messagebox.showerror("Error", "Please Write Only Numbers")
				root3.destroy()
				verify()
				return False
			if int(otp.get())!= body:
				messagebox.showerror("Error","Wrong OTP Please Write correct OTP")
				root3.destroy()
				verify()
				return False
			else:
				messagebox.showinfo("Sucess","Verification Sucessful")
				root3.destroy()
				signuppage()

		Label(root3, text='Verifying Your email', font='veredena 25 bold', fg='green').place(x=500, y=20)

		Label(root3, text='Wating Automatically to send OTP on your email', font='veredena 15', fg='black').place(x=450, y=100)

		Label(root3, text=emaildata, font='veredena 15 bold', fg='black').place(x=900, y=100)

		otp = Entry(root3, fg='black', font='veredena 15', width=30)
		otp.place(x=500, y=150)

		Label(root3, text='Enter 6-digit code', font='veredena 15', fg='black').place(x=600, y=200)

		signup = Button(root3, text='Wrong Email?', fg='steelblue', font='veredena 12', activeforeground='steelblue', border=0, command=sign)

		signup.place(x=840, y=30)

		verifed = Button(root3, text='Verify', fg='white', bg='green', font='veredena 12', width=55, activebackground='green', activeforeground='white', pady=10, command=verfication)

		verifed.place(x=450, y=600)
	except:
		messagebox.showerror("Error","Something went wrong")
	root3.mainloop()

############### End of Third Window #############

global welcomepage
def welcomepage():
		global root4
	#msg = messagebox.askquestion("Message","If You forgot your password you have to registerd first do you want to register?")
	#if msg=='yes':
		root.destroy()
		root4 = Tk()
		root4.title("WhatsApp")
		root4.geometry("1352x690+0+0")
		root4.resizable(0,0)
		icon = PhotoImage(file='whatsapp.png')
		root4.iconphoto(False,icon)


		image1 = Image.open('whatsapp.png')
		image1 = image1.resize((250, 250))
		img1 = ImageTk.PhotoImage(image1)
		Label(root4,image=img1).pack()
		def agree():
			root4.destroy()
			agrees()
		Label(root4, text='Welcome to WhatsApp', font='veredena 25 bold', fg='black').place(x=500, y=400)
		Label(root4, text='Read our Privacy Policy. Tap "Agree and continue to accept Terms of Service"', font='veredena 10 bold', fg='black').place(x=450, y=500)

		agree = Button(root4, text='Agree and continue', fg='white', bg='green', font='veredena 12', width=55, activebackground='green', activeforeground='white', pady=10, command=agree)

		agree.place(x=450, y=600)
		root4.mainloop()

############### End of Fourth Window #############

global signuppage

def signuppage():

	root5 = Tk()
	root5.title("WhatsApp")
	root5.geometry("1352x690+0+0")
	root5.resizable(0,0)
	icon = PhotoImage(file='whatsapp.png')
	root5.iconphoto(False,icon)

	def gotologin():
		if nm.get()=='':
			messagebox.showerror("Error",'Please write your Name')
			return False
		if len(nm.get()) < 2:
			messagebox.showerror('Error','Please write correct Name')
			return False
		if pwd.get()=='':
			messagebox.showerror('Error','Please write correct Password')
			return False
		if len(pwd.get()) < 6:
			messagebox.showerror("Error","Please write your correct Password")
			return False
		if cpwd.get()=='':
			messagebox.showerror("Error","Please write your Conform Password")
			return False
		if pwd.get()!=cpwd.get():
			messagebox.showerror('Error','Your Password and Conform Password did not match please try again')
			return False
		if eml.get()=='':
			messagebox.showerror("Error","Please write your Email")
			return False
		if len(eml.get()) < 12:
			messagebox.showerror("Error","Please write your correct Email")
			return False
		if eml.get()!=emaildata:
			messagebox.showerror("Error","Please write your correct Email")
			messagebox.showerror("Error","This Email does'nt match with your verification Email")
			return False
		else:
			cursor.execute("select email, password from acoount where email=%s or password=%s",(eml.get(),pwd.get()))
			res = cursor.fetchone()
			if res is not None:
				nm.delete(0,END)
				pwd.delete(0,END)
				cpwd.delete(0,END)
				eml.delete(0,END)
				messagebox.showerror("Error","This Account is already Exits")
				return False
			else:
				cursor.execute("insert into acoount (name, email, password, conformpass) values(%s,%s,%s,%s)",(nm.get(),eml.get(),pwd.get(),cpwd.get()))
				if conn.commit():
						messagebox.showinfo("Sucess", "Data Sucessfully Inserted")
				nm.delete(0,END)
				pwd.delete(0,END)
				cpwd.delete(0,END)
				eml.delete(0,END)
				messagebox.showinfo('Sucess','Signup Sucessfully')
				root5.destroy()
				#loginpage()
				checkip()

	frame1 = Frame(root5, width=666,height=690, bg="lightgrey")
	frame1.place(x=320, y = 55)
	Label(root5, text='Signup Page', font='verdena 15 bold',height=2,bg='green',fg='white',width=1352).pack(side=TOP)
	image = Image.open('whatsapp.png')
	image = image.resize((150,150))
	img=ImageTk.PhotoImage(image)
	Label(root5,image=img,bg='lightgrey').pack()
	Label(frame1,text='WhatsApp allows user agrees all terms and conditions before Signup',font='veredena 12 bold',bg='lightgrey',fg='black').place(x=80,y=200)
	Label(frame1,text='Name',font='veredena 15',bg='lightgrey',fg='black').place(x=20,y=300)
	nm=Entry(frame1,font='veredena 12',width=45)
	nm.place(x=150,y=300)

	Label(frame1,text='Password',font='veredena 15',bg='lightgrey',fg='black').place(x=20,y=380)
	pwd=Entry(frame1,font='veredena 12',width=45,show='*')
	pwd.place(x=150,y=380)

	Label(frame1,text='Conformpass',font='veredena 15',bg='lightgrey',fg='black').place(x=20,y=460)
	cpwd=Entry(frame1,font='veredena 12',width=45,show='*')
	cpwd.place(x=150,y=460)

	Label(frame1,text='Email',font='veredena 15',bg='lightgrey',fg='black').place(x=20,y=540)
	eml=Entry(frame1,font='veredena 12',width=45)
	eml.place(x=150,y=540)

	Button(frame1,text='Signup',font='veredena 15',bg='green',fg='white',cursor='hand2', border=0, activebackground='green', activeforeground='white',command=gotologin,width=50,padx=10).place(x=50,y=590)	

	root5.mainloop()

	############### End of Fifth Window #############

def chatroom():
	global message
	root6 = Tk()
	root6.title("WhatsApp")
	root6.geometry("1352x690+0+0")
	root6.config(bg='ivory')
	root6.resizable(0,0)
	icon = PhotoImage(file='whatsapp.png')
	root6.iconphoto(False,icon)

	def sendmsg():
		if writemsg.get(1.0,"end-1c")!="" or len(writemsg.get(1.0,"end-1c"))>2:
			cursor.execute("insert into chats (ip,message) values(%s,%s)",(socket.gethostname(),writemsg.get(1.0,"end-1c")))
			print(writemsg.get(1.0,"end-1c"))
			writemsg.delete(1.0,"end-1c")
			if conn.commit():
				pass
	def recivemsg():
		sy = 40
		ry = 30
		cursor.execute("select ip,message from chats")
		result = cursor.fetchall()
		for res in result:
			if res[0]!=socket.gethostname():

					sdata = ''.join(res)
					smsg = Label(root6,text=f'From Client: {res[1]}',font='veredena 12',bg='lightgrey',fg='black')
					sy+=50
					smsg.place(x=900,y=sy)
			else:
					rdata = ''.join(res)
					rmsg = Label(root6,text=f'From You: {res[1]}',font='veredena 12',bg='green',fg='white')
					ry+=50
					rmsg.place(x=50,y=ry)

	#recivemsg()

	def recive():
		while True:
			try:
				data = socket_client.recv(1024)
				if not data:
					break
					#pass
				time.sleep(1)
				message = data.decode("utf-8")
				print(message)
			except Exception as e:
				break
				print(e)
	def send():
		#while True:
			try:
				message = writemsg.get(1.0,"end-1c")
				socket_client.send(message.encode("utf-8"))
				writemsg.delete(1.0,"end-1c")
				
			except Exception as e:
				#break
				print(e)
				socket_client.close()
				#pass
	Label(root6,text='Enjoy your live chatting with your friends',bg='green',fg='white',font='veredena 15 bold',width=200,height=2).pack(side=TOP)
	writemsg = Text(root6,width=140,font='veredena 12',pady=10,padx=10)
	writemsg.place(x=0,y=650)
	#img = Image.open('send.png')
	#resizeimg = img.resize((50,50))
	#sendimg = ImageTk.PhotoImage(resizeimg)
	sendmsgbtn = Button(root6,text='Send',bg='#7fe817',fg='white',font='veredena 12',cursor='hand2',activebackground='#7fe817',activeforeground='white',border=0,command=send)
	sendmsgbtn.place(x=1300,y=650)
	
	host = 'localhost'
	port = 8080
	while True:
		try:
			socket_client = socket.socket()
			socket_client.connect((host,port))
			break
		except Exception as e:
			time.sleep(1)
	recive_thread = threading.Thread(target=recive)
	send_thread = threading.Thread(target=send)
	recive_thread.start()
	send_thread.start()
			
	root6.mainloop()

	############ End of sixth window #############

def checkip():
	host = socket.gethostname()
	cursor.execute("select * from logindata where ip = %s ",(host,))
	result = cursor.fetchone()
	if result==None:
		loginpage()
	else:
		chatroom()

global loginpage

def loginpage():
	global root
	root = Tk()
	root.title("WhatsApp")
	root.geometry("1352x690+0+0")
	root.resizable(0,0)
	icon = PhotoImage(file='whatsapp.png')
	root.iconphoto(False,icon)


	def logined():
		ip = socket.gethostname()
		if eml.get()=='':
			messagebox.showerror("Error","Please write your Email")
			return False
		if len(eml.get()) < 12:
			messagebox.showerror("Error","Please write your correct Email")
			return False
		if pwd.get()=='':
			messagebox.showerror("Error","Please write your Password")
			return False
		if len(pwd.get()) < 6:
			messagebox.showerror("Error","Please write your correct Password")
			return False
		else:
			cursor.execute("select email, password from acoount where email=%s and password=%s",(eml.get(),pwd.get()))
			res = cursor.fetchone()
			if res is not None:
				eml.delete(0, END)
				pwd.delete(0, END)
				messagebox.showinfo("Sucess","Logined Sucessfully")
				cursor.execute("insert into logindata (ip) values(%s)",(ip,))
				if conn.commit():
					pass
				root.destroy()
				chatroom()
			else:
				eml.delete(0, END)
				pwd.delete(0, END)
				messagebox.showerror('Error','Please write correct Email and Password')

	def forgotpassword():
		msg = messagebox.askquestion("Message","If you are forgot your password you have to Verify first your email do you want to verify?")
		if msg=='yes':
			root.destroy()
			agrees()

	Label(root, text='Login Page', font='verdena 15 bold',height=2,bg='green',fg='white',width=1352).pack(side=TOP)
	frame1 = Frame(root, width=666,height=690, bg="lightgrey")
	frame1.place(x=320, y = 55)
	image = Image.open('whatsapp.png')
	image = image.resize((250,250))
	img=ImageTk.PhotoImage(image)
	Label(root,image=img,bg='lightgrey').pack()

	Label(frame1,text='WhatsApp allows user agrees all terms and conditions before Login',font='veredena 12 bold',bg='lightgrey',fg='black').place(x=80,y=250)
	Label(frame1,text='Email',font='veredena 15',bg='lightgrey',fg='black').place(x=20,y=355)
	eml=Entry(frame1,font='veredena 12',width=45)
	eml.place(x=150,y=350)

	Label(frame1,text='Password',font='veredena 15',bg='lightgrey',fg='black').place(x=20,y=430)
	pwd=Entry(frame1,font='veredena 12',width=45,show='*')
	pwd.place(x=150,y=430)

	Button(frame1,text='Forgot Password',font='veredena 12',bg='lightgrey',fg='black',cursor='hand2', border=0, activebackground='lightgrey',command=forgotpassword).place(x=250,y=480)
	Button(frame1,text='New user Signup?',font='veredena 12',bg='lightgrey',fg='black',cursor='hand2', border=0, activebackground='lightgrey',command=welcomepage).place(x=250,y=520)
	Button(frame1,text='Login',font='veredena 15',bg='green',fg='white',cursor='hand2', border=0, activebackground='green', activeforeground='white',command=logined,width=50,padx=10).place(x=50,y=590)
	root.mainloop()


#loginpage()
#chatroom()
checkip()