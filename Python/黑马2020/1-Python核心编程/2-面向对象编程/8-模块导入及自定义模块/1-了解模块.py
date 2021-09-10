# 模块和包

# 了解模块
#     python模块(Module),是一个python文件,以.py结尾,包含了python对象定义和python语句,模块能定义函数、类和变量,模块里也能包含可执行代码

# 导入模块方式
#     import 模块名
#     from 模块名 import 功能名
#     from 模块名 import *

#     import 模块名 as 别名
#     from 模块名 import 功能名 as 别名

# 语法
#     1. 导入模块
#     import 模块名

#     2. 调用功能
#     模块名.功能名()

# 需求:math模块下sqrt()开平方计算

# 方法一:improt 模块名 调用<模块名.功能名>

# python中,涉及除法运算不管参与计算的数字是否有浮点数,返回的结果一定是浮点数

import math

print(math.sqrt(9))  #3.0

# 方法二:from 模块 import 功能名 调用<功能调用(不需要书写模块名)>

from math import sqrt

print(sqrt(9))  #3.0

# 方法三:from 模块名 import * 调用<功能调用(不需要书写模块名)>

# from math import *

# print(sqrt(9))  #3.0

# as定义别名

# 模块定义别名

# 需求:运行后两秒打印Hello

import time as tt

tt.sleep(2)
print('Hello')  #Hello

# 功能别名
from time import sleep as sl

sl(2)
print('Hello')  #Hello