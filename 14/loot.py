
print('Hello first, you will have to write number of items you could bring with yourself')
print('Second you will have to write prices of items separated by ","')
print('This program will tell you max price of items you could bring with yourself')
number = int(input('Write a number of items: '))
prices = input('Write a price of items: ').split(',')
prices = list(map(int, prices))
result = sum(sorted(prices, reverse=True)[:number])
print('result price is', result)