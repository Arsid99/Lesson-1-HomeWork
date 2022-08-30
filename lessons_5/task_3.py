import requests
import datetime
import msg

URL = 'https://script.google.com/macros/s/AKfycbymRVgeEy91KPw13H3-MCbt8Xh4BDgFa6jQ8jD4BPhjkpjSBmdaPYvi0I6lqpPxcjy' \
      '-7Q/exec'
now = datetime.datetime.now().date()
unic = '\U0001F479'


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


def get_data(url: str = None) -> dict:
    """
Conversion of the link in json format
    Args:
        url: We get the URL to the API table

    Returns: data from url in json format

    """
    response = requests.get(url)
    data = response.json()['data']
    return data


def check_score(data, score=80):
    """
Checking that the number of points is more than 80
    Args:
        data: In this case, it is some data, namely a list from which we extract elements and process them

        score: The minimum number of points for the verification

    Returns: Returns items with a score greater than 80

    """
    new_list = []
    for elem in data:
        if elem['score'] > score:
            new_list.append(elem)
    return new_list


def check_rewards(data, has_reward=True):
    """
Checks that the items reward parameter is true
    Args:
        data: In this case, it is some data, namely a list from which we extract elements and process them
        has_reward: Checking the reward availability parameter

    Returns: Returns the elements that contain the value of receiving a reward

    """
    new_list = []
    for elem in data:
        if elem['has_reward'] == has_reward:
            new_list.append(elem)
    return new_list


def check_age(data, min_age=9, max_age=18):
    """
Checks whether the age argument matches the specified range
    Args:
        data: In this case, it is some data, namely a list from which we extract elements and process them
        min_age: Determination of the MINIMUM age for verification
        max_age: Determination of the MAXIMUM age for verification

    Returns: Returns elem that are age-appropriate

    """
    new_list = []
    for elem in data:
        if min_age < elem['age'] < max_age:
            new_list.append(elem)
    return new_list


def add_elem_text_to_dict(data):
    """
Add an item to each dictionary in the list
    Args:
        data: A list of dictionaries to each of which you want to add a 'text' element

    Returns: We get a list of dictionaries with the added element

    """
    for elem in data:
        elem['text'] = str(msg.STUDENTS_WITH_A_HONORS.format(now, elem['name'], unic, elem['score'], elem['notes']))
    return data


def exclude_text_in_dict(data):
    """

    Args: data: We receive a list of dictionaries, from which it is necessary to extract the "text" element and add
    it to a separate list


    Returns: We get the desired element

    """
    new_list = []
    for elem in data:
        new_list.append(elem['text'])
        continue
    return new_list


def add_elem_in_file(data):
    """

    Args:
        data: Element 'text'

    Returns: Write the element to the file

    """
    for elem in data:
        work_with_files_append(data=elem + '\n')
        continue
    return data


# Variable for data in json format
google_data = get_data(URL)

# We perform the functions and transfer their results to another to combine the data
walid_score = check_score(google_data)
walid_reward = check_rewards(walid_score)
walid_age = check_age(walid_reward)

# A variable for all necessary data that needs to be processed
result_of_checks = add_elem_text_to_dict(walid_age)

# A variable to get the "text" element of each dictionary from the list
getting_the_text_element = exclude_text_in_dict(result_of_checks)

# A variable for trimming text to the required length
cropping_the_element = max_lenght_some_value(getting_the_text_element)

# A variable to add an editable element to the file
add_elem_in_file(cropping_the_element)
