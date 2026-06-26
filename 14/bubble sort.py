import random
flag = 0
N=10
numbers=[]
for i in range(N):
    numbers.append(random.randint(1,100))
print(numbers)
"""
while True:
    flag = 0
    for j in range (len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            flag = 1
    if flag == 0:
        break
"""
while flag == 1:
    flag = 0
    counter = 0
    while counter < N - 1:
        if numbers[counter] > numbers[counter + 1]:
            numbers[counter],numbers[counter + 1] = numbers[counter + 1], numbers[counter]
            flag = 1
        counter += 1

print(numbers)



