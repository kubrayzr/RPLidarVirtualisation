import os

from PCDGenerator import viewPCD


def find_pcd_files():
    paths=[]
    for root, dirs, files in os.walk("../LidarDataset"):
        for file in files:
            if file.endswith(".pcd"):
                print(os.path.join(root, file))
                paths.append(os.path.join(root, file))
    return paths



# Fonksiyonu çağırma
viewPCD(find_pcd_files()[3])
