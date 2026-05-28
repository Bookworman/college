print('this program will check if your IP is possible')
numbers = input('please enter IP: ').split('.')
for i in range(len(numbers)):
    if 0 <= int(numbers[i]) <= 255:
        continue
    else:
        print('NO')
        exit()
print('YES')