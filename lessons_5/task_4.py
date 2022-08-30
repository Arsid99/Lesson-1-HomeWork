import pprint
import msg
import config_mongodb
import datetime
import task_3


def create_db_mongodb_and_add_data(data) -> list:
    """

    Args:
        data: List of data that must be uploaded to the database

    Returns: Uploading data to the database

    """
    client = config_mongodb.host
    db = config_mongodb.database
    collection = config_mongodb.coll
    return collection.insert_many(data)


def add_elem_from_database(data, db=True, length=150):
    """

    Args:
        data: List of dictionaries in which you need to create an additional element and reduce its length
        db: True
        length: The maximum length of the added element

    Returns: Adds an element to the edited text

    """
    if db:
        now = datetime.datetime.now().date()
        for elem in data:
            elem['text'] = msg.STUDENTS_WITH_A_HONORS.format(now, elem['name'], '', elem['score'], elem['notes'])
            text_length = len(elem['text'])
            if text_length > length:
                elem['text'] = elem['text'][:length - 3]
        return data


def exclude_data_in_mongodb():
    """

    Returns: Data from the database

    """
    client = config_mongodb.host
    db = config_mongodb.database
    collection = config_mongodb.coll
    data_from_mongodb = []
    for elem in collection.find():
        data_from_mongodb.append(elem)
    return data_from_mongodb


data_from_database = add_elem_from_database(task_3.walid_age)
create_db_mongodb_and_add_data(data_from_database)
pprint.pprint(exclude_data_in_mongodb())
