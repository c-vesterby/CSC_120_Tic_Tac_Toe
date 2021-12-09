import itertools

def new_board():
    return [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]

def print_board(board):
    for row in board:
            print(row)

def add_mark(board, row, column, mark):
    if check_size(board, row):
        if check_size(board[row], column):
            if not check_mark(board, row, column):
                board[row][column] = mark
            else: 
                return "This location is already taken."
        else:
            return "invalid column size"
    else:
        return "invalid row size"

def check_size(line, value):
    if value >= 0 and value < len(line):
        return True
    
    return False

def check_mark(board, row, column):
    return board[row][column] != "-"

def mark(player_id):
    if player_id == 1:
        return "X"
    else:
        return "O"

def check_win(board):
    for row in board:
        current_mark ="" 
        count = 0
        for mark in row:
            if mark != "-":
                if count == 0:
                    count = count + 1
                    current_mark = mark

            

    # for col in range(len(board)):
    #     check = []

    #     for row in board:
    #         check.append(row[col])

    #     if row.count(row[0]) == len(row) and row [0] != ("-"):
    #             print("Winner!")
    #             return True

    # diag = []
    # for col, row in enumerate(reversed(range(len(board)))):
    #     diag.append(board[row][col])
    # if diag.count(diag[0]) == len(diag) and diag [0] != 0:
    #             print("Winner!")
    #             return True

    # diag = []
    # for ix in range(len(board)):
    #     diag.append(board[ix][ix])
    # if diag.count(diag[0]) == len(diag) and diag [0] != 0:
    #             print("Winner!")
    #             return True
    # return False    

def tic_tac_toe():
    board = new_board()
    print("Welcome to Tic Tac Toe")
    print_board(board)

    for player_id in itertools.cycle([1,2]):
        print("Player " + str(player_id) + " place your " + mark(player_id))
        
        #Need loop to run at least once.
        error = ""
        while error is not None:
            if len(error) > 0:
                print("Invalid location, " + error)
            #TODO Enter is invalid when value is not a integer
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
            error = add_mark(board, row, column, mark(player_id))
        print_board(board)
        check_win(board)


tic_tac_toe()     


