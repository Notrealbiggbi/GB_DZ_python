import view
import model

def start():
    while True:
        if view.start_lesson() == 'yes':
            try:
                model.set_class(view.input_class())
                model.set_subject(view.input_subject())
                model.open_file()
                journal = model.get_journal()
                view.list_of_child(journal)
                student = view.who_answer()
                if student == 'exit':
                    break
                mark = int(view.what_mark())
                model.student_mark(student, mark)
                model.save_file()
            except:
                view.no_class()
        elif view.start_lesson() == 'no':
            view.close_lesson()
            break


