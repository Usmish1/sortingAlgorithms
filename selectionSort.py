import pygame as pg
import sys
import random
import time
import numpy as np

pg.init()

height_values = []
screenx = 1920
screeny = 1080
screen = pg.display.set_mode((screenx, screeny))
go = True

nums = 1000
#height_values = np.random.choice(1000, nums, replace=False) + 1
while len(height_values) < nums:
    tempRand = random.randint(1, 1080)
    #if tempRand not in height_values:
    height_values.append(tempRand)
    print(tempRand)
print(f"{len(height_values)} height values have been randomly generated")
print(height_values)

white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 0,0,255

screen.fill((black))

index_num = 0
for j in height_values:
    height = j
    colour = 255,255,255
    pg.draw.rect(screen, (colour), (index_num, screeny-height, 1, 1))
    index_num += 1
pg.display.update()
time.sleep(1)

screen.fill((black))
pg.display.update()
print("Starting Sort...")
time.sleep(1)

