# Tic Tac Toe game in Python (text-based)
def print_board(board):
    """Displays the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows & columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Column win

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Main diagonal win
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Anti-diagonal win

    return None  # No winner

def is_board_full(board):
    """Checks if the board is full (draw)."""
    return all(cell != " " for row in board for cell in row)

def get_valid_input(board):
    """Gets valid player input (ensures the cell is empty)."""
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Choose another one.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter two numbers between 0 and 2.")

def tic_tac_toe():
    """Main function to run the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {players[turn % 2]}'s turn.")
        row, col = get_valid_input(board)
        board[row][col] = players[turn % 2]
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"🎉 Player {winner} wins! 🎉")
            break
        elif is_board_full(board):
            print("It's a draw! 🤝")
            break

        turn += 1

# Run the game
tic_tac_toe()
