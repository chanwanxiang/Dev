#  __str__()
# 如果类定义了__str__方法,就会打印从这个方法中的return数据,没有定义这个方法,打印这个对象的内存地址.

class Animal():
    def __init__(self,sleeptime):
        self.sleeptime = sleeptime

    def __str__(self):
        return '返回动物睡眠时间'

cat = Animal('10小时')
print(cat)  #返回动物睡眠时间