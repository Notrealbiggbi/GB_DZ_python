# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

while True:
    try:
        num = int(input('Введите число '))
        res = ''
        while num > 0:

            res = str(num % 2) + res
            num = num // 2
        print(res)
        break
    except:
        print('Надо вводить число и не ошибаться')


# num = int(input('Введите число '))
# my_list = []
# while num != 0:
#     my_list.append(str(num % 2))
#     num //= 2
# print(''.join(reversed(my_list)))



# print(f'{45:b}')



