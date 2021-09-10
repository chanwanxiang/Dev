# 字典
#     python中重要的数据类型,字典是有键值对组成集合,通过使用键来访问数据,效率很高,和list一样支持对数据的增删改查

# 特点
#     1)不是序列类型,没有下标概念,是无序的键值集合,内置的高级数据类型
#     2)用{}来表示字典对象,每隔键值对用逗号隔开
#     3)键必须是不可变的类型[数值,字符,元祖],值可以是任意的类型
#     4)每个键必定是唯一的,如果存在重复的键,后者会覆盖前者

# dictA = {}

# # key:value
# dictA['name'] = 'mars'
# dictA['age'] = 30
# dictA['pos'] = 'actor'
# print(type(dictA))
# print(dictA)

# # 通过键获取值
# print(dictA['name'])

# # 通过键修改值
# dictA['name'] = 'marss'

# # 通过updata函数修改值
# dictA.update({'height':180})
# print(dictA)

# # 遍历字典
# for key,value in dictA.items():
#     print('%s==%s'%(key,value),end=' ')

# 统计一个字符串中每个字符的个数

str = 'BEAUTIFUL THING NEVER ASK FOR ATTENTION'

dt = dict()

# 方法一
# for i in str:
#     if i not in dt.keys():
#         dt[i] = 1
#     else:
#         dt[i] += 1

# 方法二
for i in str:
    # dt.get(key,default=None) 返回指定键的值,如果键的值不存在是,返回该默认值
    dt[i] = dt.get(i, 0) + 1

print(dt)
