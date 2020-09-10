'''
Homework assignment for the 'Python is easy' course by Pirple.

Written by Ed Yablonsky.
'''

import os

'''
Draws a playing board with specified number of rows and columns.
For example, the drawPalyingBoard(3, 3) prints the following board.
 | | 
-----
 | |
-----
 | |

Returns False when the board won't fit into the entire screen,
otherwise it draws the board and returns True.
'''
def drawPlayingBoard(rows, columns):
    lines_number = rows * 2 - 1
    symbols_number = columns *  2 - 1
    terminal_size = os.get_terminal_size()
    if lines_number > terminal_size.lines or symbols_number >= terminal_size.columns:
        return False
    for line in range(lines_number):
        if line % 2 == 0:
            for symbol in range(symbols_number):
                if symbol % 2 == 0:
                    print(' ', end='')
                else:
                    print('|', end='')
            print()
        else:
            print('-' * symbols_number)
    return True
