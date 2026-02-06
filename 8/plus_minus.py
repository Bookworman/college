n=0
print("Знакочередующаяся сумма")
num = int(input('Введите число: '))
for i in range(1,num+1):
    n = n + ((-1) ** (i+1)) * i
print(n)
