# 多态

# 了解多态

# 多态指的是一类事物的多种形态(一个抽象类有多个子类,因而多态的概念依赖于继承)

# 定义:多态是一种使用对象的方法,子类重写父类方法,调用不同子类对象的相同父类方法,可以产生不同的执行效果

# 好处:调用灵活,有了多态,更容易编写通用的代码,做出通用给的编程,以适应需求的不断变化

# 实现步骤:
#     定义父类,并提供公共方法
#     定义子类,并重写父类方法
#     传递子类对象给调用者,可以看到不同子类执行效果不同

# 体验多态

# 需求:警务人员和警犬一起工作,警犬分追击敌人和追查毒品两种,携带不同的警犬,执行不同工作

# 1.定义父类,提供公共方法 警犬类 警员类
class Dog(object):
    def work(self):  #父类提供一个方法,哪怕是空方法
        print('指哪打哪')

# 2.定义子类,重新父类方法 定义两个类表示不同的警犬
class ArmyDog(Dog):  #继承Dog类
    def work(self):  #重写父类方法
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def WorkWithDog(self,dog):  #传入不同的对象,执行不同的代码,即不同的work函数
        dog.work()

# 创建对象,调用不同功能,传入不同对象,观察执行结果
# 创建警犬对象
ad = ArmyDog()
dd = DrugDog()

# 创建警员对象
sam = Person()

# 调用WorkWithDog函数,同一个类,传入不同对象,观察执行结果
sam.WorkWithDog(ad)  #追击敌人
sam.WorkWithDog(dd)  #追查毒品