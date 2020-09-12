board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' '],
]

players = ['X', 'O']
lastDroped = []
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
    if player == 0:
        return 1
    else:
        return 0

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
    global player
    global roundNumber
    lastDroped = [0, 0]
    while lastDroped[0] == 0:
        displayBoard()
        answer = input('Player ' + players[player] + ': ').strip()
        if answer.isdigit():
            lastDroped = dropTo(int(answer))
    player = nextPlayer(player)
    roundNumber += 1

while True:
    round()
