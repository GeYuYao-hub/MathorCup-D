import read
import k_means聚类分析_import
import DBSCAN聚类分析_import
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
import dddd
import seaborn as sns


def coverage(g, D, cov_Acc, d):
    dx, dy = dddd.dddd(d)
    for i in D:
        x, y = i
        for j in range(len(dx)):
            X = x + dx[j]
            Y = y + dy[j]
            if X >= 0 and X < 2500 and Y >= 0 and Y < 2500:
                cov_Acc += g[X][Y]
                g[X][Y] = 0
    return cov_Acc


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
    DD = []
    path = r'D:\数学建模\MathorCup D\MathorCup D\D题\附件\附件1 弱覆盖栅格数据(筛选).csv'
    data = read.read_csv_3(path)
    # 初始化图
    g = np.zeros([2500, 2500])
    # 初始化图参数
    all_Acc = 0.0
    cov_Acc = 0.0
    for i in data:
        g[i[0]][i[1]] = i[2]
        all_Acc += i[2]
    lD = 0
    # 读取第一个基站数据
    D = read.read_csv_2(r'D:\数学建模\MathorCup D\MathorCup D\解决问题\各级基站\1\基站点2022-04-16-20-02-30.txt')
    DD += D
    lD += len(D)
    c1 = cov_Acc
    cov_Acc = coverage(g, D, cov_Acc, 10)
    print('第一级含有{}个基站'.format(len(D)))
    print('覆盖率为 %.2f' %(((cov_Acc - c1) / all_Acc)*100) +'%')
    # 读取第二个基站数据
    D = read.read_csv_2(r'D:\数学建模\MathorCup D\MathorCup D\解决问题\各级基站\2\基站点2022-04-16-20-26-48.txt')
    DD += D
    lD += len(D)
    c1 = cov_Acc
    cov_Acc = coverage(g, D, cov_Acc, 30)
    print('第二级含有{}个基站'.format(len(D)))
    print('覆盖率为 %.2f' %(((cov_Acc - c1) / all_Acc)*100) +'%')
    # 读取第三个基站数据
    D = read.read_csv_2(r'D:\数学建模\MathorCup D\MathorCup D\解决问题\各级基站\3\基站点2022-04-16-20-45-15.txt')
    DD += D
    lD += len(D)
    c1 = cov_Acc
    cov_Acc = coverage(g, D, cov_Acc, 30)
    print('第三级含有{}个基站'.format(len(D)))
    print('覆盖率为 %.2f' %(((cov_Acc - c1) / all_Acc)*100) +'%')
    # 打印基站数
    print('一共{}个基站'.format(lD))
    ch(data, 'yuan')
    print('总业务为{},覆盖业务为{},覆盖率为{}'.format(all_Acc, cov_Acc, cov_Acc / all_Acc))
    DD = np.array(DD)
    plt.scatter(DD[:, 0], DD[:, 1], s = 10)

    plt.show()


if __name__ == '__main__':
    main()
