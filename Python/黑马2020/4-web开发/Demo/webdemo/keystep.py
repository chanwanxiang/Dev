## Django Demo

# 1. 环境搭建

# 查看Pyhotn版本(cmd命令行)
#     python

# 安装Django
#     pip install django
#     pip install -v django==2.0

# 验证Django是否成功安装
#     python -m django --version


# 2. 开发步骤详解

# 项目创建
#     django-admin startproject webdemo

# 启动Django项目
#     python manage.py runserver

# 创建Django App(django中App相当于一个功能模块)
#     python manage.py startapp appdemo

# 创建templates文件夹,appdemo目录下
#     添加index.html文件

# setting.py文件中添加新建的appdemo功能模块
#     INSTALLED_APPS

# 编写视图函数,打开webdemo/appdemo/views.py
#     编写函数返回index.html界面

# 添加路由,打开webdemo/urls.py
#     urlpatterns =

# 3. 小结

#     常用命令
#         django-admin.py startproject webdemo  #创建项目
#         python manage.py startapp appdemo  #创建app
#         python manage.py runserver  #启动 Django 中的开发服务器
#         python manage.py -h  #帮助文档