#using lists within lists, create a means of storage for a TTT tic tac toe game, noughts and crosses
#the TTT board is 3 rows and 3 columns
#Before continuing, read the below code which shows how to create a chess board
#https://github.com/chrishoran8/PythonEssentialsModule3/blob/master/PythonEssentialsModule3/rowsSection.py
#As you can see, there are multiple ways to do this. The only requirement is that you get it working
#However, if you want to challenge yourself, get it working in as little lines of code as possible


print(
    """
    +================================+
    |   Welcome to my game of....    |
    |         TIC-TAC-TOE            |
    +================================+
    """)
# Create a multi-dimensional list and set the game to "True"
board = [[" ","1","2","3"],["1","_","_","_"],["2","_","_","_"],["3","_","_","_"]] 
game = True

while game: # Whilst the game is True (as set above) continue the loop
    print(" ***** Board *****") 
    for i in board: # Outputs a 2D board created by the list above (board)
        print(i)
    
    row_select = int(input("\nPlease select a row #: ")) # Prompts user to select a row and store input as an integer
    while row_select < 1 or row_select > 3: # Checks user input is valid, if not prompt user to enter a valid number 
        row_select = int(input("Please select a valid row between (1-3): "))
    col_select = int(input("Please select a column #: "))
    while col_select < 1 or col_select > 3:
        col_select = int(input("Please select a valid column between (1-3): "))
    player_choice = input("Please choose, x, o, or q to quit: ")

    # Checks the input from player_choice, if "q" end game, else store the value in the list
    if player_choice == "q": 
        print("\nThanks for playing!","\nGoodbye" )
        game = False
    else: 
        board[row_select][col_select] = player_choice 