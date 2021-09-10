# 模块定位顺序

# 当导入一个模块,python解释器对模块位置的搜索顺序:
#     1. 当前目录
#     2. 如果不在当前目录,python则搜索在shell变量pythonpath下的每个目录
#     3. 如果都找不到,python会查看默认路径

# 模块搜素路径存储在system模块的sys.path变量中,变量里包含当前目录,pythonpath和由安装过程决定的默认目录

# 注意
#     1. 自己的文件名不要和已有的模块名重复,否则导致模块功能无法使用
#     2. 使用from模块名import功能时候,如果功能名字重复,调用到的是最后定义或导入的功能

# 避免名字重复
# import 模块名 是否担心功能名字重复的问题  --不需要  模块名.功能名 才能调用导入的功能

import time
print(time)  #<module 'time' (built-in)> 内置模块time

time = 1
print(time)  #1

# 为什么变量也能覆盖模块?
# 在python语言中,数据是通过`引用`传递的