from DZ_Questions.Seminar_08.My_variant import test

class_names = ['1А', '1Б', '1В', '1Г',
               '2А', '2Б', '2В', '2Г',
               '3А', '3Б', '3В', '3Г',
               '4А', '4Б', '4В', '4Г',
               '5А', '5Б', '5В', '5Г',
               '6А', '6Б', '6В', '6Г']

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
    global class_names
    find = input('Учеников какого класса вы хотите найти?: ')
    if find == class_names[16]:
        show(cop)
    elif find == class_names[22]:
        show(cop2)
    else:
        print('Вы ошиблись! Попробуйте найти класс снова.')


def name_serch(cop, cop2):
    name = input('Введите название класса: ')

    if name == class_names[16]:
        print(show(cop))
        print(test.class_marks2())
    elif name == class_names[22]:
        print(show(cop2))
        print(test.class_marks())
    else:
        print('Такого класса в нашей школе нет!!')

def exit_programm():
    print('Завершение программы')
    exit()




