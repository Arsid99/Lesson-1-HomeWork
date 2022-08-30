import pprint

elem_1 = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
elem_2 = ('BTC', 'ETH', 'XRP', 'LTC')

def elem_dict(elem_1, elem_2):
    result = dict(zip(elem_1, elem_2))
    return result


pprint.pprint(elem_dict(elem_1, elem_2))
