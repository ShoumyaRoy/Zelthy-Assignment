"""
Assignment 1:
Write a python class that is able to send an email from the terminal to a given email address
using smtplib library.
Expected output:
$ python -m send_email.py
> Subject? <user inputs subject>
> Body? > <user inputs a one line email body>
> Recipient? <user inputs the email address of the recipient>
> Email sent!
"""
import smtplib, ssl
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(subject,body,recipient):
	port = 465
	context = ssl.create_default_context()

	path_to_json = "./email.json"
	with open(path_to_json, "r") as handler:
	    info = json.load(handler)

	email_id = info["email_id"]
	password = info["password"]

	# subject = 'shoumya.roy@gmail.com'
	# message = str(input('Body?'))
	recipient = recipient#input('Recipient? ')
	message = MIMEMultipart()
	message['From'] = email_id
	message['To'] = recipient
	message['Subject'] = subject#input('Subject? ')
	body_message = body#input('Body? ')
	body_part = MIMEText(body_message, "plain")
	# part2 = MIMEText(html, "html")
	message.attach(body_part)
	# message.attach(part2)

	with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as smtpObj:
	    smtpObj.login(email_id, password) 
	    smtpObj.sendmail(email_id, recipient, message.as_string())         
	    print("Email sent!")

subject = input('Subject? ')
body = input('Body? ')
recipient = input('Recipient? ')
send_mail(subject,body,recipient)