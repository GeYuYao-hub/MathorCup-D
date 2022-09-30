import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib.pylab as pylab
import numpy as np
import seaborn as sns

def k_means(data,k):
    X = []
    for i in data:
        X.append([i[0], i[1]])
    X = np.array(X)
    # 2. 模型构建
    km = KMeans(n_clusters = k, init = 'k-means++', max_iter = 30)
    km.fit(X)

    # 获取簇心
    centroids = km.cluster_centers_
    # 获取归集后的样本所属簇对应值
    y_kmean = km.predict(X)
    return centroids
