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
    print(" \n***** Board *****")
    for i in board: # Outputs a 2D board created by the list above (board)
        print(i)
    valid = ["1", "2", "3"]
    x_o_q = ["x", "o", "q"]

    for a,s,d,f in board:

        if s and d and f == x_o_q[0]:
            print("\nWinner Winner Chicken Dinner!")
            print("\nThanks for playing!", "\nGoodbye")
            game = False
            break
        elif s and d and f == x_o_q[1]:
            print("\nWinner Winner Chicken Dinner!")
            print("\nThanks for playing!", "\nGoodbye")
            game = False
            break

    validate_row = True
    while validate_row:
        row = input("\nPlease select a row #: ")
        for i in valid:
            if i == row[0]:
                row = int(row)
                validate_row = False
                break
        else:
            print("Please select a valid row between (1-3)!")

    validate_col = True
    while validate_col:
        col = input("\nPlease select a column #: ")
        for i in valid:
            if i == col[0]:
                col = int(col)
                validate_col = False
                break
        else:
            print("Please select a valid col between (1-3)!")

    validate_choice = True
    while validate_choice:
        player_choice = input("\nPlease choose, x, o, or q to quit: ")
        for i in x_o_q:
            if player_choice[0] == x_o_q[-1]:
                print("\nThanks for playing!", "\nGoodbye")
                game = False
                validate_choice = False
                break
            elif i == player_choice[0]:
                free_space = True
                while free_space:
                    for x in x_o_q:
                        if board[row][col] != x:
                            board[row][col] = player_choice
                            validate_choice = False
                            free_space = False
                            break
                        else:
                            print("\nTry again that space is taken!")
                            free_space = False
                            validate_choice = False
                            break
                break
        else:
            print("Invalid character!")