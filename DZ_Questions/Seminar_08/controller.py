import database
import view





def input_my_class(inp: int):
    match inp:
        case 1:
            view.class_search(database.cop, database.cop2)
        case 2:
            view.name_serch(database.cop, database.cop2)
        case 3:
            pass
        case 4:
            view.exit_programm()


def start():
    while True:
        user_input = view.main_menu()
        input_my_class(user_input)






