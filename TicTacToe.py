# A AI based Tic Tac Toe game which is Unbeatable

import math

def initialize_board():
    return [" " for _ in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---------")
    print()

def is_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_draw(board):
    return " " not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 10 - depth
    if is_winner(board, "X"):
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_game():
    board = initialize_board()
    while True:
        print_board(board)
        
        # Human move
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] != " " or move not in range(9):
                print("Invalid move. Try again.")
                continue
            board[move] = "X"
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")
            continue
        
        if is_winner(board, "X"):
            print_board(board)
            print("Congratulations! You win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI move
        move = find_best_move(board)
        board[move] = "O"
        
        if is_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()

