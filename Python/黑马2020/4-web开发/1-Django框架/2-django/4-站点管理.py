# 站点管理

# 站点分为内容发布和公共访问两部分
#     内容发布部分由网站的管理员负责查看,添加,修改,删除数据

# django能够根据定义的模型类自动的生成管理模块
#     使用django管理模块,需要按照如下步骤操作
#         1)管理员界面本地化
#         2)创建管理员
#         3)注册模型类
#         4)发布内容到数据库

# 管理员界面本地化
#     项目名称下的setting.py文件
#         LANGUAGE_CODE = 'zh-Hans'
#         TIME_ZONE = 'Asia/Shanghai'

# 创建管理员
#     命令
#         python manage.py createsuperuser
#     重置密码
#         python manage.py changepassword username
#     登录站点
#         http://127.0.0.1/admin

# 注册模型类
#     在项目应用的admin.py文件中注册模型类
#         需要导入模型模块
#             from books.models import BookInfo,PersonInfo
#         admin登录在后台增删改查数据

# 发布内容大数据库
#     发布内容后优化模型类展示
