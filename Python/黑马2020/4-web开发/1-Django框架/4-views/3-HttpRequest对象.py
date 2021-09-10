# HttpRequest对象
#     HTTP协议向服务器传参途经
#         1)提取URL特定内容,可以在服务器端的路由中用正则表达式截取
#         2)查询字符串(query string),形如key1=value1&key2=value2
#         3)请求体(body)中发送数据,如表单数据,json,xml
#         4)在http报文的头(header)中

# URL路径参数
#     想从URL中获取值,需要在正则表达式中使用分组
#     获取值分为两种方式
#         位置参数
#             参数位置不可错
#         关键字参数
#             参数位置可以变,跟关键字保持一致即可
#     TODO:
#         两种参数的方式不要混用,在一个正则表达式中只能使用一个参数方式
#         参见books.urls

# django的QueryDict对象
#     HttpRequest对象的属性GET,POST都是QueryDict类型对象
#     与python字典不同,QueryDict类型对象用来处理同一个键带有多个值的情况
#     方法get()           根据键获取值
#         如果一个键同时拥有多个值将获取最后一个值
#         如果键不存在则返回None,可以设置默认值进行后续处理
#             get('键',默认值)
#     方法getlist()       根据键获取值,值以列表返回,可以获取指定键的所有值
#         如果键不存在则返回空列表[],可以设置默认值进行后续处理
#             getlist('键',默认值)

# 查询字符串Query String
#     获取请求路径中的查询字符串参数(形如?key1=value1&key2=value2),可以通过request.Get属性获取,返回QueryDict对象
#         参见books.urls
#     TODO:
#         查询字符串不区分请求方式,即使使客户端进行POST方式请求,依然可以通过request.GET获取请求中的查询字符串数据

# 请求体
#     请求数据格式不固定,可以是表单类型字符串,可以是JSON字符串,也可以是XML字符串,应区别对待
#     可以发送请求体数据的请求方式有POST,PUT,PATCH,DELETE

# 表单类型Form Data
#     获取前端发送的表单类型的请求体数据,可以通过request.POST属性获取,返回QueryDict对象

# 非表单类型Non-Form Data
#     非表单类型的请求体数据,django无法自动解析,可以通过request.body属性获取最原始的请求体数据,自己按照请求体格式(JSON,XML)进行解析
#     request.body返回bytes类型

# 请求头
#     可以通过request.META属性获取请求头headers中的数据,request.META为字典类型
#     常见请求头如下
#         CONTENT_LENGTH          The length of the request body (as a string)
#         CONTENT_TYPE            The MIME type of the request body
#         HTTP_ACCEPT             Acceptable content types for the response
#         HTTP_ACCEPT_ENCODING    Acceptable encodings for the response
#         HTTP_ACCEPT_LANGUAGE    Acceptable languages for the response
#         HTTP_HOST               The HTTP Host header sent by the client
#         HTTP_REFERER            The referring page, if any
#         HTTP_USER_AGENT         The client’s user-agent string
#         QUERY_STRING            The query string, as a single (unparsed) string
#         REMOTE_ADDR             The IP address of the client
#         REMOTE_HOST             The hostname of the client
#         REMOTE_USER             The user authenticated by the Web server, if any
#         REQUEST_METHOD          A string such as"GET"or"POST"
#         SERVER_NAME             The hostname of the server
#         SERVER_PORT             The port of the server (as a string)
