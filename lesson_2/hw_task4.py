# Сreating a variable to enter the year
year = int(input('Entering year, please: '))
# Creating the conditions for the execution of the request

if year % 4 == 0 and year % 100 != 0:
    # If a year is divided module 4 and the remainder of the division is zero
    # And if the year is divided by 100 using the operator "!=" and the remainder is not zero, then this is true
    print("This is a leap year")
# If a year is divided by the module 400, then the remainder of the division is zero, this is true
elif year % 400 == 0:
    print("This is a leap year")
# In all other cases, the result is negative
else:
    print("This year is not a leap year")

# Даную задачу сам не смог решить, нашёл исходный код в Интернете, принцип решения понимаю, но сам бы, правильно, не смог написать условия