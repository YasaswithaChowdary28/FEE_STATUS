import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

otp = random.randint(1111,9999)

smtp_server = "smtp.gmail.com"
smtp_port = 587

username = "yasaswithachowdary28@gmail.com"
password = "yhli srfc vvhz othw"

from_email = "yasaswithachowdary28@gmail.com"
to_email = input("Enter email to send OTP: ")
subject = "OTP Validation"
body = f"OTP Validation is {otp}. \nThank You."

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(username,password)
server.send_message(msg)
server.quit()

print("Email Sent")
attempts = 5
for i in range(attempts):
    x=int(input(f"Enter OTP Received to your mail({attempts - i}) attempts left: "))
    if(x == otp):
        print("Valid")
        break
    else:
        if i < attempts - 1:
            print(f"Invalid, Try Again. You have {attempts - i - 1} attempts left.")
        else:
            print("Invalid, No Option Left")
