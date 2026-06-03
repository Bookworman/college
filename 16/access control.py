
print('this program will control access')
print('first you will have to input permitted ID')
print('second you will have to input ID to be checked')

# 10 20 30 - first input for test
# 20 40 10 50 - second input for test

id_granted = set(input('please enter line of permitted ID: ').split())
id_unchecked = set(input('please enter line of ID for check: ').split())

for num in id_unchecked:
    if num in id_granted:
        print(f'you have permitted ID: {num}')
    else:
        print(f'you have not permitted ID: {num}')
