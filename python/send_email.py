import smtplib
from email.message import EmailMessage
import os

def send_email(options):
    smtp_host = os.environ.get('SMTP_HOST')
    smtp_port = os.environ.get('SMTP_PORT')
    smtp_user = os.environ.get('SMTP_USER')
    smtp_pass = os.environ.get('SMTP_PASS')
    from_email = os.environ.get('FROM_EMAIL')

    msg = EmailMessage()
    msg['From'] = from_email
    msg['To'] = options['mail']
    msg['Subject'] = options['subject']
    msg.set_content(options['message'])

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

