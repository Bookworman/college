numbers = [10, 20, 30, 40, 50]
counter = 0

print('this program will tell you if your number is in list')
user_number = int(input('what is your number? '))
for i in range(len(numbers)):
    if numbers[i] == user_number:
        print(f'index of your number is {i}')
        counter += 1
        break
if counter == 0:
    print('your number is not in list')