# python安装redis
#     pip install redis

# 调用模块
#     引入模块
#         from redis import StrictRedis
#     这个模块提供了StrictRedis对象,用于连接redis服务器,并按照不同类型提供了不同方法,进行交互操作

# StrictRedis对象方法
#     通过init创建对象,指定参数host,port与指定的服务器和端口连接,host默认为localhost,port默认为6379,db默认为0

#     sr = StrictRedis(host='localhost', port=6379, db=0)
#     简写
#     sr = StrictRedis()
