theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '} # Represents the tic-tac-toe board (3x3).

def printBoard(board): # Prints the board dictionary onto the screen.
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkWinner(board, player): # Check all winning combinations (rows, columns, diagonals)
    return ((board['top-L'] == board['top-M'] == board['top-R'] == player) or
            (board['mid-L'] == board['mid-M'] == board['mid-R'] == player) or 
            (board['low-L'] == board['low-M'] == board['low-R'] == player) or 
            (board['top-L'] == board['mid-L'] == board['low-L'] == player) or
            (board['top-M'] == board['mid-M'] == board['low-M'] == player) or
            (board['top-R'] == board['mid-R'] == board['low-R'] == player) or
            (board['top-L'] == board['mid-M'] == board['low-R'] == player) or
            (board['top-R'] == board['mid-M'] == board['low-L'] == player))

turn = 'X'
for i in range(9): # Allows players to enter their moves.
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    
    if theBoard[move] == ' ':  # Check if the move is on an empty space
        theBoard[move] = turn
    else:
        print("That space is already taken. Try again.")
        continue
    
    if checkWinner(theBoard, turn): # Check if the current player has won
        printBoard(theBoard)
        print('Player ' + turn + ' wins!')
        break
    
    # Switch turns
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
else:
    printBoard(theBoard)
    print("It's a tie!")