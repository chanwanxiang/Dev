# 私有权限

# 获取修改私有属性值
# 在python中,一般在类里面定义函数名getXX来获取私有属性,定义setXX用来修改私有属性值

# 1. 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子]'

    def makeCake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 2. 学校类
class School(object):
    def __init__(self):
        self.kongfu = '[黑马古法煎饼果子]'

    def makeCake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 3. 学生类 同时继承师傅类学校类
class FreshMan(Master,School):
    def __init__(self):
        # 重写父类同名属性
        self.kongfu = '[独创煎饼果子]'
        # 私有属性
        self.__money = 200000

    # 获取私有属性
    def getMoney(self):
        return self.__money

    # 修改私有属性
    def setMoney(self):
        self.__money = 500

    def makeCake(self):
        # 如果是先调用了父类的属性方法,父类属性会覆盖子类属性,故在调用属性前,先调用自己子类的初始化
        self.__init__()  #小括号不传self形参,前面已经使用self指代实例化的对象
        print(f'使用{self.kongfu}制作煎饼果子')

    # 私有属性
    def __selfinfo(self):
        print(self.__money)

# 4. 学生学生类
class NewFreshMan(FreshMan):
    pass

# 5. 创建学生学生对象
newfre = NewFreshMan()

# 6. 无法继承父类私有属性方法
# print(newfre.__money)  #AttributeError: 'NewFreshMan' object has no attribute '__money'
# newfre.__selfinfo()  #AttributeError: 'NewFreshMan' object has no attribute '__selfinfo'

# 7. 获取私有属性
print(newfre.getMoney())  #20000

# 修改私有属性
newfre.setMoney()  #500

# 获取修改后的私有属性
print(newfre.getMoney())  #500