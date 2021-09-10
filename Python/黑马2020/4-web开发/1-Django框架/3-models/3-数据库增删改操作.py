# 数据库的操作
    
#     增加数据两种方法
#     1)save
#         通过创建模型类对象,执行对象的save()方法保存到数据库中
#             from books.models import BookInfo,PeopleInfo
#             book = BookInfo(
#                 name='神雕侠侣',
#                 pubDate='1980-1-1',
#                 readCount=33,
#                 comentCount=45
#             )
#             book.save()
#     2)creat
#         通过模型类.objects.creat()保存
#             BookInfo.objects.creat(
#                 name='神雕侠侣',
#                 pubDate='1980-1-1',
#                 readCount=33,
#                 comentCount=45
#             )

#     修改数据两种方法
#     1)save
#         通过修改模型类对象属性,然后执行save()方法
#             book = BookInfo.objects.get(name='神雕侠侣')
#             book.name = '神雕侠侣(精装版)'
#             book.save()
#     2)update
#         通过模型类.objects.filter().update(),返回受影响的行数
#             BookInfo.objects.filter(name='神雕侠侣').update(name='神雕侠侣(精装版)')

#     删除数据两种方法
#     1)模型类对象delete
#         book = BookInfo.objects.get(name='神雕侠侣')
#         book.delete()
#     2)模型类.objects.filter().delete()
#         BookInfo.object.filter(name='神雕侠侣').delete()
