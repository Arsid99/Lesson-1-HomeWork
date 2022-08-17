entering_num = input('Entering number:')
elements = 0
for elem in range(1, len(entering_num) - 1):
  if entering_num[elem - 1] < entering_num[elem] > entering_num[elem + 1]:
    elements += 1
print(elements)



























# def main():
#     my_list = create_list()
#     print(my_list)
#     print(f'Number of digits, which are bigger than two of their neighbours is {neighbour(my_list)}')
#
#
# def neighbour(list_1):
#     result = 0
#     for num in range(1, len(list_1) - 1):
#         if list_1[num - 1] < list_1[num] and list_1[num] > list_1[num + 1]:
#             result += 1
#     return result
#
#
# def create_list():
#     common_list = []
#     user_number = int(input('Enter another digit (0 - end): '))
#     while user_number != 0:
#         common_list.append(user_number)
#         user_number = int(input('Enter another digit (0 - end): '))
#     return common_list
# counter = 0
# nums = [int(i) for i in input().split()]
# for index in range(1, len(nums) - 1):
#     if (nums[index] > nums[index - 1]) and (nums[index] > nums[index + 1]):
#         counter += 1
#     print(counter)
#     input()
