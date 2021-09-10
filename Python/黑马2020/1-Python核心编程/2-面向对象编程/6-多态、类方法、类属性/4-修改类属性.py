# 修改类属性

# TODO:类属性只能通过类对象修改,不能通过实例对象修改,如果通过实例对象修改,表示创建了一个同名实例属性

class Cat(object):
    eyes = 2

mm = Cat()

# # 1. 类.类属性 修改类属性
# Cat.eyes = 1
# print(Cat.eyes)  #1
# print(mm.eyes)  #1

# 2. 测试通过对象修改类属性,结果是创建了一个同名实例属性
mm.eyes = 1
print(Cat.eyes)  #2
print(mm.eyes)  #1