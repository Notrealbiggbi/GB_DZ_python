# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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

def result_list(listok_: int):
    new_list = []
    x = len(listok_) / 2 + 1
    if len(listok_) % 2 == 0:
        for i in range(int(x) - 1):
            x = listok_[i] * listok_[len(listok_) - i - 1]
            new_list.append(x)
    else:
        for i in range(int(x)):
            digit = listok_[i] * listok_[len(listok_) - i - 1]
            new_list.append(digit)
    return new_list

res = result_list(my_list)
print(f'{my_list} -> {res}')







