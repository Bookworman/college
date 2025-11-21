import math

def calculate_distance(x1, y1, x2, y2):
    """
    Находит длину прямой по точкам

    args:
       x1, y1, x2, y2:(int) - координаты точек
    returns:
       float: длина прямой
    """
    return abs(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

def calculate_triangle_area(a, b, c):
    """
    Находит площадь треугольника по формуле Герона

    args:
       a, b, c:(float) - длины сторон
    returns:
       float: площадь треугольника
    """
    p = (a+b+c)/2 # полупериметр
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

x1, y1, x2, y2, x3, y3 = map(int, input('Введите координаты точек через пробел "x1 y1 x2 y2 x3 y3"').split())
a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x1, y1, x3, y3)
c = calculate_distance(x2, y2, x3, y3)

print(round(calculate_triangle_area(a, b, c),2))