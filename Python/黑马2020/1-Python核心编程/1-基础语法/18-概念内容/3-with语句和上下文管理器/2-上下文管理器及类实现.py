# 上下文管理器
#     一个类只要实现了__enter__()和__exit__()这两个方法,通过该类创建的对象我们就称之为上下文管理器
#     with语句是由上下文管理器支撑,也就是说使用open函数创建的文件对象就是一个上下文管理器对象

# 示例代码

# 自定义上下文管理器类
class File(object):

    def __init__(self, fileName, fileMode):
        self.fileName = fileName
        self.fileMode = fileMode

    # 上文方法,负责返回操作对象资源,比如文件对象、数据库连接对象
    def __enter__(self):
        self.file = open(self.fileName, self.fileMode)
        return self.file

    # with语句执行完成以后自动执行__exit__方法
    # 下文方法,负责释放对象资源,比如关闭文件、关闭数据库连接对象
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('over')
        self.file.close()


# with语句结合上下文管理器对象使用
with File('1.txt', 'w+') as f:
    fd = f.write('ABC')
