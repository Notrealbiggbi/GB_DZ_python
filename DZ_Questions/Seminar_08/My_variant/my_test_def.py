math = [{'Иванов Иван': {'Оценки': [5, 5, 4, 3, 5, 5]}}, {'Попова Мария': {'Оценки': [4, 5, 5, 4, 5, 4]}}]


new_list = []
new_list2 = []
child = 0
new_key = []


def class_marks(data: list):
    global new_list
    global new_list2
    global child
    global new_key
    for i in math:
        for k in i.keys():
            new_key.append(k)
    print(f'1. {new_key[0]}')
    print(f'2. {new_key[1]}')
    find = int(input('Введите оценки какого ученика посмотреть: '))
    for i in math:
        for v in i.values():
            new_list.append(v)

    for i in new_list:
        for v in i.values():
            new_list2.append(v)
    while True:
        if find > len(math):
            print('Ошибка, такого ученика нет!')
            break
        else:
            for i in range(len(new_list2)):
                if find == i + 1:
                    for item in new_list2:
                        child = item
        print(f'оценки  {child}')
        ask = input('Ставить оценку или нет?: ')
        if ask == 'да':
            postav = int(input('поставить оценку: '))
            child.append(postav)
            print(f'оценки  {child}')
            print(" ")
        elif ask == 'нет':
            print('сегодня без оценки!')
            break
        else:
            print('Ошибка! да или нет')


class_marks(math)









