def play_battleship():
    from random import randint
    print("""~enter coordinates like this : x,y
    ~coordinates should be between 5,5 and 0,0""")
    board = []

    for x in range(0, 5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print_board(board)

    def coordinate_input(message="Enter coodinate:"):
        location = input(str(message))
        location = location.split(",")
        x = location[0]
        y = location[1]
        return x, y

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)
    tries = 3

    for turn in range(tries):
        print("Turn", turn + 1)
        guess_coordinates = coordinate_input()
        guess_row = int(guess_coordinates[0])
        guess_col = int(guess_coordinates[1])

        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sank my battleship!")
            break
        else:
            if guess_row not in range(5) or \
                    guess_col not in range(5):
                print("Oops, that's not even in the ocean.")

            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
            print_board(board)
            if turn == tries - 1:
                print(f"Game Over,my ship was at {ship_row},{ship_col}")


play_battleship()
