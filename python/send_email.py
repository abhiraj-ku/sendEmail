import smtplib
from email.message import EmailMessage
import os

def send_email(options):
    # Check for valid email address
    if not options['mail'] or not is_valid_email(options['mail']):
        raise ValueError("Invalid email address")

    # Validate subject
    if not options['subject'] or options['subject'].strip() == "":
        raise ValueError("Subject is required")

    # Validate message
    if not options['message'] or options['message'].strip() == "":
        raise ValueError("Message body is required")

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

def is_valid_email(email):
    # Regular expression to validate email format
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(email_regex, email))
