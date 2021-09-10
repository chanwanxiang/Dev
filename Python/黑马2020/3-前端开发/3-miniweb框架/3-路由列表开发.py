# 路由列表功能开发

# 1. 什么是路由?
#     路由就是请求的url到处理函数的映射

#     通过路由列表保存每个路由
#     请求路径         处理函数
#     /login.html     login函数
#     /index.html     index函数
#     /center.html    ceter函数

# 2. 在路由列表添加路由
#     定义路由列表
#     routelist = [
#         ('/index.html',index),
#         ('/center.html',certer)
#     ]

# 3. 根据用户请求遍历路由列表处理用户请求
#     示例代码详见webdemo文件

# 4. 小结
#     路由是请求url到处理函数的映射
#     路由列表是用来保存每一个设置好的路由
#     用户的动态资源请求通过遍历路由列表找到对应处理函数完成
