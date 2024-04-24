import pymysql
from common.logUtil import logs
from conf.confUtil import ConfigUtil

configUtil = ConfigUtil()


class ConnSql:
    def __init__(self):
        sqlConfig = {
            'host': configUtil.dealconfig('MYSQL', 'host'),
            'port': int(configUtil.dealconfig('MYSQL', 'port')),
            'user': configUtil.dealconfig('MYSQL', 'user'),
            'password': configUtil.dealconfig('MYSQL', 'password'),
            'database': configUtil.dealconfig('MYSQL', 'database')
        }
        self.conn = pymysql.connect(**sqlConfig, charset='utf8mb4')
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        logs.info('成功连接到数据库')

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


if __name__ == '__main__':
    conn = ConnSql()