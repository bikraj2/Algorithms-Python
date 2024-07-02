import random

def generate_random_board(N):
    board = []
    for col in range(N):
        row = random.randint(0, N-1)
        board.append((row, col))
    print(board)
    return board
def is_valid(board):
    for i in range(len(board)):
        for j in range(i+1, len(board)):
            if board[i][0] == board[j][0] or abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):
                return False
    return True
def las_vegas_n_queens(N):
    while True:
        board = generate_random_board(N)
        if is_valid(board):
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

# Example usage
N = 5
solution = las_vegas_n_queens(N)
print_board(solution)
