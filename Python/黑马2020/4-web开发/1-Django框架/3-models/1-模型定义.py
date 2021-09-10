# 模型类的定义
#     模型类被定义在`应用/models.py`文件中
#     模型类必须继承自Model类,位于django.db.models中

# 定义
#     在models.py文件中定义模型类
#         Sample\venvdjango1.0\BookManager\books\models.py
#     1)数据库表名
#         模型类如果未指明表名,django默认以小写app应用名_小写模型类名作为数据库名
#         可以通过db_table指明数据库表名
#     2)关于主键
#         django会为表创建自动增长的主键列,每个模型只能有一个主键列,如果使用选项设置某属性为主键后django不会再创建自动增长主键列
#         默认创建的主键列属性为id,可以使用pk(primary key)代替
#     3)属性命名限制
#         不能是python的保留关键字
#         不允许使用连续的下划线,和django的查询方式有冲突
#         定义属性时徐亚指定字段类型,通过字段类型的参数指定选项,语法:
#             属性=models.字段类型(选项)
#     4)字段类型
#         类型                        说明
#         AutoField                  自动增长的IntegerField,通常不用指定,不指定django会自动创建属性名为id的自动增长属性
#         BooleanFiled               布尔字段,值为True或False
#         NullBooleanFiled           支持Null,值为True或False
#         CharField                  字符串,参数max_length表示最大字符个数
#         TextField                  大文本字段,一般超过4000个字符使用
#         IntegerField               整数
#         DateField                  日期,参数auto_now表示每次保存对象时,自动设置该字段为当前时间
#         TimeField                  时间
#         DateTimeField              日期时间,参数同DateField
#         FileField                  上传文件字段
#         ImageField                 继承自FileField,对上传的内容进行校验,确保是有效的图片
#     5)选项
#         选项                        说明
#         null                       如True,表示允许为空,默认值为False
#         blank                      如True,表示字段允许为空白,默认值为False
#         db_column                  字段的名称,如果未指定,则使用属性的名称
#         db_index                   如True,则表中会为此字段创建索引,默认值为False
#         default                    默认
#         primary_key                如True,则该字段会成为模型的主键字段,默认值为False,一般作为AutoField的选项使用
#         unique                     如True,这个字段在表中必须有唯一值,默认值为False
#     null是数据库范畴的概念,blank是表单验证范畴的
#     6)外键
#         在设置外键时,需要通过on_delete选项指明主表删除数据时,对于外键引用表数据如何处理,在django.db.models中包含了可选常量
#             CASECADE级联,删除主表数据时连同一起删除外键表中数据
#             PROTECT保护,通过抛出ProtectedError异常,来阻止删除主表中被外键应用的数据
#             SET_NULL设置为NULL,仅在该字段null=True允许为null时可用

# 迁移
#     将模型类同步到数据库中
#     1)生成迁移文件
#         python manage.py makemigrations
#     2)同步数据库中
#         python manage.py migrate
