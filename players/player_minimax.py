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
        maxAction = None
        maxValue = float('inf') * (-1)

        succs = self.successors((board,0),self.me())
        for succ in succs:
            minVal = self.minValue(succ)
            if minVal > maxValue:
                maxValue = minVal
                maxAction = succ[2]
        return maxAction

    def successors(self,state,sym):
        available = find_empty_cells(state[0])
        moves = state[1]+1
        succs = []
        for action in available:
            nBoard = list(state[0])
            nBoard[action] = sym
            succs.append((nBoard,moves,action,len(available)-1))
        return succs

    def minValue(self,state):
        if self.isTerminal(state):
            return self.utility(state)
        v = float('inf')
        succs = self.successors(state,self.opp())
        for succ in succs:
            v = min(v,self.maxValue(succ))
        return v

    def maxValue(self,state):
        if self.isTerminal(state):
            return self.utility(state)
        v = float('inf') * (-1)
        succs = self.successors(state,self.me())
        for succ in succs:
            v = max(v,self.minValue(succ))
        return v

    def isTerminal(self,state):
        return (state[3] <= 0) or (find_winner(state[0])[0] != None)

    def utility(self,state):
        winner = find_winner(state[0])[0]
        if winner == None:
            return 0
        if winner == self.me():
            return 10 - (state[1])
        if winner == self.opp():
            return (state[1]) - 10
