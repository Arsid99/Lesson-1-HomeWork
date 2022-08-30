import requests
import task_3

URL = 'https://script.google.com/macros/s/AKfycbymRVgeEy91KPw13H3-MCbt8Xh4BDgFa6jQ8jD4BPhjkpjSBmdaPYvi0I6lqpPxcjy-7Q/exec'


def min_max_value(integer: int, min_value=0, max_value=100) -> bool:
    """
    Check if the input argument is an integer in a range
    Args:
        integer: int
        min_value: 0
        max_value: 100

    Returns: if the integer is in the min-max range, then it is true

    """
    valid_object = integer
    if min_value < valid_object < max_value:
        return True
    return False


def is_elem_int_in_dict(value: int | str | float) -> bool:
    """
    Check if the input argument is an integer
    Args:
        value: anything

    Returns: if value is integer - true

    """
    if type(value) == int:
        return True
    return False


def get_data(url: str = None) -> dict:  # dict - відображення у словнику
    """
    Conversion of the link in json format
        Args:
            url: We get the URL to the API table

        Returns: data from url in json format

        """
    response = requests.get(url)
    data = response.json()
    return data


def max_lenght_some_value(data, lenght=150):
    """
    The function receives text and truncates it to a certain number of characters
    Args:
        data: dict
        lenght: int (Maximum number of text characters)
    Returns: Truncated text, everything after truncation is replaced with "..."
    """
    new_list = []
    for elem in data:
        if len(elem) > lenght:
            result = elem[:lenght - 3] + '...'
            new_list.append(result)
            continue
        return data
    return new_list


def work_with_files_append(part_to_file: str = 'test_file.txt', data=''):
    """

    Args:
        part_to_file: The name of the file where we save the data
        data:Data type in the form of a string

    Returns:Saves the given data to a file

    """
    with open(part_to_file, 'a', encoding='utf-8') as file:
        file.write(data)


assert is_elem_int_in_dict(123) == True
assert is_elem_int_in_dict('123') == False
assert min_max_value(99) == True
assert min_max_value(123) == False
# check if the function outputs any data
assert get_data(URL), 'We have got an empty object'
# understand that we get a dictionary, check if it's true
assert type(get_data(URL)) == dict, 'We have got not a dict'
# outputting the function through pprint, we saw that there is a dictionary with a list of dictionaries named 'data', we check whether there are such
assert 'data' in get_data(URL)
# checking if a list of dictionaries exists in the data dictionary
assert type(get_data(URL)['data']) == list
# check if the function is receiving any data
assert max_lenght_some_value(task_3.getting_the_text_element)
# we know that the function receives a list, check if this list exists
assert type(max_lenght_some_value(task_3.getting_the_text_element)) == list
# we know the length of the list is 6 (that's 6 students)
assert len(max_lenght_some_value(task_3.getting_the_text_element)) <= 6
