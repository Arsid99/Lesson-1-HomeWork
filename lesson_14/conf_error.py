class MultipleError(Exception):
    def __init__(self):
        self.text = 'Enter only one argument'

    def __repr__(self):
        repr_text = 'MultipleOptionsError: (' + self.text + ')'
        return repr_text


class NoOptionsError(Exception):
    def __init__(self):
        self.text = 'No argument entered, please enter an argument'

    def __repr__(self):
        repr_text = 'NoOptionsFoundError: (' + self.text + ')'
        return repr_text


class IATAError(Exception):
    def __init__(self, iata):
        self.text = 'The value "IATA" entered is incorrect, please check and enter again'
        self.iata = iata

    def __repr__(self):
        repr_text = 'IATACodeError: (' + self.text + ', ' + self.iata + ')'
        return repr_text


class CountryError(Exception):
    def __init__(self, country):
        self.text = 'No country was found for the entered argument'
        self.country = country

    def __repr__(self):
        repr_text = 'CountryNotFoundError: (' + self.text + ', ' + self.country + ')'
        return repr_text


class CityError(Exception):
    def __init__(self, city):
        self.text = 'The city was not found for the entered argument'
        self.city = city

    def __repr__(self):
        repr_text = 'CityNotFoundError: (' + self.text + ', ' + self.city + ')'
        return repr_text


class AirportError(Exception):
    def __init__(self, airport):
        self.text = 'The airport for the entered argument was not found'
        self.airport = airport

    def __repr__(self):
        repr_text = 'AirportNotFoundError: (' + self.text + ', ' + self.airport + ')'
        return repr_text