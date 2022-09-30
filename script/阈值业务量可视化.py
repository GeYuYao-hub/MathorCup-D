import numpy as np
import read
import matplotlib.pyplot as plt
import log
import time
import sys

path = 'D:\数学建模\MathorCup D\MathorCup D\D题\附件\附件1 弱覆盖栅格数据(筛选).csv'
sys.stdout = log.Logger('日志/log{}.txt'.format(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))),
                        mode = 'w', encoding = 'utf-8')

l = [0,10, 20, 30, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
data = read.read_csv_3(path)
for r in l:
    all_acc = 0
    r_acc = 0
    acc = 0
    New_data = []
    for i in data:
        all_acc += i[2]
        if i[2] < r:
            continue
        else:
            r_acc += i[2]
            acc += 1
            New_data.append(i)
    New_data = np.array(New_data)
    print('在所有的弱势点中，业务量大于%d的基站:' % r)
    print(' ->基站数量占比:%.4f' % float(acc / len(data) * 100) + '%')
    print(' ->业务量占比:%.4f' % float(r_acc / all_acc * 100) + '%')
    print('-----------------------------')
    plt.scatter(New_data[:, 0], New_data[:, 1], s = 10)
    plt.show()
