import configparser
from conf.setting import FILE_PATH


class ConfigUtil(object):

    def __init__(self, filePath=None):
        if filePath is None:
            self.filePath = FILE_PATH['CONFIG']
        else:
            self.filePath = filePath
        self.config = configparser.ConfigParser()
        try:
            self.config.read(self.filePath)
        except Exception as e:
            print('读取 conf 文件报错{0}'.format(e))

    def dealconfig(self, section, option):
        return self.config[section][option]


if __name__ == '__main__':
    conf = ConfigUtil()
    print(conf.dealconfig('ENV', 'host'))
    print(conf.item)
