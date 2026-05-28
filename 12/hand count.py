marks = [5, 4, 3, 5, 2, 5, 4, 3, 5, 5]
counter5 = 0
counter2 = 0
print(f'there id list of marks: {marks}')
for i in range(len(marks)):
    if marks[i] == 5:
        counter5 += 1
    if marks[i] == 2:
        counter2 += 1
print(f"there are {counter5} total '5' marks,and {counter2} total '2' marks")