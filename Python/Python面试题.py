## TODO: 简述解释型和编译型编程语言?

# 解释型语言编写程序不需要编译,在执行的时候,专门有一个解释器能够将VB语言翻译成机器语言,每个语句都是执行的时候才翻译.
# 这样解释型语言每执行一次就要翻译一次,效率比较低.

# 用编译型语言写的程序执行之前,需要一个专门的编译过程,通过编译系统,把源高级程序编译成为机器语言文件.
# 运行时不需要翻译,所以编译型语言的程序执行效率较高.

## TODO: 位和字节的关系?

# bit就是位,也叫比特位,是计算机表示数据最小的单位
# byte就是字节,1byte=8bit,1byte就是1B,一个字符=2字节,1KB=1024B
# 字节就是Byte,也是B.位就是bit也是b
# 转换关系如下:1KB=1024B 1B= 8b

## TODO: (二|八|十六)进制转换成十进制:

# 先将其转换为字符串,再使用int函数,指定进制转换为二进制 
# print(int('0b1111011',2))  #123
# print(int('011',8))  #9
# print(int('0x12',16))  #18

## TODO: 十进制转化为(二|八|十六)进制

# print(bin(10))  #0b1010  # Binary
# print(oct(20))  #0o24    # Octal
# print(hex(30))  #0x1e    # Hexadecimal

## TODO: 可变对象和不可变对象

# 可变 list,dict,set
# 不可变 number,string,tuple

# 切片适用于所有序列,包括列表,字符串,元祖

# ls = [1,2,3,4,5,6,7]
# print(ls[::2])  #[1, 3, 5, 7]

## TODO: Python最大递归深度

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n + fact(n-1)
    
# print(fact(998))  #498501
## print(fact(999))  #maximum recursion depth exceeded in comparison 比较中超过了最大递归深度

## TODO: Ascii,Unicode,UTF-8,GBK区别?

# Ascii编码,最早只有127个字母被编码到计算机中,大小写英文字母,数字和一些符号
# Unicode把所有的语言统一到一套编码之中,解决不同语言出现乱码问题,常用两个字节表示一个字符
# UTF-8编码是可变长编码的Unicode编码(节省空间),UTF-8把一个Unicode编码根据不同的数字大小编码成1-6个字节,英文字母被编码成1个字节,汉字通常是3个字节
 
## TODO: 机器码和字节码?

# 机器码就是计算机可以直接执行,并且执行速度最快的代码
# 字节码是一种中间状态(中间码)的二进制代码(文件),需要直译器转译后才能成为机器码

## TODO: 列举布尔值为False的常见值?

# False None 0 '' () [] {}
# 除了标准值False和None,所以类型的数字0,空序列(空字符,空元祖,空列表,空字典)都为假


## TODO: Python的函数参数传递

# # 例1
# a = 1
# def funA(a):
#     print('函数执行之前a内存地址->'+str(id(a)))  #函数执行之前a内存地址->140735206810256
#     a = 2
#     print('函数执行之后a内存地址->'+str(id(a)))  #函数执行之后a内存地址->140735206810288

# funA(a)
# print(a,id(a))  #1 140735206810256

# # 例2
# a = []
# def funB(a):
#     print('函数执行之前a内存地址->'+str(id(a)))  #函数执行之前a内存地址->2481546879624
#     a.append(1)
#     print('函数执行之后a内存地址->'+str(id(a)))  #函数执行之后a内存地址->2481546879624
# funB(a)
# print(a,id(a))  #[1] 2481546879624

# 所有的变量都可以理解是内存中一个对象的`引用`

# 通过id来看引用a的内存地址可以比较理解:

# 第1个例子可以看到,在执行完a = 2之后,a引用中保存的值,即内存地址发生变化,由原来1对象的所在的地址变成了2这个实体对象的内存地址

# 而第2个例子a引用保存的内存值就不会发生变化:

