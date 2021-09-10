from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from books.models import BookInfo
from django.urls import reverse
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import redirect
=======
>>>>>>> 90c643c (keep coding)
=======
from django.shortcuts import redirect
>>>>>>> a312f01 (keep coding)
=======
from django.shortcuts import redirect
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7
import json

# Create your views here.

def index(request):
    # def render(request, template_name, context=None, content_type=None, status=None, using=None):
    # 参数1 当前请求
    # 参数2 模板文件
    # 参数3 传递参数

    # 实现业务逻辑
    #     到数据库查询数据
    #     组织数据
    #     传递模板

    # 把所有书籍查询出来
    # objects可以理解为模型的管理类,对模型的增删改查依赖于它
    books = BookInfo.objects.all()
    context = {
        'books':books
    }

    # 页面展示错误信息
    # result = 10 / 0

    # 路由命名及reverse反解析
    # path = reverse('books:index')
    # return redirect(request,path,context)

    return render(request,'books/index.html',context)


def detail(request,categoryid,bookid):
    # GET请求
    # # 位置,关键字参数进行传参匹配
    # print(categoryid,bookid)
    # params = request.GET
    # # 获取一键多值 QueryDict .getlist方法
    # username = params.getlist('username')
    # # 获取一键一值 .get方法
    # password = params.get('password')
    # print(username,password)

    # # POST请求 Form Date
    # params = request.POST
    # print(params)

    # # POST请求 Non-Form Data
    # # JSON形式的字符串
    # body = request.body.decode()
    # # 转换为字典,方便数据操作
    # data = json.loads(body)
    # # JSON
    # #     json.dumps      将字典转换为JSON形式的字符串
    # #     json.loads      将JSON形式的字符串转换为字典
    # print(data)

    # 请求头
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7
    # contenttype = request.META['CONTENT_TYPE']
    # POSTMAN添加name参数
    # name = request.META['HTTP_NAME']
    # print(name,contenttype)

    # HttpResponse
    # content           只传递字符串,不要传递对象字典数据,可以使用jsonResonse直接传递字典
    # statue            HTTP statues code must be an integer frmo 100 to 599
    # content-type      语法形式为大类/小类的MIME类型,形如text/html,text/css,text/javascript,application/json,image/png,image/gif等

    return render(request,'inherit.html')
    # 返回Json数据
    return JsonResponse({'name':'mass','age':'22'})
    # 返回重定向
    return redirect('http://www.baidu.com')
    return HttpResponse('deteail',status=200)

def setCookie(request):
    # 1)浏览器第一次请求服务器未携带任何cookie信息
    # 2)服务器接收到没有cookie信息的请求,设置一个cookie携带在响应中
    # 3)浏览器接收到携带cooike信息的响应,浏览器保存cookie信息到本地中
    # 4)浏览器再次向服务器发送携带cookie信息的请求
    # 5)服务器接收到携带cookie信息的请求,实现状态保持

    # Http协议角度理解cookie原理
    # 1)浏览器第一次请求服务器,请求同种没有任何cookie信息
    # 2)服务器接收到没有cookie信息的请求,响应头中携带set_cookie信息
    # 3)浏览器接收到响应再次发起请求时,会在请求头中携带cookie信息
    # 4)结合代码中是否有set_cookie操作,以此说明响应头中有无set_cookie信息

    # 判断有无cookie信息
    # if...else...

    # 获取用户信息
    username = request.GET.get('username')
    # 服务器设置cookie信息
    response = HttpResponse('setCookie')
    # max_age单位是秒,时间是从服务器接收到这个请求+秒数计算后的时间
    response.set_cookie('username',username,max_age=3600)

    # 删除cookie两种方式
    # response.delete_cookie(key)
    # response.set_cookie(key,value,max_age=0)

    return response

def getCookie(requeset):
    # 服务器接收和查看cookie信息
    cookies = requeset.COOKIES
    # cookies是一个字典
    username = cookies.get('username')
    age = cookies.get('age')
    # 得到用户信息进行其他操作
    print(username,age)

    return HttpResponse('getCookie')

