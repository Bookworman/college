final_number = 0
temp_number = 0

print('hello, you will have to write prices, and program will tell you how much you will have to pay, to stop print "0" in input, if summ is bigger than 1000 there will be discount 10%')
while True:
    temp_number = int(input('print a price: '))
    if temp_number == 0:
        break
    elif temp_number < 0:
        print('sorry, there is no negative prices')
        continue
    final_number += temp_number
if final_number >= 1000:
    final_number *= 0.9
print(f'final price is {final_number}')