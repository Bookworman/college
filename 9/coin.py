counter = 0

print('Witcher demanded payment')
money = int(input('How much does he asked?: '))
if money == 0:
    print("Congrats, it's free")
    exit()
print('You need to pay:')
while money // 25 > 0:
    counter += 1
    money -= 250
if counter != 0:
    print(f'25 coins: {counter}')
    counter = 0
while money // 10 > 0:
    counter += 1
    money -= 10
if counter != 0:
    print(f'10 coins: {counter}')
    counter = 0
while money // 5 > 0:
    counter += 1
    money -= 5
if counter != 0:
    print(f'5 coins: {counter}')
    counter = 0
while money // 1 > 0:
    counter += 1
    money -= 1
if counter != 0:
    print(f'1 coins: {counter}')
