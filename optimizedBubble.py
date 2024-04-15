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

#screen.fill((black))
pg.display.update()
print("Starting Sort...")
time.sleep(1)


t0 = time.perf_counter()
ind = 0
max = nums - 1
while True:
    if max == 0:
        break
    for i in range(0, len(height_values)-1):
        if ind == max:
            ind = 0
            max -= 1
            print(f"{(nums-1)-max} numbers have been sorted, {max} left")
        if height_values[ind] > height_values[ind+1]:
            
            #filling the 2 lines
            # rect = pg.Rect(ind, screeny-height_values[ind+1], 3, height_values[ind+1])
            # pg.draw.rect(screen, (black), rect)
            rect = pg.Rect(ind, screeny-height_values[ind], 2, height_values[ind]/10)
            pg.draw.rect(screen, (black), rect)
            underrect = pg.Rect(ind, height_values[ind], 2, height_values[ind]/10)
            pg.draw.rect(screen, (black), underrect)
            
            temp = height_values[ind]
            height_values[ind] = height_values[ind+1]
            height_values[ind+1] = temp
            
            #drawing new lines back in
            rect1 = (ind, screeny-height_values[ind], 1, 1/10)
            rect2 = (ind+1, screeny-height_values[ind+1], 1, 1/10)
            pg.draw.rect(screen, (white), rect1)
            pg.draw.rect(screen, (red), rect2)
            #pg.display.update(rect1)
            #pg.display.update(rect2)
            pg.display.update(rect)
            pg.display.update(underrect)
            
            
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
        ind += 1
    

dt = time.perf_counter() - t0
print(f"Array sorted in {dt*1E3:.1f} ms")
while True:
    for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()