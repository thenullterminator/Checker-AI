import pygame
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE,WHITE,BLACK

class Menu:

      def __init__(self,WIND):

            self.WIND = WIND
            self.draw_menu()
      
      def draw_menu(self):

            font = pygame.font.Font('freesansbold.ttf', 32)

            pygame.draw.rect(self.WIND,WHITE,(200,200,400,70))
            text = font.render(" Human vs Human ", True, BLACK, WHITE)
            textRect = text.get_rect() 
            textRect.center = (400, 240)
            self.WIND.blit(text, textRect)

            pygame.draw.rect(self.WIND,WHITE,(200,300,400,70))
            text = font.render(" Human vs AI ", True, BLACK, WHITE)
            textRect = text.get_rect() 
            textRect.center = (390, 340)
            self.WIND.blit(text, textRect)

            pygame.draw.rect(self.WIND,WHITE,(200,400,400,70))
            text = font.render(" AI vs AI ", True, BLACK, WHITE)
            textRect = text.get_rect() 
            textRect.center = (400, 440)
            self.WIND.blit(text, textRect)
            
            pygame.display.update()
      
      def selected_mode(self,pos):

            x,y = pos

            if x >= 200 and x <= 600 and y >= 200 and y<= 270:
                  return 1
            
            if x >= 200 and x <= 600 and y >= 300 and y<= 370:
                  return 2
            
            if x >= 200 and x <= 600 and y >= 400 and y<= 470:
                  return 3
            
            return None