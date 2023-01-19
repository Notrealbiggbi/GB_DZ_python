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

