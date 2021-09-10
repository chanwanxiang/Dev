# 猜拳游戏
# import random
# coun = 1
# while coun <= 10:
#     person = int(input('请出拳:[0:石头,1:剪刀,2布]'))
#     computer = random.randint(0,2)
#     if person==0 and computer==1:
#         print('好厉害,你赢了')
#         pass
#     elif person==1 and computer==2:
#         print('好厉害,你赢了')
#         pass
#     elif person==2 and computer==0:
#         print('好厉害,你赢了')
#         pass
#     elif person==computer:
#         print('平手')
#         pass
#     else:
#         print('你输了')
#         pass
# coun+=1

#直角三角形
# row = 1
# while row <= 7:
#     j=1 #控制打印图形数量
#     while j <=row:
#         print('*',end=' ')
#         j+=1
#         pass
#     print()
#     row+=1
#     pass

# 控制行数
for i in range(1,8):
    # 控制打印数量
    for j in range(1,i+1):
        if j <=i:
            print('*',end=' ')
    print()



#倒立直角三角形
# row = 7
# while row>=1:
#     i=1 #控制打印图形数量
#     while i<=row:
#         print('*',end='')
#         i+=1
#         pass
#     print()
#     row-=1
#     pass

#等腰三角形
# row=1
# while row<=7:
#     i=1
#     while i<=7-row:#控制打印空格数量
#         print(' ',end='')
#         i+=1
#         pass
#     j=1
#     while j<=2*row-1:
#         print('*',end='')
#         j+=1
#         pass
#     print()
#     row+=1

#倒立等腰三角形
# row=7
# while row>=1:
#     i=1
#     while i<=7-row:#控制打印空格数量
#         print(' ',end='')
#         i+=1
#         pass
#     j=1
#     while j<=2*row-1:#控制打印*数量
#         print('*',end='')
#         j+=1
#         pass
#     print()
#     row-=1

# tags = 'ILOVEPUBG' #字符串本身就是一个字符类型的集合
# for i in tags:
#     print(i)
#     pass

#range 此函数可以生成一个数据集合列表
#range(起始,结束:步长) 步长不能为0

# sum = 0
# for data in range(1,101):#左边包含右边不包含
#    sum+=data
#    pass
# print(sum)

# print('----for的使用----')
# for data in range(50,201):
#     if data%2 == 0:
#         print(data,end=' ')

#break和continue
#break 代表中断结束 满足条件直接的结束本次循环
#continue 结束本次循环 继续进行下次循环

# sum = 0
# for i in range(1,51):
#     if sum > 100:
#         print('执行到%d就不在执行了'%i)
#         break
#     sum += i
# print(sum)

# for i in range(1,101):
#     if i%2==0:
#         continue
#     print(i)

# for i in 'HELLOPYTHON':
#     # if i == 'O':
#     #     break
#     if i == 'O':
#         continue
#     print(i)

# #for打印99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(j,i,j*i),end=' ')
#         pass
#     print()

#for....else.... 用户三次输入密码,错误账号将会冻结
# account = 'wxchan'
# pswd = '123'
# for i in range(3):
#     acot = input('输入账号:')
#     paw = input('输入密码:')
#     if account == acot and pswd == paw:
#         print('登录成功')
#         break
# else:
#     print('账号已被冻结')

# 作业:猜年龄小游戏
# 1.允许用户最多尝试3次
# 2.每尝试3次后如果还没有才对,就问用户是否还想继续,如果回答Y或者y,继续.
# 3.如果猜对了,就直接退出.

# for i in  range(3):
# item = 0
# count = 3
# while item <=3:
#     age = int(input('输入猜测年龄:'))
#     if age > 25:
#         print('猜的大了')
#     elif age < 25:
#         print('猜的小了')
#     else:
#         print('你猜对了')
#         break
# #else:
#     item +=1
#     if item == 3:
#             choose = input('已猜3次,想不想继续猜呢,回复Y或N:')
#             if choose == 'Y' or choose == 'y':
#                 item = 0
#             elif choose == 'N' or choose == 'n':
#                 item = 4
#             else:
#                 print('请输入正确字符')

# 小王身高1.75 体重80.5千克 根据BMI公式帮小王计算它的BMI指数
# 过轻 30以下
# 正好 30到50
# 过重 50以上165

