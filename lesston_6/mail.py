import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = 'smtp.ukr.net'
PASSWORD_API = 'FHTQiLiwB0WZ6Roj'
USER_ = 'test_hillel_api_mailing@ukr.net'
password_for_email = 'qwertyuiop123456789'


def mail_sender(recipient: list, data_to_send: str):
    """
    sending e-mail with a receipt
    """
    server = SMTP_SERVER
    PASSWORD = PASSWORD_API
    USER = USER_

    recipient = [*recipient]
    sender = USER
    subject = 'Тема сообщения'
    text = data_to_send

    # for sending a file-----------------
    filepath = "task_1.py"

    from os.path import exists
    file_exists = exists(filepath)
    if not file_exists:
        print('file unavailable')
        return False
    basename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)
    # ------------------------------------

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = 'Python script <' + sender + '>'
    msg['To'] = ', '.join(recipient)
    msg['Reply-To'] = sender
    msg['Return-Path'] = sender
    msg['X-Mailer'] = 'decorator'

    part_text = MIMEText(text, 'plain')

    # for sending a file----------------------------------------------------------------------
    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(basename))
    part_file.set_payload(open(filepath, "rb").read())
    part_file.add_header('Content-Description', basename)
    part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(basename, filesize))
    encoders.encode_base64(part_file)
    msg.attach(part_file)
    # ----------------------------------------------------------------------------------------

    msg.attach(part_text)

    mail = smtplib.SMTP_SSL(server)
    mail.login(USER, PASSWORD)
    mail.sendmail(sender, recipient, msg.as_string())
    mail.quit()
    return True

mail_sender(('test_hillel_api_mailing@ukr.net', 'w.i.k.mailua@gmail.com'), 'kldsgvjdf')
