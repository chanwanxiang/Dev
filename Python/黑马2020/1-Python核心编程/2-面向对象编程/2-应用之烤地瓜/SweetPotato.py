# 烤地瓜
    # 需求主线:
    # 1. 被烤时间对应地瓜状态
    #      0-3分钟 生的
    #      3-5分钟 半生不熟
    #      5-8分钟 熟的
    #      超过8分钟 糊了
    # 2. 添加调料
    #     用户按照自己的意愿添加调料

# 步骤分析
# 需求涉及一个事物:地瓜,故案例涉及一个类:地瓜类

# 地瓜的属性
    # 被烤的时间
    # 地瓜的状态
    # 添加的调料

# 地瓜的方法
    # 被烤
    #     用户根据意愿设定每次烤地瓜的时间
    #     判断地瓜被烤总时间在哪个区间,修改地瓜状态
    # 添加调料
    #     用户根据自己意愿设定添加的调料
    #     将用户添加的调料存储
    # 显示对象信息


class SweetPotato():
    def __init__(self):
    	# 被烤时间
    	self.cookTime = 0
    	# 烤的状态
        self.state = '生的'
        # 调料列表
        self.condiment = []

    def cook(self,time):
    	# 被烤时间
    	self.cookTime += time

    	if self.cookTime < 3:
    		self.state = '生的'
    	elif 3 <= self.cookTime < 5:
    		self.state = '半生不熟'
    	elif 5 <= self.cookTime < 8:
    		self.state = '熟了'
    	elif self.cookTime >= 8:
    		self.state = '糊了'

    def addCondiments(self,condiment):
    	# 添加调料方法
    	self.condiment.append(condiment)

    def __str__(self):
    	return f'这个地瓜烤了{self.cookTime}分钟,状态{self.state},调料{self.condiment}'

 # 创建实例对象
sp = SweetPotato()
# 打印初始状态
print(sp)

sp.cook(3)
sp.addCondiment('辣椒面儿')
print(sp)

sp.cook(2)
print(sp)