import pygame
import settings as gs
from tile import Tile
from levels import LEVEL

class Board():
  """
  Hold all game elements
  """
  
  # Constructor
  def __init__(self, screen, tile_group):
    
    # Save the screen
    self.screen = screen

    # Properties
    self.score = 0
    self.health = 0
    self.round = 0
    self.round_timer = 0
    self.tile_group = tile_group

    # Assets
    self.title_font = pygame.font.Font('assets/fonts/Poultrygeist.ttf', 48)
    self.hud_font = pygame.font.Font('assets/fonts/Pixel.ttf', 24)

    # Background image
    self.background_image = pygame.transform.scale(pygame.image.load("assets/images/background.png"), (gs.WINDOW_WIDTH, gs.WINDOW_HEIGHT))
    self.background_rect = self.background_image.get_rect() 
    self.background_rect.topleft = (0, 0)

  """
  Methods
  """

  # Helper function that draws text
  def __draw_text(self, text, font, color, x, y):
    text_img = font.render(text, True, color)
    self.screen.blit(text_img, (x, y))

  # Draw the board
  def draw(self):

    # Draw background
    self.screen.blit(self.background_image, self.background_rect)

    # Draw tile group
    self.tile_group.draw(self.screen)
  
    # Draw HUD
    self.__draw_text("Score: " + str(self.score), self.hud_font, gs.WHITE, 10, gs.WINDOW_HEIGHT - 55)
    self.__draw_text("Health: " + str(self.health), self.hud_font, gs.WHITE, 10, gs.WINDOW_HEIGHT - 30)
    self.__draw_text("Round: " + str(self.round), self.hud_font, gs.WHITE, gs.WINDOW_WIDTH - 122, gs.WINDOW_HEIGHT - 55)
    self.__draw_text("Sunrise In: " + str(self.round_timer), self.hud_font, gs.WHITE, gs.WINDOW_WIDTH - 200, gs.WINDOW_HEIGHT - 30)

    # Title
    self.__draw_text("Zombie Knights", self.title_font, gs.GREEN, gs.WINDOW_WIDTH // 2 - 165, gs.WINDOW_HEIGHT - 55)

  # Generate a game map based on level
  def generate_level(self):
    level = LEVEL[0]
    
    # Loop through map row and column
    for i in range(len(level)):
      # Row
      for j in range(len(level[i])):
        elem = None
        # Columns in row i
        if level[i][j] == 1:
          elem = Tile(j * 32, i * 32, 1)
          # Dirt tile
        elif level[i][j] == 2:
          elem = Tile(j * 32, i * 32, 2)
          # Grass tile
        elif level[i][j] == 3:
          elem = Tile(j * 32, i * 32, 3)
          # Left platform tile
        elif level[i][j] == 4:
          elem = Tile(j * 32, i * 32, 4)
          # Platform tile
        elif level[i][j] == 5:
          elem = Tile(j * 32, i * 32, 5)
          # Right platform tile

        if elem is not None:
          self.tile_group.add(elem)
          
      
    
    