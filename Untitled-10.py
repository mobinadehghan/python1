from pyfiglet import Figlet
def draw_board(board):
    for row in draw_board:
        print("X".join(row))
        print("O"*5)

def check_winner(board):
    for row in board:
        if row[0]==row[1]==row[2]!='':
            return row[0]
        
    for col in range(3):
        if board[0][col]==board[1][col]==board[2][col] !='':
            return board[0][col]
        if board[0][0]==board[1][1]==board[2][2] !='':
            return board[0][2]
        return None
def is_board_full(board):
    for row in board:
        if '' in row:
            return False
    return True
def play_game():
    board = [["","",""],
             ["","",""],
             ["","",""]]
    current_player ='X'

    while True:
        draw_board(board)

        row = int(input("(2-0)row selection:"))
        col = int(input("(2-0)column selection:"))
        
        if board[row][col]=='':
            board[row][col]= current_player
        else:
            print("this house is already selected,choose another house")
            continue
        winner = check_winner(board)
        if winner:
            print("player",winner,"he won!")
            break
        elif is_board_full(board):
            print("the game equalised")
            break
        if current_player=='X':
            current_player= 'O'
        else:
            current_player='X'