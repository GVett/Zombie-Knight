# Welcome to Zombie Knights
import pygame
import settings as gs


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
  

  # Create game objects 
 

  # Background image 
  background_image = pygame.transform.scale(pygame.image.load("assets/images/background.png"), (gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT))
  background_rect = background_image.get_rect() 
  background_rect.topleft = (0, 0)
    
  # Runtime variable
  running = True 

  while running:
    # Event loop 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False 

    # Draw background 
    screen.blit(background_image, background_rect)
    
    # Update the objects 
       

    pygame.display.update() 
    clock.tick(60)

  pygame.quit() 

if __name__ == "__main__":
  main()