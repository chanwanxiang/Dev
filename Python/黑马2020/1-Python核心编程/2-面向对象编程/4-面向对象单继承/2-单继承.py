# 单继承
# 背景:师傅传授技术唯一徒弟

# 1. 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子]'

    def makeCake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 2. 徒弟类
class FreshMan(Master):
    pass

# 3. 创建徒弟对象
fre = FreshMan()

# 4. 继承师傅类的属性方法
fre.makeCake() #使用[古法煎饼果子]制作煎饼果子