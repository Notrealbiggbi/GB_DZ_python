# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


max_val = 100
# x = int(input('Введите натуральную степень k: '))


def polynomial(k):
    koeff = [randint(0, max_val) for i in range(k)]+[randint(1, max_val)]

    poly = ' + '.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(koeff) if j][::-1])


    poly = poly.replace('x** +', 'x +')

    # poly = poly.replace('x^0', '')

    poly += (' ', ' 1 ')[poly[-1] == ' + ']

    poly= (poly, poly[:-2])[poly[-2:] == '**1']
    return poly

# result = polynomial(x)
# print(f'{result} = 0')


