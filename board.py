import itertools

# player_id = itertools.cycle([1,2])
# new_board = board.replace(player_input)
# rows = [0,1,2]
# colums = [0,1,2]



def new_board():
    return [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"],
    ]

def print_board(board):
    for row in board:
            print(row)

def player_input(board, row, column, player_id):
    if player_id == 1:
        add_mark(board, row, column, "X") 
    else: 
        add_mark(board, row, column, "O")

def add_mark(board, row, column, mark):
    if check_size(board, row):
        if check_size(board[row], column):
            if not check_mark(board, row, column):
                board[row][column] = mark
            else: 
                print("This location is already taken.")
        else:
            print("invalid column size")
    else:
        print("invalid row size")

def check_size(line, value):
    if value > 0 and value < len(line):
        return True
    
    return False

def check_mark(board, row, column):
    return board[row][column] != "-"

def tic_tac_toe():
    board = new_board()
    print("Welcome to Tic Tac Toe")
    print_board(board)
    print("Player 1 place your X")
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    player_input(board, row, column, 1)
    print_board(board)


tic_tac_toe()     


