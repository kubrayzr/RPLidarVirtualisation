import os
from math import cos, sin, pi, floor

import keyboard
import pygame
import time
# Set up pygame and the display
from rplidar import RPLidar

from Point import Point
from TXTOperation import  writecsv


os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

lcd = pygame.display.set_mode((360, 360))
pygame.display.update()

# Setup the RPLidar

lidar = RPLidar(port='COM3', baudrate=256000, timeout=3)


# used to scale data to fit on the screen
points=[]
try:
    # print(lidar.info)
    scan_data = [0] * 360
    for scan in lidar.iter_scans():

        max_distance = 0
        lcd.fill((0, 0, 0))
        for (_, angle, distance) in scan:
            scan_data[min([360, floor(angle)])] = distance
            p=Point(_,angle,distance)
            points.append(p)



        closest_distance =6000000
        for angle in range(359):
            distance = scan_data[angle]
            if distance > 0:  # ignore initially ungathered data points
                max_distance = max([min([5000, distance]), max_distance])


                radians = angle * pi / 180.0
                x = distance * cos(radians)
                y = distance * sin(radians)
                point = (160 + int(x / max_distance * 119), 120 + int(y / max_distance * 119))
                #print(angle)
                lcd.set_at(point, pygame.Color(255, 0, 0))

        pygame.display.update()

        if keyboard.is_pressed('q'):
            print('Program sonlandırıldı')
            writecsv(points)
            break
except KeyboardInterrupt:
    print('Stoping.')
    lidar.stop()
    lidar.disconnect()
