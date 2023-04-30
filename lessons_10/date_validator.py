import calendar


def is_valid_date_format(value) -> bool:
    """Expect date in format data in str format YYYY-MM-DD"""
    if not value:
        return False

    is_valid_year = False
    is_valid_month = False
    is_valid_day = False
    value[0] = int(value[0])
    value[1] = int(value[1])
    value[2] = int(value[2])
    if 1919 < value[0] < 9999:
        is_valid_year = True
    if 0 < value[1] < 13:
        is_valid_month = True
    if all([calendar.isleap(value[0]), value[1] == 2, (0 < value[2] <= 29)]):
        is_valid_day = True
    elif all([calendar.isleap(value[0]), value[1] == 2, (0 < value[2] <= 28)]):
        is_valid_day = True
    elif value[1] in [1, 3, 5, 7, 8, 10, 12] and (0 < value[2] <= 31):
        is_valid_day = True
    elif value[1] in [4, 6, 9, 11] and 0 < value[2] <= 30:
        is_valid_day = True
    return all([is_valid_year, is_valid_month, is_valid_day])
