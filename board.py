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

def player_input(board, player_id, row, column):
    if player_id == 1:
        input(board, row, column, "X") 
    else: 
        input(board, row, column, "O")

def input(board, row, column, mark):
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



# def place_mark():
#     if player_id:
#         input(rows, colums)
#         print(new_board)

#     else: 
#         print("Please enter a row and column.")

# def check_mark():
#     if input in board != "-":
#         return True
#         print(new_board)
#     else:
#         return False
#         print("Another player has already taken that space. Please choose again.")

def tic_tac_toe():
    board = new_board()
    print("Welcome to Tic Tac Toe")
    print_board(board)

tic_tac_toe()     