# height = int(input('输入身高,单位厘米:'))
# weight = float(input('输入体重,单位千克:'))
# BMI = (weight/height)**2
# if BMI < 30:
#     print('过轻BMI=%s'%BMI)
# elif 30 < BMI <50:
#     print('正好')
# else:
#     print('过重')

# 字符串操作
# demo = 'Python'
# print('获取第一个字符:%s'%demo[0])
# for item in demo:
#     print(item,end=' ')
# 首字母大写
# name = 'mark'
# print(name.capitalize())
# 去除空格
# a = ' Apple '
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())

# 查找是否在字符存在
# data = 'I LOVE PYTHON'
# print(data.find('x'))
# print(data.find('O'))
# print(data.startswith('I'))
# print(data.endswith('O'))

#列表
# list = [1,2,3,'你好']
# print(type(list))
# print(list[3])
# print(len(list))#len函数可以获取列表对象中的数据个数
# strA = 'python'
# print(len(strA))
#查找
# listA = ['abcd',857,12.23,True]
# print(listA)#输出完成的列表
# print(listA[0])#输出第一个的元素
# print(listA[1:3])#从第二个开始到第3个元素区间获取
# print(listA[2:])#从第三个开始到结束
# print(listA[::-1])
# print(listA*3)
# # print(reversed(listA))
# listA.append([22,'demo'])
# print(listA)
# listA.insert(1,'插入数据')
# print(listA)
# # rsdata = list(range(10))
# # print(type(rsdata))
# listA.extend([1,23,'批量增加'])#批量增加
# print(listA)
# listA[0] = 'MARK'
# print(listA)
# listB = list(range(1,11))
# print(listB)
# del listB[0]
# print(listB)
# listB.remove(10)#移出指定元素
# print(listB)
# listB.pop(0)#移出指定索引元素
# print(listB)
# print(listB.index(5))#输出元素索引

#元祖的创建
# tupleA=()
# tupleA=('ABCD',89,12.21,'MARK',[1,2])
# print(tupleA)
# for i in tupleA:
#     print(i,end=' ')
# print(tupleA[2:3])
# print(tupleA[::-1])#表示反转字符串
# print(tupleA[::-2])#表示反转字符串 每隔2个取一次
# print(tupleA)
# print(tupleA[-2:-1:])

# 函数:在编写程序的过程中,有某一功能代码块多次出现,但是为了提高编写效率以及代码的重用,所以把具有独立功能的代码块组织成为一个模块,这就是函数.
# 代码复用的最大化以及最小冗余代码,整体代码结构信息清晰.
# 函数定义:
    # def funcname(parameter_list):
    #     pass
#函数的调用:本质就是执行函数定义里面的代码块,在调用函数之前必须先定义.

# def marsInfo():
#     print('mars height is %f'%1.8)
#     print('mars weight is %f'%2.0)
# pass
# marsInfo()#函数调用
# print('----多次输入相同的信息----')
# marsInfo()#函数调用

#[输出不同人的信息]
# def personInfo(name,weight):
#     print('%s height is %f'%(name,weight))
#     print('%s weight is %f'%(name,weight))
# pass

# personInfo('小李',80)

#参数分类
#必选参数、默认参数【缺省参数】、可选参数、关键字参数
#参数：函数为了实现某项特定功能所需要得到的外部数据

#1:必选参数
# def sum(a,b):#形式参数:只是意义上的一种参数,在定义的时候是不占内存地址的
#     sum = a+b
#     print(sum)
#     pass
# #函数调用,必选参数是必须要给值
# sum(1,2)#1,2是实际参数,是实际占用内存地址的
# sum('type','string')

#2:默认参数[缺省参数] 缺省参数始终在于参数列表中的尾部
# def sumA(a=20,b=30):
#     print('默认参数调用=%d'%(a+b))
#     pass
# def sumB(a,b=30):
#     print('默认参数调用=%d'%(a+b))
#     pass
# sumA()
# sumA(10)
# sumA(10,)

#3:可变参数(当参数的个数不确定时使用,比较灵活)
# def getCount(*args):
#     #计算累加和
#     result = 0
#     for items in args:
#         result+=items
#     pass
#     print('累加和等%d'%result)

# # getCount(1)#args是一个元祖
# getCount(1,2,3,4,5)

