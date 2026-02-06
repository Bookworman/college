print('Bishop move check')
x1, y1, x2, y2 = map(int, input('please enter coordinates in order(x1 y1 x2 x3) ').split())
if (abs(x1-x2) == abs(y1-y2)):
    print("Yes HE can")
else:
    print("Nope it wont work")