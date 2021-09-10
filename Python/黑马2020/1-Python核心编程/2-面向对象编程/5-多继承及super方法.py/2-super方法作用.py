# 多层继承 大于两层继承

# 1. 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子]'

    def makeCake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 2. 学校类
class School(Master):
    def __init__(self):
        self.kongfu = '[黑马古法煎饼果子]'

    def makeCake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

        # 2.1 super()带参数写法
        # super(School,self).__init__()
        # super(School,self).makeCake()

        # 2.2 super()无参数写法
        super().__init__()
        super().makeCake()

# 3. 学生类 同时继承师傅类学校类
class FreshMan(School):
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

    # 一次性调用父类的同名属性和方法,定义一个函数同事封装父类同名属性方法
    def makeOldCake(self):

        # 方法一:代码冗余,父类类名如果发生变化,这里代码需要频繁修改
        # Master.__init__(self)
        # Master.makeCake(self)

        # School.__init__(self)
        # School.makeCake(self)

        # 方法二:super()
        
        # 2.1 super(当前类名,self).函数()
        # super(FreshMan,self).__init__()
        # super(FreshMan,self).makeCake()

        # 2.2 无参数super()
        super().__init__()
        super().makeCake()

# 4. 创建学生对象
fre = FreshMan()

# 5. 一次性调用父类的同名属性方法
fre.makeOldCake()  #使用[古法煎饼果子]制作煎饼果子 使用[黑马古法煎饼果子]制作煎饼果子

# 使用super()可以自动查找父类,调用顺序遵循__mro__类属性顺序,比较适合单继承使用