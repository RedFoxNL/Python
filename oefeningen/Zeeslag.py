from random import randint
BOARD_SIZE = 4
NR_GUESSES = 4
turn = 0

#initializing board
board = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)
def print_board(board):
    for row in board:
        print (" ".join(row))

#start the game and printing the board
print ("Speel zeeslag!")
print_board(board)

#define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)


for turn in range(NR_GUESSES):

    # ask input from user
    input_row = int(input("Kies een rij: "))
    input_col = int(input("Kies een vak: "))

    #print Win
    if input_row == ship_row and input_col == ship_col:
        print("\n WIN!!!!!!!")
        break

    else:
        #checkt of buiten het bord
        if (input_row < 0 or input_row > 4) or (input_col < 0 or input_col > 4):
            print("Keuze is buiten bereik van het bord!\n")

        #check of keuze al eerder is gemaakt
        elif board[input_row - 1][input_col - 1] == "X":
            print ("U heeft deze al ingevoerd \n")
        else:
            #plaast een X op het bord.
            board[input_row - 1][input_col - 1] = "X"
            turn += 1

        #print hoe vaak je nog mag gokken
        print("\nU heeft nog ",NR_GUESSES-turn," kansen")
        print_board(board)
else:

    print("Game Over")