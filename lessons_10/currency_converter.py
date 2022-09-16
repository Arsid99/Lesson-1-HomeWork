import argparse
import calendar
import csv
from datetime import datetime as dt
from datetime import timedelta
import json
from pprint import pprint
import requests


URL = 'https://api.exchangerate.host/convert'


def create_args():
    parser = argparse.ArgumentParser(description='Process currency from, currency to, amount, date  '
                                                 'and do you want to save it in file.')

    parser.add_argument('currency_from', metavar='cur_from', default='USD',
                        type=str, help='currency to convert from. Default USD')

    parser.add_argument('currency_to', metavar='cur_to', default='UAH',
                        type=str, help='currency to convert to. Default UAH')

    parser.add_argument('amount', type=float, default=100,
                        help='Amount of money, you want to convert (default: 100)')

    parser.add_argument('--start_date', type=str, default=f'{dt.now().date()}',
                        help='Enter date in format YYYY-MM-DD. Default - today')

    parser.add_argument('--save_to_file', action='store_true',
                        help='This argument is enabling to save data in file. Not saving by default')

    args = parser.parse_args()
    return args


def currency_check(cur_from: str, cur_to: str) -> bool:
    with open('E:\PyCharm Community Edition 2022.1.2\Hillel_Lessons\lessons_10\symbols.json', 'r') as symbols:
        data = json.load(symbols)
        if cur_from in data['symbols'] and cur_to in data['symbols']:
            return True
        return False


def dates_check(date: str) -> list:
    dates_list = []
    now = dt.now().date()
    if is_valid_date_format(date):
        user_date = dt(*[int(x) for x in date.split('-')]).date()
        if user_date >= now:
            dates_list.append(now.strftime('%Y-%m-%d'))
            return dates_list
        else:
            while user_date <= now:
                dates_list.append(user_date.strftime('%Y-%m-%d'))
                user_date += timedelta(1)
            return dates_list
    else:
        dates_list.append(now.strftime('%Y-%m-%d'))
        return dates_list


def converter(cur_from: str, cur_to: str, amount: float, date: str):
    if currency_check(cur_from, cur_to):
        valid_date = dates_check(date)
        result = [['DATE', 'FROM', 'TO', 'AMOUNT', 'RATE', 'RESULT']]
        for day in valid_date:
            data = requests.get(URL, params={'from': cur_from, 'to': cur_to, 'amount': str(amount), 'date': day})
            response = data.json()
            converter_list = []
            converter_list.append(response['date'])
            converter_list.append(response['query']['from'])
            converter_list.append(response['query']['to'])
            converter_list.append(response['query']['amount'])
            converter_list.append(response['info']['rate'])
            converter_list.append(response['result'])
            result.append(converter_list)
        return result
    else:
        return print('Wrong currency format')


def write_to_csv(convert_result: list, to_save_check: bool):
    if to_save_check:
        with open('currency_exchange.csv', 'w') as csv_file:
            data_writer = csv.writer(csv_file)
            data_writer.writerows(convert_result)


def is_valid_date_format(value) -> bool:
    """Expect date in format data in str format YYYY-MM-DD"""
    if not value:
        return False

    try:
        year, month, day = [int(value) for value in value.split('-')]
    except Exception:
        return False

    is_valid_year = False
    is_valid_month = False
    is_valid_day = False

    if 1919 < year < 9999:
        is_valid_year = True

    if 0 < month < 13:
        is_valid_month = True

    if all([calendar.isleap(year), month == 2, (0 < day <= 29)]):
        is_valid_day = True
    elif all([calendar.isleap(year), month == 2, (0 < day <= 28)]):
        is_valid_day = True
    elif month in [1, 3, 5, 7, 8, 10, 12] and (0 < day <= 31):
        is_valid_day = True
    elif month in [4, 6, 9, 11] and 0 < day <= 30:
        is_valid_day = True

    return all([is_valid_year, is_valid_month, is_valid_day])


if __name__ == '__main__':
    arg = create_args()
    currency_data = converter(arg.currency_from, arg.currency_to, arg.amount, arg.start_date)
    pprint(currency_data)
    write_to_csv(currency_data, arg.save_to_file)