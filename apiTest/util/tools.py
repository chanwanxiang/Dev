from http import client
from xml.etree.ElementPath import prepare_self
import faker, radar
from numpy import issubdtype
import openpyxl, random
from datetime import datetime
from faker import Faker
from prestool.Tool import Tool

prest = Tool()
faker = Faker(locale='zh-CN')

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

# 基础信息
name = faker.name()
phone = faker.phone_number()
address = faker.address()
ssn = faker.ssn()
company = faker.company()
creditCard = faker.credit_card_number()
job = faker.job()
email = faker.email()

# 地理信息
city = faker.city_suffix()
country = faker.country()
# countryCode = faker.country_code()
district = faker.district()
# Gps = faker.geo_coordinate()
province = faker.province()

# 时间信息
randomdate = faker.date()
# betweendate = faker.date_between('today', '-30d')
futuredate = faker.future_date()
futuredatetime = faker.future_datetime()
randomYear = faker.year()


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
    print(name, phone, address, ssn, company, creditCard, job, email, city, country, district, province, randomdate, futuredate, futuredatetime, randomYear)
    # # 添加表头
    # # sheet.append(('姓名', '手机号', '客户编号', '管户客户经理', '报名码', '二级分行', '支行号', '支行名称', '网点号', '网点名称', '截止2022年5月31日年日均资产', '2022年5月月日均资产'))
    # sheet.title = '测试数据'
    # for i in range(201):
    #     name = cret.random_name()
    #     phone = cret.random_phone()
    #     idNo = cret.random_ssn()
    #     clientNo = idNo[:15]
    #     randCode = cret.random_string(8)
    #     inviCode = generateCode(6)
    #     baseAum = round(random.uniform(0, 100000), 2)
    #     monthAum = round(random.uniform(0, 70000), 2)
    #     sheet.append((name, phone, clientNo,'', inviCode,'', '', '', '', '',  baseAum, monthAum)
    # wb.save('info.xlsx')
