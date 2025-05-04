from tkinter import*
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',database='shopping')

cursor = conn.cursor()


def update_canvas():
    conn = mysql.connector.connect(host='localhost',user='root',password='',database='shopping')

    cursor = conn.cursor()

    canvas.delete("all")
    cursor.execute("select * from account ")
    result = cursor.fetchall()
    y = 20
    for res in result:
        canvas.create_text(200,y,text=str(res))
        y+=20
    canvas.after(1000,update_canvas)

root = Tk()
root.title("Real Time Data Canvas")
root.geometry("1100x600+150+10")

canvas = Canvas(root,width=500,height=500,bg='white')
canvas.place(x=300,y=10)


update_canvas()

root.mainloop()