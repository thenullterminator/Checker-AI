import pygame
from .constants import GRAY,BLACK,SQUARE_SIZE,DARKGRAY,CROWN

class Piece:

      PADDING = 16 
      BORDER = 0

      def __init__(self,row,col,color):

            self.row = row
            self.col = col
            self.color = color
            self.king = False
            self.x = 0
            self.y = 0
            self.cal_position()
      
      def cal_position(self):
            
            self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
            self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2    

      def make_king(self):

            self.king = True
      
      def draw_piece(self,WIND):

            radius = SQUARE_SIZE//2 - self.PADDING
            pygame.draw.circle(WIND,DARKGRAY,(self.x,self.y),radius + self.BORDER)
            pygame.draw.circle(WIND,self.color,(self.x,self.y),radius)
            if self.king:
                  WIND.blit(CROWN,(self.x-CROWN.get_width()//2,self.y-CROWN.get_height()//2))

      def move(self,row,col):

            self.row = row
            self.col = col
            self.cal_position()



