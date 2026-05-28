counter = 0

print('you have 100 dollars, lets count how many different cattle you could buy')

for bulls in range(0,110,10):
    for cows in range(0,(105 - bulls),5):
        print(f'''
        ================
        bulls: {bulls//10}
        cows: {cows//5}
        calf: {(100 - cows - bulls)//0.5}
        ================
        ''')


