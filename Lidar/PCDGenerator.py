import numpy as np
import open3d as o3d

# x ve y koordinatlarını numpy dizisine dönüştür
from TXTOperation import readCSVbyFilename


def csvToPCD(filename):
    coordinates=readCSVbyFilename(filename)

    points=[]
    for line in coordinates:
        x = line.x
        y = line.y
        points.append([x, y, 0])
    points = np.array(points)
    # Nokta bulutunu PointCloud veri yapısına dönüştür
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    # PCD dosyası olarak kaydet
    pcdName=(str(filename).replace(".csv",".pcd"))
    o3d.io.write_point_cloud(pcdName, pcd)
    return pcdName


def viewPCD(pcdName):
    # PCD dosyasını yükle
    pcd = o3d.io.read_point_cloud(pcdName)

    # # PCD dosyasını görselleştir
    o3d.visualization.draw_geometries([pcd])








