final_number = 0
temp_number = 0

print('hello, you will have to write numbers, and program will tell you which one is biggest among them, to stop print "0" in input')
while True:
    temp_number = int(input('print a number: '))
    if temp_number == 0:
        break
    elif temp_number > final_number:
        final_number = temp_number
print(f'biggest number is {final_number}')