"""
    @author : Gökhan ÖZELOĞLU

    @date : 19.08.2018

    @email : gozeloglu@gmail.com

    @WARNING : 1) You must add the email's into "user_list.txt" file.
               2) You must change the "from_address" with your mail address.
               3) You must write your "password"
               4) The most important things is that you must allow "less secure apps" on your gmail account.
               The link to allow : "
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def read_users():
    user_list = []

    with open("user_list.txt") as fp:
        for line in fp:
            user_list.append(line.strip().split("\n"))

    return user_list


def read_mail():
    mail = ""

    with open("mail.txt") as fp:
        for line in fp:
            mail += line
    return mail


from_address = "gozeloglu@gmail.com"    # My mail address. You must change with your mail address.

message = MIMEMultipart()
message['From'] = from_address

message['Subject'] = "Python email"     # The subject line. This can be changed with your mail's subject.

body_message = read_mail()    # You can write your mail here.
message.attach(MIMEText(body_message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.ehlo()

password = ""   # The mail address's password should be written here.

server.login("gozeloglu", password)
text = message.as_string()

users = read_users()
for user in users:
    message['To'] = user
    server.sendmail(from_address, user, text)

server.quit()
