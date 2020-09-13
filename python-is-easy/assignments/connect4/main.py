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

# Directions
up = [-1, 0]
down = [1, 0]
left = [0, -1]
right = [0, 1]
upLeft = [-1, -1]
upRight = [-1, 1]
downLeft = [1, -1]
downRight = [1, 1]

'''
Draws the game board in its current state
'''
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

'''
Determines the player for the next round
'''
def nextPlayer(player):
    return (player + 1) % 2

'''
Finds a topmost empty row for the specified column
'''
def findEmptyRow(column):
    for row in range(6, 0, -1):
        if symbolAt([row, column]) == ' ':
            return row
    return 0

'''
Drops current player's symbol into specified column
'''
def dropTo(column):
    if column > 0 and column < 8:
        row = findEmptyRow(column)
        if row > 0:
            position = [row, column]
            putAt(position, players[player])
            return position
    return [0, 0]

'''
Runs one game round
'''
def round():
    droped = [0, 0]
    while withinBoard(droped) == False:
        displayBoard()
        answer = input('Player ' + players[player] + ': ').strip()
        if answer.isdigit():
            droped = dropTo(int(answer))
    return droped

'''
Returns true if the position lies within the board boundaries and returns false otherwise
'''
def withinBoard(position):
    row = position[0]
    column = position[1]
    return row > 0 and row < 7 and column > 0 and column < 8

'''
Moves the specified position one step into the direction
'''
def move(position, direction):
    position[0] += direction[0]
    position[1] += direction[1]

'''
Returns new position moved one step into the direction from the source position
'''
def moved(position, direction):
    return [
        position[0] + direction[0],
        position[1] + direction[1],
    ]

'''
Returns symbol resides in the board at the specified position
'''
def symbolAt(position):
    row = position[0]
    column = position[1]
    return board[row-1][column-1]

'''
Places the symblos into the board at the specfied position
'''
def putAt(position, symbol):
    row = position[0]
    column = position[1]
    board[row-1][column-1] = symbol

'''
Returns number of positions in the direction that have the same symbol
'''
def countSiblings(position, direction):
    symbol = symbolAt(position)
    position = moved(position, direction)
    count = 0
    while withinBoard(position) and symbolAt(position) == symbol:
        count += 1
        move(position, direction)
    return count

'''
Returns true if the specified position has enough siblings in all possible directions
'''
def win(position):
    vert = countSiblings(position, up) + countSiblings(position, down) + 1
    horiz = countSiblings(position, left) + countSiblings(position, right) + 1
    diag1 = countSiblings(position, upLeft) + countSiblings(position, downRight) + 1
    diag2 = countSiblings(position, downLeft) + countSiblings(position, upRight) + 1
    return horiz >= 4 or vert >= 4 or diag1 >= 4 or diag2 >= 4

# The game

while win(round()) == False:
    player = nextPlayer(player)
    roundNumber += 1

displayBoard()
print('Player ' + players[player] + ' win!')
