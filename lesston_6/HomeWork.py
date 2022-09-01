import requests
import pprint
import validators

URL = 'https://script.google.com/macros/s/AKfycby3Fp-J3N0OM5UZhg9SHgIusHBMC2kWVXSOVsP26smPTaYS_4IiOT7sVx7ZWyC3XsVW7g/exec'
WEATHER = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'


def get_data(url: str) -> dict:  # dict - відображення у словнику
    """
    We get some data from a url and reformat it into json format
    Args:
        url: URL
    Returns: data from url in json format
    """
    response = requests.get(url)
    data = response.json()['data']
    return data


def exclude_email_in_dict(func):
    def wrapper():
        new_list = []
        for elem in func:
            new_list.append(elem['e_mail'])
            continue
        return func()
    return wrapper


@exclude_email_in_dict
def exclusion_identical_elements(data):
    new_list = [dict(s) for s in set(frozenset(d.items()) for d in data)]
    return new_list

google_data = get_data(URL)

pprint.pprint(exclusion_identical_elements())

# unique_elements = exclusion_identical_elements(google_data)

# list_email = exclude_email_in_dict(unique_elements)

# pprint.pprint(list_email)
