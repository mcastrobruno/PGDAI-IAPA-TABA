from string import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create the plain-text and HTML version of your message
text = """\
Dear $name,
We would like to remind you of your appointment tomorrow $date.


Dental Clinic Ltd"""
html = """\
<html>
  <body>
    <p>Hi, $name<br>
       We would like to remind you of your appointment tomorrow $date<br>
    </p>
  </body>
</html>
"""


def compose_email(patient_name, patient_email, appointment_date) -> MIMEMultipart:

    # Format Text representation of the email
    text_obj = Template(text)
    formatted_text = text_obj.substitute(name=patient_name, date=appointment_date)
    text_part = MIMEText(formatted_text, "plain")

    # Format HTML Representation of the email 
    html_obj = Template(html)
    formatted_html = html_obj.substitute(name=patient_name, date=appointment_date)
    html_part = MIMEText(formatted_html, "html")


    # Create email Multipart object
    message = MIMEMultipart("alternative")
    message["Subject"] = "Appointment Reminder"
    message["To"] = patient_email

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(text_part)
    message.attach(html_part)

    return message