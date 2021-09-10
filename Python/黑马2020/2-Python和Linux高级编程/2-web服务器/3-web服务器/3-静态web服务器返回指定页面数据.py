# 1. 开发自己的静态web服务器返回指定页面数据
#     返回指定页面数据实现步骤
#         1. 获取用户请求资源路径
#         2. 根据请求资源路径,读取指定文件数据
#         3. 组装指定文件数据响应报文,发送给浏览器
#         4. 判断请求文件在服务端不存在,组装404状态的响应报文,发送给浏览器

# 2. 示例代码

import os,sys,socket

def main():
    # 创建TCP服务端套接字
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    # 绑定端口号
    serverSocket.bind(('',8000))
    # 设置监听
    serverSocket.listen(128)

    while True:
        # 等待接受客户端的连接请求
        newSocket,ipPort = serverSocket.accept()
        # 接受客户端的请求信息
        recvdata = newSocket.recv(4096)
        # 判断接受数据长度是否为0
        if len(recvdata) == 0:
            newSocket.close()
            return
        # 对二进制数据进行解码
        recvcont = recvdata.decode('utf-8')
        print(recvcont)
        # 对数据按照空格分割
        requestlist = recvcont.split(' ',maxsplit=2)
        # 获取请求资源路径
        requestpath = requestlist[1]
        print(requestpath)
        # 判断请求的是否是跟目录,如果是跟目录返回指定首页
        if requestpath == "/":
            requestpath = '/index.html'
        # 响应行
        responseline = 'HTTP/1.1 200 OK\r\n'
        # 响应头
        responseheader = 'SERVER: PWS\r\n'
        # requestStr = "static\" + requestpath
        # 打开文件读取文件中的数据
        with open('static'+requestpath,'rb') as file:
            filedata = file.read()
        # 响应体二进制的数据
        responsebody = filedata
        # 响应行响应头转二进制
        response = (responseline + responseheader + '\r\n').encode('utf-8') + responsebody
        # 把数据封装成HTTP响应报文格式数据
        newSocket.send(response)
        # 关闭服务于客户端套接字
        newSocket.close()

if __name__ == '__main__':
    main()