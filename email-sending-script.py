import smtplib
import email.message
server = smtplib.SMTP('smtp.gmail.com:587')

from JuneContent import content
from emaillist import emails

email_content= content 
listofemail = emails 

msg = email.message.Message()
msg['Subject'] =' This is the subject of the email '
msg['From'] =' darsh@gmail.com'
password = " gmail password"
msg.add_header('Content-Type','Text/html')
msg.set_payload(email_content)
s= smtplib.SMTP ('smtp.gmail.com: 587')
s.starttls()

s.login(msg['From'],password)

for dest in listofemail:
    s.sendmail(msg['From'],dest.msg.as_string())
    print(f"sending to {dest}")
    
    
