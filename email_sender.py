import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config


def __send_email_mock(message : MIMEMultipart):
    print(f'Sending email to: {message["To"]}')
    print('Email sent successfully')

def __send_email_smtp(message: MIMEMultipart):
    context = ssl.create_default_context()
    message["From"] = config.sender_address
    with smtplib.SMTP_SSL(config.smtp_server, config.smtp_port, context=context) as server:
        server.login(config.smtp_username, config.smtp_password)
        server.sendmail(
            config.smtp_username, message, message.as_string()
        )

def send_email(message : MIMEMultipart):
    if not config.smtp_enabled:
        __send_email_mock(message)
    else:
        __send_email_smtp(message)

    
        