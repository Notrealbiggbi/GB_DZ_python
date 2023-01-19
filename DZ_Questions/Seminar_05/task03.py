with open('file2.txt', 'w', encoding='UTF-8') as file:
    file.write('wwwwwwwwwwwwweeeeeeeeeeeeeeeeqqqqqqqqqqqqqqqqq')


def arxivator(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding


def razarxiv(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode


with open('file2.txt') as file:
    my_azz = file.read()


result = arxivator(str(my_azz))

print(result)


res = razarxiv(result)
print(res)

with open('file3.txt', 'w', encoding='UTF-8') as ress:
    ress.write(result)


with open('file4.txt', 'w', encoding='UTF-8') as resss:
    resss.write(res)

