v = int(input('Enter the cyclists speed in km/h:'))
t = int(input('Enter the time spent on the distance in hour:'))
s = v * t

if v > 0 and s <= 99 and t >= 0:
    print(f'According to the given data, in {t} hours the cyclist will be near the mark {s}km mark.')
elif v < 0 and s >= -100 and t >= 0:
    print(f'According to the specified data, the cyclist will leave the start in'
    f'a different direction and overcome the distance {s}km mark.')
elif s >=100:
    print(f'The cyclist crossed the finish line!')
else:
    print('Some data is entered incorrectly.')