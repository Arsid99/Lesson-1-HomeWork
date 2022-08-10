number = (input('Tntering value, please: '))
# Creating a list with no elements
numbers_list = []
# Searching for elements in a variable
for elem in number:
    # Adding the found elements in int forman to the variable
    numbers_list.append(int(elem))
print(f' The sum of all values of the entered number = {(sum(numbers_list))}')