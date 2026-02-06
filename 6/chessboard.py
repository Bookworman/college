print('Chessboard color check')
x1, y1, x2, y2 = map(int, input('please enter coordinates in order(x1 y1 x2 x3) ').split())
if (((x1+y1) % 2) == ((x2+y2) % 2)):
    print("Same color")
else:
    print("Different color")