# 这里记住的是类型是属于对象的,而不是变量而对象有两种,'可更改'（mutable）与'不可更改'（immutable）对象在python中,strings, tuples, 和numbers是不可更改的对象,而 list, dict, set 等则是可以修改的对象(这就是这个问题的重点)

# 当一个引用传递给函数的时候,函数自动复制一份引用,这个函数里的引用和外边的引用没有半毛关系了.所以第一个例子里函数把引用指向了一个不可变对象,当函数返回的时候,外面的引用没半毛感觉.而第二个例子就不一样了,函数内的引用指向的是可变对象,对它的操作就和定位了指针地址一样,在内存里进行修改.

# 如果还不明白的话,这里有更好的解释: http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference

## TODO: @staticmethod 和 @classmethod

# Python其实有3个方法,即静态方法(staticmethod),类方法(classmethod)和实例方法,如下:

# def foo(x):
#     print('executing foo(%s)'%(x))

# class A(object):
#     def foo(self,x):
#         print('executing foo(%s,%s)'%(self,x))
#     @classmethod
#     def classfoo(cls,x):
#         print('executing classfoo(%s,%s)'%(cls,x))

#     @staticmethod
#     def staticfoo(x):
#         print('executing staticfoo(%s)'%x)

# a=A()
# 实例方法
# a.foo(1)
# A.foo(1) #TypeError: foo() missing 1 required positional argument: 'x' 实例方法用 类.方法 不可以用
## 类方法
# a.classfoo(1)
# A.classfoo(1)
## 静态方法
# a.staticfoo(1)
# A.staticfoo(1)

# 这里先理解下方法参数里面的self和cls.这个self和cls是对类或者实例的绑定,对于一般的函数来说我们可以这么调用foo(x),这个函数就是最常用的,它的工作跟任何东西(类,实例)无关.对于实例方法,我们知道在类里每次定义方法的时候都需要绑定这个实例,就是foo(self, x),为什么要这么做呢?因为实例方法的调用离不开实例,我们需要把实例自己传给方法,调用的时候是这样的a.foo(x)(其实是foo(a, x)).类方法一样,只不过它传递的是类而不是实例,A.classfoo(x).注意这里的self和cls可以替换别的参数,但是python的约定是这俩,还是不要改的好.
# 对于静态方法其实和普通的函数一样,不需要对谁进行绑定,唯一的区别是调用的时候需要使用a.staticfoo(x)或者A.static_foo(x)来调用.

# 实例方法  	类方法	    静态方法
# a.foo(x)     a.classfoo(x)	  a.staticfoo(x)
# A.不可用  	A.classfoo(x)      A.staticfoo(x)
# 更多关于这个问题:

# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
# https://realpython.com/blog/python/instance-class-and-static-methods-demystified/

## TODO: 迭代器和生成器

# 这个是stackoverflow里python排名第一的问题,值得一看: http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
# 这是中文版: http://taizilongxu.gitbooks.io/stackoverflow-about-python/content/1/README.html

# iterables(迭代器)
#   一个对象拥有__iter__()和__next__()方法,则这个对象就是迭代器
#   可以用在for...in...语句中的都是可迭代的,比如lists,strings,files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,
#   但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存

# generator(生成器)
#     生成器也是迭代器的一种,但是你只能迭代它们一次,原因很简单,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成,生成器和迭代器的区别就是用()代替[],还有你不能用for i in generator第二次调用生成器,首先计算0,然后会在内存里丢掉0去计算1,直到计算完全

# 这里有个关于生成器的创建问题面试官有考: 问: 将列表生成式中[]改成() 之后数据结构是否改变? 答案:是,从列表变为生成器

# ls = [x*x for x in range(10)]
# print(ls,type(ls))  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] <class 'list'>

# gr = (x*x for x in range(10))
# print(gr)  #<generator object <genexpr> at 0x000002A04FC21ED0>