#4:关键字可变参数 是一个字典类型, 键值形式
#单*是可变参数 双*是关键字可变参数
#可变参数是一个元祖类型
#关键字可变参数是一个字典类型
# def complexFunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     pass

# complexFunc(1,2,3,4,name='mass')

# 函数返回值:函数执行结束返回对象,在函数内部有return就可以返回实际的值,否则返回的是一个Null
# 类型:可以返回任意类型,返回值类型取决于return后面的类型
# 用途:给调用方返回数据
# 在一个函数体内可以出先多个return值:但是肯定只能返回一个return
# 如果在一个函数里面执行了return,以为这函数退出了,return之后的代码不再执行

# def sum(a,b):
#     sum = a+b
#     return sum#计算结果返回
#     pass

# rs = sum(10,20)#将返回值赋给其他变量
# print(rs)#函数的返回值返回到调用的地方

# def calAll(num):
#     result = 0
#     lst = []
#     i = 1
#     while i <= num:
#         result += i
#         i += 1
#         pass
#     lst.append(result)
#     return lst
#     pass

# va = calAll(10)
# print(va)
# print(type(va))

#函数嵌套调用:在一个函数之中运行其他的函数
# def funcA():
#     print('----funcA开始执行----')
#     print('----funcA执行代码----')
#     print('----funcA结束执行----')
#     pass

# def funcB():
#     print('----funcB开始执行----')
#     funcA()
#     print('----funcB结束执行----')
#     pass

# funcB()

#函数分类:有参数有返回值、有参数无返回值、无参数有返回值、无参数无返回值

#作业
# 1.接收N个数字，求总
# def sumA(*args):
#     res = 0
#     for i in args:
#         res += i
#         pass
#     return res
#     pass

# rlt = sumA(1,2,3,4,5)
# print(rlt)

# 找出传入的列表或元祖奇数位对应的元素,并返回一个新的列表
# def funcA(contain):
#     listA = []
#     index = 1
#     for i in contain:
#         if index%2 == 1:#判断奇数位
#             listA.append(i)
#             pass
#         index += 1
#         pass
#     return listA
#     pass

# rlt = funcA([1,2,3,4,5,6,7])
# print(rlt)

# print(tuple(range(10,30)))

# 检查传入字典的每一个value长度,如果大于2,仅仅保留前连个长度的内容
# def dictA(dicParms):
#     dictNew = {}
#     for key,value in dicParms.items():#获取key value
#         if len(value) > 2:
#             dictNew[key] = value[:2]
#             pass
#         else:
#             dictNew[key] = value
#             pass
#         pass
#     return dictNew
#     pass

# #函数调用
# dicObject = {'name':'mass','hobby':'basketball'}
# print(dictA(dicObject))

###第六天###
#1. 函数的类型
# A.无参数无返回值,一般用于提示信息打印
# def mvprint():
#     print('-' * 20)
#     pass
# B.无参数有返回值,多用于数据采集中,比如获取系统信息
# def mycpu():
#     return info
#     pass
# C.有参数无返回值,多用于设置默写不需要返回值得参数
# def set(a):
#     pass
# D.有参数有返回值,一般是计算型的,需要参数,最终也要返回结果
# def cal(a,b):
#     return a+b
#     pass

#2. 全局变量&局部变量
#全局变量:作用域的范围不同
#局部变量就是在函数内部定义的变量[作用域仅仅局限在函数的内部]
#不同函数可以定义相同的局部变量,互不影响
#局部变量的作用是为了临时保存数据,需要在函数中定义来存储
#当全局变量和局部变量出现重复定义的时候,程序会优先执行使用函数内部定义的变量
#如果在函数的内部需要修改全局变量,需要在函数内部使用global声明
# age = '20'#全局变量
# name = 'Lemo'
# def printName():
#     #name = 'mass'#局部变量
#     print(name,age)
#     pass

# def printest():
#     name = 'mark'#局部变量
#     print(name,age)
#     pass

# def changeGlobal():#修改全局变量
#     global age
#     age = '22'#局部变量
#     pass

# changeGlobal()
# printName()
# printest()

#函数参数引用传值
#在Python中,值是靠引用来传递来的,可以用id()查看一个对象的引用是否相同,id是值保存在内存中的那块内存地址的标识
# a=1#不可变类型
# def func(x):
#     print('%s的地址:%s'%(x,id(x)))
#     x = 2
#     print('%s的地址:%s'%(x,id(x)))
#     pass

