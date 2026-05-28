import random

numbers = []
counter = 0

for i in range(5):
    row = []
    for j in range(5):
        row.append(random.randint(1, 10))
    numbers.append(row)

print('Original list:')
for row in numbers:
    print(row)

target = int(input('Write a number to search for: '))

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        if numbers[i][j] == target:
            print(f'{i},{j}')
            counter = 1
if counter == 0:
    print('No numbers found')
