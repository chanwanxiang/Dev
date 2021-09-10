# 子类重写父类同名方法和属性

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

    def selfinfo(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 3. 学生类 同时继承师傅类学校类
class FreshMan(Master,School):
    def __init__(self):
        # 重写父类同名属性
        self.kongfu = '[独创煎饼果子]'

    def selfinfo(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 4. 创建徒弟对象
fre = FreshMan()

# 5. 继承师傅类的属性方法
fre.makeCake()  #使用[独创煎饼果子]制作煎饼果子
# 当一个类有多个父类的时候,默认使用第一个父类的同名属性和方法

# 结论:如果子类和父类拥有同名属性和方法,子类创建对象调用属性方法时,调用到的是子类里的同名属性方法