# #调用函数
# print('%s的地址:%s'%(a,id(a)))
# func(a)
# print(a)

#可变类型
# li = []
# def Test(parms):
#     #print(id(parms))
#     parms.append(1)
#     print(parms)
#     print(id(parms))
#     pass

# print(id(li))
# Test(li)

#小结
#1. 在python中,万物皆对象,在函数调用的时候,实际传递的就是对象的引用
#2. 了解原理之后,就可以更好的把控在函数内部的处理是否会影响到函数外部数据的变化
#3. 参数传递是通用对象的引用来完成 参数传递是通用对象的引用来完成 参数传递是通用对象的引用来完成

# 匿名函数
# Python中使用lambda关键字创建匿名函数
# 语法:lambda parameterlist: expression
# 特点:lambda关键字创建、没有名字的函数、匿名函数:后面的表达式有且只有一个,注意是一个表达式而不是语句、匿名函数自带return，返回就是表达式计算的结果
# 缺点:lambda只能是单个表达式,不是一个代码块,lambda的设计就是为了满足简单的函数场景,仅仅能封装优先的逻辑

# def complex(x, y):
#     return x+y
#     pass

# print(complex(1,2))
# #对应的匿名函数
# M=lambda x,y:x+y
# #通过变量去调用函数
# print(M(1,2))

# rlt = lambda a,b,c:a*b*c
# print(rlt(1,2,3))

# #lambda与三元运算
# res = lambda x,y:x if x>y else y

# print(res(12,13))

#递归函数:如果一个函数在内部不调用其他函数,而是自己本身的话,这个函数就是递归函数
#自己调用自己,必须有一个明确结束条件
#优点:代码整洁优雅,将复杂人物分解成更简单的子问题,使用递归比使用一些嵌套迭代容易
#缺点：递归难以调试,递归条件处理不好容易造成程序无法结束,直到达到最大递归错误.容易导致栈溢出，内存紧张，甚至内存泄漏
#求阶乘,定义函数
# def res(n):
#     rlt = 1
#     for i in range(1,n+1):
#         rlt *= i
#         pass
#     return rlt
#     pass

# print(res(3))

#求阶乘,递归函数
# def rlt(n):
#     if n ==1:
#         return 1
#     else:
#         return n*rlt(n-1)
#     pass

# print(rlt(3))

# 遍历文件夹下所有文件
# import os#引入文件操作模块
# def findfile(filePath):
#     listRS = os.listdir(filePath)#得到该路径下所有文件夹
#     for fileitems in listRS:
#         fullPath = os.path.join(filePath,fileitems)#获取完整文件路径
#         if os.path.isdir(fullPath):#判断是否是文件夹
#             findfile(fullPath)
#         else:
#             print(fileitems)
#         pass
#     pass
# pass

# findfile('D:\\迅雷下载\\毒液')

# 怎么去做--面向过程:根据业务逻辑从上而下编辑代码
# 函数式:将某些功能封装到代码中,日后无需重复编写,仅调用函数即可
# 谁来去做--面向对象[oop object oriented programming是一种python编程思路]:将数据与函数绑定到一起,进行封装,这样能够更快速的开发程序,减少了重复代码的重写过程

#面向对象:按照人们认识客观世界的系统思维方式,采用基于对象(实体)的概念建立模型,模拟客观世界分析、设计、实现软件的办法
#面向对象编程:是一种解决软件复用的设计和编程方法,这种方法把软件中相似的操作逻辑和操作应用数据、状态,以类的形式描述出来,以对象实例的形式在软件系统中复用,已达到提高软件开发效率应用

#类和对象

# 类就是一个模板,模板可以包含多个函数,函数在里实现一些功能
# 对象则是根据模板创建的实例,通过实例对象可以执行类中的函数
# 类:类是具有一组相同或者相似特征[属性]和行为[方法]的一系列对象组合
# 对象:对象是类的具象化

#类的组成部分
# class classname(object):#类名 属性 行为(方法)
#     pass

# 定义类和对象
# 创建类
# class personName(object):
#     name = 'mass'
#     age = 20
#     def eat(self):
#         print('正在吃饭')
#         pass
#     pass
# 创建一个对象 对象名=类名()
# m = personName()
# m.eat()#调用实例方法
# print(m.age)

