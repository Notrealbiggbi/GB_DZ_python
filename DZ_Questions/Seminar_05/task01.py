from random import randint as RI


my_candy = 150
take_candy = 0
player_candy = 0
player1_candy = 0
player2_candy = 0
bot_candy = 0

def player_or_bot():
    turn = int(input("Выбери с кем играть с ботом нажми 1 или с человеком нажми 2:  "))
    if turn == 1:
        start_game_with_bot()
    else:
        start_game_with_player()


def start_game_with_player():
    print("Игра началась всего на столе лежит 150 конфет бери \n"
            "конфеты пока их не останется но брать можно не больше 28")
    who_is_first()


def start_game_with_bot():
    print("Игра началась всего на столе лежит 150 конфет бери \n"
          "конфеты пока их не останется но брать можно не больше 28")
    who_is_first_with_bot()



def who_is_first():
    random_number = RI(1, 2)
    if random_number == 1:
        player1_turn()
    else:
        player2_turn()


def who_is_first_with_bot():
    random_number = RI(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()


def player1_turn():
    global my_candy
    global take_candy
    global player1_candy
    print(f"Твой ход Первый игрок. Конфет {my_candy}")
    take_candy = int(input("Сколько конфет возьмёшь?: "))
    while take_candy > 28 or take_candy < 0 or take_candy > my_candy:
        take_candy = int(input("Слишком ного взял. Сколько конфет возьмёшь? "))
    my_candy -= take_candy
    player1_candy += take_candy
    if my_candy > 0:
        bot_turn()
    else:
        print("Победа!!")


def player2_turn():
    global my_candy
    global take_candy
    global player2_candy
    print(f"Твой ход Второй игрок. Конфет {my_candy}")
    take_candy = int(input("Сколько конфет возьмёшь?: "))
    while take_candy > 28 or take_candy < 0 or take_candy > my_candy:
        take_candy = int(input("Слишком ного взял. Сколько конфет возьмёшь? "))
    my_candy -= take_candy
    player2_candy += take_candy
    if my_candy > 0:
        player1_turn()
    else:
        print("Победа!!")


def player_turn():
    global my_candy
    global take_candy
    global player_candy
    print(f"Твой ход. Конфет {my_candy}")
    take_candy = int(input("Сколько конфет возьмёшь?: "))
    while take_candy > 28 or take_candy < 0 or take_candy > my_candy:
        take_candy = int(input("Слишком ного взял. Сколько конфет возьмёшь? "))
    my_candy -= take_candy
    player_candy += take_candy
    if my_candy > 0:
        bot_turn()
    else:
        print("Победа!!")


def bot_turn():
    global take_candy
    global my_candy
    global bot_candy
    take_candy = my_candy % 29 if my_candy % 29 != 0 else RI(1, 28)
    my_candy -= take_candy
    bot_candy += take_candy
    print(f"Бот взял {take_candy} конфет! Осталось {my_candy} конфет")
    if my_candy > 0:
        player1_turn()
    else:
        print("Победа БОТА!!")


player_or_bot()
