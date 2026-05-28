counter = 0

print('this program will count number of pairs in line of numbers you will enter, please enter is separated by ","')
numbers = str(input('please enter numbers: ')).split(',')
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            counter += 1
print(numbers)
print(f'number of pairs: {counter}')
