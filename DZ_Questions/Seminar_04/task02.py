# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

#
# from task01 import polynomial
# max_val = 100
# x = int(input('Введите натуральную степень x: '))
# y = int(input('Введите натуральную степень y: '))
# result1 = polynomial(x)
# print(f'{result1} = 0')
# result2 = polynomial(y)
# print(f'{result2} = 0')
#
# poly1 = open('poly1.txt', 'w', encoding='UTF-8')
# poly1.write(f'{result1} = 0')
#
# poly2 = open('poly2.txt', 'w', encoding='UTF-8')
# poly2.write(f'{result2} = 0')





with open('poly1.txt', 'r', encoding='UTF-8') as text:
    my_file1 = text.readline()

with open('poly2.txt', 'r', encoding='UTF-8') as text:
    my_file2 = text.readline()


def remake(equ):
    dicktequ = {}
    equ = equ.replace(' - ', ' -').replace(' + ', ' +')
    equ = equ.split()
    equ = equ[:-2]
    for i in range(len(equ)):
        equ[i] = equ[i].replace(' + ', '').split('x**')
        dicktequ[int(equ[i][1])] = int(equ[i][0])
    return dicktequ


res = remake(my_file1)
res2 =remake(my_file2)
print(res)
print(res2)

def sumequ(dict1, dict2):
    dictres = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        f = dict1.get(i)
        s = dict2.get(i)
        if f != None or s != None:
             dictres[i] = (f if f != None else 0) + (s if s != None else 0)
    return dictres

def cef_res(dict_f):
    result = ''
    for i in dict_f.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            result = result.replace('x^1', 'x').replace('x^0', '').replace('1x^', 'x^')
    return result + ' = 0'


dict_fin = sumequ(res, res2)
# dict_fin = str(dict_fin)
print(dict_fin)

dict_final = cef_res(dict_fin)
print(dict_final)

poly = open('poly3.txt', 'w', encoding='UTF-8')
poly.write(dict_final)


