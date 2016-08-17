import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("giacomolami@gmail.com", "Glami2015")
 
msg = "YOUR MESSAGE!"
server.sendmail("giacomolami@gmail.com", "giacomolami@yahoo.com", msg)
server.quit()
