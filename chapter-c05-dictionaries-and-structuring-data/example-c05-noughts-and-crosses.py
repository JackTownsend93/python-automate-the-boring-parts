# Simple programme to play noughts and crosses (tic tac NO.)
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('---+---+---')
    print(' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('---+---+---')
    print(' ' + board['bot-L'] + ' | ' + board['bot-M'] + ' | ' + board['bot-R'])
    return 0

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(turn + ' to play. Which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)