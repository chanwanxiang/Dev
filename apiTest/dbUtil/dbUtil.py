# coding:utf-8

import pymysql
import openpyxl
from pprint import pprint
from datetime import datetime
from prestool.Tool import Tool
from warnings import filterwarnings
from configparser import ConfigParser

# 忽略mysql告警信息
filterwarnings('ignore', category=pymysql.Warning)

class mysqlDB:

    def __init__(self):
        # 建立数据库连接
        # self.conn = pymysql.connect(
        #     host='127.0.0.1', port=3333, user='root', password='123456', database='test')
        # self.conn = pymysql.connect(
        #     host='192.168.50.98', port=13306, user='root', password='123456', database='posOps')
        # self.conn = pymysql.connect(
        #     host='47.97.192.122', port=3306, user='root', password='yw123456', database='payroll-service')
        self.conn = pymysql.connect(
            host=dbinfo['host'], port=int(dbinfo['port']), user=dbinfo['user'], password=dbinfo['password'], database=dbinfo['database'])
        # 使用cursor方法获取操作游标,得到一个可以执行的sql语句,并且操作结果作为字典返回的游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标以及连接
        self.cur.close()
        self.conn.close()

    def query(self, sql, state='all'):
        self.cur.execute(sql)
        if state == 'all':
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        return data

    def execute(self, sql):
        # 更新删除新增
        try:
            # 使用execute操作数据库,执行sql并返回影响行数
            rows = self.cur.execute(sql)
            # 提交事务,不然无法保存新建或者修改数据
            self.conn.commit()
            return rows
        except Exception as e:
            print('数据库异常{0}'.format(e))
            self.conn.rollback()


if __name__ == "__main__":
    conf = ConfigParser()
    with open(r'D:/Dev/apiTest/util/dbpara.ini', 'r') as f:
        conf.read_file(f)
        dbinfo = dict(conf.items('localdb'))

    mydb = mysqlDB()

    # # 使用excel导入数据库
    # filePath = './入库.xlsx'
    # wb = openpyxl.load_workbook(filePath)
    # sheet = wb.worksheets[0]
    # for i in list(sheet.values)[1:]:
    #     mydb.execute(f"insert into `stu` set `id`={i[0]}, `stuName`='{i[1]}'")
    
    # 查询
    # print(mydb.query('select * from `yw_question`'))

    # 添加 必须使用双眼号,单眼号出错
    # answ = mydb.execute("insert into `case`(app) values('xls')")
    # answ = mydb.execute(f"insert into `yw_question` SET type_id = {str(randint(105, 120))}, question = '哈哈'")
    
    # pos巡检数据插入
    # for i in range(300001, 600001):
    #     cardname = tl.random_name()
    #     # TODO:Python在执行sql语句时,如果传入的参数是str类型应加上引号
    #     answ = mydb.execute(f"insert into `yw_order` SET `id`={i}, `status`={str(randint(0, 6))}, `type`=111, `establish_type`='机构创建', `start_time`='2021-12-31 08:00:00', `plan_end_time`='2021-12-24 08:00:00', `end_time`='2021-12-31 08:00:00', `urgency`={str(randint(0,1))}, `commerical_id`='88df536826f3dd2014567c67794cfe20', `user_name`={tl.random_phone()}, \
    #         `del_flag`='0', `create_time`='2021-12-20 08:00:00', `update_time`='2022-02-22 08:00:00', `create_dept_id`=2, `license_name`='杭州宇为科技有限公司', `license_num`='91330108MA27WYLH7Q', `license_avail_date`='2036-02-28', \
    #         `idcard_name`='{cardname}', `idcard_num`={tl.random_ssn()}, `idcard_avail_date`='2036-06-14', `idcard_type`='1', `commerical_title`='线上小店', `commerical_number`='CM0123456789110', `org_id`='57', `org_name`='测试机构', `two_branch`='贵阳分行', `two_branch_id`=2, `recstat`='0', `network`='IC0240200000', `inspect_comment`='任务成功', `inspector`='大白', `count_exception`=1, `inspect_time`='2021-12-31 08:00:00'")
    #     atta = mydb.execute(f"insert into `yw_order_attach` SET `id`={i}, `phone1`='5ea67d2a-8860-4943-b8ce-738c7e52d1d1', `phone2`='24a84e40-c1c9-4b8b-accf-1233e40638ef', `phone3`='94110294-851b-43de-80f8-2d96e4006657', `phone4`='2df0f1aa-c569-4e72-ab8a-76a8d20bfda6', `phone5`='d1122dcc-ea52-43b5-aa10-420ec9fabbb2', `phone6`='5e8295f7-8962-40ff-bdac-b4ae945780f4', `video1`='8e90359e-0412-4c19-a826-3ca69cb86391', `license_pic`='31e10435-9fc6-41bb-abe2-de32cfe3ebe4',\
    #         `idcard_person`='a46578321c570446cc0932b4704f3060', `idcard_emblem`='ba286fd359836bd2c2b65fd88225380a', `local_scene_tables`='9dff38f5d9701eaed076db57142c59a1', `custom_e_sign`='9dff38f5d9701eaed076db57142c59a1'")
    #     print(cardname)

    # 代发项目数据插入
    # for i in range(1, 1001):
    #     name = tl.random_name()
    #     idcard = tl.random_ssn()
    #     mobile = tl.random_phone()
    #     time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     openid, userid, userno = 'openid' + str(i+1), 30+i, 'cs' + str(i+1)
    #     step = mydb.execute(f"insert into `yw_users` SET `status`=1,`openid`='{openid}',`userno`='{userno}', `name`='{name}', `idcard`='{idcard}', `mobile`='{mobile}', `signup_at`='{time}', `is_in_white_list`=1, `quarter_num`=2")
    #     afte = mydb.execute(f"insert into `yw_user_signup` SET `mobile`='{mobile}', `signup_at`='{time}', `quarter_num`=2, user_id={userid}, `userno`='{userno}'") 
    
    # dt = mydb.query('SELECT * FROM `yw_users`', state='one')
    # print(dt)
