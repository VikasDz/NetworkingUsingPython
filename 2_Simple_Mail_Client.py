from cgitb import text
from fileinput import filename
from http import server
import smtplib #SMTP is a Protocal use To Send Mail.
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com' , 25)

server.ehlo()

with open('password.text', 'r') as f:
    password = f.read()

server.login('Your Username', password)

msg = MIMEMultipart()
msg['From'] = 'SatYam'
msg['To'] = 'YourEmail@gmail.com'
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'coding.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail()

