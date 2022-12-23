# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.



text =['my', 'room', 'so', 'dirty']
search = 'o'
for i in range(len(text)):
    if search in text[i]:
        print(f'В {text[i]} присутствует {search}')
    else:
        print(f'В {text[i]} нет {search}')
