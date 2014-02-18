#!/usr/bin/env python

import pygame
from random import randint,choice
import math

pygame.init()
screen = pygame.display.set_mode((900, 600))

rzeczy = ['images/platforma01.png', 'images/platforma02.png', 'images/platforma03.png',
'images/platforma04.png', 'images/totem1.png', 'images/totem2.png', 'images/drzewo1.png',
'images/drzewo2.png', 'images/cloud1.png', 'images/grass.png', 'images/box.png']

things = []
for n in rzeczy:
   things.append(pygame.image.load(n).convert_alpha())

class Platform(pygame.sprite.Sprite):
  def __init__(self, n, (x, y)):
     pygame.sprite.Sprite.__init__(self)
     w = things[n].get_width()
     h = things[n].get_height()
     self.rect =  pygame.Rect(x, y, w, h) #rand_rect()
     #self.color = (250,220,20)
     self.rect.width = w
     self.rect.height = h
     self.image = pygame.Surface((self.rect.width, self.rect.height))
     self.image = things[n]
     #self.image.fill(self.color)

  def update(self, dx):
     self.rect.left += dx

  def draw(self, background):
     background.blit(self.image, (self.rect.left, self.rect.top))



class MovingPlatform(pygame.sprite.Sprite):
  def __init__(self):
     pygame.sprite.Sprite.__init__(self)
     self.rect = rand_rect()
     self.color = (250,220,20)
     self.image = pygame.Surface((self.rect.width, self.rect.height))
     self.image.fill(self.color)
     self.dx = choice([-5,-4,-4,-3,-3,-3,-2,-2,-2,-2,2,2,2,3,3,3,4,4,5])

  def update(self):
     x = self.rect.centerx
     x += self.dx
     if x > 900 or x < 0:
       self.dx = -self.dx
       x += self.dx
     self.rect.centerx = x



def rand_rect():
   d1 = 20
   d2 = randint(40,200)
   x = -100*randint(0,12)
   y = 100*randint(0,4)
   return pygame.Rect(x,y,d2,d1)




