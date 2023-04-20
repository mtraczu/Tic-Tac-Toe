# Tic-Tac-Toe
import random

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
PLAYER_ONE = "X"
PLAYER_TWO = "O"


def print_example_board():
    print("[0]" + " | " + "[1]" + " | " + "[2]")
    print("----------")
    print("[3]" + " | " + "[4]" + " | " + "[5]")
    print("----------")
    print("[6]" + " | " + "[7]" + " | " + "[8]")


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
        try:
            player_choice = int(input("Choose from 0-8 where you want to put your mark:"))
            if player_choice in range(0, 9):
                if player_choice not in used_moves:
                    board[player_choice] = player_mark
                    used_moves.append(player_choice)
                    return board
                else:
                    print("This field is already used, select another")
            else:
                print("Wrong move")
        except ValueError:
            print("Invalid option")


def computer_move(board, player_mark):
    while True:
        player_choice = random.randint(0, 8)
        if player_choice not in used_moves:
            board[player_choice] = player_mark
            used_moves.append(player_choice)
            return board


def check_winner(win_moves, player_mark, board):
    for x in win_moves:
        if board[x[0]] == player_mark and board[x[1]] == player_mark and board[x[2]] == player_mark:
            winner = player_mark
            print_board(board)
            print("The winner is: " + player_mark)
            input("Press Enter to exit")
            return winner


def change_player(switch):
    if switch == PLAYER_ONE:
        switch = PLAYER_TWO
        return switch
    elif switch == PLAYER_TWO:
        switch = PLAYER_ONE
        return switch


def game(computer_or_human, chosen_player=PLAYER_ONE):
    board = new_board()
    winner = None
    player = chosen_player
    while len(used_moves) < 9 and (winner != PLAYER_ONE and winner != PLAYER_TWO):
        print_board(board)
        if player == PLAYER_ONE:
            print("Player " + PLAYER_ONE + " turn")
            player_move(board, player)
            winner = check_winner(WIN_MOVES, player, board)
        elif player == PLAYER_TWO:
            print("Player " + PLAYER_TWO + " turn")
            computer_or_human(board, player)
            winner = check_winner(WIN_MOVES, player, board)
        player = change_player(player)
        print(player)
    print_board(board)
    print("End of game")


def main():
    while True:
        print(LOGO)
        print("1. Start game")
        print("2. Rules of the game")
        print("3. Exit\n")
        player_choice = input("Choose option: ")
        if player_choice == "1":
            print("1. Human vs. Human")
            print("2. Human vs. Computer")
            player_choice = input("Choose option: ")
            if player_choice == "1":
                game(player_move)
            elif player_choice == "2":
                print("1. Human starts first")
                print("2. Computer starts first")
                player_choice = input("Choose option: ")
                if player_choice == "1":
                    game(computer_move)
                elif player_choice == "2":
                    game(computer_move, PLAYER_TWO)
        elif player_choice == "2":
            print("""\nPlayer chooses a number from 0 to 8, which corresponds to a field on the board. 
After choosing, there is a swap and the next player chooses their field. To win, you need to arrange 3 identical 
symbols in one line - horizontally, vertically or diagonally. The board below shows the arrangement of numbers that 
should be chosen.\n""")
            print_example_board()
            input("\nPress Enter to exit")
        elif player_choice == "3":
            print("Goodbye")
            break


main()
