#!/usr/bin/env python

import pygame
import pickle
from pygame.locals import *
from sys import exit

bg_img = 'images/bg.png'

rzeczy = ['images/platforma01.png', 'images/platforma02.png', 'images/platforma03.png',
'images/platforma04.png', 'images/totem1.png', 'images/totem2.png', 'images/drzewo1.png',
'images/drzewo2.png', 'images/cloud1.png', 'images/grass.png', 'images/box.png',
'images/mushroom.png', 'images/stone.png', 'images/croko.png', 'images/jewel.png']

try:
   items = pickle.load(open('level'))
except:
   items = []



pygame.init()

pygame.mouse.set_visible(0)

pygame.display.set_caption("Map editor!")

clock = pygame.time.Clock()

screen = pygame.display.set_mode((900, 600))
background = pygame.image.load(bg_img).convert()

things = []
for n in rzeczy:
   things.append(pygame.image.load(n).convert_alpha())

szer = background.get_width()

nr = 0
x = 0
done = True

while done:
    clock.tick(30)
    mpos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            done = False
        if event.type == MOUSEBUTTONDOWN:
            pos = event.pos
            nowy = nr, (pos[0] -x, pos[1])
            items.append(nowy)

        if event.type == KEYDOWN:
           pressed_keys = pygame.key.get_pressed()
           if pressed_keys[K_ESCAPE]:
              done = False
           if pressed_keys[K_a]:
              nr -= 1
              if nr < 0:
                 nr = len(things) - 1
           if pressed_keys[K_d]:
              nr += 1
              if nr > len(things) - 1:
                 nr = 0
           if pressed_keys[K_DELETE]:
              items = []
              background = pygame.image.load(bg_img).convert()
           if pressed_keys[K_BACKSPACE]:
              if len(items):
                 del items[-1]
                 background = pygame.image.load(bg_img).convert()


    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_q]:
       x += 10
    if pressed_keys[K_e]:
       x -= 10
    if x < -szer + 900:
       x = -szer + 900
    if x > 0:
       x = 0

    screen.blit(background, (x, 0))
    screen.blit(things[nr], mpos)

    for item in items:
      background.blit(things[item[0]],  item[1])

    pygame.display.update()

pickle.dump(items, open('mapa','w'))
pygame.display.quit()
exit()