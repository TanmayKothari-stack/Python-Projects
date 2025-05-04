import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='12345')
cursor = conn.cursor()

cursor.execute("create table ")

cursor.execute("show databases ")
result = cursor.fetchall()
for res in result:
	print(res)

