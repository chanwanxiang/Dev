## HTTP协议

# 1. HTTP协议介绍
#     HTTP全程(Hyper Text Transfer Protocol),超文本传输协议
#     超文本即超级文本的简称,是指超越文本限制或者连接,如图片,音频等都属于超文本
#     HTTP是一种基于TCP,面向无连接的,请求响应的传输协议

# 2. HTTP协议的作用
#     规定了浏览器和web服务器通信数据的格式,也就是说浏览器和web服务器通信需要使用HTTP协议

# 3. 浏览器访问web服务器的通信过程

#     1. 通过DNS(域名解析服务器)将域名解析成IP地址
#     2. 获取到IP地址
#     3. 建立连接
#     4. 发送HTTP请求
#     5. 根据请求获取资源
#     6. 服务器主机返回资源到web服务器
#     7. 返回HTTP请求

# 4. 小结
#     HTTP是超文本传输协议,基于TCP传输数据的,规定了浏览器和web服务器通信数据的格式

## URL

# 1. URL的概念
#     URL(Uniform Resource Locator),统一资源定位符,即通俗理解的网络资源地址,简称网址,通过它可以找到网络中对应的资源数据

# 2. URL的组成
#     http://news.163.com/photo?page=1&count=10
#     1. 协议部分 http:// https:// ftp://
#     2. 域名部分 news.163.com
#     3. 资源路径部分 /photo/
#     4. 查询参数部分 ?page=1&count=10 ?后面表示第一个参数,后面的参数都是用&进行连接

#     域名就是IP地址的别名,它是由点进行分割的英文字母和数据组成的,使用域名的目的就是方便记住某台主机IP地址

# 3. 小结
#     URL就是网络资源地址,通过URL能够找到网络中对应的资源数据
#     URL组成部分:
#         1. 协议部分
#         2. 域名部分
#         3. 资源路径部分
#         4. 查询参数部分[可选]