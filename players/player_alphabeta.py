#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player

# ==========================================
# Player Alphabeta
# ==========================================

class AlphabetaPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, index):
        super(AlphabetaPlayer, self).__init__(index)

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        # TODO Bonus
        return None