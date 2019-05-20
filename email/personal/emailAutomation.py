import environment
import os
import smtplib


userName = environment.data.user_name
passWord = environment.data.password

subject = 'Sab Moh Maya Hai'
content = 'tatti khaao'
msg = f'Subject: {subject}\n\n{content}'
with smtplib.SMTP('smtp.gmail.com', 587) as mail:
    mail.ehlo()
    mail.starttls()
    mail.ehlo()

    mail.login(userName,passWord)
    mail.sendmail(userName, 'bonn.indu@gmail.com', msg)

    mail.close()