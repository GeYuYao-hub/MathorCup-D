import numpy as np
import math

fa = np.zeros(10000000).astype('int')
st = np.zeros(10000000).astype('int')
path = 'D题/附件/附件1 弱覆盖栅格数据(筛选).csv'


def dis(x, y, a, b):
    return math.sqrt(math.pow(x - a, 2) + math.pow(y - b, 2))


def find(x):
    if x == fa[x]:
        return x
    else:
        fa[x] = find(fa[x])
        return fa[x]


def merge(x, y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    else:
        fa[b] = a
        return


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


data = read_csv(path)
for i in range(len(fa)):
    fa[i] = i



for i in range(len(data)):
    x, y, rate = data[i]
    for j in range(len(data)):
        a, b, c = data[j]
        if dis(x, y, a, b) <= 20:
            merge(i, j)

Acc = 0
for i in range(len(data)):
    if st[fa[i]]:
        continue
    else:
        Acc += 1
        st[fa[i]] = 1
print(len(data))
print(Acc)
