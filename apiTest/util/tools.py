from http import client
from numpy import may_share_memory
import openpyxl, random
from datetime import datetime
from prestool.Tool import Tool

cret = Tool()

def createOrderNum():
    return datetime.now().strftime('%Y%m%d%H%M%S') + '0'.zfill(1)

def generateCode(codeleng):
    # 生成指定长度的验证码
    code = ''
    char = '123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ends = len(char) - 1
    for i in range(codeleng):
        j = random.randint(0, ends)
        code +=  char[j]
    
    return code


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
    sheet.append(('姓名', '手机号', '客户编号', '管户客户经理', '报名码', '二级分行', '支行号', '支行名称', '网点号', '网点名称', '截止2022年5月31日年日均资产', '2022年5月月日均资产'))
    sheet.title = '测试数据'
    for i in range(201):
        name = cret.random_name()
        phone = cret.random_phone()
        idNo = cret.random_ssn()
        clientNo = idNo[:15]
        randCode = cret.random_string(8)
        inviCode = generateCode(6)
        aum = round(random.uniform(0, 100000), 2)
        aumMay = round(random.uniform(0, 70000), 2)
        sheet.append((name, phone, clientNo,'', inviCode,'', '', '', '', '',  aum,aumMay))
    wb.save('info.xlsx')     
