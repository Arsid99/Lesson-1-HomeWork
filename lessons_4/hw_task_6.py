from random import randint

numbers = []
for i in range(100):
    numbers.append(randint(1, 100))

new_list = []
for index in range(1, len(numbers) - 1):
    if numbers[index-1] < numbers[index] > numbers[index+1]:
        new_list.append(index)

print(f"Numbers with more than two neighbors have indices: "
      f"{new_list}, and their number is {len(new_list)}")
