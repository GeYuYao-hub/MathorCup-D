import read
import 聚类import
import numpy as np
import os
import sys
import log
import time

sys.stdout = log.Logger('D:\数学建模\MathorCup D\MathorCup D\解决问题\各块选基站日志/log{}.txt'.format(
    time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))),
    mode = 'w', encoding = 'utf-8')
out_path = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\各级基站\3\基站点{}.txt'.format(
    time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))


def point_c(x):
    res = []
    for i in x:
        xx = []
        for j in x[i]:
            xx.append(j)
        X = 0
        Y = 0
        l = len(xx)
        for k in xx:
            X += k[0]
            Y += k[1]
        res.append([int(X / l), int(Y / l)])
    return res


def get_points(data, cluster):
    dic = {}
    for i in range(len(cluster)):
        if dic.get(cluster[i]) == None:
            dic[cluster[i]] = []
        dic[cluster[i]].append([data[i][0], data[i][1]])
    return dic


def write(data, out_val_path):
    with open(out_val_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + '\n'
            f.write(s)


def traverse_dir_files(root_dir, ext = None):
    names_list = []
    paths_list = []
    for parent, _, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.'):  # 去除隐藏文件
                continue
            if ext:  # 根据后缀名搜索
                if name.endswith(tuple(ext)):
                    names_list.append(name)
                    paths_list.append(os.path.join(parent, name))
            else:
                names_list.append(name)
                paths_list.append(os.path.join(parent, name))
    if not names_list:  # 文件夹为空
        return paths_list, names_list
    return paths_list, names_list


pos_list = []


# 针对第1号区域
def main():
    # 10，1
    # 30，50
    # 30，60
    eps, min_Pts = 30, 60
    path = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\3'
    paths_list, names_list = traverse_dir_files(path)
    print('当前时间为{}'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    print('eps:{},min_Pts:{}'.format(eps, min_Pts))
    print('文件{}:'.format(path))
    for path in paths_list:
        print('文件{}:'.format(path))
        data = read.read_csv_3(path)
        X = []
        for i in data:
            X.append([i[0], i[1]])
        X = np.array(X)
        print('-->包含{}个点'.format(X.shape[0]))
        cluster = 聚类import.DBSCAN(X, eps, min_Pts)
        points = get_points(data, cluster)
        point_cc = point_c(points)
        cnt = len(point_cc)
        print('-->可分为{}类'.format(cnt))
        print('---------------------')
        for i in point_cc:
            pos_list.append(i)
    write(pos_list, out_path)


if __name__ == '__main__':
    main()
