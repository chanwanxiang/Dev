## HTTP请求报文

# 1. HTTP请求报文

# HTTP最常见的请求报文有两种
#     1. GET方式的请求报文
#     2. POST方式的请求报文

# 2. GET请求报文分析

# ---- 请求行 ----
# GET /xxxx HTTP/1.1  #GET请求方式 请求资源路径 HTTP协议版本
# ---- 请求头 -----
# Host: www.itcast.cn  #服务器的主机地址和端口号,默认是80
# Connection: keep-alive #和服务端保持长连接
# Upgrade-Insecure-Requests: 1 #让浏览器升级不安全请求,使用https请求
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36  #用户代理,也就是客户端的名称
# Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8 #可接受的数据类型
# Accept-Encoding: gzip, deflate #可接受的压缩格式
# Accept-Language: zh-CN,zh;q=0.9 #可接受的语言
# Cookie: pgv_pvi=1246921728; #登录用户的身份标识
# ---- 空一行 ----

# 3. POST请求报文分析

# ---- 请求行 ----
# POST /xmweb?host=mail.itcast.cn&_t=1542884567319 HTTP/1.1 #POST请求方式 请求资源路径 HTTP协议版本
# ---- 请求头 ----
# Host: mail.itcast.cn #服务器的主机地址和端口号,默认是80
# Connection: keep-alive #和服务端保持长连接
# Content-Type: application/x-www-form-urlencoded  #告诉服务端请求的数据类型
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 #客户端的名称
# ---- 空一行 ----
# ---- 请求体 ----
# username=hello&pass=hello #请求参数

# 4. 小结
#     一个HTTP请求报文可以由请求头,请求行,空一行,请求体组成
#     请求行是由三部分组成
#         1. 请求方式
#         2. 请求资源路径
#         3. HTTP协议版本
#     GET方式的请求报文没有请求体,只有请求行,请求头,空一行组成
#     POST方式的请求报文可以有请求行,请求头,空一行,请求体四部分组成,注意POST方式可以没有请求体,但这种格式十分少见

## HTTP响应报文

# 1. HTTP响应报文分析

# --- 响应行 ---
# HTTP/1.1 200 OK #HTTP协议版本 状态码 状态描述
# --- 响应头 ---
# Server: Tengine #服务器名称
# Content-Type: text/html; charset=UTF-8 #内容类型
# Transfer-Encoding: chunked #发送给客户端内容不确定内容长度,发送结束的标记是0\r\n, Content-Length表示服务端确定发送给客户端的内容大小,但是二者只能用其一。
# Connection: keep-alive #和客户端保持长连接
# Date: Fri, 23 Nov 2018 02:01:05 GMT #服务端的响应时间
# --- 空一行 ---
# --- 响应体 ---
# <!DOCTYPE html><html lang=“en”> …</html> #响应给客户端的数据

# 2. HTTP状态码介绍

# HTTP状态码是用于表示web服务器响应状态的3位数字代码

# 状态码  说明
# 200     请求成功
# 307     重定向
# 400     错误的请求,请求地址或者参数有误
# 404     请求资源在服务器中不存在
# 500     服务器内部源代码出现错误

# 3. 小结
#     一个HTTP响应报文是由响应行,响应头,空一行和响应体4个部分组成
#     响应行是由HTTP协议版本,状态码,状态描述三个部分组成,最常见的状态码是200