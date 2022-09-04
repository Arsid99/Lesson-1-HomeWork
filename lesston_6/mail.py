import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config_file


def mail_sender(recipient: list, data_to_send: str):
    """
    sending e-mail with a receipt
    """
    server = config_file.SMTP_SERVER
    PASSWORD = config_file.PASSWORD_API
    USER = config_file.USER_

    recipient = [*recipient]
    sender = USER
    subject = 'Weather in city(Sidorenko Roman)'
    text = data_to_send
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipient)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'decorator'

    part_text = MIMEText(text, 'plain')
    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(USER, PASSWORD)
    mail.sendmail(sender, recipient, msg.as_string())
    mail.quit()
    return True
