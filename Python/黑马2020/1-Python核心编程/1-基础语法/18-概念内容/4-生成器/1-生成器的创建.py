# 1. 生成器的介绍
#     根据制定规则生成循环数据,当条件不成立则生成数据结束,数据不是一次性全部生成处理,而是使用一个,生成一个,可以节约大量内存空间

# 2. 创建生成器的方式
#     1. 生成器推导式
#         与列表推导式类似,只不过生成器推导式使用小括号
#     2. yield关键字
#         只要在函数中有yeild关键字就是生成器

# TODO: 生成器推导式
# myGenerator = (i*2 for i in range(3))
# print(myGenerator)

# 生成器取值使用next函数获取生成器中的下一个值
# value = next(myGenerator)
# print(value)
# value = next(myGenerator)
# print(value)
# value = next(myGenerator)
# print(value)
# value = next(myGenerator)
# print(value)  #StopIteration

# while循环获取生成器中的值
# while True:
#     try:
#         value = next(myGenerator)
#         print(value)
#     except Exception as e:
#         break

# for循环内部循环调用next()函数,获取生成器中的下一个值,当出现异常for循环内部自动进行了异常捕获
# for value in myGenerator:
#     print(value)

# 在函数李看到有yield关键字,name这个函数就是生成器
def ownGenerator():
    for i in range(3):
        print('开始生成')
        # 当程序执行到yield关键字的时候代码会暂停并把结果返回,再次启动生成器的时候会在暂停的位置继续向下执行
        yield i
        print('上次数据生成')


rlt = ownGenerator()
print(rlt)

# 获取生成器下一个值
# val = next(rlt)
# print(val)

# val = next(rlt)
# print(val)

# val = next(rlt)
# print(val)

# val = next(rlt)
# print(val)

# 生成器把所有数据生成完毕后,再次next会抛出一个StopIterration异常

for value in rlt:
    print(value)
