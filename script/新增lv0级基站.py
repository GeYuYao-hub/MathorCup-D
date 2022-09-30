import read


def write(data, out_path):
    with open(out_path, 'w') as f:
        for i in data:
            s = str(int(i[0])) + ',' + str(int(i[1])) + '\n'
            f.write(s)


path = r'D:\数学建模\MathorCup D\MathorCup D\D题\附件\附件2 现网站址坐标(筛选).csv'
out_path = r'D:\数学建模\MathorCup D\MathorCup D\解决问题\各级基站\0\基站0'
data = read.read_csv_3(path)
dd = []
for i in data:
    dd.append([int(i[1]), int(i[2])])
write(dd, out_path)
