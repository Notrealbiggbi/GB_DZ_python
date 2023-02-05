

def main_menu() -> int:
    print('Главное меню')
    menu_list = ["Показать все классы",
                 "Найти класс",
                 'Показать оценки',
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


def name_serch(cop, cop2):
    name = input('Введите название класса: ')

    if name == '5A':
        print(show(cop))
    elif name == '6B':
        print(show(cop2))
    else:
        print('Такого класса в нашей школе нет!!')

def exit_programm():
    print('Завершение программы')
    exit()
