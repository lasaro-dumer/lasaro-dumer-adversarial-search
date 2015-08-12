#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import os, inspect

PATH          = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# Interface
WAIT          = 1
ZOOM          = 6
TILE_WIDTH    = 16 * ZOOM
TILE_HEIGHT   = 16 * ZOOM

# Index symbol
O    = "O"
X    = "X"
DRAW = False

# ------------------------------------------
# Movements Exceptions
# ------------------------------------------

class BlockedMovementException(Exception):
    def __init__(self, board, player, movement):
        self.board = list(board)
        self.player = player
        self.movement = movement
    def __str__(self):
        return "{} tries blocked movement {}.".format(self.player, self.movement)

class InvalidMovementException(Exception):
    def __init__(self, board, player, movement):
        self.board = list(board)
        self.player = player
        self.movement = movement
    def __str__(self):
        return "{} tries invalid movement {}.".format(self.player, self.movement)

class NoMovementException(Exception):
    def __init__(self, board, player):
        self.board = list(board)
        self.player = player
    def __str__(self):
        return "{} do not move.".format(self.player)