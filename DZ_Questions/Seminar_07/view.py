import re

def main_menu() -> int:
    print('Главное меню')
    menu_list = ["Показать все контакты",
                 'Открыть файл',
                 "Сохранить контакт",
                 "Создать контакт",
                 "Изменить контакт",
                 "Удалить контакт",
                 "Найти контакт",
                 "Выход"
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i+1}. {menu_list[i]}')
    user_input = int(input('Введи команду:> '))
    # TODO: сделать валидацию
    return user_input


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print(' ')


def db_success(db: list):
    if db:
        print('Открыл телефонную книгу')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_programm():
    print('Завершение программы')
    exit()


new_contact = dict()
find_cont = dict()


def create_contact():
    print('Создание нового контакта')

    global new_contact
    new_contact['lastname'] = input('\t Введите фамилию: ')
    new_contact['firstname'] = input('\t Введите имя: ')
    new_contact['phone'] = input('\t Введите телефон: ')
    new_contact['comment'] = input('\t Добавте комментарий: ')
    print("Незабудьте сохранить новый контакт если нужно!!!")
    return new_contact


def save_contact(new_dict: dict):
    global new_contact
    global find_cont
    contact = dict()
    ask = int(input('Что вы хотите сохранить новый контакт(1) или изменённый(2)?: '))
    if ask == 1:
        contact = new_contact
    elif ask == 2:
        contact = find_cont
    my_glist = []
    gul = ''
    for value in contact.values():
        my_glist.append(value)
    for item in my_glist:
        item = item.strip()
        item += ';'
        gul += item
    with open('database.txt', 'a', encoding='UTF-8') as file:
        file.write(f'\n{gul}')
    print('Контакт сохранён!!')


def find_contact(db: list):
    global find_cont
    print(' ')
    find_id = int(input("Введите цифру id контакта:"))
    print(" ")
    for i in range(len(db)):
        if find_id == i+1:
            find_cont = db[i]
            print(f'\t{find_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print(' ')
            break


def change_contact(db: dict):
    global find_cont
    change_cont = int(input('Что в контакте вы хотите изменить?: '))
    if change_cont == 1:
        p = input('введите фамилию')
        find_cont['lastname'] = p
    elif change_cont == 2:
        z = input('введите имя')
        find_cont['firstname'] = z
    elif change_cont == 3:
        d = input('введите телефон')
        find_cont['phone'] = d
    elif change_cont == 4:
        b = input('введите комментарий')
        find_cont['comment'] = b
    print("Контакт изменён, не забудте сохранить изменения")
    return find_cont


def delete_more(path: str):
    global find_cont
    my_glist = []
    gul = ''
    for value in find_cont.values():
        my_glist.append(value)
    for item in my_glist:
        item = item.strip()
        item += ';'
        gul += item

    with open('database.txt', 'r', encoding='UTF-8') as file:
        my_com = file.readlines()

    patern = re.compile(re.escape(gul))

    with open('database.txt', 'w', encoding='UTF-8') as file:
        for line in my_com:
            res = patern.search(line)
            if res is None:
                file.write(line)
    print('Контакт удалён из файла!!!')




