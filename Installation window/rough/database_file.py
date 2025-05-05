import mysql.connector
import shutil
import cv2
import os
conn = mysql.connector.connect(host = "localhost", user = "root", password = "", db = "tanmay")

#if conn.is_connected:
 #   print("Connetion Established")
cursor = conn.cursor()

file = input("Enter Your File Name: ")
copy = shutil.copy(file, 'My computer Python')
qry = "insert into data (file) values (%s) "
value = (file, )
insert = cursor.execute(qry, value)
sql = "select file from data "
dta = cursor.execute(sql)
res = cursor.fetchall()
for x in res:
    x = x
dis = list(x)
#print(dis)
def convertTuple(tup):
    str = ''.join(tup)
    return str
data = convertTuple(dis)
print(data)
#print(img[-1])
if(data[-1] == "t" or data[-1] == "p" or data[-1] == "l"):
    f = open(data)
    r = f.read()
    print(r)
    #print("This Is Not A Image File")
if(data[-1] == "g"):
    filer = cv2.imread(data)
    read = cv2.imshow("image", filer)
    cv2.waitKey(0)
if(data[-1] == "3"):
    os.system(data)
if(data[-1] == "4"):
    os.system(data)


