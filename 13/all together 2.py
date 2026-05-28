numbers = [8, 9, 10, 11]
print(f'original list: {numbers}')
numbers[1] = 17
numbers.extend([4,5,6])
numbers.pop(0)
numbers += numbers
numbers.insert(3, 25)
print('whoopedy doopedy? some magic')
print(f'new list: {numbers}')