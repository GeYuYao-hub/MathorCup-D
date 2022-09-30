from sklearn import datasets
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import copy


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


path = 'D题/块区/block1.csv'


def find_neighbor(j, x, eps):
    temp = np.sum((x - x[j]) ** 2, axis = 1) ** 0.5
    N = np.argwhere(temp <= eps).flatten().tolist()
    return set(N)


def DBSCAN(X, eps, min_Pts):
    k = -1
    neighbor_list = []  # 用来保存每个数据的邻域
    omega_list = []  # 核心对象集合
    gama = set([x for x in range(len(X))])  # 初始时将所有点标记为未访问
    cluster = [-1 for _ in range(len(X))]  # 聚类
    for i in range(len(X)):
        neighbor_list.append(find_neighbor(i, X, eps))
        if len(neighbor_list[-1]) >= min_Pts:
            omega_list.append(i)  # 将样本加入核心对象集合
    omega_list = set(omega_list)  # 转化为集合便于操作
    while len(omega_list) > 0:
        gama_old = copy.deepcopy(gama)
        j = random.choice(list(omega_list))  # 随机选取一个核心对象
        k = k + 1
        Q = list()
        Q.append(j)
        gama.remove(j)
        while len(Q) > 0:
            q = Q[0]
            Q.remove(q)
            if len(neighbor_list[q]) >= min_Pts:
                delta = neighbor_list[q] & gama
                deltalist = list(delta)
                for i in range(len(delta)):
                    Q.append(deltalist[i])
                    gama = gama - delta
        Ck = gama_old - gama
        Cklist = list(Ck)
        for i in range(len(Ck)):
            cluster[Cklist[i]] = k
        omega_list = omega_list - Ck
    return cluster


data = read_csv(path)
X = []
for i in data:
    X.append([i[0], i[1]])
X = np.array(X)
print(X.shape)
# X1, y1 = datasets.make_circles(n_samples = 2000, factor = .6, noise = .02)
# X2, y2 = datasets.make_blobs(n_samples = 400, n_features = 2, centers = [[1.2, 1.2]], cluster_std = [[.1]],
#                              random_state = 9)
# X = np.concatenate((X1, X2))
eps = 1
min_Pts = 1
begin = time.time()
C = DBSCAN(X, eps, min_Pts)
print(C)
end = time.time()
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c = C)
plt.show()
C = set(C)
print(C)
print(len(C))
