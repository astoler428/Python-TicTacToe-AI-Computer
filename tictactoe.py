from os import system
from random import choice

board = [" " for x in range(9)]

wins = [[0, 1, 2], 
        [3, 4, 5], 
        [6, 7, 8], 
        [0, 3, 6], 
        [1, 4, 7], 
        [2, 5, 8], 
        [0, 4, 8], 
        [2, 4, 6]]


# checks for a draw based on full board: Does not check if there is a winner though

#token is X or O
def win(token):
  for win in wins:
    if board[win[0]] == board[win[1]] == board[win[2]] == token:
      return True 
  return False

#only used for comp_move function 
def draw():
    for spot in range(9):
      if board[spot] == " ":
        return False
    return True
    


# Function: displays the current board with "X" and "O"
def print_board():
    print("\n")
    print(f"   ||   ||   ")
    print(f" {board[0]} || {board[1]} || {board[2]} ")
    print(f"   ||   ||   ")
    print("=============")
    print(f"   ||   ||   ")
    print(f" {board[3]} || {board[4]} || {board[5]} ")
    print(f"   ||   ||   ")
    print("=============")
    print(f"   ||   ||   ")
    print(f" {board[6]} || {board[7]} || {board[8]} ")
    print(f"   ||   ||   ")
    print("\n")

# Function: Takes player input and changes board with selection
def player_turn():
    while True:
        # Take player input
        raw = input("Please Select a Number 0-8: ")
        # Check for allowable inputs -> continue (reloop) if NOT allowed
        if raw not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]: continue
        # Change player raw input into integer
        else: spot = int(raw)
        # Check for if board selection has already been played -> break if not played yet
        if board[spot] == " ": break
        # Else reloop to select a new board location
        else: print("Already selected. Choose again: ")
    # Changes board using player token
    board[spot] = "X"
    


# Function: to reset game and game board
def reset():
    while True:
        # take player input
        raw = input("Would you like to play again? (Yes or No) ")
        select = raw.lower()[0]
        if select not in ["y", "n"]: continue
        elif select == 'y':
            for x in range(9):
                board[x] = " "
            system('clear')
            tic_tac_toe()
            break
        else:
            break


   

def cpu_turn():
    spot = best_cpu_move(0)
    board[spot] = 'O'


# computer finds the best move through a minmax strategy with backtracking
# -1 is comp loses, 0 is draw, 1 is comp wins
def best_cpu_move(depth):
    #base cases
    if win('X'):
      return -1
    if draw():
       return 0
    
    #start assuming a loss
    move_value = -1
    #no best spot yet
    best_spot = None
    
    # For each spot on the board
    for spot in range(9):
        #If the spot is open, try making the move there if it's open
        if board[spot] == " ":
            #set default best spot to first available move
            if best_spot == None:
              best_spot = spot
            board[spot] = "O"
            #determine the value of the best possible player response to that move
            value = best_player_move(depth)
           
            if value > move_value:
              move_value = value
              best_spot = spot
            #reset the board spot
            board[spot] = " "

#special case where it's the original depth and you are returning to the cpu_turn function
    if depth == 0:
       return best_spot

    return move_value      
            

def best_player_move(depth):
    #base cases

    if win('O'):
       return 1
    elif draw():
       return 0
    

    #start assuming a comp win
    move_value = 1
    #no best spot yet
    best_spot = None
    
    # For each spot on the board
    for spot in range(9):
        #If the spot is open, try making the move there
        if board[spot] == " ":
            #set default best spot to first available move
            if best_spot == None:
              best_spot = spot
            board[spot] = "X"
            #determine the value of the best possible player response to that move
            value = best_cpu_move(depth+1)

            if value < move_value:
              move_value = value
              best_spot = spot
            #reset the board spot
            board[spot] = " "

    return move_value   



# Function: tic-tac-toe two-player game 
def tic_tac_toe():
    # boolean controls main game while loop
    gameOn = True
    open_spaces = 9
    print("Welcome to Ari's Tic-Tac-Toe Game in Python!")

    while gameOn:
        print_board()

        player_turn()
        open_spaces -= 1

        if win('X'):
           print('X wins!')
           gameOn = False
        elif open_spaces == 0:
            print("It's a draw")
            gameOn = False
      
        cpu_turn()
        open_spaces -= 1

        if win('O'):
           print('O wins!')
           gameOn = False
            
    print_board()
    reset()
   

tic_tac_toe()