# 通过列表生成式,可以直接创建一个列表.但是,受到内存限制,列表容量肯定是有限的.而且,创建一个包含百万元素的列表,不仅是占用很大的内存空间,如:我们只需要访问前面的几个元素,后面大部分元素所占的空间都是浪费的.因此,没有必要创建完整的列表(节省大量内存空间)
# 在Python中,我们可以采用生成器:边循环,边计算的机制—>generator

# from collections import Iterable

# str = '12345'
# ls = [1,2,3,4,5]
# tu = (1,2,3,4,5)
# dc = {1:2,3:4}
# st = {1,2,3,4,5}

# # 判断一个对象是否可以迭代,上述都是可迭代的对象
# print(isinstance(str,Iterable))  #True
# print(isinstance(ls,Iterable))  #True
# print(isinstance(tu,Iterable))  #True
# print(isinstance(dc,Iterable))  #True
# print(isinstance(st,Iterable))  #True

# # 可迭代协议
# # dir监测数据对象所拥有的内置函数
# print(dir('12'))
# print(dir([1,2]))
# print(dir((1,2)))
# print(dir({1:2}))
# print(dir({1,2}))

# # __iter__方法存在于这5种数据类型

# print([1,2].__iter__())  #<list_iterator object at 0x0000017CFC908320>

# # iterator(迭代器)
# print(set(dir([1,2].__iter__()))-set(dir([1,2])))  #{'__setstate__', '__length_hint__', '__next__'}

# iter = [1,2,3,4,5].__iter__()  #<list_iterator object at 0x0000017CFC908320>

# # 获取迭代器中元素长度
# print(iter.__length_hint__())

# # 根据索引值指定从哪里开始迭代
# print(iter.__setstate__(0))

# # 一个一个取值
# print(iter.__next__())  #1
# print(iter.__next__())  #2

# 不使用for循环遍历列表

# lst = [1,2,3,4,5]

# lstiter = lst.__iter__()

# while True:
#     try:
#         item = lstiter.__next__()
#         print(item)
#     except StopIteration:
#         break

## TODO: 迭代器遵守迭代器协议,必须拥有__iter__()和__next__()方法
# from collections import Iterator

# print('__iter__' in dir(range(5)))  #True
# print('__next__' in dir(range(5)))  #False

# print(isinstance(range(5),Iterator))  #False

# range()是可迭代的,但不是迭代器


# for循环可迭代的对象(iterable) 字符串、列表、元祖、字典、集合
# for i in ls:
#     print(i)

# for j in 12345:
#     print(j)  #TypeError: 'int' object is not iterable

# 迭代器好处节省内存

# 生成器 文本监听
# 本质就是一个迭代器

## 1.生成器函数

# def produce():
#     # 下面条
#     for i in range(200):
#         yield f'做了第{i}碗面'

# g = produce()
# print(g)  #<generator object produce at 0x000002161AD45570>
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

## 2. 生成器表达式

# ls = [f'第{x}个梦' for x in range(10)]
# print(ls)  #['第0个梦', '第1个梦', '第2个梦', '第3个梦', '第4个梦', '第5个梦', '第6个梦', '第7个梦', '第8个梦', '第9个梦']

# gt = (f'第{x}个梦' for x in range(10))
# print(gt)  #<generator object <genexpr> at 0x000001E10E8A65E8>
# print(gt.__next__())
# print(next(gt))

## 面试题

# 生成器的函数
# def demo():
#     for i in range(4):
#         yield i  #在python中,使用了yeild的函数被称为生成器

# g = demo()

# # 生成器表达式
# g1 = (i for i in g)
# print(g1)  #<generator object <genexpr> at 0x000002AC16D16570>

# g2 = (i for i in g1)  #<generator object <genexpr> at 0x000002AC16D166D8>
# print(g2)

# print(list(g1))  #[0, 1, 2, 3]
# print(list(g2))  #[]

## TODO: __new__和__init__的区别

# __new__是一个静态方法,而__init__是一个实例方法.
# __new__方法会返回一个创建的实例,而__init__什么都不返回.
# 只有在__new__返回一个cls的实例时后面的__init__才能被调用.
# 当创建一个新实例时调用__new__,初始化一个实例时用__init__.

