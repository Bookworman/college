flowers = []

print('It is garden program please enter line of flowers')
print('First part: it will divide your input by lines')
print('format is "name1 color1 size1 height1, name2 color2 size2 height2, ..."')

# rose red small 30, tulip yellow medium 25, lily white large 40 - тестовый ввод

plants = [item.strip() for item in input('please enter your flowers: ').split(',')]

print('Flowers in garden:')
for item in plants:
    print(item)
print('_______________________')


print('Second part will calculate different qualities of hybrids')
print('format of input:')
print("""
Name1
Color1 Size1 Speed_of_rising1
Name2
Color2 Size2 Speed_of_rising2
Possible Sizes: big, medium, small
Possible speed of rising: fast, medium, slow
""")

name1 = input('please enter first name: ')
data1 = input('please enter first qualities: ').split()
flowers.append([name1]+data1)

name2 = input('please enter second name: ')
data2 = input('please enter second qualities: ').split()
flowers.append([name2]+data2)

if flowers[0][0] < flowers[1][0] or flowers[0][0] == flowers[1][0]:
    print(f'Color of hybrid will be: {flowers[0][1]}')
else:
    print(f'Color of color will be: {flowers[1][1]}')



