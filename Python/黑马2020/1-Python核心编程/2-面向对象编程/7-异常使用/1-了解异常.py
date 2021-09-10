# 异常

# 了解异常

# 当检测到一个错误时,解释器就无法继续执行了,反而出现了一些错误的提示,这就是所谓的异常

# 异常写法

# 语法
#     try:
#         可能发生错误的代码
#     except:
#         如果出现异常执行此代码

# 需求:尝试以只读模式打开文件,如果文件不存在,则以写的模式打开
try:
    f = open('Test.txt','r')
except:
    f = open('Test.txt','w')

# 了解异常类型

# 异常类型NameError
# print(name)

#ZeroDivisionError
# print(1/0)