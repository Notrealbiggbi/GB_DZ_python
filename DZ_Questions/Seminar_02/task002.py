# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


number = abs(int(input('Введите число ')))

my_list = [round((1+1/i)**i, 2) for i in range(1, number + 1)]
# for i in range(1, number + 1):
#     my_list.append(round((1+1/i)**i, 2))

print(f"Для number = {number} -> {my_list}")

print(f'Сумма {sum(my_list)}')