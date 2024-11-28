
# Function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

# Function to check if the board is full (a draw)
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Create an empty 3x3 board
    current_player = "X"  # Player "X" starts

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn!")

        # Player input for row and column
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        # Check if the chosen spot is empty
        if board[row][col] == " ":
            board[row][col] = current_player  # Place the player's mark
        else:
            print("Spot already taken, try again!")
            continue  # Ask for input again

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break  # Exit the game

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break  # Exit the game

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()





