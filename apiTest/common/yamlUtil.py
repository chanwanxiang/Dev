import json
import  os

import yaml
from conf.confUtil import ConfigUtil
from conf.setting import FILE_PATH
from common.logUtil import logs

# filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login.yaml')

class YamlUtil(object):

    def __init__(self, file=None):
        self.conf= ConfigUtil()
        if  file:
            self.file = file
        else:
            self.file = FILE_PATH['extract']

    def rdYaml(self, path=None):
        if path:
            path = path
        else:
            path = self.file
        try:
            with open(path, 'r') as f:
                content = yaml.safe_load(f)
                return content
        except Exception as  e:
            print('读取Yaml文件报错:{0}'.format(e))

    def wtYaml(self, value: dict):
        if not os.path.exists(FILE_PATH['extract']):
            os.system(FILE_PATH['extract'])
        try:
            file = open(FILE_PATH['extract'], 'a', encoding='utf-8')
            if isinstance(value, dict):
                writedata = yaml.dump(value, allow_unicode=True, sort_keys=False)
                file.write(writedata)
            else:
                print('暂仅支持写入字典类型数据')
        except Exception as e:
            print('写入 Ymal 文件报错{0}'.format(e))
        finally:
            file.close()

    def dealextractYaml(self, nodename):
        content = self.rdYaml()
        return content[nodename]

    def replYaml(self, data):
        if not isinstance(data, str):
            data = json.dumps(data)

        for i in range(data.count('${')):
            if '${' in data and '}' in data:
                stainx= data.index('$')
                endinx = data.index('}', stainx)
                orig = data[stainx:endinx+1]
                target = orig.strip('${}')
                values = self.dealextractYaml(target)
                data = data.replace(orig, values)

        return data

    def dealYaml(self, caseinfo):
        baseurl = self.conf.dealconfig('ENV', 'host')
        url = baseurl + caseinfo['baseinfo']['path']
        apiName = caseinfo['baseinfo']['apiName']
        method = caseinfo['baseinfo']['method']
        headers = caseinfo['baseinfo']['headers']

        for case in caseinfo['testCase']:
            logs.info('遍历用例')
            caseName = case.pop('caseName')
            validation = case.pop('validation')
            extract = case.pop('extract', None)


if __name__ == '__main__':
    yu = YamlUtil()
    case = yu.rdYaml(FILE_PATH['testcase'])
    print(case[0])
    extr = yu.rdYaml()
    token = yu.dealextractYaml('token')
    print(token)
    print(yu.replYaml(case[0]))
