import os


def read_csv_3(path):
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


def read_csv_2(path):
    data = []
    with open(path, "r") as f:  # 打开文件
        lines = f.readlines()  # 调用文件的 readline()方法
        for line in lines:
            x, y = line.split(',')
            x = int(x)
            y = int(y)
            data.append([x, y])
        return data


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
