from django.conf.urls import url
<<<<<<< HEAD
<<<<<<< HEAD
from books.views import index,detail,setCookie,getCookie,setSession,getSession,BookView,CenterView,HomeView
=======
from books.views import index,detail
>>>>>>> 90c643c (keep coding)
=======
from books.views import index,detail,setCookie,getCookie,setSession,getSession,BookView,CenterView,HomeView
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7

urlpatterns = [
    # name给url起名,可以通过name找到这个路由
    url(r'^index/$',index,name='index'),
    # 分组获取正则数据,位置参数
    # http:127.0.0.1/categoryid/bookid/
    # url(r'^(\d+)/(\d+)/$',detail),
    # 分组获取正则数据,关键字参数
    # http:127.0.0.1/categoryid=?
    url(r'^(?P<categoryid>\d+)/(?P<bookid>\d+)/$',detail),
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7
    url(r'^setCookie/$',setCookie),
    url(r'^getCookie/$',getCookie),
    url(r'^setSession/$',setSession),
    url(r'^getSession/$',getSession),

    # 参数一是正则,参数二是视图函数名称
    # BookView.as_view()返回的是一个视图函数名
    url(r'^login/$',BookView.as_view()),
    url(r'^center/$',CenterView.as_view()),
    url(r'^main/$',HomeView.as_view()),
]
<<<<<<< HEAD
=======
]
>>>>>>> 90c643c (keep coding)
=======
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7
