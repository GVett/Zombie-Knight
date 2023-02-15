import pygame
import settings as gs

class Board():
  """
  Hold all game elements
  """
  
  # Constructor
  def __init__(self, screen):
    
    # Save the screen
    self.screen = screen

    # Properties
    self.score = 0
    self.health = 0
    self.round = 0
    self.round_timer = 0

    # Assets