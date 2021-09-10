# 包
#   包将有联系的模块组织在一起,即放到同一个文件夹下,并且在这个文件夹创建一个名字为__init__.py文件,那么这个文件夹就称之为包
#   新建包后,包内部会自动创建__init__.py文件,这个文件控制着包的导入行为

# 导入包
# 方法一:

# 1. 导入
#     import 包名.模块名

# 2. 调用
#     包名.模块名.功能()

import myPackage.myModule

myPackage.myModule.selfinfo()  #myModule /n selfinfo


# 方法二:
# 必须在__init__.py文件中天剑__all__ = [],控制允许导入的模块列表

# 导入myPackage包下的模块1,使用这个模块内的selfinfo方法

#  1. 导入
#     from 包名 import *

# 2. 调用
#     模块名.功能()

# from myPackage import *

# myModule.selfinfo()  #myModule selfinfo