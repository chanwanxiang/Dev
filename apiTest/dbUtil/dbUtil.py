import pymysql

# conn = pymysql.connect(host='127.0.0.1',port=3333,user='root',password='1234',database='xdcls')

# # 操作cursor方法获取游标,得到一个可以执行的sql语句,并且将操作结果作为字典返回
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# try:
#     # 使用execute方法执行sql查询
#     cursor.execute('select * from `case`')
#     # 使用fetchall查询所有 fetchone查询单条
#     date = cursor.fetchall()
#     # date = cursor.fetchone()

#     print(date)

# except Exception as e:
#     print(e)

# finally:
#     conn.close()

from warnings import filterwarnings

# 忽略mysql告警信息
filterwarnings('ignore', category=pymysql.Warning)


class mysqlDB:

    def __init__(self):
        # 建立数据库连接
        self.conn = pymysql.connect(
            host='127.0.0.1', port=3333, user='root', password='1234', database='xdcls')
        # 使用cursor方法获取操作游标,得到一个可以执行的sql语句,并且操作结果作为字典返回的游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
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
            # 使用execute操作数据库
            rows = self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except Exception as e:
            print('数据库异常{0}'.format(e))
            self.conn.rollback()


if __name__ == "__main__":
    mydb = mysqlDB()
    # 查询
    r = mydb.query('select * from `case`')
    # 添加 必须使用双眼号,单眼号出错
    # r = mydb.execute("insert into `case`(app) values('xls')")
    print(r)
