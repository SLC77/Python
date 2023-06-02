def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty()
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)

def intro():
    print('Welcome to the Tic Tac Toe Championship')
    print('\n')

#Create a blank board

def create_grid():
    board = [[" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "],]
    return board

#Decide player's symbol choice
def sym():
     symbol_1 = input("Player 1, choose X or O.")
     if symbol_1 == "X":
         symbol_2 == "O"
         print("Player 2, you are O.")
     else:
         symbol_2 == "X"
         print('Player 2, you are X.')

#Game programe
def startgame(board, symbol_1, symbol_2, count):

    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
