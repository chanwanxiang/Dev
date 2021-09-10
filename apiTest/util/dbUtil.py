vtmsaas.yuuwei.com/qr/a?key=sdfj3185fdftg53&preOrderNumber=20210722135510562001&domain=https://signtest.yuuwei.com

import pymysql

conn = pymysql.connect("127.0.0.1", "root", "xdclass.net", "xd_api_test_demo")
# 使用 cursor 方法获取操作游标，得到一个可以执行sql语句，并且操作结果作为字典返回的游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

try:
    # 使用 execute 方法执行sql查询
    cursor.execute("select * from `case`")
    data = cursor.fetchall()
    print(data)
except Exception as e:
    print(e)
finally:
    # 关闭数据库连接
    conn.close()
