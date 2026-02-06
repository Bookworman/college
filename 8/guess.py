import random
goal = random.randint(1,10)
temp = 0
print('Угадайка')
print('Компьютер загадал число от 1 до 10, вам надо угадать его за 3 попытки')
for i in range(1,4):
    temp = int(input(f'{i}-я попытка: '))
    if temp == goal:
        print('Вы угадали!')
        exit()
    elif temp < goal:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')
print(f'К сожалению попытки закончились,было загадано число {goal}')