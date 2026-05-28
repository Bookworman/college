pos_Alex = 0
pos_Levon = 0
counter = 0

print('Queue')
print('You have to print Names, one on each row')
print('program will tell you number of peoples between "Alex" and "Levon"')
print('If there is no more people in queue, leave answer blank')
while True:
    temp = input('enter name ')
    if temp == '':
        break
    if temp == 'Alex':
        pos_Alex = counter
    if temp == 'Levon':
        pos_Levon = counter
    counter += 1
print(f'between Alex and Levon: {pos_Levon - pos_Alex - 1} people')
