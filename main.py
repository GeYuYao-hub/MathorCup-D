import matplotlib.pylab as pylab
import numpy as np
import seaborn as sns



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


def point(data, graph):
    for i in data:
        graph[i[0]][i[1]] = i[2]
    return graph


path = 'D题/附件/附件1 弱覆盖栅格数据(筛选).csv'


def heatmap():
    data = read_csv(path)
    graph = np.zeros([2500, 2500])
    graph = point(data, graph)
    ax = sns.heatmap(graph, vmin = 0, vmax = 200)

    pylab.show()

heatmap()

# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans
#
#
# def k_means():
#     # 1. 产生模拟数据
#     k = 100
#     data = read_csv(path)
#     X = []
#     for i in data:
#         X.append([i[0], i[1]])
#     X = np.array(X)
#     print(X.shape)
#     # 2. 模型构建
#     km = KMeans(n_clusters = k, init = 'k-means++', max_iter = 30)
#     km.fit(X)
#
#     # 获取簇心
#     centroids = km.cluster_centers_
#     # 获取归集后的样本所属簇对应值
#     y_kmean = km.predict(X)
#
#     # 呈现未归集前的数据
#     plt.scatter(X[:, 0], X[:, 1], s = 10)
#     plt.yticks(())
#     plt.show()
#
#     plt.scatter(X[:, 0], X[:, 1], c = y_kmean, s = 50, cmap = 'viridis')
#     plt.scatter(centroids[:, 0], centroids[:, 1], c = 'black', s = 10, alpha = 0.5)
#     plt.show()
#
# # k_means()

# 生成候选点：
