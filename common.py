#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import os, inspect

PATH          = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
WAIT          = 1
# Board
ZOOM          = 6
TILE_WIDTH    = 16 * ZOOM
TILE_HEIGHT   = 16 * ZOOM
# Modes
HUMAN         = 0
RANDOM        = 1
MINIMAX       = 2
ALPHABETA     = 3
# Index symbol
O = 1
X = 2
DRAW = 0

# ------------------------------------------
# Find winner
# ------------------------------------------

def find_winner(board):
    for i in range(3):
        # Row
        if board[i][0] != 0 and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
        # Column
        elif board[0][i] != 0 and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
    # Diagonal
    if board[0][0] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    return None

# ------------------------------------------
# Find empty cells
# ------------------------------------------

def find_empty_cells(board):
    cells = []
    for i in range(3):
        for j in range(3):
            if board[j][i] == 0:
                cells.append((i,j))
    return cells