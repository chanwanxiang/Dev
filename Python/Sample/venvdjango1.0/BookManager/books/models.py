from django.db import models

# Create your models here.

# 1). ORM
#     表对应类
#     字段对应属性    
# 2). 模型类需要继承自models.Model
# 3). 模型类会自动添加一个主键
# 4). 属性名 = 属性类型(选项)
#     属性名
#         不要使用python或mysql关键字
#         不要使用连续的下滑线(__)
#     属性类型
#         与mysql相类似
#     选项
#         charFiled必须设置max_length
#         null    是否为空
#         unique  唯一
#         default 默认值

# 书籍表
#     id,name,pubDate,readCount,commentCount,isDelete

class BookInfo(models.Model):
    # 主键当前可以自动生成
    # 书名
    name = models.CharField(max_length=10, unique=True)
    # 发布日期
    pubDate = models.DateField(null=True)
    # 阅读量
    readCount = models.IntegerField(default=0)
    # 评论量
    commentCount = models.IntegerField(default=0)
    # 是否逻辑删除
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        # 修改表名,默认books_bookinfo
        db_table = 'bookinfo'
        # 修改后台admin显示信息
        verbose_name = 'isMe'


# 准备人物列表信息的模型类
class PersonInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    # 人物名称
    name = models.CharField(max_length=20, verbose_name='名称')
    # 性别
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    # 描述信息
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # on_delete选项指明主表删除数据,对于外键引用表的数据如何处理,外键级联操作
    # 书籍:人物 1:n
    # 西游记:孙悟空,白骨精
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'personinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name
