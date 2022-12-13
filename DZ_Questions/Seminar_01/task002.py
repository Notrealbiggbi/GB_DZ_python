# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# Пример:
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

num1 = int(input('Введите координату Х '))
num2 = int(input('Введите координату Y '))

def Quarter (xc, yc):
    if(xc > 0) and (yc > 0): return 1
    if (xc < 0) and (yc > 0): return 2
    if (xc < 0) and (yc < 0): return 3
    if (xc > 0) and (yc < 0): return 4
    else: return 0

result = Quarter(num1, num2)
print(f'точки координат находятся в {result} плоскости')