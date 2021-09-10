# 1. 开发自己的静态web服务器返回固定页面数据
#     实现步骤
#         1. 编写一个TCP服务端程序
#         2. 获取浏览器发送的http请求报文数据
#         3. 读取固定页面数据,把页面数据组装成HTTP响应报文数据发送给浏览器
#         4. HTTP响应报文数据发送完成以后,关闭服务与客户端的套接字

# 2. 示例代码

import os
import sys
import socket

if __name__ == '__main__':
    # 创建TCP服务端套接字
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    serverSocket.bind(('', 8000))
    # 设置监听
    serverSocket.listen(128)

    while True:
        # 等待接受客户端的连接请求
        newSocket, ipPort = serverSocket.accept()
        # 接受客户端的请求信息
        recvdata = newSocket.recv(4096)
        print(recvdata)
        # 响应行
        responseline = 'HTTP/1.1 200 OK\r\n'
        # 响应头
        responseheader = 'SERVER: PWS\r\n'
        # 打开文件读取文件中的数据
        with open('static\index.html', 'r') as file:
            filedata = file.read()
        # 响应体
        responsebody = filedata
        response = responseline + responseheader + '\r\n' + responsebody
        # 把数据封装成HTTP响应报文格式数据
        newSocket.send(response.encode('utf-8'))

        # 关闭服务于客户端套接字
        newSocket.close()
