#!/usr/bin/env python

import pygame
import pickle
from random import randint,choice
from pygame.locals import *
from sys import exit

from platforma import Platform
from platforma import MovingPlatform
from platformers import Platformer
from kula import Bullet
from bonuses import Jewel

from enemies import Mushroom
from enemies import Stone
from enemies import Croko
from enemies import DeadMushroom

from images import PlatformerImages
from images import MushroomImages
from images import StoneImages
from images import CrokoImages
from images import JewelsImages

# Variables
bg_img = 'images/bg.png'
serce = 'images/heart.png'

rzeczy = ['images/platforma01.png', 'images/platforma02.png', 'images/platforma03.png',
'images/platforma04.png', 'images/totem1.png', 'images/totem2.png', 'images/drzewo1.png',
'images/drzewo2.png', 'images/cloud1.png', 'images/grass.png', 'images/box.png',
'images/mushroom.png', 'images/stone.png', 'images/croko.png', 'images/jewel.png']

things = []
for n in rzeczy:
   things.append(pygame.image.load(n).convert_alpha())

player_images = PlatformerImages()
mushroom_images = MushroomImages()
stone_images = StoneImages()
croko_images = CrokoImages()
jewels_images = JewelsImages()

# Pygame init
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 40)

screen = pygame.display.set_mode((900, 600))
background = pygame.image.load(bg_img).convert()
heart = pygame.image.load(serce).convert_alpha()

get = pygame.mixer.Sound("sounds/get.wav")
knocked = pygame.mixer.Sound("sounds/knocked.wav")
whoop = pygame.mixer.Sound("sounds/WhoopFlp.wav")
victory_sound = pygame.mixer.Sound("sounds/winner.wav")
fail_sound = pygame.mixer.Sound("sounds/loser.wav")
sound = pygame.mixer.Sound("sounds/sound.mp3")

pygame.display.set_caption("Platfowka")

# Open map
try:
   items = pickle.load(open('level'))
except:
   items = []


arrows = pygame.sprite.Group()
bombs =  pygame.sprite.Group()
deads = pygame.sprite.Group()

ludek = Platformer( (50,300), player_images, arrows )

j_count = 0

platforms, back, front, mushrooms, stones, crokodiles, bonuses = [], [], [], [], [], [], []

# Check items from map and do stuff
for i in items:
   if i[0] == 0 or i[0] == 1 or i[0] == 2 or i[0] == 3:

      if i[1][1] > 510 and i[1][1] < 525:
         platforms.append( Platform( i[0], (i[1][0], 520) ) ) # koryguje pratformy
      elif i[1][1] > 440 and i[1][1] < 450:
         platforms.append( Platform( i[0], (i[1][0], 445) ) )
      elif i[1][1] > 165 and i[1][1] < 185:
         platforms.append( Platform( i[0], (i[1][0], 175) ) )
      else:
         platforms.append( Platform( i[0], i[1] ) )

      print i[1]
   elif i[0] == 4 or i[0] == 5 or i[0] == 6 or i[0] == 7:
      back.append(i)
   elif i[0] == 8 or i[0] == 9:
      front.append(i)
   elif i[0] == 11:
      mushrooms.append( Mushroom(i[1], mushroom_images, deads) )   # ( (x,y), images )
   elif i[0] == 12:
      stones.append( Stone(i[1], stone_images) )            # ( (x,y), images )
   elif i[0] == 13:
      crokodiles.append( Croko(i[1], croko_images, bombs, deads) ) # ( (x,y), images )
   elif i[0] == 14:
      bonuses.append( Jewel(i[1], jewels_images) )
      j_count += 1

print platforms

jewels = pygame.sprite.Group(bonuses)
sciany = pygame.sprite.Group(platforms)
grzybki = pygame.sprite.Group(mushrooms)
kamienie = pygame.sprite.Group(stones)
kroko = pygame.sprite.Group(crokodiles)

#all = pygame.sprite.Group(platforms + [ludek])



szer = background.get_width()
x = 0
lifes = 40
points = 0

play = False
done = True
move = False
updated = False
fail = False
victory = False
dead_time = 0
#sound.play()

