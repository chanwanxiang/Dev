# 多层继承 大于两层继承

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

    def makeCake(self):
        # 如果是先调用了父类的属性方法,父类属性会覆盖子类属性,故在调用属性前,先调用自己子类的初始化
        self.__init__()  #小括号不传self形参,前面已经使用self指代实例化的对象
        print(f'使用{self.kongfu}制作煎饼果子')

    # 子类调用父类同名方法属性,把父类同名属性方法再次封装
    # 但是为保证调用到的也是父类的属性,必须在调用方法前调用父类的初始化
    def masterMakeCake(self):
        # 再次调用初始化的原因,这里想要调用父类的同名方法属性,属性在__init__初始化位置,所有需要再次调用__init__
        Master.__init__(self)
        # 父类类名.函数()
        Master.makeCake(self)

    def schoolMakeCake(self):
        School.__init__(self)
        School.makeCake(self)

# 4. 学生学生类
class NewFreshMan(FreshMan):
    pass

# 5. 创建学生学生对象
newfre = NewFreshMan()

# 6. 继承师傅类的属性方法
newfre.makeCake()  #使用[独创煎饼果子]制作煎饼果子

# 7. 子类调用父类同名方法属性
newfre.masterMakeCake()  #使用[古法煎饼果子]制作煎饼果子
newfre.schoolMakeCake()  #使用[黑马古法煎饼果子]制作煎饼果子