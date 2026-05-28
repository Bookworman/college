words = []

print('please enter number of lines you want to make')
number = int(input('what is your number? '))
for i in range(number):
    words += list(str(input('please enter line: ')))
print(words)