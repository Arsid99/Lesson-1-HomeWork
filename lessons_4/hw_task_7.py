num_list_1 = input('Entering something: ')
num_list_2 = input('Entering something: ')
set_1 = set(num_list_1)
set_2 = set(num_list_2)
# We check whether there are different values
print(sorted(set_1.difference(set_2)))
# We check whether there are the same values
print(sorted(set_1.intersection(set_2)))
#Displays distinct elements
print(set_1.symmetric_difference(set_2))

































# num_list_1 = int(input('Entering number: '))
# num_list_2 = int(input('Entering number: '))
#
# some_set_1 = {num_list_1}
# some_set_2 = {num_list_2}
# for elem in some_set_1 and some_set_2:
#     if elem in some_set_1 and some_set_2 == 1:
#         print(elem)
# print(some_set_1[2])
# print(some_set_2[1])
# # num_element_firt = []
# # num_element_second = []
# # for elem in num_list_1 and num_list_2:
# #     num_element_firt.append(num_list_1)
# #     num_element_second.append(num_list_2)
# #     if elem in num_list_1 and num_list_2 == 1:
# #         print()
