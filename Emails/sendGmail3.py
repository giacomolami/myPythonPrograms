import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
fromaddr = "giacomolami@gmail.com"
toaddr = "giacomolami@yahoo.com"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Salute! Welcome to Wine4you"
 
body = "Congratulations! You have been register on Wine4you, please access the site for wine raccomandations and social events." 
 
msg.attach(MIMEText(body, 'plain'))
 
#filename = ""
#attachment = open("/Users/giacomo.lami/code/Apps2016.pdf", "rb") 
#part = MIMEBase('application', 'octet-stream')
#part.set_payload((attachment).read())
#encoders.encode_base64(part)
#part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
#msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Glami2015")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

