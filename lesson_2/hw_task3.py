#Entering the variable input speed of the cyclist
v = (int(input('Enter the cyclists speed in km/h:')))
#Entering a variable to enter the time spent
t = (int(float(input('Enter the time spent on the distance in hour:'))))
#Distance calculation function
s = (v * t)
if s >= 100:
    print('The cyclist covered the distance')
if s > 0:
    print('The cyclist is approximately at the mark no: ' + str(s))
if s < 0:
    print('The cyclist is moving in the wrong direction')