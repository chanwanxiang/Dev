# NoSQL介绍
#     泛指非关系型数据库
#     不支持sql语法
#     存储结构跟传统关系型数据库中关系完全不同,NoSQL中存储的都是KV形式
#     NoSQL的世界中没有一种通用语言,每种NoSQL数据库都有自己的api和语法,以及适合的业务场景
#     NoSQL产品种类有redis,mongodb等

# NoSQL和SQL数据库比较
#     使用场景不同,SQL数据库适合用于关系特别复杂的数据查询场景,NoSQL反之
#     事物特性支持,SQL对事物(保证数据的一致性)的支持非常完美,而NoSQL基本不支持事物

# Redis简介
#     redis是一个开源支持网络,可基于内存亦可持久化的日志型、KV数据库,提供多种语言的API

# Redis特性
#     支持数据的持久化,可以将内存中的额数据保存在磁盘中,重启的时候可以再次加载进行使用
#     除了支持简单的KV类型数据,同时提供list、set、zset、hash等数据结构存储
#     支持数据备份,即master-slave模式数据备份

# Redis优势
#     性能极高-读写速度11万次/s,写的速度是81000次/s
#     丰富的数据类型,支持二进制案例的string、lists、hashs、sets及order sets数据类型操作

# Redis安装
#       linux宝塔一键安装

# Redis核心配置
#     reids的配置信息在redis.conf下
#     配置选项
#         绑定IP:如果需要远程访问,将此行注释,或绑定一个真实IP
#             bind 127.0.0.1

#         端口:默认6379
#             port 6379

#         是否以守护进程运行
#             如果以守护进程运行,则不会在命令行阻塞,类似于服务
#             如果以非守护进程运行,则当前终端被阻塞
#             设置yes表示守护进程,设置no表示守护非守护进程
#             daemonize yes

#         数据文件
#             dbfilename dump.rdb
