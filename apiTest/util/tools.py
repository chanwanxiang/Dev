import code
import openpyxl, random
from datetime import datetime
from prestool.Tool import Tool

cret = Tool()

def createOrderNum():
    return datetime.now().strftime('%Y%m%d%H%M%S') + '0'.zfill(2)

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
    sheet.append(('姓名', '号码', '身份证号', '邀请码'))
    sheet.title = 'info'
    for i in range(20):
        name = cret.random_name()
        phone = cret.random_phone()
        idNo = cret.random_ssn()
        inviCode = generateCode(4)
        sheet.append((name,phone, idNo, inviCode))
    wb.save('info.xlsx')     
