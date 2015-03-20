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
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.winner = None

    # ------------------------------------------
    # Update
    # ------------------------------------------

    def update(self):
        # No movements after winner is found
        if self.winner != None:
          return
        # Board is an attribute, keep it safe
        copy_of_board = y = [row[:] for row in self.board]
        if self.turn == O:
            movement = self.playerO.get_next_move(copy_of_board)
        else:
            movement = self.playerX.get_next_move(copy_of_board)
        # Apply movement if there is one
        if movement != None:
            x, y = movement
            # Valid move
            if 0 <= x <= 2 and 0 <= y <= 2:
              # Clear cell
              if self.board[y][x] == 0:
                  self.board[y][x] = self.turn
                  # Print board
                  if self.debug:
                      print "Player " + ("O" if self.turn == O else "X") + " did " + str(movement)
                      for row in self.board:
                          print [[' ', 'O', 'X'][cell] for cell in row]
                  # Find winner
                  if find_winner(self.board) != None:
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