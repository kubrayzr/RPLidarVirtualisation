from Point import Point
from datetime import datetime


from os.path import dirname,join

LidarDataset = join(dirname(__file__), "../LidarDataset")

def writecsv( points:list[Point]):
    filename=LidarDataset+"\\"+str(datetime.now().hour)+"_"+str(datetime.now().minute)+".csv"
    with open(filename, 'a+', encoding = 'utf-8') as f:
        for i in points:
            f.write(str(i.quality)+", "+str(i.angle)+","+str(i.distance)+"\n")
    return filename


def readCSVbyFilename(filename):
    points=[]
    with open(filename, "r") as f:
        lines = f.readlines()
    #quality,radianAngle,distance,x,y
    for line in lines:
        data = line.strip().split(",")
        point=Point(int(data[0]),float(data[1]),float(data[2]))
        points.append(point)
    return points