#实例方法 归类所有,所有类的实例都可以去调用
#在类的内部,使用def关键字可以定义一个实例方法,与一般函数定义不同,类方法必须包含参数self,且为第一个参数
# class Animal(object):
#     def test(self):
#         print('实例方法')
#     pass
#     #一个类里面可以有多个实例方法
#     def show(self):
#         print('Animal.show')
# pass

#属性
# 类里面定义的变量 定义在类里面,方法外面的属性称之为类属性,定义在方法里面使用self引用的属性称之为实例属性
# class Animal(object):
#     name = 'cat'#类属性
#     def __init__(self):
#         self.kind = '英短'#实例属性
#     pass
# pass

# __init__方法
# class Game(object):
    # def __init__(self):
    #     self.name = 'GameName'
    #     self.develop = 'GameDevelop'
    #__init__传参:
#     def __init__(self,GameName,GameDevelop):
#         self.name = GameName
#         self.develop = GameDevelop
#     def sale(self,sale):
#         print(self.name + '游戏售价' + sale)#实例方法
#     pass
# pass

# pubg = Game('绝地求生','蓝洞')
# # pubg = Game()
# # pubg.name = '绝地求生'#添加实例属性
# # pubg.develop = '蓝洞'#添加实例属性
# pubg.sale('98')
# print(pubg.name,pubg.develop)

# lol = Game('英雄联盟','拳头')
# # lol = Game()
# # lol.name = '英雄联盟'#添加实例属性
# # lol.develop = '拳头'#添加实例属性
# lol.sale('free')
# print(lol.name,lol.develop)

#如果有N个这样对象被实例化,那么就需要多次添加实例属性
# __init__方法,初始化方法,实例化对象时自动调用,完成一些初始化的设置

#__init__总结:
# 1. python 自带的内置函数,具有特殊函数,使用双下划线包起来的[魔术方法]
# 2. 是个初始化的方法,用来定义实例属性和初始化数据的,在创建对象的时候自动调用,不用手动调用
# 3. 利用传参的极致可以让定义功能更加方便

#理解self
# self 和对象指向同一个内存地址,可以认为self就是对象的引用
# class personInfo(object):
#     def getFood(self):
#         print(id(self))
#         pass
#     pass

# mass = personInfo()
# print('mass内存地址%s'%(id(mass)))
# mass.getFood()

#self小结
# 1. self只有在类中定义实例方法的时候才有意义,在调用时不必传入相应参数,而是由解释器自动去指向
# 2. self的字段是可以更改的,可以定义成其他的字段,默认定义self
# 3. self值得是类的实例对象本身,相当于java中的this

#魔术方法
# 在python中,有一部分内置好的特定方法,方法名是'__xxxx__'进行特定的操作时会被调用,这些方法称为魔术方法
# 1. __init__方法:初始化一个类,在创建实例对象为其赋值时使用
# 2. __str__方法:在将对象转换成字符串str(对象)测试的时候,打印对象信息,此方法只能返回字符串
# 3. __new__方法:创建并返回一个实例对象,调用了一次,就会得到一个对象
# 4. __class__:获得已知对象的类(对象.__class__)
# 5. __del__方法:对象在程序运行结束后进行对象销毁的时候调用这个方法,来释放资源

#__str__方法
# class personInfo(object):
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         pass
#     def __str__(self):
#         return '测试传参信息%s %s %s'%(self.name,self.age,self.sex) 
#         pass

#     def __new__(cls,*args,**kwargs):
#         print('new函数的执行')
#         return object.__new__(cls)#__new__方法在此真正创建对象实例,必需
#         pass

#     pass

# mass = personInfo('mass','20','男')
# print(mass)

#__new__方法__init__方法区别
#__new__类的实例方法,必须要返回该实例,否则对象就创建不成功
#__init__用来做数据属性的初始化工作,也可以认为是实例的构造方法(java构造方法),接受类的实例self并对其进行构造
#__new__至少有一个参数是cls代表要实例化的类,次参数在实例化时由pyhton解释器自动提供
#__new__函数执行要早于__init__函数

# 案例-PVP
# 西门吹雪&叶孤城
# 属性:
# name玩家名字
# blood玩家血量

# 方法:
# poke()刺对方一刀,对方掉血10滴
# exploit()砍刀,对方掉血15滴
# recover()回复10滴血
# __str__打印玩家状态

