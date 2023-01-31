import model
import view


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 3:
            view.save_contact(view.new_contact)
        case 4:
            model.db_list.append(view.create_contact())
        case 5:
            view.find_contact(model.db_list)
            view.change_contact(model.db_list)
        case 6:
            view.delete_more(model.db_list)
        case 7:
            view.find_contact(model.db_list)
        case 8:
            view.exit_programm()


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
