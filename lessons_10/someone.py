import json
import pprint
import requests
from datetime import datetime as dt
from datetime import timedelta
from date_validator import is_valid_date_format
import argparse
import csv

URL = 'https://api.exchangerate.host/convert'

with open('E:\PyCharm Community Edition 2022.1.2\Hillel_Lessons\lessons_10\symbols.json') as file:
    currencies_symbols = json.load(file)


def arg_from_currency_value():
    parser = argparse.ArgumentParser(description='Passing arguments to the currency converter')
    parser.add_argument('from', default='USD', type=str)
    parser.add_argument('to', default='UAH', type=str)
    parser.add_argument('amount', default=100.0, type=float)
    parser.add_argument('--start_date', default=dt.now().date(), type=list)
    parser.add_argument('--save_to_file', action='store_true')
    args = parser.parse_args()
    return args


arg = arg_from_currency_value()


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


def check_date(par_date):
    dates_list = []
    current_date = dt.now()
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
    par_date = check_date(input("Input params date in format 2022-09-10: ").split('-'))
    values = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    date_range = par_date
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


def save_to_csv(data: list, target_file='exchange_rate.csv'):
    with open(target_file, 'w') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(data)
    print(f'The data is saved to a file - {target_file}')


# course_list_relative_date = get_api_url_and_return_data(URL)
# pprint.pprint(course_list_relative_date)

pprint.pprint(arg_from_currency_value())
