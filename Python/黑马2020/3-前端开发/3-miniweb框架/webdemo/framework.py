# web框架专门处理动态资源请求

import sys
import json
import time
import pymysql
import os.path as op

# TODO: 路由列表手动添加路由 Django路由
routelist = [
    # ('/index.html', index),
    # ('/center.html', center),
]

# TODO: 带参数装饰器添加路由 Flask路由
def route(path):
    # 装饰器
    def decorator(func):
        # 当执行装饰器的时候就需要把路由添加到路由列表里
        # 装饰函数时候只需添加一次路由
        routelist.append((path, func))

        def inner():
            result = func()
            return result

        return inner
    # 返回一装饰器
    return decorator

# 首页数据
@route('/index.html')
def index():
    # 状态信息
    status = '200 OK'
    # 响应头
    responseheader = [('Server', 'PWS/1.1')]
    # 1. 打开指定模板文件,读取模板文件中的数据
    with open(file=op.join(sys.path[0], 'template/index.html'), mode='r', encoding='utf-8') as f:
        filedata = f.read()
    # 2. 查询数据库,模板里面的模板变量{%content%}替换成以后从数据库里查询的数据
    conn = pymysql.connect(
        host='localhost',
        port=3333,
        user='root',
        password='123456',
        database='stockinfo',
        charset='utf8'
    )
    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = 'SELECT * FROM info;'
    # 执行sql
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    print(result)
    # 关闭游标
    cursor.close()
    # 遍历数据,完成数据tr标签封装
    data = ''
    for row in result:
        data += '''<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
               </tr>''' % row

    responsebody = filedata.replace('{%content%}', data)

    # 返回的是元祖
    return status, responseheader, responsebody

# 个人中心数据接口
@route('/centerdata.html')
def centerdata():
    # 状态信息
    status = '200 OK'
    # 响应头
    responseheader = [
        ('Server', 'PWS/1.1'),
        # 指定编码格式
        ('Content-Type', 'text/html;charset=UTF-8')
    ]
    # 从数据库获取数据,再转json数据
    # 创建连接对象
    conn = pymysql.connect(
        host = 'localhost',
        port = 3333,
        user = 'root',
        password = '123456',
        database = 'stockinfo',
        charset = 'utf8'
    )
    # 获取游标
    cursor = conn.cursor()
    # 准备sql
    sql = '''SELECT i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info
            FROM info i 
            inner join focus f
            on i.id = f.info_id;
        '''
    # 执行sql
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    print(result)
    # 把元祖转成列表字典
    centerlist = [{
        'code':row[0],
        'short':row[1],
        'chg':row[2],
        'turnover':row[3],
        'price':str(row[4]),
        'highs':str(row[5]),
        'note_info':row[6]
    } for row in result]
    print(centerlist)
    # 把列表转成json字符串
    # ensure_ascii=False,表示在控制台显示中文
    jsonStr = json.dumps(centerlist,ensure_ascii=False)
    print(jsonStr)
    print(type(jsonStr))
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return status, responseheader, jsonStr

# 个人中心数据
@route('/center.html')
def center():
    # 状态信息
    status = '200 OK'
    # 响应头
    responseheader = [('Server', 'PWS/1.1')]
    # 1. 打开指定模板文件,读取模板文件中的数据
    with open(file=op.join(sys.path[0], 'template/center.html'), mode='r', encoding='utf-8') as f:
        filedata = f.read()
    # 2. 查询数据库,模板里面的模板变量{%content%}替换成以后从数据库里查询的数据
    # web框架处理后的数据
    # 获取当前时间
    responsebody = filedata.replace('{%content%}', '')
    # 返回的是元祖
    return status, responseheader, responsebody

# 404数据
def notFound():
    # 状态信息
    status = '404 NOT FOUND'
    # 响应头
    responseheader = [('Server', 'PWS/1.1')]
    # web框架处理后的数据
    data = '404 NOT FOUND'
    # 返回的是元祖
    return status, responseheader, data


def handleRuquest(env):
    # 获取动态请求资源路径
    requestpath = env['requestpath']
    print('动态资源请求地址:', env['requestpath'])
    # 判断请求动态资源路径,选择指定函数处理对应动态资源请求

    # 遍历路由列表,匹配请求url
    for path, func in routelist:
        print(path, func)
        if requestpath == path:
            # 找到指定路由,执行对应处理函数
            result = func()
            return result
    else:
        # 没有动态资源数据,返回404状态信息
        result = notFound()
        return result


# if __name__ == '__main__':
#     print(centerData())
