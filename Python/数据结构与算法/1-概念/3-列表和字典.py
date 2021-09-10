# python内置类型性能分析

# timeit模块
#     可以用来测试一小段Python代码执行速度

# class timeit.Timer(stmt='pass',setup='pass',timer=<timer function>)
#     Timer是测试小段代码执行速度的类
#     stmt参数是要测试的代码语句(statment)
#     setup参数是运行代码是需要的设置
#     timer参数是一个定时器函数,和平台有关

# timeit.Timer.timeit(number=1000)
#     Timer类中测试语句执行速度的对象方法,number参数是测试代码时的测试次数,默认为1000000次.方法返回执行代码的平均时耗,返回一个float类型的秒数

# from timeit import Timer

# def test1():
#     ls = []
#     for i in range(10000):
#         ls.append(i)

# def test2():
#     ls = []
#     for i in range(10000):
#         ls = ls + [i]

# def test3():
#     ls = [i for i in range(10000)]

# def test4():
#     ls = list(range(10000))

# def test5():
#     ls = []
#     for i in range(10000):
#         ls.extend([i])

# timer1 = Timer('test1()','from __main__ import test1')
# print('append:',timer1.timeit(1000))

# timer2 = Timer('test2()','from __main__ import test2')
# print('ls.add:',timer2.timeit(1000))

# timer3 = Timer('test3()','from __main__ import test3')
# print('列表推导:',timer3.timeit(1000))

# timer4 = Timer('test4()','from __main__ import test4')
# print('list(range(number)):',timer4.timeit(1000))

# timer5 = Timer('test5()','from __main__ import test5')
# print('extent:',timer5.timeit(1000))

# 运行结果
#     append: 0.6040402
#     ls.add: 218.9780432000000001
#     列表推导: 0.3399182999999999
#     list(range(number)): 0.20767249999999993
#     extent: 1.2539079000000002

# def test6():
#     ls = []
#     for i in range(10000):
#         ls.append(i)

# def test7():
#     ls = []
#     for i in range(10000):
#         ls.insert(0,i)

# timer6 = Timer('test6()','from __main__ import test6')
# print('append:',timer6.timeit(1000))

# timer7 = Timer('test7()','from __main__ import test7')
# print('insert:',timer7.timeit(1000))

# 运行结果
#     append: 0.5967673
#     insert: 27.2837601

# list内置操作的时间复杂度
#     Operation           Big-O Efficiency      Remarks 
#     index[]             O(1)                  索引取值
#     index assignment    O(1)                  索引赋值
#     append              O(1)
#     pop                 O(1)                  移除元素(默认最后一个)
#     pop(i)              O(n)                  移除索引值的元素
#     insert(i,item)      O(n)                  指定对象插入列表指定位置
#     del operator        O(n)
#     iteration           O(n)
#     contains(in)        O(n)                  判断是否包含某个对象
#     get Slice[x,y]      O(k)                  切片
#     del Slice           O(n)
#     set Slice           O(n+k)
#     reverse             O(n)
#     concatenate         O(k)                  列表拼接
#     sort                O(nlogn)
#     multiply            O(nk)                 列表相乘

# dict内置操作的时间复杂度
#     Operation           Big-O Efficiency      Remarks 
#     copy                O(n)                  
#     get item            O(1)
#     set item            O(1)
#     del item            O(1)
#     contains(in)        O(1)                  
#     iteration           O(n)
