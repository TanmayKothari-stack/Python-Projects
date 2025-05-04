from tkinter import*

root = Tk()
root.geometry("1000x600+200+50")
root.resizable(0,0)
def on_scroll(*args):
    canvas.yview(*args)
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

canvas = Canvas(root,width=500,height=500,bg='lightgrey',scrollregion=(0,0,800,600))
Label(canvas,text='Customer Login Details',font='verdena 12 bold',width=50,bg='mediumblue', fg='white',pady=10).place(x=0,y=0)

scrollbar = Scrollbar(root, orient='vertical',command=on_scroll)
for i in range(1,1001):
    label = canvas.create_text(200,i*50,text=f'{i}',font='verdena 12')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.place(x=300,y=50)
scrollbar.pack(fill='y',side='right')

root.mainloop()