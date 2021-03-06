## socket介绍

# 1. 引入
#     为了保证数据的完整性和可靠性我们使用TCP传输协议进行数据传输,通过IP地址找到指定设备,利用端口号指定应用程序接受数据,那么通信数据是如何完成传输的呢?
#     使用socket来完成

# 2. socket概念
#     socket(套接字)是进程之间通信的一个工具,进程之间想要进行网络通信需要基于这个socket

# 3. socket作用
#     负责进程之间的网络数据传输,好比数据的搬运工

# 4. 小结
#     进程之间网络数据传输可以通过sokcet完成,socket就是进程之间网络数据通信的工具

#     网络间通信的流程
#         1.通过IP地址找到网络指定设备
#         2.通过端口号找到对应进程的端口
#         3.通过TCP传输协议传输数据,保证数据可靠性
#         4.socket完成进程之间网络数据传输
