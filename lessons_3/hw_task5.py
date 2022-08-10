# I import the random module to use the randint function
import random

# Creating a variable with a random number
random_num = random.randint(1, 10)
chance = 0
# I am creating a loop that will repeat a maximum of 3 times
while chance < 3:
    print('Guess the number I came up with')
    user_num = int(input('Entering number, please: '))
    # We set the value so that 1 is added to the chance variable every time an attempt is made to guess a number
    chance += 1
    if user_num == random_num:
        print('You won!')
        break
    else:
        print('You lose :(')
