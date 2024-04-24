import os
import csv
from common.logUtil import logs
from conf.setting import DIR_PATH

def dealcsv(filename):
    # 读取 csv 文件数据
    try:
        with open(os.path.join(DIR_PATH, 'data', filename)) as csvfile:
            csvfile = csv.reader(csvfile)
            content = []
            for value in csvfile:
                content.append(value)
            return content
    except Exception as e:
        logs.error(e)

if __name__ == '__main__':
    print(dealcsv('user.csv'))