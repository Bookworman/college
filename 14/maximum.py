import random

numbers = []
max_number = 0


for i in range(5):
    row = []

    for j in range(5):
        row.append(random.randint(1,100))

    numbers.append(row)

print('original list: ', numbers)

for i in range(len(numbers)-1):
    for j in range(len(numbers[i])-1):
        if max_number < numbers[i][j]:
            max_number = numbers[i][j]

print('biggest among numbers: ', max_number)