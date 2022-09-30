import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pylab as pylab
import numpy as np
import seaborn as sns


def write(data, out_val_path):
    with open(out_val_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + '\n'
            f.write(s)


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
out_path = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\点集\点集3.txt'
data = read_csv(path)
X = []
for i in data:
    X.append([i[0], i[1], i[2]])
X = np.array(X)
print(X.shape)

points = []
blocks = []
cnt = 1

while (X.shape[0]):
    plt.scatter(X[:, 0], X[:, 1], s = 5)
    point = pylab.ginput(1)
    point = list(point[0])
    point[0] = int(point[0])
    point[1] = int(point[1])
    points.append([point[0], point[1]])
    # points.append([point[0],point[1]])
    # points.append([point[0][0],points[0][1]])
    plt.show()

    New_block = []
    New_data = []
    for i in X:
        if (i[0] >= point[0] and i[1] >= point[1]):
            New_block.append(i)
        else:
            New_data.append(i)

    # np.savetxt(r"D题/块区10-19/block{}.txt".format(cnt), New_block, delimiter = ",")
    with open(r"D:\数学建模\MathorCup D\MathorCup D\解决问题\3\block{}.txt".format(cnt), 'w') as f:
        for i in New_block:
            s = str(int(i[0])) + ',' + str(int(i[1])) + ',' + str(i[2]) + '\n'
            f.write(s)

    blocks.append(New_block)
    print('在第', cnt, '轮循环:')
    print('在点击了 [', point[0], ',', point[1], '] 点后')
    print('->此刻还剩', len(New_data), '个点')
    print('->该block有', len(New_block), '个点')
    print('----------------------------------')
    X = np.array(New_data)
    cnt += 1

write(points, out_path)
