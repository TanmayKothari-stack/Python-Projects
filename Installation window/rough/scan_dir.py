import os
import shutil
import mysql.connector
#conn = mysql.connector.connect(host = 'localhost', port='3306', user = 'root', password='Tanmay1@', db = 'hacking')

#cursor = conn.cursor()




path = 'c:/users/jitendra/desktop/'
#scan = os.scandir(path)
raw = os.listdir(path)
#open = open("plain.txt")
#read = open.read()
#print(read)
#run = 'c:/users/jitendra/pictures/'
#os.system(run)

try:
   for s in raw:
      #print(s)
         #print(res)
      bind = "%s%s" %(path,s)
      print(bind)
      des = 'c:/users/jitendra/My computer Python/Data'
      if(s[-1] == 'e' and s[-4] == '.' or s[-1] == 'k' and s[-4] == '.' or s[-1] == 'p'  or s[-1] == 'l' or s[1] == 'e' or s[-1] == 'x' or s[-1] == 't' and s[-4] == '.'):
         shutil.copy2(bind, des)

      #qry = "select data from hack where data = %s "
      #cursor.execute(qry, (s, ))
      #res = cursor.fetchone()
      #sql = "insert into hack (data) values (%s) "
      #value = (bind, )
      #cursor.execute(sql, value)
         #('')
except:
   print("Error Data File")

#qry = "select * from hack "
#dta = cursor.execute(qry)
#res = cursor.fetchall()
#for x in res:
   #print(x)
