## 关系型数据库管理系统

# 1. 关系型数据库管理系统的介绍
#     数据库管理系统是为管理关系型数据库而设计的软件系统,如果大疆想要使用关系型数据库就需要安装数据库管理系统,本质上是一个应用软件

#     关系型数据库管理系统可以分为
#         关系型数据库服务端软件
#         关系型数据库客户端软件

#     关系型数据库服务端软件
#         主要负责管理不同的数据库,而每个数据库里面有一些列的数据文件,数据文件就是用来存储数据的,其实数据库就是一系列数据文件的集合
#     关系型数据库客户端软件
#         主要负责和关系型数据库服务端软件进行通信,向服务端传输数据或者从服务端获取数据
    
#     说明
#         1. 用户操作关系型数据库客户端,实现数据库相关操作
#         2. 关系数据库客户端借助网络使用SQL语言和关系型数据库服务端进行数据通信
#         3. 关系型数据库服务端管理者不同的数据库,每个数据库会有一些列的数据文件,数据都保存在数据文件里面,每个数据库可以理解为一个文件夹

# 2. SQL的介绍
#     SQL(Structured Query Language)是结构化查询语言,是一种用来操作RDBMS的数据库语言,也就是说通过SQL可以操作oracle,mysql等关系型数据库
#     SQL的作用是实现数据库客户端和数据库服务端之间的通信,SQL就是通信桥梁

#     SQL语言主要分为
#         DQL:数据查询语言,用于对数据进行查询,如SELECT
#         DML:数据操作语言,对数据进行添加修改删除,如INSERT,UPDATE,DELETE
#         DDL:数据定义语言,进行数据库、表的管理等,如CREAT,DROP
#         TPL:事物处理语言,对事物进行处理,包括BEGIN TRANSACTION,COMMIT,ROLLBACK
#         DCL:数据控制语言,进行授权与权限回收,如GRANT,REVOKE

#     SQL语言不区分大小写

# 3. 小结
#     关系型数据库管理系统是一个软件,可以管理不同的数据库.想对数据库进行操作安装对应的关系型数据库管理系统软件即可
#     SQL的作用是实现数据库客户端和数据库服务端之间通信桥梁