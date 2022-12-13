# 2.
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

my_list = []

for i in range(5):
    my_list.append(int(input(f'Введите {i+1} число ')))

my_max = my_list[0]

for item in my_list:
    if my_max < item:
        my_max = item

print(f'максимальное значение списка {my_max}')


# nums = input('nums: ')
# num_list = nums.split(',')
# my_max = num_list[0]
# for num in num_list:
#     if int(my_max) < int(num):
#         my_max = num
# print(my_max)






