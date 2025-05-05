import mysql.connector
import cv2
import numpy as num
conn = mysql.connector.connect(host = 'localhost', port=3306, user = 'root', password = '' , db = 'test'

)


if conn.is_connected():
    print("Connection Established")
else:
    print("Connection Failed")

cursor = conn.cursor()


#name = input("Enter Your Name: ")
#age = int(input("Enter Your Age: "))
#position = input("Enter Your Position: ")

#query = "insert into xyz (name, age, position) values (%s, %s, %s) "
#value = (name, age, position)
#data = cursor.execute(query, value)
conn.commit()
print("Data Inserted Into Database")

sql = "select * from xyz "
dta = cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)
file = cv2.imread("background.jpg")
read = cv2.imshow('image', file)
cv2.waitKey(0)
#cv2.destroyAllWindows()
