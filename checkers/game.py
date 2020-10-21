import pygame
from .board import Board
from .constants import WHITE,BLACK,GREEN,SQUARE_SIZE,ROWS,COLS

class Game:

      def __init__(self,WIND):

            self._init()
            self.WIND = WIND

      def _init(self):

            self.selected_piece = None
            self.board = Board()
            self.turn = BLACK
            self.valid_moves = {}
      
      def reset(self):

            self._init()
      
      def winner(self):

            if self.board.black_left <=0 :

                  return "WHITE"
            elif self.board.white_left <=0 :

                  return "BLACK"
            
            if self.turn == BLACK:
                  
                  for r in range(ROWS):
                        for c in range(COLS):

                              p = self.board.get_piece(r,c)

                              if p!=0 and p.color == BLACK:

                                    valid_moves = self.board.get_valid_moves(p)
                                    if bool (valid_moves):
                                          return None
                  
                  return "WHITE" 
            elif self.turn == WHITE:

                  for r in range(ROWS):
                        for c in range(COLS):

                              p = self.board.get_piece(r,c)

                              if p!=0 and p.color == WHITE:

                                    valid_moves = self.board.get_valid_moves(p)
                                    if bool (valid_moves):
                                          return None
                  
                  return "BLACK" 
            
            return None

      def update(self):
            
            self.board.draw_all(self.WIND)
            self.draw_valid_moves(self.valid_moves)
            pygame.display.update()
      
      def select(self,row,col):

            if self.selected_piece:
                  result = self._move(row,col)
                  if not result:
                        self.selected_piece = None
                        return self.select(row,col)
                        
            else:
                  piece = self.board.get_piece(row,col)
                  if piece != 0  and piece.color == self.turn:
                        self.selected_piece = piece
                        self.valid_moves = self.board.get_valid_moves(piece)
                        return True
                  
            return False 
      
      def _move(self,row,col):

            piece = self.board.get_piece(row,col)

            if self.selected_piece and piece == 0 and (row,col) in self.valid_moves:

                  self.board.move(self.selected_piece,row,col)
                  skipped = self.valid_moves[(row,col)]
                  if skipped:
                        self.board.remove(skipped)
                  self.change_turn()
            else:
                  return False
            
            return True
      
      def draw_valid_moves(self,moves):

            for move in moves:
                  row,col = move
                  pygame.draw.circle(self.WIND,WHITE,(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE //2),12)
                  pygame.draw.circle(self.WIND,GREEN,(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE //2),10)
      
      def change_turn(self):

            self.valid_moves={}
            if self.turn == BLACK:
                  self.turn = WHITE
            else:
                  self.turn = BLACK
            
      def get_board(self):
            
            return self.board
      
      def ai_move(self,board):

            self.board = board
            self.change_turn()

