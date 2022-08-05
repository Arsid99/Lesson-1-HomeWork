#Сreating a variable to enter the value
num = (int(input('Entering value, please: ')))
#Rule if entered value > 0 - print 1
if  num > 0:
    print(1)
#Rule if entered value < 0 - print -1
elif num < 0:
    print(-1)
#Rule if entered value = 0 - print 0
else:
    print(0)