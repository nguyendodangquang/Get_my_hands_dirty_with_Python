def isValidChessBoard(board):
    piecesCount = {'b': 0, 'w': 0}
    pawnCount = {'b': 0, 'w': 0}
    hasKing = {'b': False, 'w': False}
    letterAxis = ('a','b','c','d','e','f','g','h')
    pieceColour = ('b','w')
    pieceType = ('pawn','knight','bishop','rook','queen','king')

    for k, v in board.items():
        if k[1] not in letterAxis:
            print('Position error, must from a-h')
            return False
        if int(k[0]) > 8:
            print('Position error, must from 1-8')
            return False

        if v[0] not in pieceColour:
            print('color error, must be w or b')
            return False
        if v[1:] not in pieceType:
            print('type error, must be pawn, knight, bishop, rook, queen or king')
            return False

        a = v[0]
        piecesCount[a] += 1
        if piecesCount[a] > 16:
            print('Total pieces error, max is 16')
            return False

        if v[1:] == 'pawn':
            pawnCount[v[0]] += 1
            if pawnCount[v[0]] > 8:
                print('Total pieces of pawn error, max is 8')
                return False

        if v[1:] == 'king':
            hasKing[v[0]] += 1
            if hasKing[v[0]] != 1:
                print('King number error, must be 1')
                return False
    return 'The board is good to go'
boardinput = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3c': 'wking'}
print(isValidChessBoard(boardinput))
