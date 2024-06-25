import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(user, pwd, recipient, subject, html_body):
    sender = user
    receiver = recipient if isinstance(recipient, list) else [recipient]

    # Prepare the MIME message
    message = MIMEMultipart('alternative')
    message['From'] = sender
    message['To'] = ", ".join(receiver)
    message['Subject'] = subject

    # Attach the HTML body
    html_part = MIMEText(html_body, 'html')
    message.attach(html_part)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(sender, receiver, message.as_string())
        server.close()
    except Exception as e:
        print(e)
