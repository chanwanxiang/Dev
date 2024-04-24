import allure
import operator
import jsonpath
from common.logUtil import logs
from common.dbUtil import ConnSql


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
            if asskey == 'statusCode' and assvalue != statusCode:
                flag -= 1
                allure.attach(f'预期结果:{assvalue}， 实际结果:{statusCode}', '响应code断言结果: 失败',
                              allure.attachment_type.TEXT)
                logs.error(f'contains断言失败，接口返回code{statusCode}不等于{assvalue}')
            else:
                resplist = jsonpath.jsonpath(resp, f'$...{asskey}')
                if isinstance(resplist[0], str):
                    resplist = ''.join(resplist)
                if assvalue in resplist:
                    logs.info('contains文本断言成功')
                else:
                    flag -= 1
                    allure.attach(f'预期结果:{assvalue}， 实际结果:{resplist}', '响应文本断言结果失败',
                                  allure.attachment_type.TEXT)
                    logs.error(f'预期结果:{assvalue}，实际结果:{resplist}，响应文本断言失败')

        return flag

    def equalAssert(self, asserts, resp, statusCode):
        flag = 1
        reslst = []

        # 处理实际结果数据结构，保持预期结果数据结构一致
        if isinstance(asserts, dict) and isinstance(resp, dict):
            for rest in resp:
                if list(asserts.keys())[0] != rest:
                    reslst.append(rest)
            for rl in reslst:
                del resp[rl]

            # 判断预期结果字典是否与实际结果字典一致性
            equAss = operator.eq(asserts, resp)
            if equAss:
                logs.info(f'相等断言成功:接口实际结果为{resp},等于预期结果{asserts}')
            else:
                flag -= 1
                logs.info(f'相等断言失败:接口实际结果为{resp},不等预期结果{asserts}')
        else:
            raise TypeError('equal 断言失败-类型错误，预期结果以及接口响应必须为 dict 类')

        return flag

    def sqlAssert(self, expectSql):
        flag = 1
        conn = ConnSql()
        dbValue = conn.query(expectSql)
        if dbValue:
            logs.info('db断言成功')
        else:
            flag -= 1
            logs.error('db断言失败，请检查数据库是否存在该数据')

        return flag

    def assertMain(self, expect, resp, statusCode):
        flag = 1
        try:
            for ex in expect:
                for exkey, exvalue in ex.items():
                    if exkey == 'contains':
                        flag = self.containsAssert(exvalue, resp, statusCode)
                    if exkey == 'equal':
                        self.equalAssert(exvalue, resp, statusCode)
                    if exkey == 'db':
                        self.sqlAssert(exvalue)

            assert flag == 1
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
            print(k, v)
            au.assertMain(v, resp, 200)
