# 类视图
#     在django中可以使用类来定义一个视图,称为类视图
#     使用类视图可以将视图对应的不同请求方式以类中的不同方法来区别定义
#     如下所示
#     from django.views.generic import View

#     class RegisterView(View):
#         # 类视图处理注册逻辑

#         def get(self,request):
#             # 处理GET请求,返回注册页面
#             return reder(request,'register.html')

#         def post(self,request):
#             # 处理POST请求,实现注册逻辑
#             return HttpResponse('实现注册逻辑')

#     类视图的好处
#         代码可读性好
#         类视图相对于函数视图有更高的复用性,如果其他地方需要用到某个类视图的某个特定逻辑,直接继承该类视图即可
#     定义类视图需要继承自django提供的父类View,可使用
#         from django.views.generic import View
#         from django.views.generic.base import View 导入
#     配置路由时,使用类视图的as_view()方法来添加
#         详见books.urls

#     类视图原理
#         点击as_view函数查看源码

#     类视图的多继承重新dispatch MRO继承顺序
#         使用面向对象多继承特性,详见books.views
