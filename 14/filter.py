
positive_numbers = []

# [[1, -2, 3, 0], [-5, 6, 7], [0, -1, 9, 4]]
numbers = eval(input('please enter a list of numbers: '))

print('Original list:')
for row in numbers:
    print(row)

for row in numbers:
    new_row = []
    for num in row:
        if num > 0:
            new_row.append(num)
    positive_numbers.append(new_row)

print('Filtered list:')
for row in positive_numbers:
    print(row)