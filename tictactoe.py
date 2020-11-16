board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
count = 0
position = 0
player = "X"
possibilities = [1,2,3,4,5,6,7,8,9]

def display_board():
    print(board[0], " | ", board[1], " | ", board[2], "   1|2|3")
    print(board[3], " | ", board[4], " | ", board[5], "   4|5|6")
    print(board[6], " | ", board[7], " | ", board[8], "   7|8|9")


def turn_inp(player):
    global position
    position = int(input(f"Turn for '{player}'.ENTER Position: "))
    if position not in possibilities:
        print("has to be an integer between 0-9")
        pass
    else:
        position = int(position) - 1
        if player == "X":
            board[position] = "X"

        else:
            board[position] = "O"
        display_board()


def check_rep(position1):
    if board[position1] == "X" or board[position1] == "O":
        return True
    else:
        return False


def main_loop():  # Main loop
    game_running = True
    global position
    global count
    global player

    display_board()

    while game_running:

        if count % 2 == 0:
            player = "O"

        elif count % 2 == 1:
            player = "X"

        turn_inp(player)

        if check_row() or check_col() or check_diagonal():
            print(f"{player} wins")
            break
        elif check_tie():
            print("Tie!!")
            break

        else:
            count += 1


def switch_player(player1):
    global player
    if player1 == "X":
        player = "O"
        return player
    if player1 == "O":
        player = "X"
        return player
    # if check_rep(position):
    #     print("That place is taken .try agaain")
    #     pass


def check_tie():
    if board[0] != "-" and board[1] != "-" and board[2] != "-" and board[3] != "-" and board[4] != "-" \
            and board[5] != "-" and board[6] != "-" and board[7] != "-" and board[8] != "-":
        return True


def check_row():
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        return True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return True
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        return True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return True
    else:
        return False


def check_col():
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        return True
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        return True
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        return True
    else:
        return False


def check_diagonal():
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        return True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return True
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        return True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return True


main_loop()
