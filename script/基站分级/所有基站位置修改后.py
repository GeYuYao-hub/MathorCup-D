path1 = r'D:\数学建模\MathorCup D\MathorCup D\script\基站分级\添之前的基站.txt'
path2 = r'D:\数学建模\MathorCup D\MathorCup D\script\基站分级\添之后的基站.txt'
output = r'D:\数学建模\MathorCup D\MathorCup D\script\基站分级\自己添的基站.txt'

import read


def write(data, out_path):
    with open(out_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + ',' + str(int(i[2])) + '\n'
            f.write(s)


out = []
data1 = read.read_csv_3(path1)
data2 = read.read_csv_3(path2)
for i in data2:
    flag = False
    for j in data1:
        if i == j:
            flag = True
            break
    if flag:
        continue
    else:
        i[2] = int(i[2])
        out.append(i)
print(out)
print(len(out))
write(out,output)
