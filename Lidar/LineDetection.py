import random

import cv2
import np as np
import numpy as np

image = cv2.imread('img2.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9,9))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)

minLineLength =1000
maxLineGap = 40
lines = cv2.HoughLinesP(close,1,np.pi/180,100,minLineLength,maxLineGap)
colors = []
print(len(lines))
for _ in range(len(lines)):
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    colors.append(color)

for line, color in zip(lines, colors):
    for x1, y1, x2, y2 in line:

        cv2.line(image, (x1, y1), (x2, y2), color, 3)

cv2.imshow('thresh', thresh)
cv2.imshow('close', close)
cv2.imshow('image', image)
cv2.waitKey()

