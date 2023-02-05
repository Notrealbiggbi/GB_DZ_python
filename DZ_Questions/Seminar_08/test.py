import pandas as pd


def class_marks():
    excel_data = pd.read_excel('6B.xlsx')
    data = pd.DataFrame(excel_data, columns=['id', 'Русский язык', "Английский", "География"], )
    print("Итоговые оценки 6B:\n", data)


def class_marks2():
    excel_data2 = pd.read_excel('5A.xlsx')
    data2 = pd.DataFrame(excel_data2, columns=['id', 'Русский язык', "Английский", "География"], )
    print("Итоговые оценки 5A:\n", data2)

