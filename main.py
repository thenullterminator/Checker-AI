import pygame
from checkers.constants import WIDTH,HEIGHT,SQUARE_SIZE,WHITE,BLACK
from checkers.menu import Menu
from checkers.board import Board
from checkers.game import Game
from minimax.algo import minimax

pygame.init()

# frame refresh rate.
FPS=60 

# creating a window for our game
WIND = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("CHECKERS")

def get_square_pos_from_mouse(pos):

      x,y = pos
      row = y//SQUARE_SIZE
      col = x//SQUARE_SIZE
      return row,col

def main():

      run = True
      clock = pygame.time.Clock()
      game = Game(WIND)
      menu = Menu(WIND)
      Mode = None

      while run:

            # setting refresh rate..
            clock.tick(FPS) 

            if Mode and game.winner() != None:
                  print(game.winner()+" WON!!")
                  font = pygame.font.Font('freesansbold.ttf', 32) 
                  text = font.render(game.winner()+" WON!!", True, BLACK, WHITE)
                  textRect = text.get_rect() 
                  textRect.center = (WIDTH // 2, WIDTH // 2)
                  WIND.fill(WHITE)
                  WIND.blit(text, textRect)
                  pygame.display.update()
                  pygame.time.delay(5000)
                  run=False
            
            if (Mode == 2 or Mode ==3) and game.turn == WHITE:
                  value,new_board = minimax(game.get_board(),5, True,game,float('-inf'),float('+inf'))
                  pygame.time.delay(1000)
                  game.ai_move(new_board)
            
            if Mode ==3 and game.turn == BLACK:
                  value,new_board = minimax(game.get_board(),5, False,game,float('-inf'),float('+inf'))
                  pygame.time.delay(1000)
                  game.ai_move(new_board)


            #setting event loop
            for event in pygame.event.get():

                  if event.type == pygame.QUIT:
                        run = False
                  
                  if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if Mode == None:
                              Mode = menu.selected_mode(pos)
                              print("Selected Mode: "+str(Mode))

                        if Mode == 1 or Mode == 2:

                              row,col = get_square_pos_from_mouse(pos)
                              game.select(row,col)
            
            if Mode:
                  game.update()
      
      # close the window.
      pygame.quit()

main()