
id_dict = dict()


def read_data(path):
    with open(path, 'r', encoding='UTF-8') as data:
        result = data.readlines()
    for item in result:

        item = item.split(';')
        id_dict['Дата рождения'] = item[0]
        id_dict['Место жительства'] = item[1]
        id_dict['Телефон'] = item[2]
        id_dict['Русский язык'] = item[3]
        id_dict['Алгебра'] = item[4]
        id_dict['Литература'] = item[5]
        id_dict['География'] = item[6]

    return id_dict


res = read_data('Иванов_Иван.txt')
for v in id_dict.items():
    print(v)

