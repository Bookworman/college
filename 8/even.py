counter = 0
print('проверка 10 чисел на четность')
for i in range(1,11):
    num = int(input(f'введите {i} число: '))
    if num % 2 != 0:
        counter = 1
if counter == 1:
    print('NO')
else:
    print('YES')
