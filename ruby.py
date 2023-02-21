import pygame
import settings as gs

class RubyFixed(pygame.sprite.Sprite):
  """Ruby that stays in place"""

  # Constructor
  def __init__(self, x, y):
    super().__init__()

    # Animation
    self.ruby_sprites = []

    # Fill the list with images (TODO: make into a loop)
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile000.png"), (64, 64)))
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile001.png"), (64, 64)))
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile002.png"), (64, 64)))
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile003.png"), (64, 64)))
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile004.png"), (64, 64)))
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile005.png"), (64, 64)))
    self.ruby_sprites.append(pygame.transform.scale(pygame.image.load("assets/images/ruby/tile006.png"), (64, 64)))

    # Load image and get rect
    self.current_sprite = 0
    self.image = self.ruby_sprites[self.current_sprite]
    self.rect = self.image.get_rect()
    self.rect.bottomleft = (x, y)

  # Override Sprite update method
  def update(self):
    self.animate(self.ruby_sprites, gs.ANIMATION_SPEED)

  # Animate the sprite
  def animate(self, sprite_list, speed):
    if self.current_spite < len(sprite_list) - 1:
      self.current_sprite += speed
    else:
      self.current_sprite = 0

    self.image = sprite_list[int(self.current_sprite)]