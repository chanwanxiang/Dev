import os,sys,json,datetime,openpyxl

sys.path.append(r'D:\Coding-Always\Read-Search-Ask\【1】Python\测试\小滴课堂\Python接口自动化\apiTest')

from util.requestUtil import RequestUtil
from dbUtil.dbUtil import mysqlDB

filePath = r'D:\Coding-Always\Read-Search-Ask\【1】Python\测试\小滴课堂\Python接口自动化\apiTest\测试用例.xlsx'

class xsclassTestCase:

    # 根据项目加载全部测试用例 execl
    def loadallcasebyApp(self,app):
        print('loadallcasebyApp')
        wb = openpyxl.load_workbook(filePath)
        sheet = wb.worksheets[0]
        allcase = [x for x in list(sheet.values) if x[1] == app]

        listN = []
        dictN = {}

        for x in allcase:
            listdict = list(zip(list(sheet.values)[0],x))
            for x in listdict:
                dictN[x[0]] = x[1]
            listN.append(dictN)
            dictN = {}

        return listN

    # 根据项目加载全部测试用例 mysql
    # def loadallcasebyApp(self,app):
    #     print('loadallcasebyApp')
    #     mydb = mysqlDB()
    #     allcase = mydb.query("select * from `case` where app='%s'"%app)

    #     return allcase

    # 根据id找测试用例 execl
    def findcasebyid(self,caseid):
        print('findcasebyid')
        wb = openpyxl.load_workbook(filePath)
        sheet = wb.worksheets[0]
        singlecase = [x for x in list(sheet.values) if x[0] == caseid]
        
        dictN = {}
        listdict = list(zip(list(sheet.values)[0],singlecase[0]))
        # print(listdict)
        for x in listdict:
            dictN[x[0]] = x[1]

        return dictN

    # 根据id找测试用例 mysql
    def findcasebyid(self,id):
        print('findcasebyid')
        mydb = mysqlDB()
        sql = "select * from `case` where id=%d"%id
        onecase = mydb.query(sql,state='one')
        return onecase

    # 根据项目和key加载配置 execl
    # def loadconfigbyAppandKey(self,app,key):
    #     print('loadconfigbyAppandKey')
    #     wb = openpyxl.load_workbook(filePath)
    #     sheet = wb.worksheets[1]
    #     singleconfig = [x[3] for x in list(sheet.values) if x[1] == app and x[2] == key][0]
    #     return singleconfig

    # 根据项目和key加载配置 mysql
    def loadconfigbyAppandKey(self,app,key):
        print('loadconfigbyAppandKey')
        mydb = mysqlDB()
        sql = "select * from `config` where app='{0}' and dict_key='{1}'".format(app,key)
        result = mydb.query(sql,state='one')
        return result['dict_value']

    # 根据测试用例id更新响应内容和测试内容 execl
    # def updataResulebyCaseid(self,response,isPass,msg,caseid):
    #     print('updataResulebyCaseid')
    #     wb = openpyxl.load_workbook(filePath)
    #     sheet = wb.worksheets[0]
    #     colu = sheet['A']
    #     for x in colu:
    #         if x.value == caseid:
    #             rows = x.row
    #     currenttime = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    #     if isPass:
    #         sheet.cell(rows,14,isPass)
    #         sheet.cell(rows,15,msg)
    #         sheet.cell(rows,16,currenttime)
    #         sheet.cell(rows,17,str(response))
    #     else:
    #         sheet.cell(rows,14,isPass)

    #     wb.save('xs 更新后的数据.xlsx')

    # 根据测试用例id更新响应内容和测试内容 mysql
    def updataResulebyCaseid(self,response,isPass,msg,caseid):
        print('updataResulebyCaseid')
        currenttime = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
        if isPass:
            sql = "update `case` set response='{0}',pass='{1}',msg='{2}',update_time='{3}' where id={4}".format('',isPass,msg,currenttime,caseid)
        else:
            sql = "update `case` set response=\"{0}\",pass='{1}',msg='{2}',update_time='{3}' where id={4}".format(str(response),isPass,msg,currenttime,caseid)

        print(sql)
        mydb = mysqlDB()
        rows = mydb.execute(sql)
        return rows

    # 执行全部用例
    def runAllCase(self,app):
        print('runAllCase')

        # 获取接口域名
        apiHostobj = self.loadconfigbyAppandKey(app,'host')

        # 获取全部用例
        allcase = self.loadallcasebyApp(app)

        for case in allcase:
            # print(case)
            # 判断用例是否需要运行
            if case['run'] == 'yes':
                try:
                    # 执行用例
                    response = self.runCase(case,apiHostobj)

                    # 断言判断
                    assertMsg = self.assertResponse(case,response)

                    # 更新结果存储数据库
                    rlt = self.updataResulebyCaseid(response,assertMsg['isPass'],assertMsg['msg'],case['id'])
                    print('已经更新结果')

                except Exception as e:
                    print('用例id=%s,标题:%s,执行报错:%s'%(case['id'],case['title'],e))
    # 执行单个用例
    def runCase(self,case,apiHostobj):
        print('runCase')
        headers = json.loads(case['headers'])
        body = json.loads(case['request_body'])
        method = case['method']
        reqUrl = apiHostobj + case['url']

        # 是否需要前置条件
        if case['pre_case_id'] > -1:
            print('前置条件处理')
            preCaseid = case['pre_case_id']
            preCase = self.findcasebyid(preCaseid)
            
            # 递归调用
            preResponse = self.runCase(preCase,apiHostobj)

            # 前置条件断言
            preAssertMsg = self.assertResponse(preCase,preResponse)
            
            if not preAssertMsg['isPass']:

                # 前置条件不通过直接返回
                preResponse['msg'] = '前置条件没有通过,'+ preResponse['msg']
                return preResponse

            # 判断当前case需要的前置条件哪个字段
            preFields = json.loads(case['pre_fields'])
            for preFiled in preFields:
                if preFiled['scope'] == 'header':
                    # 遍历headers,替换对应的字段值,寻找同名字段
                    for header in headers:
                        filedName = preFiled['field']
                        if header == filedName:
                            filedValue = preResponse['data'][filedName]
                            headers[filedName] = filedValue
            
                elif preFiled['scope'] == 'body':
                    print('替换body')

        # 发起请求
        req = RequestUtil()
        response = req.request(reqUrl,method,headers=headers,params=body)
        print(response)
        return response

    # 断言响应内容,更新用例执行情况
    def assertResponse(self,case,response):
        print('assertResponse')

        assertType = case['assert_type']
        expectResult = case['expect_result']

        isPass = False 

        # 判断业务状态码
        if assertType == 'code':
            responseCode = response['code']
            if int(expectResult) == responseCode:
                isPass = True
                print('测试用例通过')
            else:
                print('测试用例没有通过')
                isPass = False
        
        elif assertType == 'data_json_array':
            dataAaary = response['data']
            if dataAaary is not None and isinstance(dataAaary,list) and len(dataAaary) > int(expectResult):
                isPass = True
                print('测试用例通过')
            else:
                print('测试用例没有通过')
                isPass = False

        elif assertType == 'data_json':
            data = response['data']
            if data is not None and isinstance(data,dict) and len(data) > int(case['expect_result']):
                isPass = True
                print('测试用例通过')
            else:
                print('测试用例没有通过')
                isPass = False

        msg = '模块:%s,标题:%s,断言类型:%s,响应:%s'%(case['module'],case['title'],assertType,response['msg'])
        assertMsg = {'isPass':isPass,'msg':msg}
        return assertMsg

    # 发送邮件
    def sendTestReport(self,app):
        print('sendTestReport')

if __name__ == "__main__":
    print('main')
    xs = xsclassTestCase()
    # print(xs.loadallcasebyApp('小滴课堂'))
    # print(xs.loadconfigbyAppandKey('小滴课堂','host'))
    # print(xs.updataResulebyCaseid('12341\12\12\12',False,'1234',10))
    # print(xs.findcasebyid(6))
    # case6 = {'id': 6, 'app': '小滴课堂', 'module': 'user', 'title': '用户个人信息', 'method': 'get', 'url': '/pub/api/v1/web/user_info', 'run': 'yes', 'headers': '{"token":"$token$"}', 'pre_case_id': 1, 'pre_fields': '[{"field":"token","scope":"header"}]', 'request_body': '{}', 'expect_result': None, 'assert_type': 'data_json', 'pass': 'True', 'msg': '模块:user,标题:用户个人信息,断言类型是:data_json,响应msg:None', 'update_time': datetime.datetime(2020, 7, 1, 18, 53, 29), 'response': ''}
    # xs.runCase(case6,'https://api.xdclass.net')
    xs.runAllCase('小滴课堂')