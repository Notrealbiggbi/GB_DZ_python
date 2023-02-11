journal = {}

with open('2A_math.txt', 'r', encoding='UTF-8') as data:
    file = data.readlines()
    for sub in file:
        journal[sub.split(':')[0]] = list(map(int, sub.split(':')[1].split()))


def sredn_orif():
    global journal
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:15} {journal.get(child)}')

    marks = list()
    for mark in journal.values():
        marks.append(mark)

    for digs in marks:
        ex = 0
        for dig in digs:
            ex += dig / len(digs)
        print(f'Итоговая оценка {round(ex, 2)}')

student = input('кто пойдёт отвечать? ')

mark = int(input('какую оценку ставим? '))
marks = list(journal.get(student))
marks.append(mark)
journal[student] = marks


new_file = []
with open('2A_math.txt', 'r', encoding='UTF-8') as data:
    file = data.readlines()
item = []
for student, marks in journal.items():
    item.append(student + ':' + ' '.join(list(map(str, marks))))
new_file.append(item)
with open('2A_math.txt', 'w', encoding='UTF-8') as data:
    for item in new_file:
        data.write('\n'.join(item))





ask = int(input('Если хотите узнать итоговые оценки учеников нажмите 1: '))

if ask == 1:
    sredn_orif()
else:
    print('Значит переходим дальше')


# while True:
#     comment = input("Введите сообщение: ")
#     if comment == 'exit':
#         break
#     elif comment == 'delete':
#         with open('comments.txt', 'w', encoding='UTF-8') as data3:
#             data3.write('')
#             break
#
#     with open('comments.txt', 'r', encoding='UTF-8') as data:
#         com_save = data.read()
#
#     with open('comments.txt', 'w', encoding='UTF-8') as data2:
#         new_com = data2.write(f'{str(com_save)}')
#         new_com2 = data2.write(f'{comment}\n')
#         data2.close()






