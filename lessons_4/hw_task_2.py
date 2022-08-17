user_num = None
user_elements = []
while user_num != 0:
    user_num = int(input('Enter the required numbers and enter 0 at the end: '))
    user_elements.append(int(user_num))

def multiplication(user_elements):
    '''

    Args:
        user_elements: entered numbers

    Returns: multiplication numbers

    '''
    multiplication_of_list = 1
    for num in user_elements[0:-1]:
        multiplication_of_list *= num
    return multiplication_of_list


def even_func(user_elements):
    '''

    Args:
        user_elements: entered numbers

    Returns: even numbers

    '''
    even_number = 0
    for num in user_elements[0:-1]:
        if num % 2 == 0:
            even_number += 1
    return even_number


def odd_func(user_elements):
    '''

    Args:
        user_elements: entered numbers

    Returns:odd numbers

    '''
    odd_number = 0
    for num in user_elements[0:-1]:
        if num % 2 != 0:
            odd_number += 1
    return odd_number


def second_max(user_elements):
    '''

    Args:
        user_elements: entered numbers

    Returns: second max value in entered numbers

    '''
    my_set = set(user_elements)
    element = list(my_set)
    element.sort()
    return element[-2]


def total_max(user_elements):
    '''

    Args:
        user_elements: entered numbers

    Returns: the number of elements equal to its largest element

    '''
    result = 0
    for num in user_elements:
        if num == max(user_elements):
            result += 1
    return result


def main():
    print(f'The entered elements are: {user_elements[0:-1]}')
    print(f'The number of entered elements: {len((user_elements[0:-1]))}')
    print(f'The sum of the entered elements: {sum(user_elements)}')
    print(f'The product of the introduced elements is: {multiplication(user_elements)}')
    print(f'The average arithmetic value of the entered elements is:{int(sum(user_elements[0:-1]) / len((user_elements[0:-1])))}')
    print(f'The maximum value of the elements: {max(user_elements)},value index - {user_elements.index(max(user_elements))}')
    print(f'Number of even values: {even_func(user_elements)}')
    print(f'Number of odd values: {odd_func(user_elements)}')
    print(f'The second maximum value is this: {second_max(user_elements)}')
    print(f'Elements equal to the maximum value: {total_max(user_elements)}')


main()
