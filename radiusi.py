import math

def calculate_rectangle_area(weight, height):
    """Вычисляет площадь прямоугольника
    Args:
        width, height (float): размеры прямоугольника
    returns:
        float: Площадь прямоугольника"""
    area = weight * height
    return area

def calculate_circle_area(radius):
    """Вычисляет радиус круга
        Args:
            radius (float): радиус круга
        returns:
            float: радиус круга"""
    area = 2 * math.pi * radius
    return area

weight, height = map(float, input("Введите высоту и ширину прямоугольника").split())
print(calculate_rectangle_area(weight, height))

radius = float(input("Введите радиус круга"))
print(calculate_circle_area(radius))