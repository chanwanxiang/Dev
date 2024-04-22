import allure

from common.logUtil import logs
import jsonpath


class AssertUtil:
    '''
    接口断言模式封装
    1. 包含字符串
    2. 结果相等或者不等断言
    3. 断言接口返回值中的任意一值
    4. 数据库断言
    5. 通过其他接口辅助
    '''

    def containsAssert(self, asserts, resp, statusCode):
        # 断言状态标识 0:失败 1:成功
        flag = 1
        for asskey, assvalue in asserts.items():
            print(asskey, assvalue, type(assvalue))
            if asskey == 'statusCode' and assvalue != statusCode:
                flag -= 1
                allure.attach(f'预期结果:{assvalue}， 实际结果:{resp}，响应断言结果失败')
                logs.error(f'contains断言失败，接口返回码{statusCode}不等于{assvalue}')
            else:
                resplist = jsonpath.jsonpath(resp, f'$...{asskey}')
                print(f'resp的值是{resplist}')
                if isinstance(resplist[0], str):
                    resplist = ''.join(resplist)
                if assvalue in resplist:
                    print('断言成功')
                else:
                    flag -= 1
                    logs.error(f'预期结果:{assvalue}，实际结果:{resplist}，响应文本断言失败')

        return flag

    def equalAssert(self, asserts, resp, statusCode):
        if isinstance(asserts, dict) and isinstance(resp, dict):
            pass

    def notEqualAssert(self, asserts, resp):
        pass

    def assertMain(self, expect, resp, statusCode):
        flag = 1
        try:
            for ex in expect:
                for exkey, exvalue in ex.items():
                    if exkey == 'contains':
                        flag = self.containsAssert(exvalue, resp, statusCode)
                    if exkey == 'equal':
                        self.equalAssert(exvalue, resp, statusCode)

            assert  flag == 1
            logs.info('测试成功')
        except Exception as e:
            logs.error('测试失败')
            logs.error(f'异常信息:{e}')
            assert flag == 1


if __name__ == '__main__':
    import jsonpath
    from conf.setting import FILE_PATH
    from common.yamlUtil import YamlUtil

    yu = YamlUtil()
    case = yu.rdYaml(FILE_PATH['testcase'])[0]['testCase'][0]['validation']
    print(case)
    au = AssertUtil()
    resp = {'error_code': None, 'msg': '登录成功', 'msg_code': 200, 'orgId': '6140913758128971280',
            'token': '2eA527a8EcF2Ff9E01D00DbED62F7', 'userId': '8345231644817030159'}
    for i in case:
        for k, v in i.items():
            au.containsAssert(v, resp, 200)
