import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pylab as pylab
import numpy as np
import seaborn as sns

point_path = 'D:\数学建模\MathorCup D\MathorCup D\解决问题\点集\点集3.txt'


def read_point(point_path):
    x = []
    y = []
    with open(point_path, "r") as f:  # 打开文件
        lines = f.readlines()  # 调用文件的 readline()方法
        for line in lines:
            xx, yy = line.split(',')
            x.append(int(xx))
            y.append(int(yy))
    return x, y


def read_csv(path):
    data = []
    with open(path, "r") as f:  # 打开文件
        lines = f.readlines()  # 调用文件的 readline()方法
        for line in lines:
            x, y, rate = line.split(',')
            x = int(x)
            y = int(y)
            rate = float(rate)
            data.append([x, y, rate])
        return data


path = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\分级弱势点\3.txt'
data = read_csv(path)
x, y = read_point(point_path)
X = []
for i in data:
    X.append([i[0], i[1], i[2]])
X = np.array(X)
print(X.shape)
plt.scatter(X[:, 0], X[:, 1], s = 10)
plt.plot(x, y, 'r.', linewidth = 2)
plt.show()