# 1. 定义个类角色 role
# import time #导入时间
# class role(object):
#     def __init__(self,name,HP):#构造初始化函数,角色名字&血量
#         self.name = name
#         self.HP = HP
#         pass
#     def poke(self,enemy):#敌人
#         enemy.HP -= 10
#         info = '[%s]刺了[%s]一刀'%(self.name,enemy.name)
#         print(info)
#         pass
#     def exploit(self,enemy):
#         enemy.HP -= 15
#         info = '[%s]砍了[%s]一刀'%(self.name,enemy.name)
#         print(info)
#         pass
#     def recover(self):
#         self.HP += 10
#         info = '[%s]回复了10滴血'%(self.name)
#         print(info)
#         pass
#     def __str__(self):
#         return '[%s]的状态值[%s]'%(self.name,self.HP)
#     pass

# # 创建两个实例化对象

# xmcx = role('西门吹雪',100)
# ygc = role('叶孤城',100)

# while True:
#     if xmcx.HP <= 0 or ygc.HP <= 0:
#         break
#     xmcx.poke(ygc)
#     print(xmcx)
#     print(ygc)
#     ygc.exploit(xmcx)
#     print(xmcx)
#     print(ygc)
#     xmcx.recover()
#     print('***********')
#     time.sleep(1)#休眠一秒钟
# print('对战结束')

# 面向对象三大特征:封装-继承-多态
# 析构函数
# 析构方法:当一个对象被删除或者被销毁时,python解释器也会默认调用一个方法,这个方法为__del__()方法,也称为析构方法
# class Animal(object):
#     def __init__(self,name):
#         self.name = name
#         print('这是初始化方法')
#         pass
#     def __del__(self):
#         #来操作对象的释放 一旦释放完毕对象便不能使用
#         print('当在某个作用于下面没有被[引用]的情况下解析器会自动调用此函数来释放内存空间')
#         print('这是析构方法')
#         print('%s这个对象被彻底释放'%self.name)
#         pass
#     pass

# cat = Animal('肉肉')
# input('程序等待')#程序没有执行完毕,在等待中,析构函数不会释放对象清理内存

# 析构方法总结:
# 1. 当整个程序脚本指向完毕后会自动调用__del__方法
# 2. 当对象被手动销毁时也会自动调用__del__方法
# 3. 析构函数一般用于资源回收,利用__del__方法销毁对象回收内存等资源

# 封装、继承、多态
# 封装:指的是把内容封装到某个地方,便于后面的使用
# 继承:子承父业[属性-行为]
# 对于面向对象的继承,其实就是将多个类的共有方法提取到父类中,子类仅需继承父类而不必一一实现每个方法

#单继承
# class Animal(object):
#     def eat():
#         print('进食')
#     pass
#     def drink():
#         print('饮水')
#     pass
# pass

# class dog(Animal):
#     def ww():
#         print('小狗汪汪叫')
# class cat(Animal):
#     def mm():
#         print('小猫喵喵叫')

# dog.eat()
# dog.drink()
# dog.ww()
# print('*'*10 + '猫的行为' + '*'*10)
# cat.eat()
# cat.drink()
# cat.mm()

#多继承 C类可以继承A,B两个类,C可以调用A,B两个类的方法
# class Ghost():
#     def canfly(self):
#         print('会飞')
#     pass
# class monkey():
#     def eatPeach(self):
#         print('吃桃')
#     pass
# class wukong(Ghost,monkey):
#     pass
# wukong.canfly()
# wukong.eatPeach()

# 问题:当多个父类中存在相同方法时,应该去调用哪个
# class D(object):
#     def eat(self):
#         pirnt('D.eat')
# class C(D):
#     def eat(self):
#         print('C.eat')

# class B(D):
#     pass
# class A(B,C):
#     pass

# abs = A()
# abs.eat()#在执行eat方法时顺序为 A - B(A的第一个父类) - C(A的第二个父类) - B类的父类(A父类结束)
# print(A.__mro__)#可以显示类的继承关系,类.__mro__,而非 对象.__mro__

#间接继承
# class GrandFather(object):
#     def eat(self):
#         print('吃的方法')

# class Father(GrandFather):
#     pass

# class Son(Father):
#     pass

# son = Son()
# son.eat()#此方法是从GrandFahter继承过来的
# print(Son.__mro__)
