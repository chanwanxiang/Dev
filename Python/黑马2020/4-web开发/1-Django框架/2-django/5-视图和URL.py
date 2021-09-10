# 视图和URL
#     站点管理管理页面做好,接下来就是做公共访问页面
#     对于django的设计框架MVT
#         用户在URL中请求的是视图
#         视图接收请求后进行处理
#         并将处理的结果返回给请求者
#     使用视图时需要进行两步操作
#         1)定义视图
#         2)配置URLconf

# 定义视图
#     视图就是一个python函数,被定义在应用的views.py中
#     视图的第一个参数是HttpRequest类型对象request,包含了所有的请求信息
#     视图必须返回HttpResponse对象,包含返回给请求者的响应信息
#     需要导入HttpResonse模块 from django.http import HttpResponse

# 配置URLconf让请求找到视图
#     查找视图过程
#         1)请求者在浏览器地址栏中输入URL,请求到网站
#         2)网站获取URL信息
#         3)与编写好的URLconf逐条匹配
#         4)匹配成功则调用对应的视图
#         5)如果所有的URLconf都没有匹配成功,则返回404

# 项目URLconf入口
#     setting.py
#         ROOT_URLCONF = 'BookManager.urls'

# 需要两步完成URLconf配置
#     在项目中定义URLconf
#         urls.py
#     在应用中定义URLconf
#         新建urls.py
