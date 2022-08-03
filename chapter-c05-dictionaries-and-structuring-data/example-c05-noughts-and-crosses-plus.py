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

if __name__ == "__main__":
    turnCount = 0
    win = False
    turn = 'X'
    while win == False:
        for i in range(9):
            printBoard(theBoard)
            print(turn + ' to play. Which space?')
            
            # Check input is valid.
            while True:
                move = str(input())
                if move in theBoard.keys() and theBoard[move] == ' ':
                    break
                elif move not in theBoard.keys():
                    print('Invalid board position. Valid board positions are...')
                    for key in theBoard:
                        print('\t' + key)
                elif theBoard[move] != ' ':
                    print('Oi! That space is occupied!')
                else:
                    print('Er... you can\'t do that...')

            # Apply turn.           
            theBoard[move] = turn

            # Check if a win condition has occured:
            #  - Horizontal.
            if theBoard.get('top-L') == theBoard.get('top-M') == theBoard.get('top-R') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            elif theBoard.get('mid-L') == theBoard.get('mid-M') == theBoard.get('mid-R') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            elif theBoard.get('bot-L') == theBoard.get('bot-M') == theBoard.get('bot-R') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            #  - Vertical.
            elif theBoard.get('top-L') == theBoard.get('mid-L') == theBoard.get('bot-L') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            elif theBoard.get('top-M') == theBoard.get('mid-M') == theBoard.get('bot-M') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            elif theBoard.get('top-M') == theBoard.get('mid-M') == theBoard.get('bot-M') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            #  - Diagonal.
            elif theBoard.get('top-L') == theBoard.get('mid-M') == theBoard.get('bot-R') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            elif theBoard.get('bot-L') == theBoard.get('mid-M') == theBoard.get('top-R') != ' ':
                print('<<< ' + turn + ' WINS! >>>')
                win = True
                break
            else:
                break

        # Increment turn counter and check for stalemate.
        turnCount += 1
        if turnCount == 9:
            print('<<< STALEMATE! >>>')
            break

        # Turn over to next player.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)