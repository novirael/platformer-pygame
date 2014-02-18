import pygame
import random

def number2d(n):
   if n < 10: return "0" + str(n)
   return str(n)



class PlatformerImages:
 def __init__(self):
  self.p_right = []
  self.p_left = []
  self.p_stay = []
  self.p_shoot_right = []
  self.p_shoot_left = []

  nazwy = [ "images/player/running e00" + number2d(i) + ".bmp" for i in range(8)]
  for n in nazwy:
     self.p_right.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.p_right[-1].get_at( (1,1) )
     self.p_right[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/player/running w00" + number2d(i) + ".bmp" for i in range(8)]
  for n in nazwy:
     self.p_left.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.p_left[-1].get_at( (1,1) )
     self.p_left[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/player/staying e.bmp", "images/player/staying w.bmp"]
  for n in nazwy:
     self.p_stay.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.p_stay[-1].get_at( (1,1) )
     self.p_stay[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/player/shooting e00" + number2d(i) + ".bmp" for i in range(13)]
  for n in nazwy:
     self.p_shoot_right.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.p_shoot_right[-1].get_at( (1,1) )
     self.p_shoot_right[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/player/shooting w00" + number2d(i) + ".bmp" for i in range(13)]
  for n in nazwy:
     self.p_shoot_left.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.p_shoot_left[-1].get_at( (1,1) )
     self.p_shoot_left[-1].set_colorkey( (r,g,b) )

 def get_rect(self):
   return self.p_right[0].get_rect()



class MushroomImages:
 def __init__(self):
  self.mushroom_right = []
  self.mushroom_left = []
  self.dead_mushroom_right = []
  self.dead_mushroom_left = []

  nazwy = [ "images/mushroom/walking e00" + number2d(i) + ".bmp" for i in range(8)]
  for n in nazwy:
     self.mushroom_right.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.mushroom_right[-1].get_at( (1,1) )
     self.mushroom_right[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/mushroom/walking w00" + number2d(i) + ".bmp" for i in range(8)]
  for n in nazwy:
     self.mushroom_left.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.mushroom_left[-1].get_at( (1,1) )
     self.mushroom_left[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/mushroom/disappear e00" + number2d(i) + ".bmp" for i in range(7)]
  for n in nazwy:
     self.dead_mushroom_right.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.dead_mushroom_right[-1].get_at( (1,1) )
     self.dead_mushroom_right[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/mushroom/disappear w00" + number2d(i) + ".bmp" for i in range(7)]
  for n in nazwy:
     self.dead_mushroom_left.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.dead_mushroom_left[-1].get_at( (1,1) )
     self.dead_mushroom_left[-1].set_colorkey( (r,g,b) )

 def get_rect(self):
   return self.mushroom_right[0].get_rect()



class StoneImages:
 def __init__(self):
  self.stone_right = []
  self.stone_left = []
  """
  nazwy = [ "images/stone/rolling stone e00" + number2d(i) + ".bmp" for i in range(1,24)]
  for n in nazwy:
     self.stone_right.append(pygame.image.load(n).convert().subsurface(pygame.Rect(20,15,62,62)))
     r,g,b,a = self.stone_right[-1].get_at( (1,1) )
     self.stone_right[-1].set_colorkey( (r,g,b) )
  """
  nazwy = [ "images/stone/rolling stone w00" + number2d(i) + ".bmp" for i in range(1,24)]
  for n in nazwy:
     self.stone_left.append(pygame.image.load(n).convert().subsurface(pygame.Rect(8,8,50,50)))
     r,g,b,a = self.stone_left[-1].get_at( (1,1) )
     self.stone_left[-1].set_colorkey( (r,g,b) )

 def get_rect(self):
   return self.stone_left[0].get_rect()



class CrokoImages:
 def __init__(self):
  self.croko_attack = []
  self.croko_looking = []
  self.croko_daying = []

  nazwy = [ "images/croko/attack w00" + number2d(i) + ".bmp" for i in range(11)]
  for n in nazwy:
     self.croko_attack.append(pygame.image.load(n).convert().subsurface(pygame.Rect(15,15,95,80)))
     r,g,b,a = self.croko_attack[-1].get_at( (1,1) )
     self.croko_attack[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/croko/looking w00" + number2d(i) + ".bmp" for i in range(11)]
  for n in nazwy:
     self.croko_looking.append(pygame.image.load(n).convert().subsurface(pygame.Rect(15,15,95,80)))
     r,g,b,a = self.croko_looking[-1].get_at( (1,1) )
     self.croko_looking[-1].set_colorkey( (r,g,b) )

  nazwy = [ "images/croko/tipping over w00" + number2d(i) + ".bmp" for i in range(11)]
  for n in nazwy:
     self.croko_daying.append(pygame.image.load(n).convert().subsurface(pygame.Rect(15,15,95,80)))
     r,g,b,a = self.croko_daying[-1].get_at( (1,1) )
     self.croko_daying[-1].set_colorkey( (r,g,b) )

 def get_rect(self):
   return self.croko_attack[0].get_rect()



class JewelsImages:
 def __init__(self):
   self.jewels = []

   nazwy = [ "images/jewels/jewel red00" + number2d(i) + ".bmp" for i in range(32)]
   for n in nazwy:
     self.jewels.append(pygame.image.load(n).convert().subsurface(pygame.Rect(18,5,30,30)))
     r,g,b,a = self.jewels[-1].get_at( (1,1) )
     self.jewels[-1].set_colorkey( (r,g,b) )

 def get_rect(self):
   return self.jewels[0].get_rect()




