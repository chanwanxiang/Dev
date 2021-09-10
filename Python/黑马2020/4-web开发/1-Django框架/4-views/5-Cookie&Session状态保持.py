# 状态保持
#     浏览器请求服务器是无状态的
#     无状态指一次用户请求时,浏览器与服务器无法知道之前这个用户做过什么,每次请求都是一次新的请求
#     无状态原因是浏览器与服务器是使用Socket套接字进行通信的,服务器将请求结果返回给浏览器后,会关闭当前Socket连接
#         而且服务器也会在处理页面完毕后销毁页面对象
#     要保持下来用户浏览的状态,比如用户是否登录,浏览过哪些商品等,实现状态保持主要有两种方式
#         1)在客户端存储信息用cookie
#         2)在服务端存储信息用session

# Cookie
#     cookie,有时也用其复数形式cookies,指网站为了辨别用户身份,进行session跟踪而存储在用户本地终端上的数据(通常经过加密)
#     cookie是由服务器生成,发送给User-Agent(一般是浏览器),浏览器会将cookie的key/value保存到本地的文本文件内,下次请求同一网站时就发送改cookie给服务器
#     cookie的名称和值可以有服务器开发自己定义,这样服务器可以知道该用户是否是合法用户以及是否需要重新登录
#     服务器可以利用cookie包含信息的任意性来筛选并经常维护这些信息,以判断HTTP传输中的状态,cookie最典型应用在记住用户ID
#     TODO:
#         cookie是存储在浏览器中的一段纯文本信息,建议不要存敏感信息如密码,应为浏览器可能被其他人使用

# cookie说明
#     1)浏览器第一次请求服务器未携带任何cookie信息
#     2)服务器接收到没有cookie信息的请求,设置一个cookie携带在响应中
#     3)浏览器接收到携带cooike信息的响应,浏览器保存cookie信息到本地中
#     4)浏览器再次向服务器发送携带cookie信息的请求
#     5)服务器接收到携带cookie信息的请求,实现状态保持

# Http协议角度理解cookie原理
#     1)浏览器第一次请求服务器,请求同种没有任何cookie信息
#     2)服务器接收到没有cookie信息的请求,响应头中携带set_cookie信息
#     3)浏览器接收到响应再次发起请求时,会在请求头中携带cookie信息
#     4)结合代码中是否有set_cookie操作,以此说明响应头中有无set_cookie信息

# cookie的特点
#     TODO:
#     cookie是保存在客户端的一段纯文本信息
#     cookie以键值对的格式进行信息的存储
#     cookie基于域名(IP)安全,不同域名的cookie是不能相互访问的
#     当浏览器请求某网站时,会将浏览器存储的跟网站相关的所有cookie信息提交给网站服务器
#     同源策略
#         什么是源,源就是协议域名端口号(https://www.baidu.com:8080)
#         同源策略是浏览器的一个安全功能,不同源的客户端脚本在没有明确授权的情况下,不能读写对方资源

# 设置cookie
#     通过HttpResonse对象中的set_cookie方法设置cookie
#         HttpResponse.set_cookie(cookie名,value=cookie值,max_age=cookie有效期)
#         max_age单位为秒,默认为None,如果是临时cookie,可将max_age设置为None

# 读取cookie
#     通过HttpResonse对象中的cookieS属性来读取本次请求携带的cookie值,request.cookieS为字典类型
#         def cookie(requeset):
#             cookieName = requeset.cookieS.get('username')

# 删除cookie
#     可以通过HttpResponse对象中的delete_cookie方法来删除
#         response.delete_cookie('username')

# Session
#     实现状态保持的在服务端存储信息的方法,依赖cookie,如果客户端禁用了cookie,session不能实现
#     django默认启用session,可在setting.py文件配置
#     TODO:session依赖于cookie,sessin依赖于cookie,sessin依赖于cookie
#          1)更换浏览器,不能再获取到session信息
#          2)不更换浏览器,删除浏览器中的sessionid,获取不到session信息
#          3)再去执行setSession,会重新生成seesionid信息

# session流程
#     1)浏览器发送请求到服务器携带敏感信息
#     2)服务器验证通过请求信息将用户对象放入session中,session存在内存中
#     3)服务器向浏览器发送响应数据,将sessionid存入响应头中的cookie信息
#     4)浏览器接受到响应后将cookie信息保存起来(包含sessionid信息),发送请求到服务器携带sessionid cookie请求
#     5)服务器根据sessionid从内存中获取用户信息
#     6)服务器返回响应数据


# session存储方式
#     保存在数据库或者本地缓存,可在setting.py文件配置
#         1)数据库为默认存储方式
#             session表结构包括三个数据:键值过期时间
#         2)本地缓存
#             存储在本机缓存中,如果丢失则不能找回,比数据库方式读写更快
#         3)混合存储
#             优先从本机缓存中获取,如无则通过数据库查询
#             SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
#         4)Redis
#             在Redis中保存session,需要引入第三方扩展,可以使用django-redis解决
#                 安装扩展
#                     pip install django-redis
#                 配置setting.py
#                     CACHES = {
#                         'default': {
#                             'BACKEND': 'django_redis.cache.RedisCache',
#                             'LOCATION': 'redis://127.0.0.1:6379/1',
#                             'OPTIONS': {
#                                 'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#                             }
#                         }
#                     }
#                     SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
#                     SESSION_CACHE_ALIAS = 'default'

# session操作
#     通过HttpRequest对象的session属性进行会话的读写操作
#         1)以键值对的形式写session
#             request.session['key'] = value
#         2)根据键读取值
#             request.session.get('key',defaultValue)
#         3)清空所有session,在存储中删除值的部分
#             request.session.clear()
#         4)清除session数据,在存储中删除session整条数据
#             request.session.flush()
#         5)删除session中的指定键及值,在存储中只删除某个键及对应的值
#             del request.session['key']
#         6)设置session的有效期
#             request.session.set_expiry(value)
#             如果value是一个整数,那么session将在value秒没有活动后过期
#             如果value为0,那么用户session的cookie将在用户的浏览器关闭时过期
#             如果value为None,那么seesion有效期将采用系统默认值,默认为两周,可以通过setting.py中配置session_cookie_AGE来设置全局默认值         
