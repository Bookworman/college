print('Queen move check')
x1, y1, x2, y2 = map(int, input('please enter coordinates in order(x1 y1 x2 x3) ').split())
if (abs(x1-x2) == abs(y1-y2)) or x1 - x2 == 0 or y1 - y2 == 0   :
    print("Yes SHE can")
else:
    print("Nope it wont work")