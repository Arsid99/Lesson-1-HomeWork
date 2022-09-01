# from typing import Callable
# from rich import print
#
# def auth_decorator(func: callable):
#     def wrapper(*agrs, **kwargs):
#         name = input('Enter you name: ')
#         password = input('Input you password: ')
#         if name == '1' and password == '1':
#             result = func(*agrs, **kwargs)
#             return result
#         print('Not allowed')
#     return wrapper
#
# @auth_decorator
# def mult_to_two(value):
#     """
#     \
#     Args:
#         value:(str|int|float|list):
#
#     Returns:
#         value (str|int|float|list) mylt 2
#
#     """
#     result = value * 2
#     return result
#
# def postman(instance):
#     def bond007(*args, **kwargs):
#         print(f"I have got {args} ang {kwargs}")
#         print(f'I work as a {instance.__name__}')
#         print("do something cool")
#         result = instance(*args, *kwargs)
#         print('go to bar')
#     bond007.__doc__ = instance.__doc__
#     return bond007()
# @postman
# def builder(bricks = 50):
#     build = bricks * 5
#     return build
# @postman
# def teacher():
#     print('I work in school')
#     log = {'Alex': 5}
#     return log
#
# print(builder(5))
#
# print(builder.__doc__)
#


example = '234'


def password_check(func):
    def wrapper(*args, **kwargs):
        for user_try in range(3):
            password = input('Enter password: ')
            if password == example:
                result = func(*args, **kwargs)
                return result
        print('Denied')
    return wrapper()


@serializer
def power_me(n=0):
    print(f"I am puwerful")

# power_me(n = 5656)















