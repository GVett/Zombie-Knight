import pygame

class Tile(pygame.sprite.Sprite):
  """
  Generic tile object that will build the board 32 x 32 at a time
  """
  def __init__(self, x, y, tile_type):
    super().__init__()

    if tile_type == 1:
      # Tile for dirt
      self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (1).png"), (32, 32))
    elif tile_type == 2:
      # Tile for grass
      self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (2).png"), (32, 32))
    elif tile_type == 3:
      # Tile for left platform
      self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (3).png"), (32, 32))
    elif tile_type == 4:
      # Tile for center platform
      self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (4).png"), (32, 32))
    elif tile_type == 5:
      # Tile for right platform
      self.image = pygame.transform.scale(pygame.image.load("assets/images/tiles/Tile (5).png"), (32, 32))

    # Generate rectangle for image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)

    # Create a mask for fine collision detection
    self.mask = pygame.mask.from_surface(self.image)