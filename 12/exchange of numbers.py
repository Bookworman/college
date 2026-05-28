import random

number = []

for i in range(5):
    number.append(random.randint(1,100))

print(f'list of numbers: {number}')

min_index = number.index(min(number))

number[0], number[min_index] = number[min_index], number[0]

print('woopedy doopedy some magic')
print(f'new list of numbers: {number}')