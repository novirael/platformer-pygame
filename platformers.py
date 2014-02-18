#!/usr/bin/env python

import pygame
import random
import math
from pygame.locals import *
from kula import Bullet

pygame.mixer.init()

szer = -3600

left_arrow = "images/arrow-left.png"
right_arrow = "images/arrow-right.png"

fire = pygame.mixer.Sound("sounds/fire arrow.wav")


class Platformer(pygame.sprite.Sprite):

  def __init__(self,  pos, images, bullets):
     pygame.sprite.Sprite.__init__(self)
     self.images = images
     self.x, self.y = pos
     self.prev = pos
     self.vx = self.vy = 0
     self.rect = self.images.get_rect()
     self.rect.centerx = self.x
     self.rect.centery = self.y
     self.bullets = bullets
     self.wait = 0
     self.turning = 1
     self.in_move = False
     self.shooting = False
     self.nr = 0
     self.nr_s = 0

  def update(self):
     self.prev = self.x,self.y
     self.x += self.vx
     self.y += self.vy
     self.vy += 0.6
     if self.vy > 7:
       self.vy = 7

     if self.x < 0:
        self.x = 0
     if self.y < 0:
        self.y = 0
        self.vy = 0
     if self.x > -szer + 900:
        self.x = -szer + 900
     if self.y > 600:
       self.y = 0

     self.rect.centerx = self.x
     self.rect.centery = self.y


     self.nr += 0.5

     if self.nr > 7:
        self.nr = 0

     if self.wait > 0:
        self.wait -= 1

     if self.shooting:
        if self.nr_s > 12:
          self.nr_s = 0
          self.shooting = False
        else:
          self.nr_s += 0.5


  def fire(self):
     if self.wait == 0:
        vx = 10
        vy = 0
        if self.turning == 1:
           bullet = Bullet( (self.rect.centerx + 3 * vx, self.rect.centery + 3 *vy), vx, vy, right_arrow)
        elif self.turning == -1:
           bullet = Bullet( (self.rect.centerx + 3 * -vx, self.rect.centery + 3 *vy), -vx, vy, left_arrow)
        self.bullets.add(bullet)
        self.wait = 10
        fire.play()

  def draw(self, screen):
     self.rect.top = self.rect.top +5
     # If turn Right
     if self.turning == 1:
        if self.in_move:
          screen.blit(self.images.p_right[int(self.nr)], (self.rect.left, self.rect.top))
        elif self.shooting:
          screen.blit(self.images.p_shoot_right[int(self.nr_s)], (self.rect.left, self.rect.top))
        else:
          screen.blit(self.images.p_stay[0], (self.rect.left, self.rect.top))

     # If turn Left
     elif self.turning == -1:
        if self.in_move:
          screen.blit(self.images.p_left[int(self.nr)], (self.rect.left, self.rect.top))
        elif self.shooting:
          screen.blit(self.images.p_shoot_left[int(self.nr_s)], (self.rect.left, self.rect.top))
        else:
         screen.blit(self.images.p_stay[1], (self.rect.left, self.rect.top))


  def collision(self,rect):
     new_x,new_y = self.x,self.y
     self.x,self.y = self.prev
     self.rect.centerx = self.x
     self.rect.centery = self.y

     if rect.top >= self.rect.bottom:
        self.vy = 0
        self.x = new_x
        self.rect.centerx = new_x
     else:
        self.y = new_y
        self.rect.centery = self.y

  def drive(self,pressed_keys):
    self.vx = 0
    if not self.shooting:
       if pressed_keys[K_LEFT]:
         self.vx = -5
         self.turning = -1
         self.in_move = True
       elif pressed_keys[K_RIGHT]:
         self.vx = +5
         self.turning = 1
         self.in_move = True
       else:
          self.in_move = False

    if pressed_keys[K_LALT]:
       self.vy -= 1
       self.in_move = False
    if pressed_keys[K_LCTRL]:
       if self.vy == 0:
         self.vy -= 15
       self.in_move = False
    if pressed_keys[K_SPACE]:
       self.fire()
       self.shooting = True
       self.in_move = False
