#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *

# ==========================================
# Player Alphabeta
# ==========================================

class AlphabetaPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(AlphabetaPlayer, self).__init__(symbol)
        self.alpha = float('inf') * (-1)
        self.beta = float('inf')

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        maxAction = None
        maxValue = float('inf') * (-1)
        available = find_empty_cells(board);

        for action in available:
            res = self.result((board,0,1),action,self.me())
            minVal = self.minValue(res)
            if minVal > maxValue:
                maxValue = minVal
                maxAction = action

        return maxAction

    def result(self,state,action,sym):
        nBoard = list(state[0])
        nBoard[action] = sym
        nextActions = find_empty_cells(nBoard)
        return (nBoard,nextActions,state[2]+1)

    def minValue(self,state):
        if self.isTerminal(state):
            return self.utility(state)
        v = float('inf')
        for action in state[1]:
            v = min(v,self.maxValue(self.result(state,action,self.opp())))
            if v <= self.alpha:
                return v
            self.beta = min(v,self.beta)
        return v

    def maxValue(self,state):
        if self.isTerminal(state):
            return self.utility(state)
        v = float('inf') * (-1)
        for action in state[1]:
            v = max(v,self.minValue(self.result(state,action,self.me())))
            if v >= self.beta:
                return v
            self.alpha = max(self.alpha,v)
        return v

    def isTerminal(self,state):
        return (len(state[1]) == 0) or (find_winner(state[0])[0] != None)

    def utility(self,state):
        winner = find_winner(state[0])[0]
        free = len(state[1])
        if winner == None:
            return 0
        if winner == self.me():
            return 10 * free * state[2]
        if winner == self.opp():
            return -10 * free * state[2]
