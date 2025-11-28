import os
import yaml
from common.logsUtil import logs
from conf.setting import DIR_PATH


class YamlUtil(object):

    def __init__(self) -> None:
        pass

    def rdYaml(self, path):
        path = os.path.join(DIR_PATH, f'testcase/{path}/{path}.yaml')
        try:
            with open(path, 'r') as f:
                content = yaml.safe_load(f)
                return content[0]['testcase']
        except Exception as e:
            logs.error(f'读取Yaml文件失败:{e}')

if __name__ == '__main__':
    yu = YamlUtil()
    print(yu.rdYaml('login')['url'])
