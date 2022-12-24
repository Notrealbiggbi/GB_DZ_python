# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

while True:
    try:
        numbers = input('Введите числа списка через пробел ').split()
        for i in range(len(numbers)):
            numbers[i] = numbers[i].replace(',', '.')
        my_list = []
        for i in range(len(numbers)):

            numbers[i] = float(numbers[i])
            my_list.append(numbers[i])
        break
    except:
        print('Вводите только цифры')

print(my_list)
new_list = []
for i in range(len(numbers)):
    x = 0
    while numbers[i] > 1:
        x = numbers[i] % 1
        break
    new_list.append(round(x, 3))

ar = []
for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
    ar.append(new_list[i])

k = min(ar)
for i in range(len(ar)):
    if ar[i] == k:
        ar.pop(k)


for i in range(len(ar)):
    ar[i] = float(ar[i])
    new_list.append(ar[i])

print(new_list)

print(f'{max(new_list)} - {min(new_list)} = {round(max(new_list) - min(new_list), 3)}')

