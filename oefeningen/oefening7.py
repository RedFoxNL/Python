from random import randint


BOARD_SIZE = 4
NR_GUESSES = 4
turn = 0
#initializing board
board = []
guesses = []
for x in range(BOARD_SIZE):
    board.append(["O"] * BOARD_SIZE)

def print_board(board):
    for row in board:
        print (" ".join(row))

#start the game and printing the board
print ("Let's play Battleship!")
print_board(board)

#define where the ship is
ship_row = randint(0, BOARD_SIZE-1)
ship_col = randint(0, BOARD_SIZE-1)


#here your code :
#-ask the user for a guess
guess = int((input("Take a guess: ")))
guesses.append(guess)
turn + 1
#-if the user's right, the game ends
if guess == ship_col and ship_row:
    print("You've won the game")

#-warn if the guess is out of the board
if guess > ship_row or guess > ship_col:
    print("The number you've submitted is to large for this game, try again")
    print(NR_GUESSES-1)

#-warn if the guess was already made
for answers in guesses:
    if guess == guesses:
        print("The number you've submitted is already used, try another number")

#-if the guess is wrong, mark the point with an X and start again
if guess != ship_col:
    if guess != ship_row:
        board.append("X", guess)

#-print turn and board again here
print(NR_GUESSES)
print_board(board)
if turn == NR_GUESSES-1:
    print("Game Over")