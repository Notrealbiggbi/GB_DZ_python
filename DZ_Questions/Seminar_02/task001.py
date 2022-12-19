# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

number = float(input('Введите число '))

def Sum_dig(n):
    n = abs(n)
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

result = Sum_dig(number)
print(int(result))
