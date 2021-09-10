# 类装饰器
#     使用类装饰已有的函数

class MyDecorator(object):
    def __init__(self,func):
        self.__func = func
        pass

    # 实现__call__方法,让对象变成可调用对象,可调用的对象能够像函数使用
    def __call__(self,*args,**kwargs):
        # 对已有的函数封装
        print('课已讲完')
        self.__func()

@MyDecorator # @MyDecorator -> show = MyDecorator(show)
def show():
    print('快要放学')

# 执行show -> show() -> 对象()
show()

# 扩展: 函数之所以能够调用是因为函数内部实现了__call__

def sample():
    print('HAHA')

print(dir(sample))