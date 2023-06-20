
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from Lidar.PCDGenerator import viewPCD
from Lidar.TXTOperation import readCSVbyFilename

arr=[1.53,1.5339956,1.5409843,1.5479403,1.5459074,1.5698668,1.5678197,1.5777647,1.5836343,1.6015576,1.6124736,1.6083832,1.6742799,0.,0.,0.,0.,0.,0.,2.3073106,2.324145,2.3309727,2.361603,2.3704076,2.3972018,2.4449847,2.4577649,2.480535,2.4923,2.4970572,2.5218034,2.5495417,2.537551,2.6057124,2.611423,2.5831351,2.559838,2.5745234,2.5812037,2.6208665,2.681515,2.6791742,2.726809,2.7694383,2.7804413,2.7920718,2.8116927,2.8605022,2.8740938,2.909668,2.9262414,2.9528039,2.984356,3.006904,3.035441,3.0459774,3.0854938,3.1180053,3.135516,3.075054,3.1035438,3.1580143,3.171495,3.1989617,3.2334175,3.2588694,3.2923098,3.3267415,3.356168,3.3925831,3.4259918,3.5673387,3.5977335,3.6501095,3.69748,3.7398455,3.7182345,3.6876218,3.658001,3.6667018,3.7360067,0.,4.0278606,4.3360415,4.3813467,4.1310973,4.395272,4.430551,4.5008054,4.5640564,4.6372952,4.729519,4.7837524,4.87796,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,5.3878627,5.1700807,5.152204,4.995386,5.129426,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,7.918638,7.7662506,7.6648364,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,4.9105034,4.883085,4.8007374,4.810275,4.8078275,4.8163686,4.844885,4.8534284,4.885942,0.,4.907473,0.,0.,0.,0.,0.,0.,0.,0.,7.8126216,7.782214,7.751807,7.8433456,0.,0.,0.,0.,3.5681338,3.566499,0.,0.,3.7295783,3.7458959,0.,0.,0.,0.,0.,0.,0.,0.,0.,4.224759,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]

points=readCSVbyFilename("C:\\Users\\Can\\PycharmProjects\\Lidar\\LidarDataset\\15_34.csv")

distances=[]
for point in points:
    if point.distance>100:
        distances.append(0)
    else:
        distances.append(point.distance)


# Verilerinizi yükleyin veya oluşturun
scan = np.array(arr,dtype=np.float32)
angles = np.linspace(0, 2*np.pi, scan.shape[0]+1, dtype=np.float32)[:-1]
ranges = arr
data = np.column_stack((angles, ranges))

# Verilerinizi normalleştirin
scaler = StandardScaler()
data = scaler.fit_transform(data)

# K-means nesnesi oluşturun ve fit() yöntemini kullanarak verilerinizi kümelere ayırın
kmeans = KMeans(n_clusters=8, random_state=0)
kmeans.fit(data)

# Küme merkezlerini alın ve sonuçları yazdırın
centers = kmeans.cluster_centers_
print(centers)

# Kümelere atanan etiketleri alın ve sonuçları yazdırın
labels = kmeans.labels_
print(labels)

# Verileri ve küme merkezlerini görselleştirin
plt.scatter(data[:, 0], data[:, 1], c=labels)
plt.scatter(centers[:, 0], centers[:, 1], marker='*', s=200, c='#050505')
plt.show()

viewPCD("C:\\Users\\Can\\PycharmProjects\\Lidar\\LidarDataset\\15_34.pcd")
