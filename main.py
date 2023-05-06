from csv import DictReader
import email_composer
import email_sender


with open('scheduling.csv', newline='') as csvfile:
    reader = DictReader(csvfile)
    
    for record in reader:
        name = record['patient_name']
        email = record['patient_email']
        appointment_date = record['date_and_time']

        composed_email = email_composer.compose_email(name, email, appointment_date)
        email_sender.send_email(composed_email)



