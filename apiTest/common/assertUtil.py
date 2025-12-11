import allure
import operator
import jsonpath
from common.logUtil import logs
from common.dbUtil import ConnSql


class AssertUtil:

    def containsAssert(self, asserts, resp, status_code):
        # 断言状态标识 0:失败 1:成功
        flag = 1
        for asskey, assvalue in asserts.items():
            # 断言status_code
            if asskey == 'status_code' and assvalue != status_code:
                flag -= 1
                allure.attach(f'预期结果:{assvalue}， 实际结果:{status_code}', 'status_code断言失败',
                              allure.attachment_type.TEXT)
                logs.error(f'contains断言失败，接口返回code{status_code}不等于{assvalue}')
            else:
                resplist = jsonpath.jsonpath(resp, f'$..{asskey}')
                if isinstance(resplist[0], str):
                    resplist = ''.join(resplist)
                if assvalue in resplist:
                    allure.attach(f'预期结果:{assvalue}， 实际结果:{resplist}', '响应文本断言成功',
                                  allure.attachment_type.TEXT)
                    logs.info('contains文本成功')
                else:
                    flag -= 1
                    allure.attach(f'预期结果:{assvalue}， 实际结果:{resplist}', '响应文本断言失败',
                                  allure.attachment_type.TEXT)
                    logs.error(f'预期结果:{assvalue}，实际结果:{resplist}，响应文本断言失败')

        return flag

    def equalAssert(self, asserts, resp, status_code):
        flag = 1
        reslst = []

        # 处理实际结果数据结构，保持预期结果数据结构一致
        if isinstance(asserts, dict) and isinstance(resp, dict):
            for rest in resp:
                # 处理实际结果中多余的key，预期结果仅一个键值对
                if list(asserts.keys())[0] != rest:
                    reslst.append(rest)
            for rl in reslst:
                del resp[rl]

            # 判断预期结果字典是否与实际结果字典一致性
            equAss = operator.eq(asserts, resp)
            if equAss:
                allure.attach(f'预期结果:{asserts}， 实际结果:{resp}', '相等断言成功',
                              allure.attachment_type.TEXT)
                logs.info(f'相等断言成功:接口实际结果为{resp},等于预期结果{asserts}')
            else:
                flag -= 1
                allure.attach(f'预期结果:{asserts}， 实际结果:{resp}', '相等断言失败',
                              allure.attachment_type.TEXT)
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

    def mainAssert(self, expect, resp, status_code):
        flag = 1
        try:
            for ex in expect:
                for exkey, exvalue in ex.items():
                    if exkey == 'contains':
                        flag = self.containsAssert(exvalue, resp, status_code)
                    if exkey == 'equal':
                        self.equalAssert(exvalue, resp, status_code)
                    if exkey == 'db':
                        self.sqlAssert(exvalue)

            assert flag == 1
            logs.info('测试成功')
        except Exception as e:
            logs.error('测试失败')
            logs.error(f'异常信息:{e}')
            assert flag == 1
