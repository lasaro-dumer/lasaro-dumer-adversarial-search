#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player

# ==========================================
# Player Minimax
# ==========================================

class MinimaxPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(MinimaxPlayer, self).__init__(symbol)

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        # TODO
        return None