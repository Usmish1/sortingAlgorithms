import pygame as pg
import sys
import random
import time
import numpy as np

height_values = []
completed = False
heights = {}

pg.init()

screenx = 1000
screeny = 1000
screen = pg.display.set_mode((screenx, screeny))
times = 0
# while times < 10:
#     if not completed:
#         for e in range(1, 499):
#             go = True
#             while go:
#                 i = random.randint(1, 499)
#                 if i not in height_values:
#                     #print(i, " is being set")
#                     height_values.append(i)
#                     go = False
#             height = i
#             pg.draw.rect(screen, (255,255,255), (e+150, 1000-height, 1, height))
#         print(height_values)
#     completed = True
#     pg.display.update()
#     time.sleep(0.05)
#     times += 1
    
#     for e in pg.event.get():
#                 if e.type == pg.QUIT:
#                     pg.quit()
#                     sys.exit()

nums = 500
height_values = np.round(np.linspace(0, 1000, 1000),0)
np.random.shuffle(height_values)
print(f"{len(height_values)} height values have been randomly generated")

screen.fill((0,0,0))
index_num = 0
for j in height_values:
    height = j
    colour = 255,255,255
    pg.draw.rect(screen, (colour), (index_num*2, screeny-height, 1, height))
    index_num += 1
pg.display.update()
time.sleep(3)

print("continuing")

t0 = time.perf_counter()

go = True
while True:
    in_row = 0
    ind = 0
    #max = 100
    #gone_through = 0
    max = nums - 1
    while go:
        if max == 0:
            dt = time.perf_counter() - t0
            print(f"Array sorted in {dt*1E3:.1f} ms")
        if ind == max:
        #     gone_through = 120
            ind = 0
            max -= 1
            print(f"{(nums-3)-max} numbers have been sorted, {max} left")           
        #     #break
        # if ind == max and gone_through == 100:
        #     max += 100
        #     ind = max
        #     gone_through = 0
        # if ind == max:
        #     ind = max-100
        #     gone_through += 1
        # randomizer = random.randint(0,5)
        # if height_values[ind-1] - height_values[ind+1] > 300 and height_values[ind-1] + 299 + randomizer < 997:
        #     print("starting large diff switch")
        #     temp = height_values[ind-1]
        #     temp1 = height_values[ind+299+randomizer]
        #     height_values[ind-1] = temp1
        #     height_values[ind+299+randomizer] = temp
        #     print(f"Large Difference between {height_values[ind]} and {height_values[ind+1]}, switching: {temp}, {temp1}")
        #     screen.fill((0,0,0))
        #     index_num = 0
        #     #print(f"Rendering: {index_num}")
        #     for j in height_values:
        #         height = j 
        #         pg.draw.rect(screen, (255,255,255), (index_num, 1000-height, 2, height))
        #         index_num += 1
        #     #print(f"Render {index_num} completed")
        #     pg.display.update()
        #     for e in pg.event.get():
        #             if e.type == pg.QUIT:
        #                 pg.quit()
        #                 sys.exit()
            
   
        if height_values[ind] > height_values[ind+1]:
            temp = height_values[ind]
            temp1 = height_values[ind+1]
            height_values[ind] = temp1
            height_values[ind+1] = temp
            in_row = 0
            #print(f"switching {temp}, {temp1} to -> {height_values[ind]}, {height_values[ind+1]}")
            screen.fill((0,0,0))
            index_num = 0
            #print(f"Rendering: {ind}")
            for j in height_values:
                height = j
                if j == temp:
                    colour = 255,0,0
                else:
                    colour = 255,255,255
                pg.draw.rect(screen, (colour), (index_num*2, screeny-height, 1, height))
                index_num += 1
            #print(f"Render {index_num} completed")
            pg.display.update()
        else:
            in_row += 1
        #print(ind)
        ind += 1
        for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
    print(in_row)
    
    for e in pg.event.get():
                if e.type == pg.QUIT:
                    pg.quit()
                    sys.exit()



# height_values.sort(reverse=True)
# print(height_values)
# while True:
#     screen.fill((0,0,0))
#     index_num = 1
#     for j in height_values:
#         height = j * 2
#         pg.draw.rect(screen, (255,255,255), (index_num, 1000-height, 2, height))
#         index_num += 1
    
#     pg.display.update()
    
#     for e in pg.event.get():
#                 if e.type == pg.QUIT:
#                     pg.quit()
#                     sys.exit()
    

# while True:
#     index_num = 0
#     for j in height_values:
#         if index_num > 0:
#             if j < height_values[index_num-1]:
#                 temp = height_values[index_num-1]
#                 #print(temp)
#                 height_values[index_num-1] = j
#                 #print(height_values[index_num-1])
#                 j = temp
#                 #print(j)
#                 break
#         index_num += 1
        
        
        
#     screen.fill((0,0,0))
#     index_ = 1
#     for j in height_values:
#         height = j * 2
#         pg.draw.rect(screen, (255,255,255), (index_, 1000-height, 2, height))
#         index_ += 1
#     pg.display.update()