# # 配置
#     在项目文setting.py中保存了数据库的连接配置信息,django默认初始配置使用sqlite数据库
#     1)使用mysql数据库首先需要安装驱动程序
#         pip install pymysql
#     2)在django工程同名子目录__init__.py文件中添加如下语句
#         import pymysql
#         pymysql.install_as_MySQLdb()
#     3)修改DATEBASE配置信息
#         DATABASES = {
#             'default': {
#                 'ENGINE': 'django.db.backends.mysql',
#                 'HOST': '127.0.0.1',  # 数据库主机
#                 'PORT': 3306,  # 数据库端口
#                 'USER': 'root',  # 数据库用户名
#                 'PASSWORD': '123456',  # 数据库用户密码
#                 'NAME': 'book'  # 数据库名字
#             }
#         }
#     4)在数据库中创建数据库
#         create database book charset=utf8     

# shell工具
#     django的manage工具提供了shell命令,帮助我们配置好当前工程的运行环境(如连接好数据库),以便可以直接在终端中执行测试python语句
#     通过如下命令进入shell
#         python manage.py shell
#     导入连个模型类,以便后续使用
