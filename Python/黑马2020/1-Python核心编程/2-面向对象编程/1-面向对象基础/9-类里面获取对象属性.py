语法:self.属性名

class Animal():
    def sleep(self):
        print('sleep')

    def selfinfo(self):
        # 类里面获取实例属性的方法  self.属性
        print(self.cost)

# 添加实例属性
cat = Animal()
cat.cost = '10小时'

# 对象调用实例方法
cat.selfinfo()  #10小时