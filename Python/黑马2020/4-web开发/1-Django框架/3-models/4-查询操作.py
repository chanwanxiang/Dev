# 基本条件查询
#     get          查询单一结果,如果不存在会抛出模型类.DoesNotExist异常
#     all          查询多个结果
#     count        查询结果数量
   
#     查询id为1的书籍
#         BookInfo.objects.get(id=1)

#     查询所有书籍信息
#         BookInfo.object.all()

#     查询书籍数量
#         BookInfo.objects.count()

# 过滤查询
#     实现sql中的where功能,包括
#         get     过滤单一结果
#         filter  过滤多个结果
#         exclude 排除掉符合条件剩下的结果
#     对于过滤条件使用,上述三个方法相同,以filter讲解
#         属性名称__比较运算符=值
#     1)相等
#     exact       表示判等
#     查询编号为1的书籍
#         BookInfo.objects.get(id__exact=1)
#     2)模糊查询
#     contains     是否包含
#         查询书名包含`湖`的书籍
#             BookInfo.objects.filter(name__contains='湖')
#     startswith endswith     以指定值开头或结尾
#         查询书名以`部`结尾的书籍
#             BookInfo.objects.filter(name__endswith='部')
#     3)空查询
#     isnull       是否为空
#         查询书名为空的书籍
#             BookInfo.objects.filter(name__isnull=True)
#     4)范围查询
#     in           是否包含在范围
#         查询编号为1或3或5的书籍
#             BookInfo.objects.filter(id__in=[1,3,5])
#     5)比较查询
#         gt      大于(greater then)
#         gte     大于等于(greater then equal)
#         lt      小于(less then)
#         lte     小于等于(less then equal)
#         查询编号大于3的书籍
#             BookInfo.objects.filter(id__gt=3)
#         TODO: 不等于的运算使用exclude()过滤器
#         查询编号不等于3的书籍
#             BookInfo.objects.exclude(id__exact=3)
#     6)日期查询
#         year,month,day,week_day,hour,minute,second      对日期时间类型的属性进行运算
#         查询1980年发表的书籍
#             BookInfo.objects.filter(pubDate__year=1980)
#         查询1990年1月1日后发表的书籍
#             BookInfo.objects.filter(pubDate__gt='1990-1-1')

# F和Q对象
#     F对象被定义在django.db.models,用于两个属性之间比较
#     语法
#         Models.objects.filter(属性名称__比较运算符=F(属性名))
#             查询阅读量大于等于评论量的书籍
#                 BookInfo.objects.filter(readCount__gt=F('commentCount'))
        
#         对于多个过滤器逐个调用表示逻辑与关系,同sql语句中的where部分的and关键字
#             查询阅读量大于20,并且编号小于3的图书
#                 BookInfo.objects.filter(readCount__gt=20,id__lt=3)
#             或
#                 BookInfo.objects.filter(readCount__gt=20).filter(id__lt=3)
#     Q对象被定义在django.db.models,实现逻辑或or的查询,需要使用Q()对象结合|运算符
#     语法
#         Models.objects.filter(Q(属性名称__比较运算符=值)|Q(属性名称__比较运算符=值))
#             查询阅读量大于20或者编号小于3的书籍
#                 BookInfo.objects.filter(Q(readCount__gt=20)|Q(id__lt=3))
#             Q对象除了与或关系还可以加~表示非的关系
#             查询编号不等于3的书籍
#                 BookInfo.objects.filter(~Q(id__exact=3))

# 聚合函数和排序函数
#     聚合函数
#         使用aggregate()过滤器调用聚合函数
#         聚合函数包括Avg,Count,Max,Min,Sum,被定义在django.db.models
#             查询书籍总阅读量
#                 BookInfo.objects.aggregrate(Sum('readCount'))
#                 返回一个字典类型
#                     {'属性名__聚合函数小写':值}

#     排序
#         使用order_by对结果进行排序
#             对书籍的阅读量进行默认升序
#                 BookInfo.objects.all().order_by('readCount')
#             降序
#                 BookInfo.objects.all().order_by('-readCount')
