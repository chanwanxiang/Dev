# 面向对象 继承
# python中面向对象的继承指的是多个类之间的所属关系,即子类默认继承父类的所有属性方法

# 1. 定义父类
class Animal():
    # 父类属性
    def __init__(self):
        self.sleep = 'sleep'

    # 父类方法
    def selfinfo(self):
        print(self.sleep)

# 2. 定义子类
class Cat(Animal):
    pass

# 3. 创建子类对象
cat = Cat()

# 4. 验证子类继承父类所有属性方法
cat.selfinfo()  #sleep