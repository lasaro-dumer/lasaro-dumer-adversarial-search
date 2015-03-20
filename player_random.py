#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import random
from common import *

# ==========================================
# Player Random
# ==========================================

class Player_Random:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, index):
        self.index = index

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        cells = find_empty_cells(board)
        if len(cells) == 0:
            return None
        return random.choice(cells)