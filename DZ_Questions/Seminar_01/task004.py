# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

num1 = int(input('Введите координату Х1 '))
num2 = int(input('Введите координату Y1 '))
num3 = int(input('Введите координату X2 '))
num4 = int(input('Введите координату Y2 '))

def Range(x1, y1, x2, y2):
    range_x = x1 - x2
    range_y = y1 - y2
    range_z = math.sqrt(range_x * range_x + range_y * range_y)
    return range_z

result = Range(num1, num2, num3, num4)
print(f"A({num1},{num2}): B({num3},{num4}) -> {round(result, 3)}")