def setSession(requeset):
    # 1)浏览器发送请求到服务器携带敏感信息
    # 2)服务器验证通过请求信息将用户对象放入session中,session存在内存中
    # 3)服务器向浏览器发送响应数据,将sessionid存入响应头中的cookie信息(Cookie:sessionid-xxxx)
    # 4)浏览器接受到响应后将cookie信息保存起来(包含sessionid信息),发送请求到服务器携带sessionid cookie信息
    # 5)服务器根据sessionid从内存中获取用户信息
    # 6)服务器返回响应数据

    # Http协议角度理解session原理
    # 1)初次请求,请求头中没有携带任何cookie信息
    # 2)views在设置seesion时,会将数据保存到数据库中,设置一个cookie信息,cookie会在响应头中发送到浏览器
    # 3)再次请求,浏览器都会在请求头中携带session cookie信息
    print(requeset.COOKIES)
    # 假设用户名密码验证通过
    userid = 1
    # 设置seesion信息
    # 1)将数据库保存在数据库中
    # 2)设置一个cookie信息,这个cookie信息是以sessionid为key
    requeset.session['userid'] = userid
    # 返回响应
    return HttpResponse('setSession')

def getSession(requeset):
    print(requeset.COOKIES)
    userid = requeset.session['userid']
    print(userid)

    return HttpResponse('getSession')

# 登录界面
#     GET     请求获取登录界面
#     POST    请求验证登录(用户名和密码是否正确)

# 一个视图包含两个请求
# 函数面向过程-没有记忆
# def login(requeset):

#     # 区分业务逻辑
#     if requeset.method == 'GET':
#         pass
#     else:
#         pass
#     pass

# 面向对象
#     类视图是采用面向对象思路
#     1)定义类视图
#         [1]继承自View
#         [2]不同的请求方式有不同的业务逻辑
#             类视图的方法直接采用http的请求方式命名类里面的方法,如get,post
#         [3]类视图的方法的第二个参数必须是请求实例对象
#             类视图的方法必须要有返回值,返回值是HttpResponse及其子类


from django.views import View

class BookView(View):

    def get(self,requeset):
        
        return HttpResponse('get')

    def post(self,requeset):
        
        return HttpResponse('post')

# 个人中心页面  必须登录才能显示
#     GET     请求展示个人中心
#     POST    请求实现个人中心信息修改

from django.contrib.auth.mixins import LoginRequiredMixin

class CenterView(LoginRequiredMixin,View):

    def get(self,request):

        return HttpResponse('个人中心')

    def post(self,request):
        
        return HttpResponse('个人中心修改')

from datetime import datetime

class HomeView(View):

    def get(self,request):
        # http://127.0.0.1:8000/main/?username=xxxx
        # 获取数据
        username = request.GET.get('username')
        # 组织数据
        context = {
            'username':username,
            'age':22,
            'birthday':datetime.now(),
            'friends':['mass','rose','lisa'],
            'salary':{
                '2019':10000,
                '2020':12000,
                '2021':15000,
            },
            'desc':'<script>alert("hot")</script>'
        }

        return render(request,'main.html',context=context)
<<<<<<< HEAD
=======
    contenttype = request.META['CONTENT_TYPE']
    # POSTMAN添加name参数
    # name = request.META['HTTP_NAME']
    # print(name,contenttype)

<<<<<<< HEAD
    return HttpResponse('deteail')
>>>>>>> 90c643c (keep coding)
=======
    # HttpResponse
    # content           只传递字符串,不要传递对象字典数据,可以使用jsonResonse直接传递字典
    # statue            HTTP statues code must be an integer frmo 100 to 599
    # content-type      语法形式为大类/小类的MIME类型,形如text/html,text/css,text/javascript,application/json,image/png,image/gif等

    return redirect('http://www.baidu.com')
    return HttpResponse('deteail',status=200)
>>>>>>> 6bb9653 (keep coding)
=======
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7
