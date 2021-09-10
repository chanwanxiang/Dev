# 关联查询
#     由一到多的访问语法
#         一对应的模型类对象.多对应的模型类名小写_set
#             查询书籍id=1的所有人物信息
#                 book = BookInfo.objects.get(id=1)
#                 book.personinfo_set.all()

#     由多到一的访问语法
#         多对应的模型类对象.多对应的模型类中的关系类属性名
#             查询人物id=1的书籍信息
#                 person = PersonInfo.objects.get(id=1)
#                 person.book()

# 关联过滤查询
#     由多模型类条件查询一模型类数据
#     语法
#         关联模型类名小写__属性名__条件运算符=值
#             查询人物有`郭靖`的书籍
#                 BookInfo.objects.filter(personinfo__name__exact='郭靖')
#             查询人物描述包含`八`的书籍
#                 BookInfo.objects.filter(personinfo__descriptions__contains='八')
#     由一模型类条件查询多模型类数据
#     语法
#         一模型类关联属性名__一模型类属性名__条件运算符=值
#             查询书名为`天龙八部`所有人物
#                 PersonInfo.objects.filter(book__name='天龙八部')
#             查询书籍阅读量大于30的所有书籍人物
#                 PersonInfo.objects.filter(book__readCount__gt=30)
