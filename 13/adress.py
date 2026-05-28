print('this program will split your adress')
adress = str(input('please enter adress: ')).split('\\')
for i in range(len(adress)):
    print(adress[i])