## TCP客户端程序开发

# 1. TCP客户端程序开发示例代码

# 导入socket模块
import socket

if __name__ == '__main__':

    # 1. 创建TCP客户端套接字
    # AF_INET:表示ipv4
    # SOCK_STEAM:tcp传输协议
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2. 和服务端套接字建立连接,网络调试助手模拟服务端
    clientSocket.connect(('192.168.44.1',8090))
    
    # 3. 发送数据到服务端
    senddetail = 'isMe'
    # 对发送数据进行编码成为二进制数据
    senddata = senddetail.encode('gbk')
    clientSocket.send(senddata)
    
    # 4. 接收服务端的数据
    # 1024表示每次接受的最大字节数
    recvdata = clientSocket.recv(1024)
    # 对二进制数据进行解码
    recvdetail = recvdata.decode('gbk')
    print(f'接受服务端的数据为:{recvdetail}')
    
    # 5. 关闭套接字
    clientSocket.close()