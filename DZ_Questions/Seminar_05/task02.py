from random import randint as RI

board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}


def print_board(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


turn = 'X'

for _ in range(9):
    if board['1'] == 'X' and board['2'] == 'X' and board['3'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['4'] == 'X' and board['5'] == 'X' and board['6'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['7'] == 'X' and board['8'] == 'X' and board['9'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['1'] == 'X' and board['5'] == 'X' and board['9'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['3'] == 'X' and board['5'] == 'X' and board['7'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['1'] == 'X' and board['4'] == 'X' and board['7'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['2'] == 'X' and board['5'] == 'X' and board['8'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    elif board['3'] == 'X' and board['6'] == 'X' and board['9'] == 'X':
        print('Игра окончена выиграли крестики!')
        break
    if board['1'] == 'O' and board['2'] == 'O' and board['3'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['4'] == 'O' and board['5'] == 'O' and board['6'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['7'] == 'O' and board['8'] == 'O' and board['9'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['1'] == 'O' and board['5'] == 'O' and board['9'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['3'] == 'O' and board['5'] == 'O' and board['7'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['1'] == 'O' and board['4'] == 'O' and board['7'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['2'] == 'O' and board['5'] == 'O' and board['8'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    elif board['3'] == 'O' and board['6'] == 'O' and board['9'] == 'O':
        print('Игра окончена выиграли нолики!')
        break
    print(' ')
    print_board(board)
    print(' ')
    move = input('Введи номер поля куда хочешь поставить крестик или нолик от 1 до 9: ')
    print(' ')
    board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


print_board(board)
print(' ')
print('Игра окончена!!!')



# ИГРА В КРЕСТИКИ НОЛИКИ 2.0

maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

def print_maps():
    print(maps[0], end="")
    print(maps[1], end="")
    print(maps[2])

    print(maps[3], end="")
    print(maps[4], end="")
    print(maps[5])

    print(maps[6], end="")
    print(maps[7], end="")
    print(maps[8])

def step_maps(step, simbol):
    ind = maps.index(step)
    maps[ind] = simbol


def get_result():
    win = ""

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    return win


def check_line(sum_O, sum_X):

    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if maps[line[j]] == "O":
                o += 1
            if maps[line[j]] == "X":
                x += 1
        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if maps[line[j]] != "O" and maps[line[j]] != "X":
                    step = maps[line[j]]
    return step

def AI():

    step = ""

    step = check_line(0, 2)

    if step == "":
        step = check_line(0, 2)

    if step == "":
        step = check_line(1, 0)

    if step == "":
        if maps[4] != "X" and maps[4] != "O":
            step = 5

    if step == "":
        if maps[0] != "X" and maps[0] != "O":
            step = 1

    return step

game_over = False
human = True

while game_over == False:

    print_maps()

    if human == True:
        symbol = "X"
        step = int(input("Твой Ход Кожаный мешок: "))
    else:
        print("Мой ход, а ты подожди ")
        symbol = "O"
        step = AI()


    if step != "":
        step_maps(step, symbol)
        win = get_result()
        if win != "":
            game_over = True
        else:
            game_over = False
    else:
        print(" Ничья!")
        game_over = True
        win = "дружба"

    human = not(human)

print_maps()
print(f"Победил(а), {win}")