## 搭建Python自带静态web服务器

# 1. 静态web服务器是很么?
#     可以为发出请求的浏览器提供静态文档的程序
#     平时浏览新闻数据网站,新闻数据每天都在发生变化,那访问的这个页面就是动态的,而我们开发的是静态的,页面数据不会发生变化

# 2. 如何搭建Python自带的静态web服务器?
#     搭建Pyhotn自带的静态web服务器使用pyhton -m http.server 端口号
#     TODO: -m表示运行包里面的模块,执行这个命令的时候,需要你进入你自己指定静态文件目录,然后通过浏览器就能访问对应的HTML文件了,这样一个静态web服务器就搭建完成

# 3. 访问搭建的静态web服务器?

# 4. 查看浏览器和搭建的静态web服务器的通信过程
#     使用浏览器F12键查看

# 5. 小结
#     静态web服务器是为发出请求的浏览器提供静态文档的程序
#     搭建Python自带的web服务器使用python -m http.server 端口号 这个命令即可,端口号不指定默认是8000