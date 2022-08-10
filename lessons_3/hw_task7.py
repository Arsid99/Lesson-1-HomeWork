user_num = int(input('Entering number, please: '))
# We add the first value by which the entered number will be multiplied
first_value = 1
# In the cycle, we specify to take num in range from 1, because if it is 0, then all values will be multiplied by 0
# And up to the value user + 1, because the range is built in such a way that the entered number does not fall into the range
for num in range(1, user_num + 1):
    first_value *= num
    print(f' {user_num}! = {first_value}')
