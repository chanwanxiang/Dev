# TODO: 带有参数的装饰器,其实就是定义了一个函数,让函数接受参数,在函数内部返回的是一个装饰器,再使用函数内部的装饰器对下面的函数进行装饰

# 装饰器只能接受一个参数并且是函数类型
def returnDecorator(flag):
    def decorator(func):
        def inner(a, b):
            if flag == '+':
                print('正在努力执行加法计算')
            elif flag == '-':
                print('正在努力执行减法运算')
            func(a, b)
        return inner
    return decorator

# 加法计算
# decorator = returnDecorator('+') , @decorator -> addNum = decorator(addNum) -> inner
@returnDecorator('+')
def addNum(a, b):
    rlt = a+b
    print(rlt)

# 减法计算
@returnDecorator('-')
def subNum(a, b):
    rlt = a-b
    print(rlt)


addNum(1, 2)
subNum(1, 2)

# 小结:
#     使用带有参数的装饰器,起始就是在装饰器外面又包裹了一个函数,使用该函数接收参数,返回是装饰器,因为@符号需要配合装饰器使用
