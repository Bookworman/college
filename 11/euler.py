print('this program will calculate a^5 + b^5 + c^5 + d^5 = e^5 for numbers < 150')

for e in range(1, 151):
    e5 = e ** 5
    for a in range(1, e):
        a5 = a ** 5
        for b in range(a, e):
            b5 = b ** 5
            for c in range(b, e):
                c5 = c ** 5
                for d in range(c, e):
                    if a5 + b5 + c5 + d**5 == e5:
                        print(a + b + c + d + e)