import smtplib as s
connection = s.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user='sushmakotnalatanmaykothari@gmail.com',password="lgyqsmaukiphyaqe")

subject = "Hello"
body = "This is the first mail from te python"
connection.sendmail("sushmakotnalatanmaykothari.com","kotharijitendra960@gmail.com",f"Subject: {subject}\n\n{body}")
connection.quit()
print("Email send sucessfully")