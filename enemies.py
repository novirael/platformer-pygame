#!/usr/bin/env python

import pygame
import random
from random import randint,choice
import math
from pygame.locals import *
from kula import Bullet

szer = -3600
bomb = "images/bomb.png"

pygame.mixer.init()
shoot = pygame.mixer.Sound("sounds/hatch.wav")

class Mushroom(pygame.sprite.Sprite):

  def __init__(self,  pos, images, dead):
     pygame.sprite.Sprite.__init__(self)
     self.images = images
     self.x, self.y = pos
     self.prev = pos
     self.vx = self.vy = 2
     self.rect = self.images.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.turning = 1
     self.nr = 0
     self.max = 130
     self.distance = 0
     self.w_prawo = True
     self.dead = dead

  def update(self, dx):
     self.prev = self.x,self.y

     if self.w_prawo:
        self.x += self.vx + dx
        self.distance += self.vx
        if self.distance > self.max:
           self.w_prawo = False
           self.turning = -1
     else:
        self.x -= self.vx - dx
        self.distance -= self.vx
        if self.distance < -self.max:
           self.w_prawo = True
           self.turning = 1

     self.y += self.vy + 5
     self.rect.centerx = self.x
     self.rect.centery = self.y

     self.nr += 0.5
     if self.nr > 7:
        self.nr = 0

  def hit(self):
     umarly_grzyb = DeadMushroom( (self.rect.centerx, self.rect.centery), self.images, self.turning)
     self.dead.add(umarly_grzyb)

  def draw(self, screen):

     # If turn Right
     if self.turning == 1:
        screen.blit(self.images.mushroom_right[int(self.nr)], (self.rect.left, self.rect.top))

     # If turn Left
     else:
        screen.blit(self.images.mushroom_left[int(self.nr)], (self.rect.left, self.rect.top))

  def collision(self,rect):
     new_x,new_y = self.x,self.y
     self.x, self.y = self.prev
     self.rect.centerx = self.x
     self.rect.centery = self.y

     if rect.top >= self.rect.bottom:
        self.vy = 0
        self.x = new_x
        self.rect.centerx = new_x
     else:
        self.y = new_y
        self.rect.top = self.y


class DeadMushroom(pygame.sprite.Sprite):

  def __init__(self, pos, images, turning):
     pygame.sprite.Sprite.__init__(self)
     self.images = images
     self.x, self.y = pos
     self.rect = self.images.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.nr = 0
     self.turning = turning

  def update(self, dx):
     self.x += dx
     self.rect.centerx = self.x
     self.nr += 0.5
     if self.nr > 5:
        self.nr = 6

  def draw(self, screen):

     # If turn Right
     if self.turning == 1:
        screen.blit(self.images.dead_mushroom_right[int(self.nr)], (self.rect.left, self.rect.top+10))

     # If turn Left
     else:
        screen.blit(self.images.dead_mushroom_left[int(self.nr)], (self.rect.left, self.rect.top+10))


class Stone(pygame.sprite.Sprite):

  def __init__(self,  pos, images):
     pygame.sprite.Sprite.__init__(self)
     self.images = images
     self.x, self.y = pos
     self.prev = pos
     self.vx = self.vy = 4
     self.rect = self.images.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.nr = 0
     self.collide = False

  def update(self, dx):
     self.prev = self.x,self.y
     if self.collide:
        self.x -= self.vx
     self.y += self.vy
     self.x += dx
     if self.x < 0:
        self.vx = - self.vx
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.nr += 0.5
     if self.nr > 7:
        self.nr = 0

  def draw(self, screen):
     screen.blit(self.images.stone_left[int(self.nr)], (self.rect.left, self.rect.top))

  def collision(self,rect):
     new_x,new_y = self.x,self.y
     self.x, self.y = self.prev
     self.rect.centerx = self.x
     self.rect.centery = self.y

     if rect.top >= self.rect.bottom:
        self.x = new_x
        self.rect.centerx = new_x
     else:
        self.y = new_y
        self.rect.top = self.y
     self.collide = True


class Croko(pygame.sprite.Sprite):

  def __init__(self,  pos, images, bullets, dead):
     pygame.sprite.Sprite.__init__(self)
     self.images = images
     self.x, self.y = pos
     self.prev = pos
     self.vx = self.vy = 4
     self.rect = self.images.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.bullets = bullets
     self.nr = 0
     self.wait = 0
     self.shooting = False
     self.dead = dead
     self.hited = 0

  def update(self, dx):
     self.prev = self.x,self.y
     self.y += self.vy
     self.x += dx
     self.rect.centerx = self.x
     self.rect.centery = self.y
     x = randint(0,500)
     if x < 5:
        self.shooting = True
        self.fire()

     if self.wait == 0:
        self.shooting = False
     if self.wait > 0:
        self.wait -= 1

     self.nr += 0.25
     if self.nr > 10:
        self.nr = 0

  def hit(self):
     if self.hited > 2:
        umarly_kroko = DeadCroko( (self.rect.centerx, self.rect.centery), self.images)
        self.dead.add(umarly_kroko)
     print self.hited

  def draw(self, screen):
     if self.shooting:
        screen.blit(self.images.croko_attack[int(self.nr)], (self.rect.left, self.rect.top))
     else:
        screen.blit(self.images.croko_looking[int(self.nr)], (self.rect.left, self.rect.top))

  def collision(self,rect):
     new_x,new_y = self.x,self.y
     self.x, self.y = self.prev
     self.rect.centerx = self.x
     self.rect.centery = self.y

     if rect.top >= self.rect.bottom:
        self.x = new_x
        self.vy = 0
        self.rect.centerx = new_x
     else:
        self.y = new_y
        self.rect.top = self.y

  def fire(self):
     if self.wait == 0:
        vx = 6
        vy = 0
        bullet = Bullet( (self.rect.centerx + 3 * -vx, self.rect.centery + 3 *vy), -vx, vy, bomb)
        self.bullets.add(bullet)
        self.wait = 30
        self.shooting = True
        #shoot.play()

class DeadCroko(pygame.sprite.Sprite):

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
     if self.nr > 9:
        self.nr = 10

  def draw(self, screen):
     screen.blit(self.images.croko_daying[int(self.nr)], (self.rect.left, self.rect.top))

