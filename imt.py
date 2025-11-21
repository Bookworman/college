weight, height = map(float, input("Введите ваши параметры тела через пробел ( вес(кг) рост(м) )").split())
imt = weight / (height * height)
print(round(imt, 1))