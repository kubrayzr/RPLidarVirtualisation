import numpy as np


class Point:
    def  __init__(self,quality,angle,distance):
        self.quality=quality
        self.angle=angle
        self.distance = distance
        self.radianAngle=np.radians(angle)
        self.x=distance * np.cos(self.radianAngle)
        self.y=distance * np.sin(self.radianAngle)












