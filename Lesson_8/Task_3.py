import pprint

new_list =  ['a', 'b', 'c', 'd', 'e']

def main_func(list) -> dict:
    reslut = dict(enumerate(list))
    return reslut

pprint.pprint(main_func(new_list))