def input_class():
    return input('С каким классом работаем? ').upper()

def input_subject():
    return input('Какой предмет? ').lower()

def who_answer():
    return input('кто будет отвечать? ')

def what_mark():
    return input('На какую оценку ответил? ')

def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')

def no_class():
    return print('Такого класса нет!')

def start_lesson():
    return input('Начнём урок? ')

def close_lesson():
    return print('Урок закончен!!')
