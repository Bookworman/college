
id_all = {0,1,2,3,4,5,6,7,8,9,10}

print('this program will tell you which people are not was at work')
print('you will have to input three lines of numbers')
# 1 2 3 - first input for tes
# 4 5 6 - second input for test
# 7 8 9 - third input for test
id_1 = set(map(int, input('please enter line of first ID: ').split()))
id_2 = set(map(int,input('please enter line of second ID: ').split()))
id_3 = set(map(int,input('please enter line of third ID: ').split()))

absent = id_all - id_1 - id_2 - id_3

print(f"Id of people who were not at work: {' '.join(map(str, absent))}")
