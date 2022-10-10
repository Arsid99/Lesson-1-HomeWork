import re


class ValidityPassword:
    __PATTERN_PASSWORD = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$-+=])[a-zA-Z\d@#$-+=]{8,}$'
    __PATTERN_NUMBER = r'\d'
    __PATTERN_UPPER_LETTER = r'[A-Z]'
    __PATTERN_LOWER_LETTER = r'[a-z]'
    __PATTERN_SYMBOL = r'[@#$-+=]'
    __PATTERN_CORRECT_LENGTH = r'.{8,}'

    def check_requirements(self, password: str) -> str:
        error = {
            self.__PATTERN_NUMBER: 'There must be at least one digit.\n',
            self.__PATTERN_UPPER_LETTER: 'There must be at least 1 uppercase letter.\n',
            self.__PATTERN_LOWER_LETTER: 'There must be at least 1 letter in lower case.\n',
            self.__PATTERN_SYMBOL: 'There must be at least 1 single character: @, #, $, -, +, =.\n',
            self.__PATTERN_CORRECT_LENGTH: 'The length of the password must be at least 8 characters.\n'
        }
        ret_msg = ''
        if re.search(self.__PATTERN_PASSWORD, password) is None:
            for pattern, msg in error.items():
                if re.search(pattern, password) is None:
                    ret_msg += msg
            return ret_msg

        return 'The password is correct'


def client_code():
    msg = ''
    validity = ValidityPassword()
    while msg != 'The password is correct':
        password = input('Enter your password: ')
        msg = validity.check_requirements(password)
        print(msg)


if __name__ == '__main__':
    client_code()
