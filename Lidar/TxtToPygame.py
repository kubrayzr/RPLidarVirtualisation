import os
from math import cos, sin, pi, floor

import keyboard
import pygame
import time
# Set up pygame and the display
from rplidar import RPLidar

from Point import Point
from TXTOperation import writecsv, readCSVbyFilename

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

lcd = pygame.display.set_mode((720, 720))
pygame.display.update()




points=[]
max_distance = 0
lcd.fill((0, 0, 0))
scan_data = [0] * 360
scan= readCSVbyFilename("/LidarDataset/13_0.csv")
for x in scan:

    p=Point(x.quality,x.angle,x.distance)
    points.append(p)



closest_distance =6000000
for i in range(0,len(points)):
    distance=points[i].distance
    if distance > 0:  # ignore initially ungathered data points
        max_distance = max([min([5000, distance]), max_distance])
        x = points[i].x
        y = points[i].y

        point = (250 + int(x / max_distance * 119), 450 + int(y / max_distance * 119))
        #print(angle)
        lcd.set_at(point, pygame.Color(255, 0, 0))

    pygame.display.update()




