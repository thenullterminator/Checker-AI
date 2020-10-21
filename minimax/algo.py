from copy import deepcopy
import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

def minimax(board, depth, max_player, game, alpha, beta):

      if depth == 0 or game.winner() != None:

            return board.heurestic_score(),board
      
      if max_player:
            
            maxEval = float('-inf')
            best_move = None
            
            for move in get_all_moves(board,WHITE,game):
                  evalution = minimax(move,depth-1,False,game,alpha,beta)[0]
                  maxEval = max(maxEval,evalution)

                  if maxEval == evalution:
                        best_move = move

                  alpha = max(alpha,maxEval)
                  if beta <= alpha :
                        maxEval = float('+inf')
                        break
                        
                  
            return maxEval, best_move
      else:
            minEval = float('+inf')
            best_move = None
            
            for move in get_all_moves(board,BLACK,game):
                  evalution = minimax(move,depth-1,True,game,alpha,beta)[0]
                  minEval = min(minEval,evalution)

                  if minEval == evalution:
                        best_move = move

                  beta = min(beta,minEval)
                  if beta <= alpha:
                        minEval = float('-inf')
                        break
                  
            
            return minEval, best_move

def simulate_move(piece, move, board, game, skip):

      board.move(piece,move[0],move[1])
      if skip:
            board.remove(skip)
      
      return board

def get_all_moves(board, color, game):

      moves=[]

      for piece in board.get_all_pieces(color):

            valid_moves = board.get_valid_moves(piece)
            for move,skip in valid_moves.items():

                  temp_board = deepcopy(board)
                  temp_piece =  temp_board.get_piece(piece.row,piece.col)
                  new_board = simulate_move(temp_piece, move, temp_board, game, skip)
                  moves.append(new_board)
      
      return moves