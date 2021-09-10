# 模型

# 当前项目开发都是数据驱动
# 以下为书籍信息管理的数据关系,书籍和人物是:一对多的

# 书籍信息表
# 字段名      字段类型        字段说明
# id         AutoField      主键
# name       CharField      书名

# 人物信息表
# 字段名      字段类型        字段说明
# id         AutoField      主键
# name       CharField      人名
# gender     BooleanField   性别
# book       ForeignKey     外键

# django进行数据库开发的提示:
#     MVT设计模式中的的Model,专门负责和数据库交互,对应models.py
#     由于Model中内嵌了ORM框架,所以不需要直接面向数据库编程
#     而是定义模型类,通过模型类和对象完成数据表的增删改查
#     ORM框架就是把数据表的行与对应的对象建立关联,互相转换,是的数据库的操作面向对象

# ORM与DataBase对应关系
#     ORM         DB
#     类名         数据表
#     对象         数据行
#     属性         字段

# 使用django进行数据库开发的步骤
#     1)定义模型类
#     2)模型迁移
#         生成迁移文件(不会在数据中生成表,只会创建一个数据表和模型对应关系)
#         python manage.py makemigrations
#         开始迁移
#         python manage.py migrate
#     3)操作数据库
