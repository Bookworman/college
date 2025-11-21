money = int(input('Какое количество денег надо выдать? (кратно 100)'))
print('Будет выдано\n5000 купюр: ', (money // 5000))
money %= 5000
print('2000 купюр: ', (money // 2000))
money %= 2000
print('1000 купюр: ', (money // 1000))
money %= 1000
print('500 купюр: ', (money // 500))
money %= 500
print('200 купюр: ', (money // 200))
money %= 200
print('100 купюр: ', (money // 100))