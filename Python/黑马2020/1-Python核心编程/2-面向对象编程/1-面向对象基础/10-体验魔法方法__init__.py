# __init__()方法的作用:初始化对象
    # 在创建一个对象时默认被调用,不需要手动调用
    # __init__(self)中的self参数,不需要开发者传递,python解释器会自动把当前的对象引用传递过去.

class Animal():
    def __init__(self):
        # 添加实例属性
        self.sleeptime = '10小时'

    # 添加实例方法
    def selfinfo(self):
        print(self.sleeptime)

# 实例对象
cat = Animal()

# 调用实例方法
cat.selfinfo()