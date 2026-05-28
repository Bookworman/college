counter = 1

print('Number printer(on conditions)')
number = int(input('Please enter a number:'))
while counter <= number:
    if 5 <= counter <= 9 or 17 <= counter <= 37 or 78 <= counter <= 87:
        counter += 1
        continue
    print (counter)
    counter += 1

