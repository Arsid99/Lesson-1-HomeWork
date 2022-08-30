import pprint
import time

def time_sleep(func):
    def wrapper():
        count = 3
        while count > 0:
            time.sleep(1)
            print(count)
            count -= 1
        return func()
    return wrapper

@time_sleep
def what_time_is_it_now():
    return time.strftime('%H:%M')

pprint.pprint(what_time_is_it_now())
