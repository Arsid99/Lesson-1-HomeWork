import re
import csv


class CarNumber:
    valid_format_number = r'^[ABCEHIKMOPTX|АВСЕНІКМОРТХ]{2}\d{4}[ABCEHIKMOPTX|АВСЕНІКМОРТХ]{2}$'
    convert_letters = {'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'I': 'І', 'K': 'К', 'M': 'М', 'O': 'О',
                       'P': 'Р', 'T': 'Т', 'X': 'Х'}

    def __init__(self):
        self.bd_code_region = {}
        self.import_bd_code_region()

    def is_car_number(self, car_number: str) -> bool:
        if re.search(self.valid_format_number, car_number) is None:
            return False
        return True

    def translated_code_in_ua(self, car_number: str) -> str:
        code_ua = ''
        code_en = car_number[:2]
        number = car_number[2:7]
        for letter in code_en:
            if ord('A') <= ord(letter) <= ord('X'):
                code_ua += self.convert_letters[letter]
            else:
                code_ua += letter
        return code_ua[:2] + number + car_number[-2:]

    def get_name_region(self, car_number: str) -> str:
        car_number = self.translated_code_in_ua(car_number)
        for region, code in self.bd_code_region.items():
            if car_number[:2] in code:
                return region
        return 'None'

    def import_bd_code_region(self):
        with open('ua_auto.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                self.bd_code_region[r['Регіон']] = [r['Код 2004'], r['Код 2013']]


def main():
    car_number = input('Enter the car number: ')
    validity = CarNumber()
    if validity.is_car_number(car_number):
        print(f'The car number: {car_number}\n Region of registration: {validity.get_name_region(car_number)}')
    else:
        print('Invalid number.')


if __name__ == '__main__':
    main()
