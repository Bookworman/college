counter_3 = 0
counter_last = 0
counter_even = 0
summ_1 = 0
multiply = 1
counter_05 = 0
temp_number = 0

print('Program will count many random things')
number = int(input('Enter a number: '))
last_number = number % 10
while number != 0:
    temp_number = number % 10
    if temp_number == 3:
        counter_3 += 1
    if temp_number == last_number:
        counter_last += 1
    if temp_number % 2 == 0:
        counter_even += 1
    if temp_number > 5:
        summ_1 += temp_number
    if temp_number > 7:
        multiply *= temp_number
    if temp_number == 0 or temp_number == 5:
        counter_05 += 1
    number //= 10
print(f"'3' met in number:{counter_3}")
print(f"last number met in number:{counter_last}")
print(f"even numbers met in number:{counter_even}")
print(f"summ number that bigger than 5 met in number:{summ_1}")
print(f"multiply of numbers greater than 7:{multiply}")
print(f"'0' and '5' met in number:{counter_05}")
