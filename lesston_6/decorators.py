import requests
import validators
import functools
import mail
import datetime
import configuration

now = datetime.datetime.now().date()
URL = 'https://script.google.com/macros/s/AKfycby3Fp-J3N0OM5UZhg9SHgIusHBMC2kWVXSOVsP26smPTaYS_4IiOT7sVx7ZWyC3XsVW7g/exec'
WEATHER = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'


@functools.lru_cache
def get_data_from_api_url(url):
    response = requests.get(url)
    data = response.json()
    return data


def exclusion_identical_elements(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        email_set = set()
        unique_elements = []
        for elem in result:
            new_tuple = tuple(elem.items())
            if new_tuple not in email_set:
                email_set.add(new_tuple)
                unique_elements.append(elem)
        return unique_elements

    return wrapper


def checking_email_in_dictionary(function):
    def wrapper(*args, **kwargs):
        list_of_valid_data = []
        result = function(*args, **kwargs)
        for elem in result:
            if validators.email(elem['e_mail']):
                list_of_valid_data.append(elem)
        return list_of_valid_data

    return wrapper


def email_sender_decorator(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        list_of_recipient = {}
        for elem in result:
            if type(elem) == dict and 'e_mail' in elem and 'city' in elem:
                if elem['city'] not in list_of_recipient:
                    list_of_recipient.update({elem['city']: {elem['e_mail']}})
                else:
                    list_of_recipient[elem['city']].add(elem['e_mail'])
        for city in list_of_recipient:
            weather = get_data_from_api_url(WEATHER.format(city_name=city))
            result_string = configuration.MSG.format(now, weather['name'], weather['main']['temp'],
                                                   weather['weather'][0]['main'],
                                                   configuration.weather_icon[weather['weather'][0]['icon']],
                                                   weather['main']['humidity'])
            mail.mail_sender(list_of_recipient[city], result_string)

    return wrapper


@email_sender_decorator
@exclusion_identical_elements
@checking_email_in_dictionary
def weather_sending(url):
    new_data = get_data_from_api_url(url)['data']
    return new_data


weather_sending(URL)
