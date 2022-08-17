first_day_distance = int(input('Enter the distance the athlete ran on the first day in km  : '))
distance_after_n_day = int(input('Enter the distance to determine the number of days required:  '))
day = 0
while first_day_distance < distance_after_n_day:
    first_day_distance *= 1.1
    day += 1
print(f'The athlete submits the distance after {day} days')
