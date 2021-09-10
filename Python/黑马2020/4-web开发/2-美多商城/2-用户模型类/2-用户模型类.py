# 定义用户模型类

# django默认用户认证系统
#     django自带用户认证系统
#         处理用户账号、组、权限以及基于cookie的用户会话
#     django认证系统位置
#         django.contrib.auth包含认证框加的核心和默认模型
#     django认证系统同时处理认证和授权
#         认证一个用户是否是它声称的那个人,可用于账号登录
#         授权决定一个通过认证的用户被允许做什么
#     django认证系统包含内容
#         用户    用户模型类、用户认证
#         权限    标识一个用户是否可以做一个特定任务,MIS系统常用
#         分组    对多个具有相同权限用户进行统一管理,MIS系统常用
#         密码    一个可配置的密码哈希系统,设置密码、密码校验

# django默认用户模型类
#     django认证系统中提供了用户模型类User保存用户的数据
#         User对象是认证系统的核心
#     django认证系统用户模型类位置
#         django.contrib.auth.models.User    
#     User父类AbstractUser介绍
#         User对象基本属性
#             创建用户(注册用户)必须      username、password
#             创建用户(注册用户)可选      email、first_name、last_name、last_login、date_joined、is_active、is_staff、is_superuse
#             判断用户是否通过认证(登录)   is_authenticated
#         创建用户(注册用户)方法
#             user = User.objects.create_user(username,email,password,**extra_fields)
#         用户认证(登录)方法
#             from django.contrib.auth import authenticate
#             user = authenticate(username=username,password=password,**kwargs)
#         处理密码方法
#             设置密码        set_password(raw_password)
#             校验密码        check_password(raw_password)

# 自定义用户模型类
#     为什么要自定义用户模型类
#         django默认用户模型类中没有期望字段,如phone信息,需要自定义用户模型类来满足需求
#     如何自定义用户模型类
#         继承自AbstractUser
#         新增期望字段phone

# 迁移用户模型类
#     通过源码 django.conf.global_settings
#     AUTH_USER_MODEL = 'auth.User'
#     django用户模型类是通过全局配置项AUTH_USER_MODEL决定

#     配置规则
#         AUTH_USER_MODEL = '应用名.模型类名'
    
#     指定本项目用户模型类
#         AUTH_USER_MODEL = 'users.User'

#     迁移用户模型类
#         创建迁移文件
#             python manage.py makemigrations
#         执行迁移文件
#             python manage.py migrate

# TODO:
#     1.用户认证系统中的用户模型类,是通过全局配置项AUTH_USER_MODEL决定
#     2.如果迁移自定义用户模型类,必须先配置AUTH_USER_MODEL
