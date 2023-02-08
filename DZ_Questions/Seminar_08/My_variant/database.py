# Создаём функцию чтения из файла(нашей базы данных)


class Read:
    def __init__(self, path):
        self.path = path
        self.db_list = []

    def file_read(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            result = data.readlines()
        for item in result:
            id_dict = dict()
            item = item.split()
            id_dict['lastmame'] = item[0]
            id_dict['name'] = item[1]
            self.db_list.append(id_dict)
        return self.db_list

    def file_read2(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            result = data.readlines()
        for item in result:
            id_dict = dict()
            item = item.strip().split(':')
            id_dict['ФИО'] = item[0]
            id_dict['Оценки'] = item[1]
            self.db_list.append(id_dict)
        return self.db_list


new_db_list = Read('5A.txt')
new_db_list2 = Read('6B.txt')
new_db_list3 = Read('math.txt')

cop = new_db_list.file_read()
cop2 = new_db_list2.file_read()
cop3 = new_db_list3.file_read2()

new_dict = None
for c in cop3:
    for i in c.values():
        new_dict = i
    print(new_dict)



