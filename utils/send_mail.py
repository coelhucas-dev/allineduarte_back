import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, recipient_email, subject, body):
    smtp_server = smtplib.SMTP_SSL('smtp.example.com', 465)
    smtp_server.login(sender_email, sender_password)

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    smtp_server.send_message(msg)
    smtp_server.quit()
