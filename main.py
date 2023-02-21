# Welcome to Zombie Knights
import pygame
import settings as gs
from board import Board


def setup():
  #1 Setup engine
  pygame.init() 

  #2 Display surface 
  screen = pygame.display.set_mode((gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT)) 

  #3 Caption
  pygame.display.set_caption("Zombie Knight")

  #4 Clock 
  clock = pygame.time.Clock() 

  #5 Return the goodies
  return screen, clock 


def main():
  # Setup the game engine 
  screen, clock = setup() 

  # Create groups 
  tile_group = pygame.sprite.Group()

  # Create game objects 
  board = Board(screen, tile_group)

  # Testing (NOT PRODUCTION)
  board.generate_level()
  
  # Runtime variable
  running = True 

  while running:
    # Event loop 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False 
    
    # Update the objects 
    board.draw()
       

    pygame.display.update() 
    clock.tick(60)

  pygame.quit() 

if __name__ == "__main__":
  main()