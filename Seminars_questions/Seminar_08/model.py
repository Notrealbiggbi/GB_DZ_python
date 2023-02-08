# def open_file(file_name):
#
#     with open(file_name, 'r', encoding='UTF-8') as f:
#         clas = []
#         for i, line in enumerate(f):
#             #[str, {'rus':[]}]
#             name, subjects = line.strip().split('.')
#             clas.append([name, {}])
#             for subject in subjects.split(';'):
#                 journ = subject.split(':')
#             #print(journ)
#                 clas[i][1][journ[0]] = journ[1].split(',')
#         print(clas)
#         return clas
#
#
# def save_file(file_name, clas):
#     with open(file_name, 'r', encoding='UTF-8') as f:
#         for i in range(len(clas)):
#             s = clas[i][0] + '.'
#             subj = []
#             for k, v in clas[i][1].items():
#                 subj.append(f"{k}: {','.join(v)}")
#             s += ';'.join(subj)
#             f.write(f'{s}')
#
#
# def print_class(clas, subj):
#     for i in range(len(clas)):
#         s = clas[i][0] + ': '
#         #v =clas[i][1][subj]
#         s += f"[{', '.join(clas[i][1][subj])}]"
#         print(f'{s}')
#
#
#
#
# clas = open_file('7A.txt')
# subj = input('Введите название предмета: ')
# #save_file('8b.txt',clas)
# print_class(clas, subj)
#
# while True:
#     call_pupil = input('кто пойдёт к доске: ')
#     for s in clas:
#         if s[0] == call_pupil:
#             break
#         else:
#             print(f'{call_pupil} отсутствует в классе, нужно ввести фамилию повторно')
#
# evall = input('Оценка: ')
