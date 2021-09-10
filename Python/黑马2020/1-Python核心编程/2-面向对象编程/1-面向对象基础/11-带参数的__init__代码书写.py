# 带参数的__init__()  对不同的对象设置不同的初始化属性

class Animal():
    def __init__(self,sleeptime):
        self.sleeptime = sleeptime

    def selfinfo(self):
        print(self.sleeptime)

cat = Animal('1小时')
dog = Animal('8小时')

cat.selfinfo()
dog.selfinfo()