## TODO: 单例模式
#     单例模式是一种常用的软件设计模式.在它的核心结构中只包含一个被称为单例类的特殊类.
#     通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问,从而方便对实例个数的控制并节约系统资源.
#     如果希望在系统中某个类的对象只能存在一个,单例模式是最好的解决方案.

# __new__()在__init__()之前被调用,用于生成实例对象.利用这个方法和类的属性的特点可以实现设计模式的单例模式.
# 单例模式是指创建唯一对象,单例模式设计的类只能实例

## 1 使用__new__方法

# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance

# class MyClass(Singleton):
#     a = 1

## 2 共享属性

# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.

# class Borg(object):
#     _state = {}
#     def __new__(cls, *args, **kw):
#         ob = super(Borg, cls).__new__(cls, *args, **kw)
#         ob.__dict__ = cls._state
#         return ob

# class MyClass2(Borg):
#     a = 1

## 3 装饰器版本

# def singleton(cls):
#     instances = {}
#     def getinstance(*args, **kw):
#         if cls not in instances:
#             instances[cls] = cls(*args, **kw)
#         return instances[cls]
#     return getinstance

# @singleton
# class MyClass:
#   pass

## 4 import方法

# 作为python的模块是天然的单例模式

# # mysingleton.py
# class MySingleton(object):
#     def foo(self):
#         pass

# mysingleton = MySingleton()

# # to use
# from mysingleton import mysingleton

# mysingleton.foo()

## TODO: 匿名函数

# lab = lambda x : x*x
# 冒号前x为参数,冒号后x*x为表达式,返回值是该表达式的结果

# print(lab)  #<function <lambda> at 0x000002A646DFA840>

# lambda配合sorted使用
# dc = {1:'c',2:'b',3:'a'}
# newdc = sorted(dc.items(),key=lambda x:x[1])

# print(newdc)  #[(3, 'a'), (2, 'b'), (1, 'c')]

## TODO: Python函数式编程
# 这个需要适当的了解一下吧,毕竟函数式编程在Python中也做了引用

# python中函数式编程支持:

# filter 函数的功能相当于过滤器.调用一个布尔函数bool_func来迭代遍历每个seq中的元素；返回一个使bool_seq返回值为true的元素的序列
# filter() 函数用于过滤序列,过滤掉不符合条件的元素,返回一个迭代器对象,如果要转换为列表,可以使用 list() 来转换
# 该接收两个参数,第一个为函数,第二个为序列,序列的每个元素作为参数传递给函数进行判断,然后返回 True 或 False,最后将返回 True 的元素放到新列表中

# a = [1,2,3,4,5,6,7]
# b = filter(lambda x: x > 5, a)
# print(b)

# map函数是对一个序列的每个项依次执行函数,下面是对一个序列每个项都乘以2
# map() 会根据提供的函数对指定序列做映射
# 第一个参数 function 以参数序列中的每一个元素调用 function 函数,返回包含每次 function 函数返回值的新列表


# a = map(lambda x:x*2,[1,2,3])
# list(a)  #[2, 4, 6]

# reduce函数是对一个序列的每个项迭代调用函数,下面是求3的阶乘:
# reduce() 函数会对参数序列中元素进行累积
# 函数将一个数据集合（链表,元组等）中的所有数据进行下列操作:用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作,得到的结果再与第三个数据用 function 函数运算,最后得到一个结果

# from functools import reduce

# fact = reduce(lambda x,y:x*y,range(1,4))
# print(fact)

# zip函数
# zip() 函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,然后返回由这些元组组成的列表.
# 如果各个迭代器的元素个数不一致,则返回列表长度与最短的对象相同,利用 * 号操作符,可以将元组解压为列表.

# a,b = [1,2,3],[4,5,6]
# ziped = zip(a,b)
# print(list(ziped))

## TODO: Python里的拷贝 引用赋值&传值赋值

# 引用和copy(),deepcopy()的区别
# https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html

