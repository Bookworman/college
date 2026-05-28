print('you have to write three numbers each bigger than last one')
number1 = int(input("enter first number"))
while True:
    number2 = int(input('enter second number'))
    if number1 >= number2:
        print('nah, it is must be BIGGER')
    else:
        number1 = number2
        break
while True:
    number2 = int(input('enter third number'))
    if number1 >= number2:
        print('nah, it is must be BIGGER')
    else:
        print('You have made it')
        break
