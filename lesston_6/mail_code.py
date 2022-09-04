# import datetime
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from functools import lru_cache
# import requests
# import config_file
# import validators


def delete_duplicates(func):
    """
    This function deletes duplicates from the list
    :param func: function
    :return: list
    """
    def wrapper(list_validated):
        """
        :param list_validated: list
        :return: list
        """
        no_duplicates_list = []
        temp_set = set()

        for item in list_validated:
            text_appears = f'{item}'

            if text_appears not in temp_set:
                no_duplicates_list.append(item)
                temp_set.add(text_appears)
        func(no_duplicates_list)

    return wrapper


def validate_emails(func):
    """
    This function is validating e_mails
    :param func: function
    :return: list
    """
    def wrapper(list_from_url):
        mails_validated = []
        for m in list_from_url:
            if validators.email(m['e_mail']):
                mails_validated.append(m)
        func(mails_validated)

    return wrapper


def get_data_from_url(func):
    """
    This function is getting data from url
    :param func: function
    :return: list
    """
    def wrapper(url):
        response = requests.get(url)
        data = response.json()
        func(data['data'])

    return wrapper


@lru_cache(maxsize=None)
@get_data_from_url
@validate_emails
@delete_duplicates
def get_weather_and_send(list_mails: list):
    """
    This function is getting weather from url, checking date, creating message and send it to mails from the list
    :param list_mails: list
    :return: None
    """
    now = datetime.datetime.now().date()
    for item in list_mails:
        url_with_city = config_file.URL_FOR_WEATHER.format(item['city'])
        response = requests.get(url_with_city)
        data = response.json()
        datetime.datetime.now()
        if data['weather'][0]['icon'] in config_file.weather_smiles:
            message = config_file.message_to_send.format(item['name'], now, item['city'],
                                                         data['main']['temp'], data['weather'][0]['main'],
                                                         config_file.weather_smiles[data['weather'][0]['icon']],
                                                         data['main']['humidity'])
            server = config_file.SMTP_SERVER
            PASSWORD = config_file.PASSWORD_API
            USER = config_file.USER_

            recipient = [item['e_mail']]
            sender = USER
            subject = "Wheather in your city from Serhii Turchyn"
            text = message
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

if __name__ == '__main__':

    get_weather_and_send(config_file.URL)