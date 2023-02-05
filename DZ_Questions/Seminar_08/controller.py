from database import Read
import test

import view

pf = Read('5A.txt')
pf2 = Read('6B.txt')
cop = pf.file_read()
cop2 = pf2.file_read()


def input_my_class(inp: int):
    match inp:
        case 1:
            view.class_search(cop, cop2)
        case 2:
            view.name_serch(cop, cop2)
        case 3:
            pass
        case 4:
            view.exit_programm()


def start():
    while True:
        user_input = view.main_menu()
        input_my_class(user_input)






