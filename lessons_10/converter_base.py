import json
import pprint
import requests
from datetime import datetime as dt
from datetime import timedelta
from date_validator import is_valid_date_format
import argparse
from write_to_csv import write_to_csv_file

URL = 'https://api.exchangerate.host/convert'

with open('symbols.json') as file:
    currencies_symbols = json.load(file)


def create_args_from_parser():
    parser = argparse.ArgumentParser(description='The necessary values for obtaining the currency envelope result are '
                                                 'indicated')
    parser.add_argument('parameter_from', metavar='cur_from', default='USD',
                        type=str, help='Сurrency from. Default USD')

    parser.add_argument('parameter_to', metavar='cur_to', default='UAH',
                        type=str, help='Сurrency to. Default UAH')

    parser.add_argument('parameter_amount', type=float, default=100.0,
                        help='What amount needs to be converted (default: 100)')

    parser.add_argument('parameter_date', type=str, default=f'{dt.now().date()}',
                        help='Enter date in format year-month-day, for example 2022-02-24. Default - today')
    args = parser.parse_args()
    return args


def check_from(currency_from):
    if currency_from in currencies_symbols['symbols']:
        return currency_from
    return 'USD'


def check_to(currency_to):
    if currency_to in currencies_symbols['symbols']:
        return currency_to
    return 'UAH'


def check_amount(par_amount):
    if not par_amount:
        return 100.0
    return float(par_amount)


def check_date():
    dates_list = []
    current_date = dt.now()
    par_date = input("Input params date in format "
                     "2022-09-10: ").split('-')
    user_date = dt(*[int(value) for value in par_date])
    if is_valid_date_format(par_date):
        if user_date >= current_date:
            return [current_date.strftime('%Y-%m-%d')]
        else:
            while user_date <= current_date:
                dates_list.append(user_date.strftime('%Y-%m-%d'))
                user_date += timedelta(1)
            return dates_list


def get_api_url_and_return_data(url):
    currency_from = check_from(input('Input params currency in format "USD": '))
    currency_to = check_to(input('Input params currency in format "UAH": '))
    par_amount = check_amount(input('Input params amount in format "500": '))
    values = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    date_range = check_date()
    for date in date_range:
        response = requests.get(url, params={'date': date,
                                             'amount': par_amount,
                                             'from': currency_from,
                                             'to': currency_to})
        new_list = []
        data = response.json()
        new_list.append(data['date'])
        new_list.append(data['query']['from'])
        new_list.append(data['query']['to'])
        new_list.append(data['query']['amount'])
        new_list.append(data['info']['rate'])
        new_list.append(data['result'])
        values.append(new_list)
    return values

course_list_relative_date = get_api_url_and_return_data(URL)
write_to_file = write_to_csv_file(course_list_relative_date)
