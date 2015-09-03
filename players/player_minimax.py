#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *

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

        # TODO Here you will implement the Minimax algorithm.
        # This method may return the best movement based on Minimax score
        # for the current board.

        # If you want, you can use here some helper functions:
        #
        # - find_winner(board): This method checks if someone wins in the
        #   parametrized board and return a tuple (Winner, Winner movement).
        #
        # - find_empty_cells(board): This method checks if there are available
        #   moves in the parametrized board. It returns an array containing
        #   the available moves.
        #
        # - print_board(board): This method helps you debugging your code.
        #   It prints a board filled with the executed moves.
        #   WARNING: printing can slow your code. Use it just for debug.
        #
        maxAction = None
        maxValue = float('inf') * (-1)
        available = find_empty_cells(board);
        print available
        for action in available:
            res = self.result((board,0,1),action)
            minVal = self.minValue(res)
            if minVal > maxValue:
                maxValue = minVal
                maxAction = action
        print 'moving to ',maxAction
        return maxAction

    def result(self,state,action):
        nBoard = list(state[0])
        nBoard[action] = self.symbol
        return (nBoard,find_empty_cells(nBoard),state[2]+1)

    def minValue(self,state):
        if self.isTerminal(state):
            return self.utility(state)
        v = float('inf')
        for action in state[1]:
            v = min(v,self.maxValue(self.result(state,action)))
        return v

    def maxValue(self,state):
        if self.isTerminal(state):
            return self.utility(state)
        v = float('inf') * (-1)
        for action in state[1]:
            v = max(v,self.minValue(self.result(state,action)))
        return v

    def isTerminal(self,state):
        return (len(state[1]) == 0) or (find_winner(state[0])[0] != None)

    def utility(self,state):
        winner = find_winner(state[0])[0]
        free = state[1]
        if winner == None:
            return 5 * free * state[2]
        if winner == self.symbol:
            return 10 * free * state[2]

        return -10 * free * state[2]
