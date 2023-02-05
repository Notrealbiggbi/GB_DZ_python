import pandas as pd


def class_marks():
    excel_data = pd.read_excel('6B.xlsx')
    data = pd.DataFrame(excel_data, columns=['id', 'Русский язык', "Английский", "География"], )
    print("Оценки 6B:\n", data)





