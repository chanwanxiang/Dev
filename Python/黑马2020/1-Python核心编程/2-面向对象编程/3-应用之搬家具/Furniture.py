# 搬家具

# 需求
# 将小于房子剩余面积的家具摆放到房子中

# 步骤分析
# 涉及两个事物:房子和家具,故案例涉及两个类,房子类和家具类

# 定义类

# 房子类:
#     实例属性
#         房子地理位置
#         房子占地面积
#         房子剩余面积
#         房子内的家具列表
#     实例方法
#         容纳家具
#     显示房屋信息

# 家具类
#     家具名称
#     家具占地面积

# 定义家具的类
class Furniture():

    def __init__(self,name,area):
        # 家具名称
        self.name = name
        # 家具占地面积
        self.area = area


class Home():

    def __init__(self,addr,area):
        # 地理位置
        self.addr = addr
        # 房屋面积
        self.area = area
        # 剩余面积
        self.freeArea = area
        # 家具列表信息
        self.furniture = []

    def __str__(self):
        # 显示房屋信息
        return f'房屋地理位置{self.addr},房屋面积{self.area},剩余面积{self.freeArea},家具列表{self.furniture}'

    def addFurniture(self,item):  #item 家具对象
        # 容纳家具
        if item.area <= self.freeArea:
            # 剩余房屋面积
            self.freeArea -= item.area
            # 家具列表
            self.furniture.append(item.name)
        else:
            print(f'房屋剩余面积过小,无法容纳家具{item.name}')


# #创建家具对象
bed = Furniture('双人床',6)
sofa = Furniture('沙发',10)
desk = Furniture('桌子',985)

# #创建房子对象
myHome = Home('北京',1000)

print(myHome)

myHome.addFurniture(bed)
myHome.addFurniture(sofa)
myHome.addFurniture(desk)

print(myHome)