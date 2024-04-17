import  os

import yaml

filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login.yaml')
print(filePath)

class YamlUtil(object):

    def __init__(self, file=None):
        if  not file:
            self.file = file
        else:
            self.file = 'extract.yaml'

    def rdYaml(self):
        try:
            with open(filePath, 'r') as f:
                content = yaml.safe_load(f)
                return content
        except Exception as  e:
            print('读取 Yaml 文件报错{0}'.format(e))
    def wtYaml(self, value: dict):
        fileRout = r'extract.ymal'
        if not os.path.isfile(fileRout):
            os.system(fileRout)
        try:
            file = open(fileRout, 'a', encoding='utf-8')
            if isinstance(value, dict):
                writedata = yaml.dump(value, allow_unicode=True, sort_keys=False)
                file.write(writedata)
            else:
        except Exception as e:
            print('写入 Ymal 文件报错{0}'.format(e))
        finally:
            file.close()



if __name__ == '__main__':
    yu = YamlUtil()
    print(yu.rdYaml())