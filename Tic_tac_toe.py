# A list of lists = matrix
board = [
    ['1','2','3'],      #[1=00,2=01,3=02]
    ['4','5','6'],      #[4=10,5=11,6=12]
    ['7','8','9']       #[7=20,8=21,9=22]
]


# Function: displays the tic-tac-toe board in the console
def display_board():
    i = 0
    for row in board:
        print('|'.join(row))
        if i < 2:
            print('-'*5)
            i= i+1


# Function: check if a player won the game
def check_win():
    #Check for Xs
    # Horizontal
    if board[0][0] == board[0][1] == board[0][2] == 'X':
        print("player X complete a horizontal line --> WINNER!!")
        return True
    elif board[1][0] == board[1][1] == board[1][2] == 'X':
        print("player X complete a horizontal line --> WINNER!!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == 'X':
        print("player X complete a horizontal line --> WINNER!!")
        return True
    # Vertical
    elif board[0][0] == board[1][0] == board[2][0] == 'X':
        print("player X complete a vertical line --> WINNER!!")
        return True
    elif board[0][1] == board[1][1] == board[2][1] == 'X':
        print("player X complete a vertical line --> WINNER!!")
        return True
    elif board[0][2] == board[1][2] == board[2][2] == 'X':
        print("player X complete a vertical line --> WINNER!!")
        return True
    # Diagonal
    elif board[0][0] == board[1][1] == board[2][2] == 'X':
        print("player X complete a diagonal line --> WINNER!!")
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'X':
        print("player X complete a diagonal line --> WINNER!!")
        return True
    #Check for Ys
    # horizontal
    elif board[0][0] == board[0][1] == board[0][2] == 'Y':
        print("player Y complete a horizontal line --> WINNER!!")
        return True
    elif board[1][0] == board[1][1] == board[1][2] == 'Y':
        print("player Y complete a horizontal line --> WINNER!!")
        return True
    elif board[2][0] == board[2][1] == board[2][2] == 'Y':
        print("player Y complete a horizontal line --> WINNER!!")
        return True
    # Vertical
    elif board[0][0] == board[1][0] == board[2][0] == 'Y':
        print("player Y complete a vertical line --> WINNER!!")
        return True
    elif board[0][1] == board[1][1] == board[2][1] == 'Y':
        print("player Y complete a vertical line --> WINNER!!")
        return True
    elif board[0][2] == board[1][2] == board[2][2] == 'Y':
        print("player Y complete a vertical line --> WINNER!!")
        return True
    # Diagonal
    elif board[0][0] == board[1][1] == board[2][2] == 'Y':
        print("player Y complete a diagonal line --> WINNER!!")
        return True
    elif board[0][2] == board[1][1] == board[2][0] == 'Y':
        print("player Y complete a diagonal line --> WINNER!!")
        return True
    
    # No win detected
    return False


#
def get_player_input():
    input_val = int(input("Enter the number of the cell you want to mark (1-9): "))
    if input_val == 1:
        row = 0 
        col = 0
    elif input_val == 2:
        row = 0
        col = 1
    elif input_val == 3:
        row = 0
        col = 2
    elif input_val == 4:
        row = 1
        col = 0
    elif input_val == 5:
        row = 1
        col = 1
    elif input_val == 6:
        row = 1
        col = 2
    elif input_val == 7:
        row = 2
        col = 0
    elif input_val == 8:
        row = 2
        col = 1
    elif input_val == 9:
        row = 2
        col = 2
    else:
        print("Invalid input. Please enter a number between 1 and 9")
        # Recursively call the function again to prompt the user for valid input
        return get_player_input()
    
    return row, col


# Function: Shows the current player's movement on the board
def make_move(row, col, player):
    board [row][col] = player


# Function: change from one player to another 
def switch_player(player):
    if player == 'X':
        player = 'Y'
    elif player == 'Y':
        player = 'X'
    return player    


def main():
    current_player = 'X'
    while True:
        display_board()
        row, col = get_player_input()
        make_move(row, col, current_player)
        # Checks if the win condition is met
        if check_win():     
            display_board()
            print(f"Player {current_player} wins!")
            break
        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()






# Enter players name
#player_1 = input("Enter a name for player 1: ")
#player_2 = input("Enter a name for player 2: ")

#print("Ok! the players are", player_1, "and", player_2)
#print(player_1, "starts the game")


