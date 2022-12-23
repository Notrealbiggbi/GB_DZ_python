# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

import random
from random import randint as RI

# number = abs(int(input('Введите кол-во элементов списка ')))
#
# my_list = []
# for i in range(number):
#     my_list.append(RI(5, 15))
# print(my_list)
#
# New_list =[]
# New_list.append(sorted(my_list, key=lambda my_list: random.random()))
# print(*New_list)

# random.shuffle(my_list)
# print(my_list)

def new_list(size: int):
    list_ = []
    for i in range(size):
        list_.append(i)
    return list_

my_list = new_list(10)

def my_shuffle(my_list: list):
    for i in range(len(my_list)):
        ni = random.randint(0, len(my_list) - 1)
        my_list[i], my_list[ni] = my_list[ni], my_list[i]


print(my_list)
my_shuffle(my_list)
print(my_list)



