board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

players = ['X', 'O']
player = 0
roundNumber = 1

def displayBoard():
    print('Round', roundNumber)
    print('=' * 15)
    print('|1|2|3|4|5|6|7|')
    print('-' * 15)
    for row in board:
        print('|', end='')
        for cell in row:
            print(cell + '|', end='')
        print()
    print('=' * 15)

def nextPlayer(player):
    return (player + 1) % 2

def findEmptyRow(slot):
    for row in range(6, 0, -1):
        if board[row-1][slot-1] == ' ':
            return row
    return 0

def dropTo(column):
    if column > 0 and column < 8:
        row = findEmptyRow(column)
        if row > 0:
            board[row-1][column-1] = players[player]
            return [row, column]
    return [0, 0]

def round():
    droped = [0, 0]
    while droped[0] == 0:
        displayBoard()
        answer = input('Player ' + players[player] + ': ').strip()
        if answer.isdigit():
            droped = dropTo(int(answer))
    return droped

def countDown(position):
    row = position[0]
    column = position[1]
    symbol = board[row-1][column-1]
    count = 0
    for row in range(row, 7):
        if board[row-1][column-1] != symbol:
            break
        count += 1
    return count

def countLeft(position):
    row = position[0]
    column = position[1]
    symbol = board[row-1][column-1]
    count = 0
    for column in range(column, 0, -1):
        if board[row-1][column-1] != symbol:
            break
        count += 1
    return count

def countRight(position):
    row = position[0]
    column = position[1]
    symbol = board[row-1][column-1]
    count = 0
    for column in range(column, 8):
        if board[row-1][column-1] != symbol:
            break
        count += 1
    return count

def countLeftDiagonal(position):
    row = position[0]
    column = position[1]
    symbol = board[row-1][column-1]
    count = 0
    while row < 7 and column > 0:
        if board[row-1][column-1] != symbol:
            break
        count += 1
        row += 1
        column -= 1
    return count

def countRightDiagonal(position):
    row = position[0]
    column = position[1]
    symbol = board[row-1][column-1]
    count = 0
    while row < 7 and column < 8:
        if board[row-1][column-1] != symbol:
            break
        count += 1
        row += 1
        column += 1
    return count

def win(position):
    down = countDown(position)
    left = countLeft(position)
    right = countRight(position)
    ldiag = countLeftDiagonal(position)
    rdiag = countRightDiagonal(position)
    return down >= 4 or left >= 4 or right >= 4 or ldiag >= 4 or rdiag >= 4

while win(round()) == False:
    player = nextPlayer(player)
    roundNumber += 1

displayBoard()
print('Player ' + players[player] + ' win!')
