import smtplib
myemail = 'sushmakotnalatanmaykothari@gmail.com'

mypassword = 'SUSHMA1234567' #fnpp qizr nmtm ehpx

connection = smtplib.SMTP("smtp.gmail.com",587)
connection.ehlo()
connection.starttls()
connection.login(user='sushmakotnalatanmaykothari@gmail.com',password="lgyqsmaukiphyaqe")

subject = "WhatsApp"
body = "Hello Hi How Are You"

msg = f"subject:{subject}\n\n{body}"

reciver = ['sushmakotnalatanmaykothari@gmail.com'] #'sushmakothari593@gmail.com']

connection.sendmail("sushmakotnalatanmaykothari@gmail.com", reciver,msg)

connection.close()