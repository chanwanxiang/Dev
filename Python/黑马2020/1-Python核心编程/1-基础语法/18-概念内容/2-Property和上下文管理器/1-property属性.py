# property属性

# 1. property属性介绍
#     定义property属性就是把一个方法当做属性进行使用,这样做可以简化代码使用

#     定义property属性的两种方式
#         1. 装饰器方式
#         2. 类属性方式

# 2. 装饰器的方式

# class Student(object):
#     def __init__(self):
#         # 私有属性
#         self.__age = 0

#     def age(self):
#         print('获取属性')
#         return self.__age


# stud = Student()
# age = stud.age()
# print(age)

# property and


# class Student(object):
#     def __init__(self):
#         # 私有属性
#         self.__age = 0

#     # 当对象调用age属性的时候就会执行下面的方法
#     @property
#     def age(self):
#         print('获取属性')
#         return self.__age

#     @age.setter
#     def age(self, newAge):
#         print('设置属性')
#         if 0 <= newAge <= 100:
#             self.__age = newAge
#         else:
#             print('百岁')


# TODO:使用装饰器方式的property属性那么方法名要保持一致

# stud = Student()
# age = stud.age
# print(age)

# stud.age = 20
# age = stud.age
# print(age)

# 3. 类属性方式

class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    def getAge(self):
        print('获取属性')
        return self.__age

    def setAge(self, newAge):
        print('设置属性')
        if 0 <= newAge <= 100:
            self.__age = newAge
        else:
            print('百岁')

    # getAge 表示获取age属性时候执行方法
    # setAge 表示设置age属性时候执行方法
    age = property(getAge, setAge)


stud = Student()
age = stud.age
print(age)

stud.age = 20
age = stud.age
print(age)