# import copy
# a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

# b = a  #赋值,传对象的引用  #  赋值引用,a和b都指向同一个对象 # TODO: 引用赋值
# c = copy.copy(a)  #对象拷贝,浅拷贝  #  浅拷贝,a和c是一个独立的对象,但他们的子对象还是指向统一对象(是引用),只拷贝顶级对象,或者说父级对象
# d = copy.deepcopy(a)  #对象拷贝,深拷贝  #  深拷贝,a和b完全拷贝了父对象及其子对象,两者是完全独立的 ,拷贝所以对象,顶级对象及其嵌套对象 # TODO: 传值赋值

# a.append(5)  #修改对象a  #a = [1, 2, 3, 4, ['a', 'b'],5]
# a[4].append('c')  #修改对象a中的['a', 'b']数组对象  #a = [1, 2, 3, 4, ['a', 'b','c'],5]

# print('a = ', a)
# print('b = ', b)
# print('c = ', c)
# print('d = ', d)

# # 输出结果:
# a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
# c =  [1, 2, 3, 4, ['a', 'b', 'c']]
# d =  [1, 2, 3, 4, ['a', 'b']]

## TODO: Python垃圾回收机制

# Python GC(garbage collection)主要使用引用计数（reference counting）来跟踪和回收垃圾
# 在引用计数的基础上,通过“标记-清除”（mark and sweep）解决容器对象可能产生的循环引用问题
# 通过“分代回收”（generation collection）以空间换时间的方法提高垃圾回收效率

# 1 引用计数
# PyObject是每个对象必有的内容,其中ob_refcnt就是做为引用计数
# 当一个对象有新的引用时,它的ob_refcnt就会增加
# 当引用它的对象被删除,它的ob_refcnt就会减少.引用计数为0时,该对象生命就结束了

# import sys

# sys.getrefcount(a)  #查看对象引用计数

# 优点:
#     1. 简单
#     2. 实时性
# 缺点:
#     1. 维护引用计数消耗资源
#     2. 循环引用

# 2 标记-清除机制
#     基本思路是先按需分配,等到没有空闲内存的时候从寄存器和程序栈上的引用出发
#     遍历以对象为节点、以引用为边构成的图,把所有可以访问到的对象打上标记,然后清扫一遍内存空间,把所有没标记的对象释放

# 3 分代回收
#     分代回收的整体思想是:将系统中的所有内存块根据其存活时间划分为不同的集合
#     每个集合就成为一个“代”,垃圾收集频率随着“代”的存活时间的增大而减小,存活时间通常利用经过几次垃圾回收来度量

# Python默认定义了三代对象集合,索引数越大,对象存活时间越长

# 举例: 当某些内存块M经过了3次垃圾收集的清洗之后还存活时,我们就将内存块M划到一个集合A中去,而新分配的内存都划分到集合B中去
# 当垃圾收集开始工作时,大多数情况都只对集合B进行垃圾回收,而对集合A进行垃圾回收要隔相当长一段时间后才进行,这就使得垃圾收集机制需要处理的内存少了,效率自然就提高了
# 在这个过程中,集合B中的某些内存块由于存活时间长而会被转移到集合A中,当然,集合A中实际上也存在一些垃圾,这些垃圾的回收会因为这种分代的机制而被延迟

## TODO: Python中的 is 和 ==

#   is是对比地址(id),==是对比值

## TODO: read,readline,readlines

# import os,sys

# with open(os.path.join(sys.path[0],'sample.txt'),'w+') as f:
#     details = f.readlines()
#     print(type(details))

#     read(size)
#       读取整个文件,指定大小内容,以byte为单位,size为读入的字符数,返回str类型
#     readline
#       读取下一行,使用生成器方法,放到一个字符串变量,返回str类型
#     readlines
#       读取文件所有内容,按行为单位放到一个列表中,返回list类型
#     xreadlines
#       读取文件所有内容,返回一个生成器,Python3中已经没有这个方法
