# 路由命名
#     定义路由时,可以为路由命名,方便查找特定视图具体路径信息
#     1)使用include函数定义路由时,可以使用namespace参数定义路由的命名空间
#         url(r'^',include('books.urls',namesapce='books'))
#     命名空间表示,凡是book.urls中定义的路由,均属于namespace指明的book名下
#     命名空间避免了不同应用中的路由使用了相同的名字发生冲突,使用命名空间区别开
#     2)在定义普通路由时,可以使用name参数指明路由名字

# reverse反解析
#     使用reverse函数,可以根据路由名称,返回具体路径
#     from django.urls import reverse

#     def index(request):
        
#         url = reverse('books:index')
#         print(url)
    
#     对于没有指明namespace的,reverse(路由name)
#     对于指明namespace的,reverse(命名空间namespace:路由name)
