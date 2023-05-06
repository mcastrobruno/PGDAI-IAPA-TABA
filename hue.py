# import the smtplib module. It should be included in Python by default
import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login('x22155686@student.ncirl.ie', 'Bb741852@helena')
import smtplib
import time

server = smtplib.SMTP_SSL('host', 587)
server.ehlo()
server.login('x22155686@student.ncirl.ie', 'Bb741852@helena')

server.ehlo()

print ('server working fine')

time.sleep(5)

sender = "myemail@......."

receivers = ["myemail@......"]

subject = "SMTP e-mail Test" 

msg = "This is an automated message being sent by Python. Python is the mastermind behind    this."

server.sendmail(sender, receivers, subject, msg)

print ('sending email to outlook')

server.quit()