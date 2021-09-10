# 装饰器的使用

# 1. 装饰器的使用场景
#     1. 函数执行时间统计
#     2. 输出日志信息


import time

# 定义的装饰器
def decorator(func):
    def inner():
        # 内部函数对已有函数进行装饰
        srt = time.time()
        func()
        end = time.time()
        print('函数耗时->',end-srt)

    return inner

@decorator # work = decorator(work) -> work = inner
def work():
    for i in range(10000):
        print(i)

work()