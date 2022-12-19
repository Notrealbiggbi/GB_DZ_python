# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


number = abs(int(input('Введите число ')))

my_list = []
for i in range(number):
    my_list.append(round((1+1/(i+1))**(i+1), 2))

print(f"Для number = {number} -> {my_list}")

print(f'Сумма {sum(my_list)}')