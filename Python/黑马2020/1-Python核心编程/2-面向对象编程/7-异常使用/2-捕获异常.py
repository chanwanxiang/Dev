# 了解异常类型

# 异常类型NameError
# print(name)

#ZeroDivisionError
# print(1/0)

# 捕获异常类型
#     1.如果尝试执行的代码块的异常类型和要捕获的异常类型不一致,则无法捕获异常
#     2.一般try下方只放一行尝试执行的代码

# try:
#     可能发生错误的代码
# except 异常类型:
#     如果捕获到该异常类型执行的代码

try:
    print(name)
except NameError:
    print('NameError错误')  #NameError错误

# 捕获多个指定异常

# 当捕获多个异常时,可以把要捕获的异常类型的名字,方法except后,并使用元祖的方式进行书写
try:
    print(1/0)
except (NameError,ZeroDivisionError):
    print('错误')  #错误

# 捕获异常描述信息

try:
    print(name)
except (NameError,ZeroDivisionError) as msg:
    print(msg)  #name 'name' is not defined

# 捕获所有异常

# Exception是所有程序异常类的父类

try:
    print(1/0)
except Exception  as msg:
    print(msg)  #division by zero

# 异常的else,finally

try:
    print(1)
except Exception as msg:
    print(msg)
else:
    print('else是没有异常执行的代码块')  #else是没有异常执行的代码块
finally:
    print('finally无论有无异常都要执行的代码块')  #finally无论有无异常都要执行的代码块