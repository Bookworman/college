print('this program will print all possible combinations of months that summarize to 365 days')

for month_28 in range(14):
    for month_30 in range(((365 - month_28 * 28) // 30 + 1)):
        for month_31 in range(((365 - month_28 * 28 - month_30 * 30) // 31 + 1)):
            temp = month_28 * 28 + month_30 * 30 + month_31 * 31
            if temp == 365:
                print(f'''
                _____________________
                28 months: {month_28}
                30 months: {month_30}
                31 months: {month_31}
                _____________________
                ''')