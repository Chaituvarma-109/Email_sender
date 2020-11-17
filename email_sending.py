import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email = EmailMessage()

receipent_mail = input('enter the receiver email: ')

email['from'] = 'dummy'
email['to']  =  receipent_mail
email['subject'] = 'Hi! this is test mail, Dont worry!!!!!'

email.set_content('I am a good boy')

mail = input('enter your email: ')
password = input('enter your password: ')

with smtplib.SMTP(host='smtp.gmail.com',port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(mail, password)
    smtp.send_message(email)

    print('all good boss!!!')