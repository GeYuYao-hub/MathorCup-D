import read
import numpy as np
import dddd
import math
import matplotlib.pyplot as plt

g = np.zeros([2500, 2500])

out_path = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\添加并调整后.txt'


def write(data, out_path):
    with open(out_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + ',' + str(int(i[2])) + '\n'
            f.write(s)


class Queue:
    '''队列'''

    def __init__(self):
        self.__list = []

    def push(self, item):
        '''往队列中添加一个item元素，进队'''
        self.__list.append(item)

    def pop(self):
        '''从队列头部删除一个元素，出队'''
        if self.__list:
            return self.__list.pop(0)
        else:
            return None

    def front(self):
        return self.__list[0]

    def is_empty(self):
        '''判断队列是否为空'''
        if len(self.__list) == 0:
            return True
        else:
            return False

    def size(self):
        '''返回队列的大小'''
        return len(self.__list)


def havenused(pos):
    dx, dy = dddd.dddd(10)
    for i in range(len(dx)):
        a = pos[0] + dx[i]
        b = pos[1] + dy[i]
        if 0 <= a < 2500 and 0 <= b < 2500:
            if g[a][b] != 0:
                return True
    return False


def caldis(pos1, pos2):
    dis = math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return dis


def transpos(pos, st):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    New_pos = [-1, -1]
    isok = False
    q = Queue()
    q.push(pos)
    while not q.is_empty():
        t = q.pop()
        if st[t[0]][t[1]] != 0:
            continue
        st[t[0]][t[1]] = 1
        if havenused(t):
            for i in range(len(dx)):
                a = t[0] + dx[i]
                b = t[1] + dy[i]
                if 0 <= a < 2500 and 0 <= b < 2500:
                    p = [a, b]
                    if caldis(p, pos) < 10:
                        q.push(p)
        else:
            isok = True
            New_pos = t
            break

    return isok, New_pos


all = 0
notpro = 0
mod_Acc = 0
pro = 0
pos_path_before = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\确认前基站位置'
paths_list, names_list = read.traverse_dir_files(pos_path_before)
k = 1
for i in paths_list:
    data = read.read_csv_2(i)
    if i == r'D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\确认前基站位置\1':
        k = 2
    elif i == r'D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\确认前基站位置\2':
        k = 3
    elif i == r'D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\确认前基站位置\3':
        k = 3

    if i == r'D:\数学建模\MathorCup D\MathorCup D\解决问题\确认最终基站位置\确认前基站位置\0':
        for pos in data:
            all += 1
            notpro += 1
            g[pos[0]][pos[1]] = 1
    else:
        for pos in data:
            all += 1
            # 如果该点在上一级别已经被标过了就忽略
            if g[pos[0]][pos[1]] != 0:
                pro += 1
                continue
            # 如果该点周围有基站，就寻找新的点
            if havenused(pos):
                st = g.copy()
                isok, New_pos = transpos(pos, st)
                if isok:
                    g[New_pos[0]][New_pos[1]] = k
                    mod_Acc += 1
                else:
                    pro += 1
            #  如果该点各方面符合条件，就标1
            else:
                notpro += 1
                g[pos[0]][pos[1]] = k
l = []
for i in range(2500):
    for j in range(2500):
        if g[i][j] != 0 and g[i][j] != 1:
            l.append([i, j, g[i][j]])
write(l, out_path)
print('没问题的点有%d个，占比%.4f' % (notpro, (notpro / all)))
print('修改的点有%d个，占比%.4f' % (mod_Acc, (mod_Acc / all)))
print('无药可救的点有%d个，占比%.4f' % (pro, (pro / all)))
