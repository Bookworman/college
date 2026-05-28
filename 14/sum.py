import random

numbers = []
total_sum = 0
max_row_sum = 0
max_row_index = 0


for i in range(5):
    row = []
    for j in range(5):
        row.append(random.randint(1, 100))
    numbers.append(row)

print('Original list:')
for row in numbers:
    print(row)

print('Sum of each row:')
for i in range(len(numbers)):
    row_sum = sum(numbers[i])
    print(f'Row {i + 1}: {row_sum}')
    total_sum += row_sum

    if row_sum > max_row_sum:
        max_row_sum = row_sum
        max_row_index = i

print('Total sum:', total_sum)
print('Row with maximum sum:', max_row_index + 1)
print('Maximum row sum:', max_row_sum)