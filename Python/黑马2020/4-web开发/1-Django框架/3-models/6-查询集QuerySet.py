# 查询集QuerySet
#     概念
#         django的ORM中存在查询集的概念
#         查询集亦称为查询结果集,QuerySet表示从数据库中获取的对象集合
#         当调用如下过滤器方法是,django会返回查询集(而不是简单的列表)
#             all()           返回所有数据
#             filter()        返回满足条件数据
#             exclude()       返回满足条件之外数据
#             order_bu()      返回结果进行排序
#         对查询集可以再次调用过滤器进行过滤
#             books = BookInfo.objects.filter(readCount__gt=30).order_by('pubDate')
#         意味着查询集可以含有零个,一个或者多个过滤器,过滤器基于所给的参数限制查询结果
#         判断某一个查询集中是否有数据
#             exists()        判断查询集中是否有数据,如果有则返回True,没有则返回False

#     两大特性
#         1)惰性执行
#             创建查询集不会访问数据库,直到调用数据才会进行访问,调用数据的情况包括迭代,序列化,与if合用
#             如当执行如下语句,并未进行数据库查询,只是创建了一个结果集books
#             books = BookInfo.objects.all()
#             for book in books:
#                 print(book.name)
#         2)缓存(性能优化)
#             同一个结果集,第一次使用时会发生数据库的查询,然后django会把结果缓存下来,再次使用这个结果集时会使用缓存的数据,减少了查询数据库的次数
#             情况一如下是两个查询集,无法重用缓存数据,每次查询都会与数据库进行一次交互,增加了数据库负载
#                 [book.name for book in BookInfo.objects.all()]
#                 [book.name for book in BookInfo.objects.all()]
#             情况二经过存储后,可以重用查询集,第二次使用缓存中的数据
#                 books = BookInfo.objects.all()
#                 [book.name for book in books]

#     限制查询集
#         可以对查询集进行取下标或切片操作,等同于sql中的limit和offset子句
#         TODO:不支持负数索引
#             对查询集进行切片后返回一个新的查询集,不会立即执行查询
#             如果获取一个对象,直接使用[0],等同于[0,1].get()
#             如果没有数据.[0]引发IndexError异常.[0:1].get如果没有数据引发DoesNotExist异常
#             获取第一,二项数据
#                 BookInfo.objects.all()[0,2]

#     分页
#         # 导入分页模块
#         from django.core.paginator import Paginator

#         books = BookInfo.objects.all()
#         # 创建分页实例
#         p = Paginator(books,2)
#         # 获取指定页的数据
#         page = p.page(1)
#         # 获取分页数据
#         totalPage = paginator.num_pages
