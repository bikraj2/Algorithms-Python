import random
def generate_board(n):
    board =[]
    for col in range(n):
        row = random.randint(0,n-1)
        board.append((row,col))
    return board
def isValid(board):
    for i in range(len(board)):
        for j in range(i+1,len(board)):
            if board[i][0] == board[j][0] or ((abs(board[i][0]-board[j][0]) ==(abs(board[i][1]-board[j][1])))):
                return False
    return True
def n_queens(n):
    while True:
        board = generate_board(n)
        if (isValid(board)):
            return board

def print_board(board):
    N = len(board)
    for row in range(N):
        line = ""
        for col in range(N):
            if (row, col) in board:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")
print_board(n_queens(1000))

