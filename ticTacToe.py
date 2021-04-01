theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M':
' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] + '|')
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space')
    move = input()
    theBoard[move] = turn
    if ((theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'X') or (theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == 'X') or (theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == 'X') or  (theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == 'X') or (theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == 'X') or (theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == 'X') or (theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == 'X')):
        print('X Win')
        break

    elif ((theBoard['top-L'] == theBoard['top-M'] == theBoard['top-R'] == 'O') or (theBoard['low-L'] == theBoard['low-M'] == theBoard['low-R'] == 'O') or (theBoard['top-L'] == theBoard['mid-L'] == theBoard['low-L'] == 'O') or  (theBoard['top-M'] == theBoard['mid-M'] == theBoard['low-M'] == 'O') or (theBoard['top-R'] == theBoard['mid-R'] == theBoard['low-R'] == 'O') or (theBoard['top-L'] == theBoard['mid-M'] == theBoard['low-R'] == 'O') or (theBoard['top-R'] == theBoard['mid-M'] == theBoard['low-L'] == 'O')):
        print('O Win')
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
