import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user='root', password = '', db='chat_room')

cursor = conn.cursor()

close_app = False
while not close_app:
    qry =  "select chats from chat "
    cursor.execute(qry)
    data = cursor.fetchall()

    for x in data:
        x = x
        dis = list(x)
        def convert(tup):
            str = ''.join(tup)
            return str
        result = convert(dis)
        display = f"{result}\n"

        print(display)
    
    msg = input("Type a message: ")
    if(msg == ""):
        print("Please write a message first")
    elif(msg =="Delete" or msg =="delete"):
        sql = "delete from chat"
        cursor.execute(sql)
    else:
        query = "insert into chat (chats) values (%s) "
        value = (msg, )
        cursor.execute(query, value)

        conn.commit()
        print("Message Sent Sucessfully\n")
