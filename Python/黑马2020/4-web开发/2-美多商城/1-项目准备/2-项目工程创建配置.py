# 创建工程
#     准备代码托管仓库(github.mall)
#         选择语言
#         添加.gitignore选择语言
#     克隆代码仓库
#     创建工程
#         1)创建虚拟环境
#         2)安装django框架
#         3)创建django工程

# 配置开发环境
#     项目环境分为开发环境生产环境
#         开发环境用于编写调试项目代码
#         生产环境用于项目线上部署运行
#     1)新建配置文件
#     2)指定开发环境配置文件

# 配置jinja2模板引擎
#     安装jinja2模板
#     配置jinja2模板引擎
#         setting->templates
#     补充jinja2模板引擎环境
#         1)创建jinja2模板引擎环境配置文件
#         2)编写jinja2模板引擎环境配置代码
#         3)加载jinja2模板引擎环境
    
# 配置mysql数据库
#     新建mysql数据库
#         1)新建数据库
#         $ create database meiduo charset=utf8;
#         2)新建mysql用户
#         $ create user meiduoer identified by '123456';
#         3)授权meiduoer用户访问meiduo数据库
#         $ grant all on meiduo to 'meiduoer'@'%';
#         4)授权结束后刷新特权
#         $ flush privileges;
#     配置mysql数据库
#         setting -> templates -> DATABASES
#     安装pymysql扩展包
#         1)安装驱动程序
#         2)在工程同名子目录的__init__.py文件,添加代码
        
# 配置redis数据库(缓存数据)
#     安装django-redis
#     配置redis数据库(分库管理)
#         default
#             默认redis配置项,采用0号redis库
#         session
#             状态保持redis配置项,采用1号redis库

# 配置工程文件(日志记录采用logging模块)
#     配置工程日志
#     准备日志文件目录
#     使用日志的记录器
#     git管理工程日志

# 配置前端静态文件(cssimagesjs)
#     准备静态文件
#     指定静态文件加载路径
