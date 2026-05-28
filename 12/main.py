numbers = []

print('please enter a number, and program will give you list of numbers form 1 to your number')
goal = int(input('whats your number? '))
for i in range(1,goal+1):
    numbers.append(i)
print(numbers)
