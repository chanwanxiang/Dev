# 多任务版TCP服务端程序开发

# 1. TCP服务端程序开发示例代码

# 导入socket模块
import socket
import threading


# 处理客户端请求数据
def handleClientRequest(newClient, ipPort):
    # 5. 循环接受客户端的数据
    while True:
        recvdata = newClient.recv(1024)
        # 容器类型判断是否可以直接使用if语句进行判断,如果容器类型里面有数据表示条件成立,否则条件失败
        # 容器类型:列表,字典,元祖,字符串,set,range,二进制数据
        if recvdata:
            recvdetail = recvdata.decode('gbk')
            print(f'接收客户端数据为{recvdetail},{ipPort}')

            # 6. 发送数据到客户端
            senddata = '问题正在处理'
            senddetail = senddata.encode('gbk')
            newClient.send(senddetail)
        else:
            print(f'客户端已下线{ipPort}')
            break
    # 关闭和客户端通信
    newClient.close()


if __name__ == '__main__':
    # 1. 创建TCP服务端套接字,serverSocket只复制等待接收客户端的连接请求,收发消息不使用该套接字
    # socket.AF_INET 与IPV4地址族进行通信
    # socket.SOCK_STREAM 面向连接socket,TCP协议
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用,表示服务端程序退出端口号立即释放
    # SOL_SOCKET 表示当前套接字
    # SOL_REUSEADDR 表示复用端口号选项
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 2. 绑定端口号
    # 第一个参数表示IP地址,一般不用指定,表示本机的任何一个IP均可
    # 第二个参数表示端口号
    serverSocket.bind(('', 9090))

    # 3. 设置监听
    # 128:表示最大等待建立连接的个数
    serverSocket.listen(128)

    # 4. 等待接受客户端的连接请求
    # TODO: 当客户端和服务端建立连接成功,会返回一个新的套接字

    # 循环等待接受客户端的连接请求
    while True:
        # 主线程专门等待接受客户端连接请求
        newClient, ipPort = serverSocket.accept()
        print(f'客户端IP和端口号为{ipPort}')

        # 当客户端与服务端建立连接成功,创建子线程,让子线程专门负责接受客户端的消息
        subThread = threading.Thread(
            target=handleClientRequest, args=(newClient, ipPort))
        # 设置守护主线程,主线程退出子线程销毁
        subThread.setDaemon(True)
        # 启动子线程
        subThread.start()

    # 7. 关闭服务端套接字,表示服务端以后不再等待接受客户端的连接请求
    # serverSocket.close()  #服务端程序需要一直运行,关闭服务端的套接字代码可以省略不写
