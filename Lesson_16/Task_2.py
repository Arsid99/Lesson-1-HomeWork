import re


class PhoneNumber:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.correct_number = re.sub(r'\D', '', self.phone_number)
        self.formatted_ua = self.format_ua_num()

    def format_ua_num(self):
        if len(self.correct_number) < 13:
            format_phone = re.sub(r"^(.*?)(0\d{2})(\d{3})(\d{2})(\d{2})$", r"(+38) \2 \3-\4-\5", self.correct_number)
            return format_phone
        else:
            return self.phone_number


if __name__ == '__main__':
    number_string = str(input('Enter phone number: '))
    number = PhoneNumber(number_string)
    print(number.format_ua_num())