# conding:utf-8
import os
from configparser import ConfigParser

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dbpara.ini')
print(filePath)

class dealConfig(ConfigParser):
    def __init__(self, filePath):
        # 继承类的初始化
        super().__init__()
        self.read(filePath, encoding='utf-8')
    

if __name__ == '__main__':
    conf = dealConfig(filePath)
    print(conf.items('localdb'))
