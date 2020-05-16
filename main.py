#-----Global Variables----------------

# Get the board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"] 

# To check is game is still going
game_going_on = True

#Check who wins or got tie
winner = None

#Check who is the current player
current_player = "X"


#Display the initial board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

#Play or Start the game
def play_game(): 
  
  
  print("Tic-Tac-Toe game. Here we go!!")

  #Display the inital board
  
  display_board()

  while game_going_on:
    
    #Handle a single turn to particular player
    handle_turn(current_player)

    #To check is game is over
    check_game_over()

    #Flip to another player
    flip_player()

    

  # The game has ended
  if winner =="X" or winner =="O":
    print(winner + " wons.")
  elif winner== None: 
    print("It's a Tie!")

    
 
#Handle a single turn to the particular player
def handle_turn(player):
  print(player + "'s turn.")
  position = input("Choose a number between 1-9: ")

  valid = False
  while not valid:

    #Check for valid input
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a number between 1-9: ")

    position = int(position) - 1

    #Allow to enter values if the position is empty
    if  board[position] == "-":
      valid = True
    else:
      print("The place is already filled.Enter again ")
  
  board[position]= player
  display_board()

#To check if game is over
def check_game_over():
  check_win()
  check_tie()
  

def check_win():

  global winner
  #check rows
  row_winner = check_rows()
  #check columns
  column_winner = check_columns()
  #check diagonals
  diagonal_winner = check_diagonals()


  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None 
  return


def check_rows():
  #Set up global variable
  global game_going_on

  #check if any of the rows have same value and is not empty
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  #if any rows does have a match, flag the value of game going on
  if row1 or row2 or row3:
    game_going_on = False

  #Return X or O
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return

def check_columns():
   #Set up global variable
  global game_going_on

  #check if any of the columns have same value and is not empty
  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"

  #if any rows does have a match, flag the value of game going on
  if column1 or column2 or column3:
    game_going_on = False
  
  #Return X or O
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  return
  

def check_diagonals():
   #Set up global variable
  global game_going_on

  #check if any of the diagonals have same value and is not empty
  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"
  
  #if any rows does have a match, flag the value of game going on
  if diagonal1 or diagonal2: 
    game_going_on = False
  
  #Return X or O
  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[2]
  
  return


def check_tie():
  global  game_going_on
  if "-" not in board:
    game_going_on = False
  return


def flip_player():
  global current_player

  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return


play_game()

while True:
  answer = input("Do you wish to play again? (y/n)")
  if answer == 'y':
    board=["-"] * 9
    game_going_on = True
    play_game()
  else:    
    print('The end.')





