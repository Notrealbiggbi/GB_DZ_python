# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


while True:
    try:
        numbers = input('Введите числа списка через пробел ').split()
        my_list = []
        for i in range(len(numbers)):
          numbers[i] = int(numbers[i])
          my_list.append(numbers[i])
        break
    except:
        print('Вводите только цифры')


def sum_negativ_numbers(n_list):
    sum_num = 0
    for i in range(len(my_list)):
        if i % 2 == 1:
            sum_num += my_list[i]
    return sum_num

result = sum_negativ_numbers(my_list)
print(f'{my_list} -> Сумма элементов на нечётных позициях равна -> {result}')
