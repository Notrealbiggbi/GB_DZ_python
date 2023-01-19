from random import randint as RT


my_candy = RT(29, 101)
print(f'Это игра в "Кто взял последнюю конфету тот и выиграл" \nВот кол-во конфет {my_candy}')
tu = "Первый Игрок"

for _ in range(my_candy):

    if my_candy != 0:
        print(f'\n Ход: {tu}\n')
        turn = int(input(' Введи сколько конфет хочешь взять но не больше 28: '))
        res = my_candy - turn
        my_candy = res
        print(f'\nКонфет осталось: {res}\n')
        if tu == "Первый Игрок":
            tu = "Второй Игрок"
        else:
            tu = "Первый Игрок"
    else:
        break
if tu == "Первый Игрок":
    tu = "Второй Игрок"
else:
    tu = "Первый Игрок"

print(f"Игра окончена!!! Выиграл {tu}")
