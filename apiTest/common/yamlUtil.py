import json
import os
import jsonpath

import yaml
import allure
from conf.confUtil import ConfigUtil
from conf.setting import FILE_PATH
from common.logUtil import logs
from common.requestUtil import RequestUtil
from  common.assertUtil import AssertUtil


# filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'login.yaml')

class YamlUtil(object):

    def __init__(self, file=None):
        self.conf = ConfigUtil()
        self.rqus = RequestUtil()
        self.assu = AssertUtil()
        if file:
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
        except Exception as e:
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
                stainx = data.index('$')
                endinx = data.index('}', stainx)
                orig = data[stainx:endinx + 1]
                target = orig.strip('${}')
                values = self.dealextractYaml(target)
                data = data.replace(orig, values)

        return data

    def dealYaml(self, caseinfo):
        baseurl = self.conf.dealconfig('ENV', 'host')
        url = baseurl + caseinfo['baseinfo']['path']
        allure.attach(url, f'接口地址:{url}')
        apiName = caseinfo['baseinfo']['apiName']
        allure.attach(apiName, f'接口名称:{apiName}')
        method = caseinfo['baseinfo']['method']
        allure.attach(method, f'请求方式:{method}')
        headers = caseinfo['baseinfo']['headers']
        allure.attach(str(headers), f'接口请求头的信息:{headers}', allure.attachment_type.TEXT)
        cookies = {}
        # try:
        #     cookies = self.replYaml(['baseinfo']['cookies'])
        #     allure.attach(cookies, f':cookies{cookies}', allure.attachment_type.TEXT)
        # except Exception as e:
        #     pass

        for case in caseinfo['testCase']:
            caseName = case.pop('caseName')
            allure.attach(caseName, f'测试用例名称:{caseName}')
            validation = case.pop('validation')
            extract = case.pop('extract', None)
            extracts = case.pop('extracts', None)
            resp = self.rqus.runMain(apiName=apiName, caseName=caseName, url=url, method=method, headers=headers,
                                   cookies=cookies, file=None, **case)
            allure.attach(str(resp), f'接口实际响应信息:{resp}', allure.attachment_type.TEXT)
            allure.attach(str(case),f'请求参数:{case}',allure.attachment_type.TEXT)
            print(resp)

            if extract:
                self.extractinfo(extract, resp)
            if extracts:
                pass

            # 断言
            self.assu.assertMain(validation, resp, resp['msg_code'])


    def extractinfo(self, extract, resp):
        try:
            for i, j in extract.items():
                extrinfo = {i: '未提取到数据，返回值为空或 json 提取表达式错误'}
                if '$' in j:
                    extrajson = jsonpath.jsonpath(resp, j)[0]
                    if extrajson:
                        extrinfo = {i: extrajson}
                    logs.info(f'json提取到的参数:{extrinfo}')
                    self.wtYaml(extrinfo)
        except Exception as e:
            logs.error(f'接口返回值提取异常{e}')

    def clearextractYaml(self):
        with open(FILE_PATH['extract'], 'w') as f:
            f.truncate()


if __name__ == '__main__':
    yu = YamlUtil()
    case = yu.rdYaml(FILE_PATH['testcase'])

    print(yu.extractinfo(case[0]), type(yu.dealYaml(case[0])))
