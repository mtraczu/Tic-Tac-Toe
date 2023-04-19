# Tic-Tac-Toe
# 1. Zrobic menu z opcjami: 1. Start gry > Zaczynasz pierwszy czy komputer zaczyna pierwszy, 2. Ilosc wygranych i przegranych, 3. Wyjscie z gry
# 2. Zrobic plansze gry
# 3. Zrobic wygrywajace ruchy

""" Po rozpoczeciu gry w zaleznosci kto pierwszy zaczyna stawia swoj znak,
        Petla:
        Sprawdzenie wygrywajacych ruchow oraz czy ruch zostal wykonany i nastepuje zamiana stron

"""
LOGO = """
         _______ _        _______           _______
        |__   __(_)      |__   __|         |__   __| 
           | |   _  ___     | | __ _  ___     | | ___   ___ 
           | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\ 
           | |  | | (__     | | (_| | (__     | | (_) |  __/ 
           |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|
"""


def menu():
    while True:
        print(LOGO)
        print("1. Rozpocznij gre")
        print("2. Sprawdz ilosc przegranych i wygranych")
        print("3. Wyjdz z gry\n")
        player_choice = input("Wybierz opcje: ")
        if player_choice == "1":
            print("1. Czlowiek vs Czlowiek")
            print("2. Czlowiek vs Komputer")
            player_choice = input("Wybierz opcje: ")
            if player_choice == "1":
                print("Tutaj bedzie funkcja")
            elif player_choice == "2":
                print("1. Zaczynam jako pierwszy")
                print("2. Komputer Zaczyna jako pierwszy")
                player_choice = input("Wybierz opcje: ")
                if player_choice == "1":
                    print("Funkcja gry zaczyna czlowiek")
                elif player_choice == "2":
                    print("funkcja gry - zaczyna komputer")
        elif player_choice == "2":
            print("Sprawdzam wyniki")
            input("Nacisnij enter aby wyjsc")
        elif player_choice == "3":
            print("Good Bye")
            break


Empty_board_list = ["x", "x", "x", " ", " ", " ", "o", "o", "o"]

#menu()


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def new_board():
    board = []
    field = " "
    for _ in range(0,9):
        board.append(field)
    return board


board = new_board()
print_board(board)
