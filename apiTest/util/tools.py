from http import client
import faker
import openpyxl, random
from datetime import datetime
from faker import Faker
from prestool.Tool import Tool

cret = Tool()
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


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheet = wb.worksheets[0]
    # 添加表头
    # sheet.append(('姓名', '手机号', '客户编号', '管户客户经理', '报名码', '二级分行', '支行号', '支行名称', '网点号', '网点名称', '截止2022年5月31日年日均资产', '2022年5月月日均资产'))
    sheet.title = '测试数据'
    # for i in range(201):
    #     name = cret.random_name()
    #     phone = cret.random_phone()
    #     idNo = cret.random_ssn()
    #     clientNo = idNo[:15]
    #     randCode = cret.random_string(8)
    #     inviCode = generateCode(6)
    #     baseAum = round(random.uniform(0, 100000), 2)
    #     monthAum = round(random.uniform(0, 70000), 2)
    #     sheet.append((name, phone, clientNo,'', inviCode,'', '', '', '', '',  baseAum, monthAum))

    #   `org_id` bigint(22) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
    #   `data_dt` date DEFAULT NULL COMMENT '数据时间（日更新）',
    #   `int_org_num_branch` varchar(32) DEFAULT NULL COMMENT '二级分行机构编码',
    #   `int_org_num_branch_nm` varchar(64) DEFAULT NULL COMMENT '二级分行名称',
    #   `int_org_num_subbranch` varchar(32) DEFAULT NULL COMMENT '一级支行机构编码',
    #   `int_org_num_subbranch_nm` varchar(64) DEFAULT NULL COMMENT '一级支行名称',
    #   `int_org_num` varchar(32) DEFAULT NULL COMMENT '网点机构编码',
    #   `int_org_num_nm` varchar(64) DEFAULT NULL COMMENT '网点机构名称',
    # mydb.execute(f"INSERT INTO `biz_int_org_num_info` SET `data_dt`='2022-07-05', `int_org_num_branch`=1000", )
    for i in range(100):
        bankName = faker.province() + faker.city()
        data_dt = '2022-07-05' # 0240100001

        int_org_num_branch = '2002401' + str(i).zfill(5)
        int_org_num_branch_nm = bankName + '分行'
        int_org_num_subbranch = '1002401' + str(i).zfill(5)
        int_org_num_subbranch_nm = bankName + '支行'
        int_org_num = '02401' + str(i).zfill(5)
        int_org_num_nm = bankName + '机构'

        sheet.append((data_dt, int_org_num_branch, int_org_num_branch_nm, int_org_num_subbranch, int_org_num_subbranch_nm, int_org_num, int_org_num_nm))
        
    wb.save('info.xlsx')     
