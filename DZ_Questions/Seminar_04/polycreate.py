from task01 import polynomial
max_val = 100
x = int(input('Введите натуральную степень x: '))
y = int(input('Введите натуральную степень y: '))
result1 = polynomial(x)
print(f'{result1} = 0')
result2 = polynomial(y)
print(f'{result2} = 0')

poly1 = open('poly1.txt', 'w', encoding='UTF-8')
poly1.write(f'{result1} = 0')

poly2 = open('poly2.txt', 'w', encoding='UTF-8')
poly2.write(f'{result2} = 0')