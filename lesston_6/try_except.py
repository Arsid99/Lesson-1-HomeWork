
# n = 1
# m = 2
# if type(m) in (int, float) and m != 0 and type(n) in (int, float):
#     r = n/m
#     print(r)
# else:
#     print('not correct')
def test():

    try:
        data = int(input('enter the number >>> '))
    except ValueError as err:
        print('err')
        data = 0
    except Exception as err:
        pass

    else:
        print('all OK')
    # finally:
    #     print("finally")
    #     return 55

    result = data + 600
    return result


user_input = input('enter a number in numeric format: 666.999 >>>>')
left, right = user_input.split('.')
if left.isdigit() and right.isdigit():
    print(float(user_input))

print(test())






