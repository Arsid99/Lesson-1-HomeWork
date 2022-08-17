a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
if a < b:
    for elem in range(a, b + 1):
        print(elem, end=" ")
else:
    # We use a step of -1 so that the numbers are displayed in reverse order
    for elem in range(a, b + -1 , -1):
        print(elem, end=" ")

