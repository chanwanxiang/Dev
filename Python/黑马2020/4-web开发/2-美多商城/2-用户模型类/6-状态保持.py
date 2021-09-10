# 状态保持

# login()方法介绍
#     1)用户登入本质
#         状态保持
#         将通过认证的用户的唯一标识信息写入到当前浏览器的cookie和服务端的session中
#     2)login()方法
#         django用户认证系统提供了login()方法
#         封装了写入session操作,帮助我们快速登入一个用户,并实现状态保持
#     3)login()位置
#         django.contrib.auth.__init__.py文件中
#     4)状态保持session数据存储位置

# login()方法登入用户
#     保存注册数据
#     登入用户,实现状态保持
#     响应注册结果
    