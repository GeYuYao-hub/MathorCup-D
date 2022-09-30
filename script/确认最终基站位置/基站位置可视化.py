import read
import k_means聚类分析_import
import DBSCAN聚类分析_import
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import dddd
import seaborn as sns

hong = 0.0
wei = 0.0


def coverage(data, D):
    all_Acc = 0.0
    cov_Acc = 0.0
    g = np.zeros([2500, 2500])

    for i in data:
        g[i[0]][i[1]] = i[2]
        all_Acc += i[2]
    for i in D:
        x, y, k = i
        global wei
        global hong
        if k == 2:
            dx, dy = dddd.dddd(10)

        else:

            dx, dy = dddd.dddd(30)

        for j in range(len(dx)):
            X = x + dx[j]
            Y = y + dy[j]
            if X >= 0 and X < 2500 and Y >= 0 and Y < 2500:
                cov_Acc += g[X][Y]
                if k == 2:
                    wei += g[X][Y]
                else:
                    hong += g[X][Y]
                g[X][Y] = 0
    print('总业务为{},覆盖业务为{},覆盖率为{}'.format(all_Acc, cov_Acc, cov_Acc / all_Acc))
    print('hong:', hong/all_Acc)
    print('wei', wei/all_Acc)


def point(data, graph):
    for i in data:
        graph[i[0]][i[1]] = i[2]
    return graph


def heatmap(data):
    graph = np.zeros([2500, 2500])
    graph = point(data, graph)
    ax = sns.heatmap(graph, vmin = 0, vmax = 200)


def ch(data, mode = 'yuan'):
    if mode == 'yuan':
        data = np.array(data)
        plt.scatter(data[:, 0], data[:, 1], s = 10)
    else:
        heatmap(data)


def main():
    pos_path = r"D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\添加并调整后所有基站位置.txt"
    path = 'D:\数学建模\MathorCup D\MathorCup D\D题\附件\附件1 弱覆盖栅格数据(筛选).csv'
    data = read.read_csv_3(path)
    D = read.read_csv_3(pos_path)
    coverage(data, D)
    print('一共{}个基站'.format(len(D)))
    ch(data, 'yuan')
    D = np.array(D)
    plt.scatter(D[:, 0], D[:, 1], s = 10)

    plt.show()


if __name__ == '__main__':
    main()
