import json
import os
import sys
from datetime import datetime

# 追加导包路径
#sys.path.insert(0, r'.\.\apiTest')
sys.path.append('/Users/ivi/Dev/apiTest')

from dbUtil.dbUtil import mysqlDB
from util.jarUtil import *
from util.requestUtil import RequestUtil
from util.tools import *


class xsclassTestCase:

    # 根据项目加载全部测试用例 mysql
    def loadallcasebyApp(self,app):
        mydb = mysqlDB()
        allcase = mydb.query("select * from `case` where app='%s'"%app)

        return allcase

    # 根据id找测试用例 mysql
    def findcasebyid(self, id):
        mydb = mysqlDB()
        sql = "select * from `case` where id=%d" % id
        onecase = mydb.query(sql, state='one')
        return onecase

    # 根据项目和key加载配置 mysql
    def loadconfigbyAppandKey(self, app, key):
        mydb = mysqlDB()
        sql = "select * from `config` where app='{0}' and dict_key='{1}'".format(
            app, key)
        result = mydb.query(sql, state='one')
        return result['dict_value']

    # 根据测试用例id更新响应内容和测试内容 mysql
    def updataResulebyCaseid(self, response, isPass, msg, caseid):
        currenttime = datetime.now().strftime('%y-%m-%d %H:%M:%S')
        if isPass:
            sql = "update `case` set response='{0}',pass='{1}',msg='{2}',update_time='{3}' where id={4}".format(
                '', isPass, msg, currenttime, caseid)
        else:
            sql = "update `case` set response=\"{0}\",pass='{1}',msg='{2}',update_time='{3}' where id={4}".format(
                str(response), isPass, msg, currenttime, caseid)

        mydb = mysqlDB()
        rows = mydb.execute(sql)
        return rows

    # 执行全部用例
    def runAllCase(self, app):

        # 获取接口域名
        apiHostobj = self.loadconfigbyAppandKey(app, 'host')

        # 获取全部用例
        allcase = self.loadallcasebyApp(app)

        for case in allcase:
            # print(case)
            # 判断用例是否需要运行
            if case['run'] == 'yes':
                try:
                    # 执行用例
                    response = self.runCase(case, apiHostobj)

                    # 断言判断
                    assertMsg = self.assertResponse(case, response)

                    # 更新结果存储数据库
                    rlt = self.updataResulebyCaseid(
                        response, assertMsg['isPass'], assertMsg['msg'], case['id'])

                except Exception as e:
                    print('用例id=%s,标题:%s,执行报错:%s' %
                          (case['id'], case['title'], e))
    # 执行单个用例
    def runCase(self, case, apiHostobj):
        rsa = RsaSign()
        headers = json.loads(case['headers'])
        
        if case['app'] == '团餐机二期':
            body = json.loads(case['request_body'])
            if 'clientTransNo' in body['bizContent']:
                body['bizContent']['clientTransNo'] = createOrderNum()
            encrytedbody = rsa.encrypted(json.dumps(body))
            body = json.loads('{"request":"' + encrytedbody + '"}')
        else:
            body = json.loads(case['request_body'])
        method = case['method']
        reqUrl = apiHostobj + case['url']

        # 是否需要前置条件
        if case['pre_case_id'] > -1:
            preCaseid = case['pre_case_id']
            preCase = self.findcasebyid(preCaseid)

            # 递归调用
            preResponse = self.runCase(preCase, apiHostobj)

            # 前置条件断言
            preAssertMsg = self.assertResponse(preCase, preResponse)

            if not preAssertMsg['isPass']:

                # 前置条件不通过直接返回
                preResponse['msg'] = '前置条件没有通过,' + preResponse['msg']
                return preResponse

            # 判断当前case需要的前置条件哪个字段
            preFields = json.loads(case['pre_fields'])
            for preFiled in preFields:
                if preFiled['scope'] == 'header':
                    # 遍历headers,替换对应的字段值,寻找同名字段
                    for header in headers:
                        filedName = preFiled['field']
                        if header in ['YW-MAC-TOKEN', 'token'] :
                            filedValue = preResponse['response'][filedName]
                            headers['YW-MAC-TOKEN'] = filedValue
                            
                elif preFiled['scope'] == 'body':
                    print('替换body')
            
        # 发起请求
        req = RequestUtil()
        response = req.request(reqUrl, method, headers=headers, params=body)
        if case['app'] == '团餐机二期':
            response = json.loads(rsa.decrypted(response['response']))
        info = '模块:%s,标题:%s,响应:%s' % (
                case['module'], case['title'], response)
        print('-' * 10)
        print(info)
        return response

    # 断言响应内容,更新用例执行情况
    def assertResponse(self, case, response):
        assertType = case['assert_type']
        expectResult = case['expect_result']

        isPass = False

        # 判断业务状态码
        if assertType == 'code':
            responseCode = response['code']
            if int(expectResult) == responseCode:
                isPass = True
            else:
                isPass = False

        elif assertType == 'data_json_array':
            dataAaary = response['data']
            if dataAaary is not None and isinstance(dataAaary, list) and len(dataAaary) > int(expectResult):
                isPass = True
            else:
                isPass = False

        elif assertType == 'data_json':
            data = response['data']
            if data is not None and isinstance(data, dict) and len(data) > int(case['expect_result']):
                isPass = True
            else:
                isPass = False

        msg = '模块:%s,标题:%s,断言类型:%s,响应:%s' % (
            case['module'], case['title'], assertType, response['msg'])
        assertMsg = {'isPass': isPass, 'msg': msg}
        return assertMsg

    # 发送邮件
    def sendTestReport(self, app):
        print('sendTestReport') 


if __name__ == "__main__":
    xs = xsclassTestCase()

    # print(xs.loadallcasebyApp('小滴课堂'))
    # print(xs.loadconfigbyAppandKey('小滴课堂','host'))
    # print(xs.findcasebyid(6))
    # case6 = {'id': 6, 'app': '小滴课堂', 'module': 'user', 'title': '用户个人信息', 'method': 'get', 'url': '/pub/api/v1/web/user_info', 'run': 'yes', 'headers': '{"token":"$token$"}', 'pre_case_id': 1, 'pre_fields': '[{"field":"token","scope":"header"}]', 'request_body': '{}', 'expect_result': None, 'assert_type': 'data_json', 'pass': 'True', 'msg': '模块:user,标题:用户个人信息,断言类型是:data_json,响应msg:None', 'update_time': datetime.datetime(2020, 7, 1, 18, 53, 29), 'response': ''}
    # xs.runCase(case6,'https://api.xdclass.net')
    # xs.runAllCase('团餐机二期')
    
    xs.runAllCase('团餐机二期')
    