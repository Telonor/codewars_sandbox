"""
Solution for "Tic-Tac-Toe Checker" kata:
https://www.codewars.com/kata/525caa5c1bf619d28c000335
"""
import re

WIN_COORDS = (
    # diagonals
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
    # cols
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    # rows
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2))
)

X = 1
O = 2
EMPTY = 0


NOT_SOLVED = -1
X_WIN = 1
O_WIN = 2
CATS_GAME = 0

BOARD_SIZE = (3, 3)


def prepare_data(data):
    data = str(data)

    result = re.findall(
        '[\d]',
        data
    )

    if not result:
        raise ValueError

    l = map(int, result[:BOARD_SIZE[0]*BOARD_SIZE[1]])

    return [l[i:i + BOARD_SIZE[0]] for i in xrange(0, len(l), BOARD_SIZE[0])]


def isSolved(board):
    board = prepare_data(board)
    empty = False

    for coords in WIN_COORDS:
        xstreak = []
        ostreak = []

        prev_val = None

        for idx, coord in enumerate(coords):
            val = board[coord[0]][coord[1]]

            if not empty:
                empty = val == EMPTY

            if not idx:  # first iteration
                prev_val = val
                xstreak.append(val == X)
                ostreak.append(val == O)
            else:
                xstreak.append(val == prev_val)
                ostreak.append(val == prev_val)
                prev_val = val

        if all(xstreak):
            return X_WIN
        elif all(ostreak):
            return O_WIN
    if empty:
        return NOT_SOLVED
    else:
        return CATS_GAME
