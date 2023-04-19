# Tic-Tac-Toe
LOGO = """
         _______ _        _______           _______
        |__   __(_)      |__   __|         |__   __| 
           | |   _  ___     | | __ _  ___     | | ___   ___ 
           | |  | |/ __|    | |/ _` |/ __|    | |/ _ \\ / _ \\ 
           | |  | | (__     | | (_| | (__     | | (_) |  __/ 
           |_|  |_|\\___|    |_|\\__,_|\\___|    |_|\\___/ \\___|
"""

WIN_MOVES = (
    [0, 1, 2],
    [3, 4, 6],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
)
used_moves = []
player_one = "X"
player_two = "O"


def print_example_board():
    print("[0]" + " | " + "[1]" + " | " + "[2]")
    print("----------")
    print("[3]" + " | " + "[4]" + " | " + "[5]")
    print("----------")
    print("[6]" + " | " + "[7]" + " | " + "[8]")


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


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def new_board():
    board = []
    field = " "
    for _ in range(0, 9):
        board.append(field)
    return board


def player_move(board, player_mark):
    while True:
        player_choice = int(input("Wybierz od 0-8 gdzie chcesz postawic znak: "))
        if player_choice not in used_moves:
            board[player_choice] = player_mark
            used_moves.append(player_choice)
            return board
        else:
            print("te pole jest juz zajete, wybierz inne")


def check_winner(WIN_MOVES, player_mark, board):
    for x in WIN_MOVES:
        if board[x[0]] == player_mark and board[x[1]] == player_mark and board[x[2]] == player_mark:
            winner = player_mark
            print("wygral gracz: " + player_mark)
            return winner

def who_first(choice):
    if choice == 1:
        player = player_one
        print("Zaczyna gracz X")
        return player
    elif choice == 2:
        player = player_two
        print("Zaczyna gracz O")
        return player


def change_player(switch):
    if switch == player_one:
        switch = player_two
        return switch
    elif switch == player_two:
        switch = player_one
        return switch


board = new_board()
winner = None
player = player_one
while len(used_moves) < 9 and (winner != player_one and winner != player_two):
    print_board(board)
    player_move(board, player)
    winner = check_winner(WIN_MOVES, player, board)
    print(winner)
    player = change_player(player)
    print(player)
print_board(board)
print("Koniec gry")
