import pygame
from pygame.locals import *

class Jewel(pygame.sprite.Sprite):
  def __init__(self, pos, images):
     pygame.sprite.Sprite.__init__(self)
     self.images = images
     self.x, self.y = pos
     self.rect = self.images.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.nr = 0

  def update(self, dx):
     self.x += dx
     self.rect.centerx = self.x
     self.nr += 0.5
     if self.nr > 31:
        self.nr = 0

  def draw(self, screen):
     screen.blit(self.images.jewels[int(self.nr)], (self.rect.left,self.rect.top) )