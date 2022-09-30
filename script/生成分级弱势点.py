import numpy as np
import read
import matplotlib.pyplot as plt
import log
import time
import sys

path = 'D:\数学建模\MathorCup D\MathorCup D\D题\附件\附件1 弱覆盖栅格数据(筛选).csv'
sys.stdout = log.Logger('日志/log{}.txt'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))),
                        mode = 'w', encoding = 'utf-8')


def write(data, out_path):
    with open(out_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + ',' + str(i[2]) + '\n'
            f.write(s)


data = read.read_csv_3(path)
l = [[], [], []]
acc = [0, 0, 0]
all_acc = 0
for i in data:
    all_acc += i[2]
    if i[2] > 100:
        acc[0] += i[2]
        l[0].append(i)
    elif 30 < i[2] <= 100:
        acc[1] += i[2]
        l[1].append(i)
    elif i[2] <= 30:
        acc[2] += i[2]
        l[2].append(i)

for i in range(len(l)):
    print(' ->基站数量占比:%.4f' % float(len(l[i]) / len(data) * 100) + '%')
    print(' ->业务量占比:%.4f' % float(acc[i] / all_acc * 100) + '%')
    print('-----------------------------')
    path = 'D:\数学建模\MathorCup D\MathorCup D\解决问题\分级弱势点\{}.txt'.format(i + 1)
    write(l[i], path)
