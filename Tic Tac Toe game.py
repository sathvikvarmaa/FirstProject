# Define a 3x3 board using a list of lists
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Define a function to display the current state of the board
def display_board():
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-+-+-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-+-+-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

# Define a function to check if a player has won
def check_win(player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Define a function to check if the board is full
def check_tie():
    for row in board:
        if " " in row:
            return False
    return True

# Define the main game loop
def play_game():
    current_player = "X"
    while True:
        # Display the current state of the board
        display_board()
        # Ask the current player to make a move
        print("It's " + current_player + "'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        # Check if the move is valid
        if board[row][col] == " ":
            board[row][col] = current_player
            # Check if the current player has won
            if check_win(current_player):
                print(current_player + " wins!")
                display_board()
                return
            # Check if the game is tied
            if check_tie():
                print("It's a tie!")
                display_board()
                return
            # Switch to the other player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        else:
            print("Invalid move. Please try again.")

# Start the game
play_game()
