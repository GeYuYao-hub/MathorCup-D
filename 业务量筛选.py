import read

path = 'D题/附件/附件1 弱覆盖栅格数据(筛选).csv'
out_path = 'D题/附件/附件1筛选后.csv'


def write(data, out_val_path):
    with open(out_val_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + ',' + str(i[2]) + '\n'
            f.write(s)


acc = 0
New_data = []
data = read.read_csv_3(path)
for i in data:
    if i[2] < 10:
        continue
    else:
        acc += 1
        New_data.append(i)
write(New_data, out_path)
print(acc / len(data))
