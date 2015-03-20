#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from common import *

# ==========================================
# Player Human
# ==========================================

class Player_Human:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, index):
        self.index = index

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        empty_cells = find_empty_cells(board)
        print "Available cells:"
        for index, cell in enumerate(empty_cells):
            print "    " + str(index) + ": (" + str(cell[0]) + ', ' + str(cell[1]) + ")"
        movement = -1
        while movement < 0 or movement >= len(empty_cells):
            movement = int(raw_input('Cell index: '))
        return empty_cells[movement]