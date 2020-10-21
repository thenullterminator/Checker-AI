import pygame
from .constants import BROWN,ROWS,GRAY,SQUARE_SIZE,COLS,WHITE,BLACK
from .piece import Piece


class Board:

      def __init__(self):

            self.board = [] # 2D list representing the board.
            self.black_left = self.white_left = 12 # 12 pieces each .
            self.black_kings = self.white_kings =0 # initally kings are zero 
            self.create_board()

      def create_board(self):

            for r in range(ROWS):
                  self.board.append([])
                  for c in range(COLS):

                        if c%2 == ((r+1)%2):
                              if r < 3:
                                    self.board[r].append(Piece(r,c,WHITE))
                              elif r > 4:
                                    self.board[r].append(Piece(r,c,BLACK))
                              else:
                                    self.board[r].append(0)
                        else:
                              self.board[r].append(0)
                              
      def draw_board(self,WIND):

            WIND.fill(BROWN)

            for r in range(ROWS):
                  for c in range(r%2,ROWS,2):
                        pygame.draw.rect(WIND,GRAY,(r*SQUARE_SIZE,c*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
      
      def draw_all(self,WIND):

            self.draw_board(WIND)

            for r in range(ROWS):
                  for c in range(COLS):

                        piece = self.board[r][c]
                        if piece != 0:
                              piece.draw_piece(WIND)

      def get_piece(self,row,col):
            
            return self.board[row][col]
      
      def move(self,piece,row,col):

            temp = self.board[piece.row][piece.col]
            self.board[piece.row][piece.col] = self.board[row][col]
            self.board[row][col] = temp

            piece.move(row,col)

            if row == ROWS-1 or row == 0:
                  piece.make_king()

                  if piece.color == WHITE:
                        self.white_kings+=1
                  else:
                        self.black_kings+=1
      
      def remove(self,pieces):

            for piece in pieces:
                  self.board[piece.row][piece.col] = 0
                  if piece != 0:
                        if piece.color == BLACK:
                              self.black_left-=1
                              if piece.king:
                                    self.black_kings-=1
                        else:
                              self.white_left-=1
                              if piece.king:
                                    self.white_kings-=1

      def get_valid_moves(self,piece):

            moves = {}
            left = piece.col-1
            right = piece.col+1
            row = piece.row

            if piece.color == BLACK or piece.king:
                  moves.update(self._traverse_left(row-1,max(row-3,-1),-1,piece.color,left,piece.king))
                  moves.update(self._traverse_right(row-1,max(row-3,-1),-1,piece.color,right,piece.king))

            if piece.color == WHITE or piece.king:
                  moves.update(self._traverse_left(row+1,min(row+3,ROWS),1,piece.color,left,piece.king))
                  moves.update(self._traverse_right(row+1,min(row+3,ROWS),1,piece.color,right,piece.king))

            return moves
      
      def _traverse_left(self,start,stop,step,color,left,king,skipped=[]):
            
            moves = {}
            last = []

            for r in range(start,stop,step):

                  if left < 0:
                        break
                  
                  current = self.board[r][left]

                  if current == 0:
                        
                        if skipped and not last:
                              break
                        elif skipped:
                              moves[(r,left)] = last + skipped
                        else:
                              moves[(r,left)] = last
                        
                        if last :
                              skipped=skipped+last

                              if step == -1 or king:
                                    row = max(r-3,-1)
                                    moves.update(self._traverse_left(r-1,row,-1,color,left-1,king,skipped))
                                    moves.update(self._traverse_right(r-1,row,-1,color,left+1,king,skipped))
                              elif step == 1 or king:
                                    row = min(r+3,ROWS)
                                    moves.update(self._traverse_left(r+1,row,1,color,left-1,king,skipped))
                                    moves.update(self._traverse_right(r+1,row,1,color,left+1,king,skipped))

                        break

                  elif current.color == color:
                        break
                  else:
                        last = [current]

                  left-=1
            
            return moves

      def _traverse_right(self,start,stop,step,color,right,king,skipped=[]):
            
            moves = {}
            last = []

            for r in range(start,stop,step):

                  if right >= COLS:
                        break
                  
                  current = current = self.board[r][right]

                  if current == 0:
                        
                        if skipped and not last:
                              break
                        elif skipped:
                              moves[(r,right)] = last + skipped
                        else:
                              moves[(r,right)] = last
                        
                        if last :
                              skipped=skipped+last

                              if step == -1 or king:
                                    row = max(r-3,-1)
                                    moves.update(self._traverse_left(r-1,row,-1,color,right-1,king,skipped))
                                    moves.update(self._traverse_right(r-1,row,-1,color,right+1,king,skipped))
                              elif step == 1 or king:
                                    row = min(r+3,ROWS)
                                    moves.update(self._traverse_left(r+1,row,1,color,right-1,king,skipped))
                                    moves.update(self._traverse_right(r+1,row,1,color,right+1,king,skipped))

                        break

                  elif current.color == color:
                        break
                  else:
                        last = [current]


                  right +=1

            
            return moves
      
      def heurestic_score(self): # white is our AI player.

            return int(self.white_left-self.black_left + 0.5*(self.white_kings-self.black_kings))
      
      def get_all_pieces(self,color):

            pieces=[]
            for row in self.board:
                  for piece in row:
                        if piece != 0  and piece.color == color:
                              pieces.append(piece)
            
            return pieces



      


