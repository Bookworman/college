first, second, temp = 0, 0, 0
print('Программа для нахождения двух наибольших чисел')
count = int(input('Из скольки чисел выбираем? '))
for i in range(1, count+1):
    temp = int(input(f'Введите {i}-е число: '))
    if temp >= second:
        if temp >= first:
            second = first
            first = temp
            continue
        second = temp
print(f'Первое:{first}')
print(f'Второе:{second}')
