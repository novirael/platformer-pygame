import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from math import *

class Bullet(pygame.sprite.Sprite):
  def __init__(self, pos, vx, vy, img):
     pygame.sprite.Sprite.__init__(self)
     self.x, self.y = pos
     self.vx = vx
     self.vy = vy
     self.image = pygame.image.load(img)
     #self.image.set_colorkey( (255,255,255) )
     self.rect = self.image.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y

  def update(self, dx):
     self.x += self.vx + dx
     self.y += self.vy
     self.rect.centerx = self.x
     self.rect.centery = self.y

  def draw(self, screen):
     screen.blit(self.image, (self.rect.left,self.rect.top) )

