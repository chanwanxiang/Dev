import openpyxl
from datetime import datetime
from prestool.Tool import Tool

cret = Tool()

def createOrderNum():
    return datetime.now().strftime('%Y%m%d%H%M%S') + '0'.zfill(2)


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
    sheet.append(('姓名', '号码', '身份证号'))
    sheet.title = 'info'
    for i in range(20):
        name = cret.random_name()
        phone = cret.random_phone()
        id = cret.random_ssn()
        sheet.append((name,phone, id))
    wb.save('info.xlsx')     
