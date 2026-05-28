money = 1000

print('it ATM program')

while True:
    print('''
    1.Your balance
    2.Withdraw 100
    3.Deposit 100
    4.Exit
    ''')
    command = int(input('please enter number of command to execute:'))
    match command:
        case 1:
            print(f'your balance is {money}')
        case 2:
            if money >= 100:
                print('withdraw is successful')
                money -= 100
            else:
                print('there is not enough money')
        case 3:
            money += 100
            print('deposit is successful')
        case 4:
            print('have a nice day')
            break
        case _:
            print('invalid command')