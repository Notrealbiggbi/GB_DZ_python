import test




def main_menu() -> int:
    print('Главное меню')
    menu_list = ["Показать Имена и  Фамилии учеников",
                 "Найти класс и его итоговые оценки",
                 ' ',
                 "Выход"
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i+1}. {menu_list[i]}')
    user_input = int(input('Введи команду:> '))
    if user_input > len(menu_list):
        print('Такого пункта в меню нет! Будьте внемательней')
    else:
        return user_input


def show(my_list: list):
    print(' ')
    for i in range(len(my_list)):
        user_id = i + 1
        print(f'\t{user_id}', end='. ')
        for v in my_list[i].values():
            print(f'{v}|', end=' ')
        print(' ')


def class_search(cop, cop2):
    find = int(input('Учеников какого класса вы хотите найти?: '))
    if find == 1:
        show(cop)
    elif find == 2:
        show(cop2)
    else:
        print('Вы ошиблись! Попробуйте найти класс снова.')


def name_serch(cop, cop2):
    name = input('Введите название класса: ')

    if name == '5A':
        print(show(cop))
        print(test.class_marks2())
    elif name == '6B':
        print(show(cop2))
        print(test.class_marks())
    else:
        print('Такого класса в нашей школе нет!!')

def exit_programm():
    print('Завершение программы')
    exit()




