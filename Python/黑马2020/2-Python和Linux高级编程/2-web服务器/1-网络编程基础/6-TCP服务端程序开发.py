## TCP服务端程序开发

# 1. TCP服务端程序开发示例代码

# 导入socket模块
import socket

if __name__ == '__main__':
    
    # 1. 创建TCP服务端套接字,serverSocket只复制等待接收客户端的连接请求,收发消息不使用该套接字
    serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口号复用,表示服务端程序退出端口号立即释放
    # SOL_SOCKET 表示当前套接字
    # SOL_REUSEADDR 表示复用端口号选项
    serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    
    # 2. 绑定端口号
    # 第一个参数表示IP地址,一般不用指定,表示本机的任何一个IP均可
    # 第二个参数表示端口号
    serverSocket.bind(('',9090))
    
    # 3. 设置监听
    # 128:表示最大等待建立连接的个数
    serverSocket.listen(128)
    
    # 4. 等待接收客户端的连接请求
    # TODO: 当客户端和服务端建立连接成功,会返回一个新的套接字
    newClient,ipPort = serverSocket.accept()
    print(f'客户端IP和端口号为{ipPort}')
    
    # 5. 接受客户端的数据
    recvdata = newClient.recv(1024)
    recvdetail = recvdata.decode('gbk')
    print(f'接收客户端数据为{recvdetail}')

    # 6. 发送数据到客户端
    senddata = '问题正在处理'
    senddetail = senddata.encode('gbk')
    newClient.send(senddetail)
    newClient.close()

    # 7. 关闭服务端套接字,表示服务端以后不再等待接受客户端的连接请求
    serverSocket.close()