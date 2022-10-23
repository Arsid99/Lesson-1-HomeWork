import argparse
import csv
from pprint import pp
from conf_error import *


def arguments_parce():
    parser = argparse.ArgumentParser(description='Choose only one key to find airport info')
    parser.add_argument('--iata_code', type=str, metavar='iata',
                        help='Enter IATA code of an airport, for example - "00A"', default=None)
    parser.add_argument('--country', type=str, metavar='country',
                        help='Enter country of an airport, for example - "US"', default=None)
    parser.add_argument('--name', type=str, metavar='name',
                        help='Enter name of an airport, for example - "Kharkiv International Airport"', default=None)

    args = parser.parse_args()
    return args


def arguments_check(func):
    def wrapper(iata, country, name):
        try:
            if iata is None and country is None and name is None:
                return NoOptionsError()
            if iata is not None and country is not None and name is not None:
                return MultipleError()
            if iata is None and country is not None and name is not None:
                return MultipleError()
            if iata is not None and country is None and name is not None:
                return MultipleError()
            if iata is not None and country is not None and name is None:
                return MultipleError()

        except NoOptionsError as NOE:
            print(NOE.__repr__())

        except MultipleError as MOE:
            print(MOE.__repr__())

        return func(True, iata, country, name)

    return wrapper


def is_iata_format_valid(iata: str = None) -> bool:
    if len(iata) == 3:

        if iata.isupper():
            return True
        else:
            return False

    return False


@arguments_check
def airport_search(validator, iata, country, name):
    if validator:
        if iata is not None:
            return airport_iata_search(iata)
        if country is not None:
            return airport_country_search(country)
        if name is not None:
            return airport_name_search(name)


def airport_iata_search(iata):
    with open('airport-codes_csv.csv', encoding='utf-8') as file:
        airports = csv.reader(file)
        data = []

        if is_iata_format_valid(iata):
            for row in airports:
                if iata in row[9]:
                    data.append(row)
        else:
            return IATAError(iata)

    try:
        if len(data) == 0:
            return AirportError(iata)
        return data

    except AirportError as AE:
        print(AE.__repr__())

    except IATAError as IE:
        print(IE.__repr__())


def airport_country_search(country):
    with open('airport-codes_csv.csv', encoding='utf-8') as file:
        airports = csv.reader(file)
        data = []

        for row in airports:
            if country in row[5]:
                data.append(row)

    try:
        if len(data) == 0:
            return CountryError(country)
        return data

    except CountryError as CE:
        print(CE.__repr__())


def airport_name_search(name):
    with open('airport-codes_csv.csv') as file:
        airports = csv.reader(file)
        data = []

        for row in airports:
            if name in row[2]:
                data.append(row)

    try:
        if len(data) == 0:
            return AirportError(name)
        return data

    except AirportError as AE:
        print(AE.__repr__())


if __name__ == '__main__':
    arg = arguments_parce()
    pp(airport_search(arg.iata_code, arg.country, arg.name))
