# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи



dig_fib = int(input('Введите число Фибоначчи: '))

def nego_fibonacci(x):
    fib1 = 0
    fib2 = 1
    my_list = []
    my_list.append(fib1)
    my_list.append(fib2)
    for i in range(2, x + 1):
        fib1, fib2 = fib2, fib1 + fib2
        my_list.append(fib2)
    print(my_list)

    fib_1 = 0
    fib_2 = 1
    new_list = []
    new_list.append(fib_2)
    for i in range(2, x + 1):
        fib_1, fib_2 = fib_2, fib_1 - fib_2
        new_list.append(fib_2)
    print(new_list)
    new_list.reverse()

    new_list2 = []

    for i in range(len(new_list)):
        new_list2.append(new_list[i])


    for i in range(len(my_list)):
        new_list2.append(my_list[i])

    return new_list2


result = nego_fibonacci(dig_fib)
print(f'для k = 8 список будет выглядеть так: {result} Негафибоначчи')























# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# print(fibonacci(9))

