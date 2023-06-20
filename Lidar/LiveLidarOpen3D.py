import time
from rplidar import RPLidar
import numpy as np
import os
from math import cos, sin, pi, floor
import pygame
import keyboard

from Point import Point
from PCDGenerator import viewPCD, csvToPCD
from TXTOperation import writecsv


def getScanByLidar():
    PORT_NAME = 'COM3'  # RPLIDAR S1'nin bağlı olduğu port adı


    lidar = RPLidar(PORT_NAME, baudrate=256000, timeout=3)
    infos=[]
    c = 0
    for i, scan in enumerate(lidar.iter_scans()):
        # scan, sensör tarafından okunan tarama verilerini içerir
        # Burada tarama verileriyle istediğiniz işlemi gerçekleştirebilirsiniz
        print('Tarama: ', i)
        for (_, angle, distance) in scan:
            p = Point(_, angle, distance)
            infos.append(p)
            if len(infos)==3600*10 :
                print('Program sonlandırıldı')
                c = 1
                break
        if c == 1:
            break


        # Txt dosyasına yazdır

    csv = writecsv(infos)

    # Txt Dosyasını PCD formatına çevir.
    pcd=csvToPCD(csv)
    print(pcd)

    # pcd dosyasını görüntüle
    viewPCD(pcd)

    lidar.stop()
    lidar.disconnect()






getScanByLidar()