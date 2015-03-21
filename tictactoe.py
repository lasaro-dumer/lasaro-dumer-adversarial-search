#!/usr/bin/env python
# Four spaces as indentation [no tabs]

import sys
from common import *
from player_human import *
from player_random import *
from player_minimax import *
from player_alphabeta import *

# ==========================================
# TicTacToe
# ==========================================

class TicTacToe:

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, playerO, playerX, debug = True):
        self.debug = debug
        self.playerO = self.setup_player(O, playerO)
        self.playerX = self.setup_player(X, playerX)
        self.turn = O
        self.board = [0 for i in range(9)]
        self.winner = None

    # ------------------------------------------
    # Update
    # ------------------------------------------

    def update(self):
        # No movements after winner is found
        if self.winner:
          return
        # Board is an attribute, keep it safe sending a duplicate
        if self.turn == O:
            movement = self.playerO.get_next_move(list(self.board))
        else:
            movement = self.playerX.get_next_move(list(self.board))
        # Apply movement if there is one
        if movement != None:
            # Valid move
            if 0 <= movement <= 8:
              # Clear cell
              if self.board[movement] == 0:
                  self.board[movement] = self.turn
                  # Print board
                  if self.debug:
                      print "\nPlayer " + ("O" if self.turn == O else "X") + " did " + str(movement)
                      for row in [0,3,6]:
                          print [' OX'[cell] for cell in self.board[row:(row+3)]]
                  # Find winner
                  if find_winner(self.board):
                      self.winner = self.turn
                      if self.debug:
                          print "Player " + ("O" if self.turn == O else "X") + " won the game"
                  elif not find_empty_cells(self.board):
                      self.winner = DRAW
                      if self.debug:
                          print "No player won the game"
                  self.turn ^= 3 # 1 => 2, 2 => 1
              else:
                  raise Exception("Player " + str(self.turn) + " tried to make a blocked movement: " + str(movement))
            else:
                raise Exception("Player " + str(self.turn) + " tried to make an invalid movement: " + str(movement))

    # ------------------------------------------
    # Setup player
    # ------------------------------------------

    def setup_player(self, index, type):
        if type == HUMAN:
            if self.debug:
                print "Player " + ("O" if index == O else "X") + " is HUMAN"
            return Player_Human(index)
        elif type == RANDOM:
            if self.debug:
                print "Player " + ("O" if index == O else "X") + " is RaNdOM"
            return Player_Random(index)
        elif type == MINIMAX:
            if self.debug:
                print "Player " + ("O" if index == O else "X") + " is miniMAX"
            return Player_Minimax(index)
        elif type == ALPHABETA:
            if self.debug:
                print "Player " + ("O" if index == O else "X") + " is AlphaBeta"
            return Player_Alphabeta(index)
        else:
            raise Exception("Player type is invalid: " + str(type))

# ==========================================
# Main
# ==========================================
if __name__ == "__main__":
    if len(sys.argv) == 3:
        playerO = int(sys.argv[1])
        playerX = int(sys.argv[2])
    else:
        print "Loading default random players"
        playerO = RANDOM
        playerX = RANDOM
    game = TicTacToe(playerO, playerX)
    while game.winner == None:
        game.update()