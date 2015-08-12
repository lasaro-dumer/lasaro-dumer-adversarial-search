#!/usr/bin/env python
# Four spaces as indentation [no tabs]

class PlayerMeta(type):

    def __repr__(cls):
        return cls.__name__.replace("Player", "").lower()

# ==========================================
# Player Interface
# ==========================================

class Player(object):

    __metaclass__ = PlayerMeta

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        self.symbol = symbol

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        raise NotImplementedError()

    # ------------------------------------------
    # Get Symbol
    # ------------------------------------------

    def me(self):
        return self.symbol

    # ------------------------------------------
    # Get Opponent
    # ------------------------------------------

    def opp(self):
        return "O" if self.symbol == "X" else "X"

    # ------------------------------------------
    # Find empty cells
    # ------------------------------------------

    def find_empty_cells(self, board):
        return [index for index in range(9) if board[index] == None]

    # ------------------------------------------
    # String representation
    # ------------------------------------------

    def __repr__(self):
        return "Player {} ({})".format(self.symbol, type(self).__name__)