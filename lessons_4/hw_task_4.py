a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = list(range(a, b))

for elem_1 in c:
    for elem_2 in range(a+1, elem_1+2):
        print(elem_2, end='')
    print()