while done:

    # fps
    clock.tick(30)

    ###################### EVENTS ######################

    for event in pygame.event.get():
       if event.type == QUIT:
          done = False
       if event.type == KEYDOWN:
          pressed_keys = pygame.key.get_pressed()
          if pressed_keys[K_ESCAPE]:
             done = False

    pressed_keys = pygame.key.get_pressed()

    if not fail and not victory:

       # Draw background
       screen.blit(background, (x, 0))

       ################### STATES UPDATE ###################

       ludek.drive(pressed_keys)
       ludek.update()

       if dead_time > 0:
         dead_time -= 1

       # Delete bad
       for a in arrows:
         if a.x > 900 or a.x < 0:
            arrows.remove(a)
       for b in bombs:
          if b.x > 900 or b.x < 0:
            arrows.remove(b)
       for k in kamienie:
          if k.y > 600:
            kamienie.remove(k)


       # Collisions with platform
       for p in platforms:
          if pygame.sprite.collide_rect(p,ludek):
             ludek.collision(p.rect)
          for m in mushrooms:
             if pygame.sprite.collide_rect(p, m):
                m.collision(p.rect)
          for s in stones:
             if pygame.sprite.collide_rect(p, s):
                s.collision(p.rect)
          for c in crokodiles:
             if pygame.sprite.collide_rect(p, c):
                c.collision(p.rect)


       for s in stones:
         if pygame.sprite.collide_rect(ludek, s) and dead_time == 0:
            #ludek.y = 0
            lifes -= 1
            knocked.play()

       for g in grzybki:
         if pygame.sprite.collide_rect(ludek, g) and dead_time == 0:
            #ludek.y = 0
            lifes -= 1
            dead_time = 100
            knocked.play()

       for k in kroko:
         if pygame.sprite.collide_rect(ludek, k) and dead_time == 0:
            #ludek.y = 0
            lifes -= 1
            dead_time = 100
            knocked.play()
       for b in bombs:
         if pygame.sprite.collide_rect(ludek, b) and dead_time == 0:
            #ludek.y = 0
            lifes -= 1
            dead_time = 100
            knocked.play()

       # Collision aroows-enemies
       for a in arrows:
          for g in grzybki:
             if pygame.sprite.collide_rect(a, g):
                g.hit()
                grzybki.remove(g)
                arrows.remove(a)
                whoop.play()
          for k in kroko:
             if pygame.sprite.collide_rect(a, k):
                k.hited += 1
                k.hit()
                if k.hited > 2:
                   kroko.remove(k)
                arrows.remove(a)
                whoop.play()


       #if pygame.sprite.groupcollide(arrows, grzybki, True, True):
       #   whoop.play()

       #if pygame.sprite.groupcollide(arrows, kroko, True, True):
       #   whoop.play()

       if pygame.sprite.groupcollide(arrows, bombs, True, True):
          whoop.play()

       # Collecting jewels
       for j in jewels:
          if pygame.sprite.collide_rect(j, ludek):
            jewels.remove(j)
            points += 1
            get.play()



       # Screen and items scrolling
       #  (x = real position of x)
       if x != 0:
         if ludek.x < 450:
           x += 5
           sciany.update(5)
           grzybki.update(5)
           kamienie.update(5)
           kroko.update(5)
           arrows.update(5)
           bombs.update(5)
           deads.update(5)
           jewels.update(5)
           updated = True
           ludek.x += 5
       if x != -szer + 900:
         if ludek.x > 450:
           x -= 5
           sciany.update(-5)
           grzybki.update(-5)
           kamienie.update(-5)
           kroko.update(-5)
           arrows.update(-5)
           bombs.update(-5)
           deads.update(-5)
           jewels.update(-5)
           updated = True
           ludek.x -= 5
         if x < -szer + 900:
           x = -szer + 900
         if x > 0:
           x = 0
       if not updated:
          grzybki.update(0)
          kamienie.update(0)
          kroko.update(0)
          arrows.update(0)
          bombs.update(0)
          deads.update(0)
          jewels.update(0)
       updated = False


       ##################### END UPDATE ####################

       ###################### DRAWING ######################


       # Draw elements of background
       for b in back:
         nr = b[0]
         screen.blit(things[nr], (b[1][0] + x, b[1][1] ) )

       # Draw platforms
       sciany.draw(screen)

       # Draw jewels
       for j in jewels:
          j.draw(screen)

       # Draw dead mushrooms
       for d in deads:
          d.draw(screen)

       # Draw player
       ludek.draw(screen)

       # Draw enemies
       for k in kamienie:
          k.draw(screen)

       for g in grzybki:
          g.draw(screen)

       for k in kroko:
          k.draw(screen)

       # Draw elements of frontground
       for f in front:
         nr = f[0]
         screen.blit(things[nr], (f[1][0] + x, f[1][1] ) )

       # Draw arrows
       arrows.draw(screen)

       # Draw bombs
       bombs.draw(screen)


       # Draw Hearts
       if lifes > 0: screen.blit(heart, (5,5))
       if lifes > 1: screen.blit(heart, (40,5))
       if lifes > 2: screen.blit(heart, (75,5))

       # Draw points
       napis = "JEVELS: " + str(points)
       screen.blit(font.render(napis, True, (255,255,255) ), (790,10))

       #################### END DRAWIND ####################

       if lifes < 1:
          fail = True
          play = True
          fail_sound.play()
          screen.blit(font2.render("You Fail!", True, (255,255,255) ), (380,280))
       if points == j_count:
          victory = True
          play = True
          victory_sound.play()
          screen.blit(font2.render("You Win!", True, (255,255,255) ), (380,280))

    # Display update
    pygame.display.update()


pygame.display.quit()
exit()