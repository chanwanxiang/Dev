# __all__
# 如果一个模块文件中有__all__变量,当使用 from xxxx import * 导入时,只能导入这个列表中的元素

from myModule import *

A()  #func A

# B方法没有添加到__all__列表,只有__all__列表里的方法才能导入
# B()  #NameError: name 'B' is not defined