# 服务端客户端命令

# 服务端

#     服务器端的命令为redis-server
#     可以使用help查看帮助文档
#         redis-server --help

#     个人习惯
#         ps aux | grep redis 查看rdis服务进程
#         kill -9 pid         杀死redis服务

# 客户端

#     客户端的命令为redis-cli
#     可以使用help查看帮助文档
#         redis-cli --help

#     连接redis
#         redis-cli

#     运行测试命令
#         ping

#     切换数据库
#         数据看没有名称,默认16个,通过0-15标识,连接redis默认选择第一个数据库
#             select 10


# 数据结构
#     redis是key-value的数据结构,每条数据都是一个键值对
#     键的类型是字符串
#     TODO: 键不能重复

#     值的类型分为五种:

#         字符串  string
#             字符串类型是redis中最为基础的数据存储类型,它在redis中是二进制安全的,意味着该类型可以接受任何格式的数据,如
#             jepg图像数据或者json对象描述信息等,在redis中字符串类型的value最多可以容纳的数据长度是512M

#         哈希    hash
#                 hash用于存储对象,对象的结构为属性.值,值的类型为string

#         列表    list
#             列表的元素类型为string,按照插入顺序排序

#         集合    set
#             无序集合,元素为string类型,元素具有唯一性,不重复,对于集合没有修改操作

#         有序集合 zset
#             sortset,有序集合,元素为string类型,元素具有唯一性,不重复,每个元素都会关联一个double类型的score,表示权重,通过权重将元素从小到大排序,对于集合没有修改操作
    
# string数据操作行为

#     1. 保存
#         如果设置的键不存在则为添加,已经存在则是修改

#         设置键值
#             set key value
#             例: 设置键为name值为mass数据
#                 set name mass
#         设置键值及过期的时间
#             setex key secconds value
#             例: 设置键为aaaa值为bbbb过期时间3秒数据
#                 setex aaaa 3 bbbb
#         设置多个键值
#             mset key1 value1 key2 value2...
#             例: 设置键为a1值为python,键为a2值为java,键为a3值为c++
#                 mset a1 python a2 java a3 c++
#         追加值
#             append key value
#             例: 向键为a1中追加值ic
#                 append a1 ic

#     2. 获取
#         根据键获取值,如果不存在此键则返回nil
#             get key
#             例: 获取键name的值
#                 get name
#         根据多个键获取多个值
#             mget key1 key2...
#                 例: 获取键a1,a2,a3的值
#                     mget a1 a2 a3

#     3. 修改           
    

#     4. 删除

# hash数据操作行为

#     1. 增加修改
#         设置单个属性
#             hset key filed value
#             例: 设置键user1属性name为mass
#                 hset user1 name mass
#         设置多个属性
#             hmset key filed values filed value2
#             例: 设置键user2的属性name为ssma,属性age为22
#                 hmset user2 name ssma age 22
    
#     2. 获取
#         获取指定键所有属性
#             hkeys key
#             例: 获取键user1所有属性
#                 hkeys user1
#         获取一个属性的值
#             hget key filed
#             例: 获取键user1属性name的值
#                 hget user1 name
#         获取多个属性的值
#             hvals key
#             例: 获取键user1所有属性的值
#                 hvals user1

#     3. 删除
#         删除整个hash键及值,使用del命令,删除属性,属性对应的值会被一并删除
#             hdel key filed1 filed2
#             例: 删除键user1的属性name
#                 hdel user1 name

# list数据操作行为

#     1. 增加
#         在(左|右)插入数据
#             lpush key value1 value2...
#             例: 从键为l1的列表左侧加入数据a,b,c
#                 lpush l1 a b c
#             rpush key value1 value2...
#             例: 从键为l2的列表右侧插入数据a,b,c
#                 rpush l1 a b c
#         在指定元素的前或后插入新元素
#             linsert key before|after 现有元素 新元素
#             例: 在键为l1的列表中元素b前加入newb
#                 linsert l1 before b newb

#     2. 获取
#         返回列表里指定范围内的元素
#             lrange key start stop
#                 start,stop为元素的下标索引
#                 索引从左侧开始,第一个元素为0
#                 索引可以是负数,表示从尾部开始计数,如-1表示最后一个元素
#             例: 获取键l1列表所有元素
#                 lrange l1 0 -1

#     3. 设置指定索引位置的元素值
#         lset key index value
#             索引从左侧开始,第一个元素为0
#             索引可以是负数,表示从尾部开始计数,如-1表示最优一个元素
#         例: 修改键l1的列表中下标为1的元素值为z
#             lset l1 1 z

#     4. 删除
#         删除指定元素
#             lrem key count value
#                 将列表中前count次出现的值为value的元素移除
#                 count>0:从头往尾移除
#                 count<0:从尾往头移除
#                 count=0:移除所有
#             例: 向列表ls中加入元素a,b,a,b,a,b
#                     lpush l1 a b a b a b
#                 从ls列表右侧开始删除2个b
#                     lrem l1 -2 b
#                 查看列表ls所有元素
#                     lrange l1 0 -1

# set数据操作行为

#     1. 增加
#         sadd key member1 member2...
#         例: 向键a1的集合中添加元素zhangsan,lisi,wangwu
#             sadd a1 zhangsan lisi wangwu

#     2. 获取
#         smembers key
#         例: 返回键a1的集合中所有元素
#             smembers a1

#     3. 删除
#         srem key
#         例: 删除键a1集合中元素wangwu
#             srem a1 wangwu

# zset数据操作行为

#     1. 增加
#         zadd key socre1 members1 score2 member2...
#         例: 向键a1的集合中添加元素wangwu,lisi,zhangsan,权重分别为3,2,1
#             zadd a1 3 wangwu 2 lisi 1 zhangsan
        
#     2. 获取
#         zrange key start stop
#             返回指定范围内的元素
#             start,stop为元素的下表索引
#             索引是从左侧开始,第一个元素为0
#             索引可以是负数,表示从尾部开始计数,如-1表示最后一个元素
#         例: 获取键a1集合中的所以元素
#             zrange a1 0 -1

#         zrangebyscore key min max
#             返回score值在min和max之间成员
#         例: 获取键a1在集合中权限值为3和4之间的成员
#             zrangebyscore 3 4

#         zscore key members
#             返回成员member的score的值
#         例: 获取键a1集合元素zhangsan的权重
#             zscore a1 zhangsan

#     3. 删除
#         删除指定元素
#             zrem key member1 member2...
#         例: 删除集合a1中元素zhangsan
#             zrem a1 zhangsan
#         删除权重在指定范围内的元素
#             zremrangebyscore key min max
#         例: 删除集合a1中权限值在5,6之间的元素
#             zremrangebyscore a1 5 6

# 键命令

#     查找键,参数支持正则表达式
#         keys pattern
#         例: 查看所有键
#             keys *
#         例: 查看名称中包含a的键
#             keys a*

#     判断键是否存在,如果存在返回1,不存在返回0
#         exists key1
#         例: 判断键a1是否存在
#             exists a1
    
#     查看可以对应的value类型
#         type key
#         例: 查看键a1的值类型,为redis支持五种类型的一种
#             type a1

#     删除键及对应值
#         del key1 key2
#         例: 删除键a1 a2
#             del a1 a2

#     设置过期时间,以秒为单位,如果没有指定多起事件则一直存在,知道使用del移除
#         expire key secconds
#             例: 设置键a1过期时间为3秒
#                 expire a1 3

#     查看有效时间,以秒为单位
#         ttl key
#             例: 查看键a1的有效时间
#                 ttl a1
