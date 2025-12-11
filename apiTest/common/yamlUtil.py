import os
import json
import yaml
import allure
import jsonpath
from datetime import datetime
from common.logUtil import logs
from conf.confUtil import ConfigUtil
from conf.setting import FILE_PATH
from common.assertUtil import AssertUtil
from common.requestUtil import RequestUtil


class YamlUtil(object):

    def __init__(self, file=None):
        self.assu = AssertUtil()
        self.conf = ConfigUtil()
        self.rqus = RequestUtil()

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
            cases = []
            with open(path, 'r') as f:
                content = yaml.safe_load(f)
                content = json.loads(self.replYaml(content))
                # 处理用例
                if len(content) <= 1:
                    content = content[0]
                    baseinfo = content['baseinfo']
                    for case in content['testCase']:
                        cases.append([baseinfo, case])
                    return cases
                else:
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
                logs.info(f'写入extract文件数据:{writedata}')
                file.write(writedata)
            else:
                print('暂仅支持写入字典类型数据')
        except Exception as e:
            print('写入 Ymal 文件报错{0}'.format(e))
        finally:
            file.close()

    def dealextractYaml(self, nodename, stepnodename=None):
        content = self.rdYaml()
        try:
            if stepnodename is None:
                return content[nodename]
            else:
                return content[nodename][stepnodename]
        except Exception as e:
            logs.error(f'从extract文件中获取{nodename}节点数据失败:{e}')
            return 'Unknown'

    def replYaml(self, data):
        if not isinstance(data, str):
            data = json.dumps(data)
        for i in range(data.count('${')):
            if '${' in data and '}' in data:
                stainx = data.index('${')
                endinx = data.index('}', stainx)
                orig = data[stainx:endinx + 1]
                valu = orig.strip('${}')
                funcname = valu[:valu.index('(')]
                funcpara = valu[valu.index('(') + 1:valu.index(')')]
                # 获取替换函数的值
                targetfunc = getattr(self, funcname, 'Unknown')
                if targetfunc != 'Unknown':
                    # 执行替换函数
                    target = targetfunc(*funcpara.split(',') if funcpara else '')
                    data = data.replace(orig, str(target))
                else:
                    data = data.replace(orig, targetfunc)

        return data

    def dealYaml(self, baseinfo, case):
        baseurl = self.conf.dealconfig('ENV', 'host')
        url = baseurl + baseinfo['path']
        allure.attach(url, f'接口地址:{url}')
        apiName = baseinfo['apiName']
        allure.attach(apiName, f'接口名称:{apiName}')
        method = baseinfo['method']
        allure.attach(method, f'请求方式:{method}')
        headers = baseinfo['headers']
        allure.attach(str(headers), f'接口请求头的信息:{headers}', allure.attachment_type.TEXT)
        cookies = {}
        if baseinfo.get('cookies'):
            # 处理cookies字符串为字典类型
            cookies = eval(baseinfo['cookies'])
            allure.attach(str(cookies), f'接口请求头的cookie信息:{cookies}', allure.attachment_type.TEXT)
        caseName = case.pop('caseName')
        allure.attach(caseName, f'测试用例名称:{caseName}')
        validation = case.pop('validation')
        extract = case.pop('extract', None)
        extractlist = case.pop('extractlist', None)
        resp, status_code = self.rqus.runMain(apiName=apiName, caseName=caseName, url=url, method=method,
                                              headers=headers,
                                              cookies=cookies, file=None, **case)
        allure.attach(str(case), f'请求参数:{case}', allure.attachment_type.TEXT)
        allure.attach(str(resp), f'接口实际响应信息:{resp}', allure.attachment_type.TEXT)

        if extract:
            self.extractinfo(extract, resp)
        if extractlist:
            self.extractinfo(extractlist, resp)

        # 断言
        self.assu.mainAssert(validation, resp, status_code)

    def extractinfo(self, extract, resp):
        # json 提取参数
        try:
            for i, j in extract.items():
                extrinfo = {i: '未提取到数据，返回值为空或 json 提取表达式错误'}
                if '$' in j:
                    extrajson = jsonpath.jsonpath(resp, j)
                    extrinfo = {i: extrajson} if len(extrajson) > 1 else {i: extrajson[0]}
                    logs.info(f'json提取到的参数:{extrinfo}')
                    self.wtYaml(extrinfo)
        except Exception as e:
            logs.error(f'接口返回值提取异常{e}')

    def clearextractYaml(self):
        with open(FILE_PATH['extract'], 'w') as f:
            f.truncate()

    def dealextractdata(self, data):
        if isinstance(data, str):
            data = json.loads(data)
        funcname = self.replYaml(data)

    @staticmethod
    def nowtime():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


if __name__ == '__main__':
    yu = YamlUtil()
    case = yu.rdYaml(FILE_PATH['extract'])
    # token = yu.dealextractYaml('token')
    token = yu.dealextractYaml('goodid', 0)
    # case = yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/userManger/addUser.yaml')
    print(token)
