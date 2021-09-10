# 上下文管理器的函数实现
#     python提供了一个@contextmanger的装饰器可将一个函数成为上下文管理器,进一步简化了上下文管理器的实现方式,
#     通过yield将函数分割成两部分,yeild上面的语句在__enter__方法中执行,yield下面的语句在__exit__方法中执行,紧跟在yeild后面的参数是函数的返回值

from contextlib import contextmanager

# 加上装饰器这个代码,那下面函数创建的对象就是一个上下文管理器
@contextmanager
def myOpen(fileName, fileMode):
    try:
        file = open(fileName, fileMode)
        # yield关键字之前的代码可以认为是上文方法,负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        print('over')
        # yield关键字之后的代码可以认为是下文方法,负责释放操作对象资源
        file.close()


# 普通函数不能结合with语句使用,with语句结合上下文管理器使用
with myOpen('1.txt', 'w+') as f:
    f.write('ABC')
