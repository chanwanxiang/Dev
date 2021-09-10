###  一. Python基础

IPython是一种基于python的交互式解释器,相较于原生python交互式环境,提供了更加强大的编辑和交互功能.

>安装 pip install ipython
>使用 ipython

#### 1.1 语法

##### 1.1.1 代码中修改不可变数据类型会出现什么问题?

```python
a = 'abc'

print(a[0])

a[0] = 'b'

```

> TypeError: str object does not support item assignment

##### 1.1.2 a=1,b=2,不用中间变量交换a,b的值?

方法一:

```python
a = a + b
b = a - b
a = a - b

```

方法二:

```python
a, b = b, a 
```

##### 1.1.3 pirnt调用底层什么方法?

print 方法默认调用 sys.stdout.write 方法,即往控制台打印字符串

##### 1.1.4 简述input()函数理解?

input()获取用户输入,不论用户输入的是什么,获取到的都是字符串类型

#### 1.2 条件与循环

如果明确知道循环执行的次数或者对一个容器进行迭代,推荐使用for-in循环

如果要构造不知道具体循环次数的循环结构,推荐使用while循环

##### 1.2.1 range和xrange的区别?

两者用法相同,不同的是 range 返回的结果是一个列表,而 xrange 的结果是一个生成器,前者是直接开辟一块内存空间来保存列表,后者是边循环边使用,只有使用时才会开辟内存空间,所以当列表很长时,使用 xrange 性能要比range好,Python3中没有xrange函数

##### 1.2.2 直角三角形、等腰三角形、99乘法表实现?

**直角三角形**

方法一 for循环

```python
# 行数
for i in range(1,10):
    # 打印*数
    for j in range(i):
        print('*', end=' ')
    # 换行
    print()
    
```

**等腰三角形**

方法一 for循环

**99乘法表**

方法一 for循环

```python
# 行数
for i in range(1,10):
    # 打印相乘
    for j in range(1,i+1):
        print(f'{j}*{i}={i*j}', end=' ')
    # 换行
    print()
    
```

#### 1.3 文件操作

##### 1.3.1 4G内存如何读取5G文件?

可以通过生成器,分多次读取,每次读取数量相对少的数据(比如500MB)进行处理,处理结束后在读取后面的500MB的数据

##### 1.3.2 read、readline和readlines的区别?

read:读取整个文件
readline:读取下一行,使用生成器方法
readlines:读取整个文件到一个迭代器以供我们遍历

#### 1.4 异常

##### 1.4.1 在except中return后还会不会执行finally中的代码?怎么抛出自定义异常?

会继续处理 finally 中的代码,用 raise 方法可以抛出自定义异常

```python
# 在python中,抛出自定义异常的语法为raise异常类对象

# 需求:密码长度不够,则报异常(用户输入密码,如果输入长度不足6位,则报错,即抛出自定义异常,并捕获该异常)

# 自定义异常类,继承Exception
class ShortPswError(Exception):
    def __init__(self,length,minlen):
        # 用户输入的密码长度
        self.length = length
        # 系统要求最低密码长度
        self.minlen = minlen

    # 设置抛出异常描述信息
    def __str__(self):
        return f'您设置的密码是{self.length}位,不能少于{self.minlen}位'

def main():
    # 抛出异常:尝试执行,用户输入密码,如果长度小于6,抛出异常
    try:
        psw = input('请您输入密码:')
        if len(psw) < 6:
            # 抛出异常类创建的对象
            raise ShortPswError(len(psw),6) 
    # 捕获异常
    except Exception as msg:  
        print(msg)
    else:
        print('success')

main()

```

##### 1.4.2 介绍一下except的作用和用法？

except: 捕获所有异常 
except: <异常名>: 捕获指定异常 
except: <异常名 1, 异常名 2> : 捕获异常1或者异常 2 
except: <异常名>,<数据>:捕获指定异常及其附加的数据 
except: <异常名 1,异常名 2>:<数据>:捕获异常名1或者异常名2,及附加的数据

```python
try:
    print(1)
except Exception as msg:
    print(msg)
# else是没有异常执行的代码块
else:
    print('else是没有异常执行的代码块')
# finally无论有无异常都要执行的代码块
finally:
    print('finally无论有无异常都要执行的代码块')
    
```

#### 1.5 模块与包

##### 1.5.1 常用的Python标准库都有哪些?

os 操作系统、time 时间、random 随机、pymysql 连接数据库、threading 线程、multiprocessing 进程、queue 队列

##### 1.5.2 赋值、浅拷贝和深拷贝的区别?

```python
import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

b = a  #赋值,传对象的引用,赋值引用,a和b都指向同一个对象 # TODO:引用赋值,与传值赋值区分
c = copy.copy(a)  #对象拷贝,浅拷贝  #  浅拷贝,a和c是一个独立的对象,但他们的子对象还是指向同一对象(是引用),只拷贝顶级对象,或者说父级对象
d = copy.deepcopy(a)  #对象拷贝,深拷贝  #  深拷贝,a和b完全拷贝了父对象及其子对象,两者是完全独立的 ,拷贝所以对象,顶级对象及其嵌套对象 # TODO: 传值赋值

a.append(5)  #修改对象a  #a = [1, 2, 3, 4, ['a', 'b'],5]
a[4].append('c')  #修改对象a中的['a', 'b']数组对象  #a = [1, 2, 3, 4, ['a', 'b','c'],5]

print('a = ', a)
print('b = ', b)
print('c = ', c)
print('d = ', d)

# 输出结果:
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
c =  [1, 2, 3, 4, ['a', 'b', 'c']]
d =  [1, 2, 3, 4, ['a', 'b']]

```

**赋值**
在Python中,对象的赋值就是简单的对象引用

```python
a = b
```

在上述情况下, a 和 b 是一样的,他们指向同一片内存, b 不过是 a 的别名,是引用
我们可以使用 b is a 去判断,返回 True,表明他们地址相同,内容相同,也可以使用 id() 函数来查看两个列表的地址是否相同
赋值操作(包括对象作为参数、返回值)不会开辟新的内存空间,它只是复制了对象的引用,也就是说除了 b 这个名字之外,没有其他的内存开销,修改了 a,也就影响了 b,同理,修改了 b 也就影响了 a

**浅拷贝**
浅拷贝会创建新对象,其内容非原对象本身的引用,而是原对象内第一层对象的引用 
浅拷贝有三种形式:切片操作、工厂函数、copy 模块中的 copy 函数 
比如上述的列表 a 
切片操作:b = a[:] 或者 b = [x for x in a] 
工厂函数:b = list(a) 
copy 函数:b = copy.copy(a) 
浅拷贝产生的列表 b 不再是列表 a 了,使用 is 判断可以发现他们不是同一个对象,使用 id 查看, 他们也不指向同一片内存空间但是当我们使用 id(x) for x in a 和 id(x) for x in b 来查看 a 和 b 中元 素的地址时,可以看到二者包含的元素的地址是相同的
在这种情况下,列表 a 和 b 是不同的对象,修改列表 b 理论上不会影响到列表 a 但是要注意的是,浅拷贝之所以称之为浅拷贝,是它仅仅只拷贝了一层,在列表 a 中有一个嵌套的 list,如果我们修改了它,情况就不一样了
比如：a[4].append('c'),查看列表 c,会发现列表 c 也发生了变化,这是因为,我们修改了嵌套的 list,修改外层元素,会修改它的引用,让它们指向别的位置,修改嵌套列表中的元素,列表的地址并未发生变化,指向的都是用一个位置

**深拷贝**
深拷贝只有一种形式,copy 模块中的 deepcopy() 函数,深拷贝和浅拷贝对应,深拷贝拷贝了对象的所有元素,包括多层嵌套的元素.因此,它的时间和空间开销要高,同样的对列表 a,如果使用 d = copy.deepcopy(a),再修改列表 d 将不会影响到列表 a,即使嵌套的列表具有更深的层次,也不会产生任何影响,因为深拷贝拷贝出来的对象根本就是一个全新的对象, 不再与原来的对象有任何的关联

**拷贝的注意点**
对于非容器类型,如数字、字符,以及其他的原子类型,没有拷贝一说,产生的都是原对象的引用
如果元组变量值包含原子类型对象,即使采用了深拷贝,也只能得到浅拷贝

##### 1.5.3 \__init__和\_\_new\_\_的区别?

\_\_init\_\_在对象创建后,对对象进行初始化
\_\_new\_\_ 是在对象创建之前创建一个对象,并将该对象返回给 init(为对象分配内存, 返回对象引用)

```python
class MusicPlayer(object):

    #为对象分配内存空间
    def __new__(cls, *args, **kwargs):

        #1、创建对象时,new方法会被自动调用
        print("创建对象，分配内存空间")

        #2、为对象分配空间
        instance = super().__new__(cls)

        #3、返回对象引用
        return instance
    
    #对象初始化，定义实例属性
    def __init__(self):
        print("播放器初始化")

#创建播放器对象
player = MusicPlayer()
print(player)

```

##### 1.5.4 Python中如何生成随机数?

在Python中用于生成随机数的模块是 random,在使用前需要 import

```python
import random

# 生成一个 0-1 之间的随机浮点数
print(random.random())

# 生成[a,b]之间的浮点数
print(random.uniform(1.1, 1.2))

# 生成[a,b]之间的整数
print(random.randint(2, 5))

# 从特定序列中随机取一个元素,这里的序列可以是字符串、列表、元组等
print(random.choice('12345'))

```

##### 1.5.5 输入某年某月某日,判断这一天是这一年的第几天?

在Python中用于日期模块是 datetime,在使用前需要 import

```python
import datetime 

def dayofyear(): 
    year = input('请输入年份:') 
    month = input('请输入月份:') 
    day = input('请输入天:') 
    date1 = datetime.date(year=int(year), month=1, day=1)
    date2 = datetime.date(year=int(year), month=int(month), day=int(day))
    
    return (date2 - date1).days + 1
                  
```

##### 1.5.6 打乱一个排好序的list对象ls?

```python
import random

ls = [1,2,3,4,5]
print(random.shuffle(ls))

```

##### 1.5.7 说明一下os.path和sys.path分别代表什么?

os.path 主要要是用于对系统路径文件的操作
sys.path 主要是对 Python 解释器的系统环境参数的操作(动态的改变 Python 解释器搜索路径)

##### 1.5.8 Python中的os模块常见方法?

os.remove() 删除文件 
os.rename() 重命名文件
os.getcwd() 取得当前工作目录
os.path.join() 将分离的各部分组合成一个路径名
os.path.exists() 是否存在
os.path.getsize() 返回文件大小
os.path.isfile()是否为文件

##### 1.5.9 Python的sys模块常用方法?

sys.argv 命令行参数 List,第一个元素是程序本身路径
sys.modules.keys() 返回所有已经导入的模块列表
sys.path 返回模块的搜索路径,初始化时使用 PYTHONPATH 环境变量的值

##### 1.5.10 模块和包是什么?

在 Python 中,模块是搭建程序的一种方式
每一个 Python 代码文件都是一个模块,并可以引用 其他的模块,比如对象和属性,一个包含许多 Python 代码的文件夹并且其中有_\_init\_\_.py文件的就是一个包,一个包可以包含模块和子文件夹

#### 1.6 Python特性

##### 1.6.1 Python是强语言类型还是弱语言类型?

Python 是强类型的动态脚本语言
强类型:不允许不同类型相加 
动态:不使用显示数据类型声明,且确定一个变量的类型是在第一次给它赋值的时候
脚本语言:一般也是解释型语言,运行代码只需要一个解释器,不需要编译

##### 1.6.2 Python是如何进行类型转换的?

内建函数封装了各种转换函数,可以使用目标类型关键字强制类型转换
进制之间的转换可以用 int('str', base='n')将特定进制的字符串转换为十进制,再用相应的进制转换函数将十进制转换为目标进制

可以使用内置函数直接转换的有
list---->tuple tuple(list)
tuple---->list list(tuple)

##### 1.6.3 Python中的作用域?

Python 中,一个变量的作用域总是由在代码中被赋值的地方所决定
当 Python 遇到一个变量的话，它会按照这的顺序进行搜索
本地作用域(Local)--->当前作用域被嵌入的本地作用域(Enclosing locals)--->全局/模块作用域 (Global)--->内置作用域(Built-in)

##### 1.6.4 简述解释型和编译型编程语言

解释型语言编写程序不需要编译,在执行的时候,专门有一个解释器能够将 VB 语言翻译成机器语言,每个语句都是执行的时候才翻译这样解释型语言每执行一次就要翻译一次,效率比较低.

用编译型语言写的程序执行之前,需要一个专门的编译过程,通过编译系统,把源高级程序编译成为机器语言文件运行时不需要翻译,所以编译型语言的程序执行效率较高

##### 1.6.5 位和字节的关系?

bit就是位,也叫比特位,是计算机表示数据最小的单位
byte就是字节,1byte=8bit,1byte就是1B,一个字符=2字节,1KB=1024B
字节就是Byte,也是B.位就是bit也是b
转换关系如下:1KB=1024B 1B= 8b

##### 1.6.6 (二|八|十六)进制转换成十进制

先将其转换为字符串,再使用int函数,指定进制转换为二进制 

```python
print(int('0b1111011',2))  #123

print(int('011',8))  #9

print(int('0x12',16))  #18

```

##### 1.6.7 十进制转化为(二|八|十六)进制

```python
print(bin(10))  #0b1010  # Binary

print(oct(20))  #0o24    # Octal

print(hex(30))  #0x1e    # Hexadecimal

```

##### 1.6.8 Ascii,Unicode,UTF-8,GBK区别?

Ascii编码,最早只有127个字母被编码到计算机中,大小写英文字母,数字和一些符号
Unicode把所有的语言统一到一套编码之中,解决不同语言出现乱码问题,常用两个字节表示一个字符
UTF-8编码是可变长编码的Unicode编码(节省空间),UTF-8把一个Unicode编码根据不同的数字大小编码成1-6个字节,英文字母被编码成1个字节,汉字通常是3个字节

##### 1.6.9 机器码和字节码

机器码就是计算机可以直接执行,并且执行速度最快的代码
字节码是一种中间状态(中间码)的二进制代码(文件),需要直译器转译后才能成为机器码

##### 1.6.10 列举布尔值为False的常见值?

除了标准值 False 和 None,所以类型的数字 0,空序列(空字符,空元祖,空列表,空字典)都为假

##### 1.6.11 Python变量作用域,局部和全局变量?

**变量定义以后，是有一定的使用范围，称之为变量的作用域**

局部变量作用域:只能在被声明的函数内部访问,函数外部无法使用

全局变量作用域:可以在整个程序范围内访问,任意函数都可以访问

```python
#1.局部变量，外部访问不了
def f1 (v1,v2): #参数也属于局部变量
    sum = v1+v2
    a = 5  #局部变量，函数外部访问不了
    return sum

print(a) #报错，NameError: name 'a' is not defined
 
#2.全部变量,函数里外都可以访问
a =3

def f3(v2):
  # a = a+1  注意：报错，因为局部作用域内只能引用全局域变量的值，而不能修改全局作用域的值。
  # b = a+1  则不会报错，引用全局变量的值，运算后给赋给局部变量b.
    return a+1   #外部的全局变量函数内部使用

print(f3(1))  #4

#3.如果全局变量的名字和局部变量的名字相同，那么函数内部使用的是局部变量
sum = 5

def f2(v2):
    sum = 0
    while v2 < 10:
        sum += v2   #这里sum使用的是局部变量的初始值0，而不是全局sum=5
        v2 += 1
    return sum

print(sum)  #5
print(f2(0))  #45

```

**Python的作用域由def、class、lambda等语句产生,if、try、for等语句并不会产生新的作用域,换句话说就是if,try,for等语句里面定义的变量并不会随着该语句执行结束而回收,而是可以到处引用的,if,try,for等语句内变量作用域实际范围受其所在的def、class、lambda范围约束**

##### 1.6.12 Python对象属性查看

1. type() 用于基础类型判断如 int、str,type不会认为子类是一种父类类型,不考虑继承关系
2. isinstance() 用于基础类型判断,会认为子类是一种父类类型,内部会检查继承关系
3. dir() 返回一个对象所有属性和方法
4. hasattr(object, x) 判断这个对象有无x属性

#### 1.7 string

##### 1.7.1 string定义,什么是可变、不可变数据类型?

字符串是字符集合或者字符数组
字符串是序列字符的数组,并写在引号中,python中没有字符数据类型,'a'是长度为1的字符串

可变不可变指的是内存中的值是否可以被改变
不可变类型指的是对象所在内存块里面的值不可以改变,有数值、字符串、元组
可变类型则是可以改变,主要有列表、字典、集合

##### 1.7.2 如何理解Python中字符串中的\字符?

有三种不同的含义
1.转义字符
2.路径名中用来连接路径名
3.编写太长代码手动软换行

##### 1.7.3 string常用方法

###### 1)str.strip('x') 

移出字符串的首尾指定字符(默认为空格或换行符)

```python
str = '0baidu0'

print(str.strip('0'))  #baidu

str = '  baidu  '

print(str.strip())  #baidu

```

###### 2)str.find('x')

检测字符串中是否包含子字符串x,包含子字符串返回开始索引值,否则返回-1

```python
str = '1234567'

str.find('1')  #0

str.find('0')  #-1

```

###### 3)其他

```python
def main():
    str = '1234567'
    
    # len函数计算字符串长度
    len(str)
    
    # 字符串首字母大写
    str.capitalize()
    
    # 字符串大写
    str.upper()
    
    # 字符串是否以指定字符开头
    str.startwith('1')  #True
    
    # 字符串是否以指定字符结尾
    str.endswith('1')  #False
    
    # 检查字符串是否由数字构成
    str.isdigit()  #True
    
    # 检查字符串是否由字母构成
    str.isalpha()  #False
    
    # 检查字符串是否由数字和字母构成
    str.isalnum()  #False
    
if __name__ == '__main__':
    main()
    
```

##### 1.7.4 写出反转字符串的方法

###### 1)切片

```python
str = '12345'

pirnt(str[::-1])

```

###### 2)列表reverse方法

```python
str = '12345'

ls = list(str)
ls.reverse()

print(''.join(ls))

```

###### 3)列表推导

```python
str = '12345'

nstr = ''.join(str(-x) for x in range(1, len(str)+1))

```

###### 4)双指针交换

```python
str = list('12345')

left, righ = 0, len(str)-1
while left < right:
    str[left], str[righ] = str[righ], str[left]
    left += 1
    righ -= 1
    
```



##### 1.7.5 将字符串"k:1|k1:2|k2:3|k3:4"，处理成 Python 字典：{k:1， k1:2， ... } ,字典里的 k 作为字符串处理

##### 1.7.6 请按 ls 中元素的 age 由大到小排序

##### 1.7.7 设计一个函数产生指定长度验证码,验证码由大写字母和数字组成

```python
import random

def generateCode(codelen=4):
    # 生成指定长度验证码

    charall = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    endindex = len(charall)-1

    code = ''

    for x in range(codelen):
        index = random.randint(0, endindex)
        code += charall[index]
    
    return code

print(generateCode())

```

#### 1.8 tuple

tuple:元组,元组将多样的对象集合到一起,不能修改,通过索引进行查找,使用括号()
应用场景:把一些数据当做一个整体去使用,不能修改

```python
a = '1'
b = '1',


pirnt(type(a))  #string

pirnt(type(b))  #tuple

```

#### 1.9 list

list是 Python 中使用最频繁的数据类型,在其他语言中通常叫做数组,通过索引进行查找,使用方括号[], 列表是有序的集合

##### 1.9.1 列表常用方法

###### 1) 增加

在指定位置插入数据 列表.insert(index, value)

```python
ls = [1, 2, 3, 4, 5]

# 列表下标为0的地方插入数据
ls.insert(0,0)

# 列表下标为6的地方插入数据,列表最大下标为4,自动补位插到最后位置
ls.insert(6,6)

```

在列表末尾追加数据 列表.append(value)

```python
ls = [1, 2, 3, 4, 5]

# 末尾追加
ls.append(6)

```

将可迭代对象追加到列表 列表.extend(iterable)

```python
str = '12345'
ls = []

ls.extend(str)

```

###### 2)删除

删除指定索引数据 del 列表[index]

```python
ls = [1, 2, 3, 4, 5]

del ls[4]

```

删除第一个出现的指定元素 列表.remove(value)

```python
ls = [1, 2, 3, 4, 5]

ls.remove(5)

```

删除末尾数据 列表.pop() 返回值是被删除元素

```python
ls = [1, 2, 3, 4, 5]

ls.pop()

```

删除指定索引元素并返回此元素 列表.pop(index)

```python
ls = [1, 2, 3, 4, 5]

ls.pop(4)

```

清空列表元素 列表.clear()

```python
ls = [1, 2, 3, 4, 5]

ls.clear()

```

###### 3)排序

升序排序 列表.sort(reverse=False)

```python
ls = [5, 4, 3, 2, 1]

ls.sort()

```

逆序反转 列表.reverse()

```python
ls = [5, 4, 3, 2, 1]

ls.reverse()

```

###### 4)统计相关

数据在列表中出现的次数 列表.count(value)

```python
ls = [1, 2, 3, 4, 5]

ls.count(1)

```

##### 1.9.2 ls[10]和ls[10:]

尝试获取列表的切片,开始的 index 超过了成员个数不会产生 IndexError,而是仅仅返回一个空列表

```python
ls = [1, 2, 3, 4, 5]


print(ls[10])  #IndexError: list index out of range

print(ls[10:])  #[]

```

##### 1.9.3 给定两个列表,怎么找出他们相同的元素和不同的元素?

```python
l1 = [1, 2, 3]
l2 = [3, 4, 5]

set1 = set(l1)
set2 = set(l2)

print(set1&set2)
print(set1^set2)

```

##### 1.9.4 列表去重

###### 1)set去重

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

nls = list(set(ls))
# key是用来进行比较的元素,只有一个参数,具体的函数的参数就是取自于可迭代对象中,指定可迭代对象中的一个元素来进行排序
nls.sort(key=ls.index)

```

###### 2)循环去重

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

nls = []

for x in ls:
    if x not in nls:
        nls.append(x)
        
```

###### 3)dict属性

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

newdic = {}.fromkeys(ls)

nls = list(newdic)

```

###### 4)count + remove

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

for x in ls[:]:
    if ls.count(x) != 1:
        ls.remove(x)
        
```

##### 1.9.5 列表合并

###### 1)循环

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]

for i in l2:
    l1.append(i)

print(a)

```

###### 2)使用+

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1 = l1 + l2

print(l1)

```

###### 3)使用extend关键字

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l1.entend(l2)

print(l1)

```

如果列表很大,extend效率比+更高

##### 1.9.6 列表排序

使用sort()或者内建函数sorted()对列表进行排序

sort()方法是对原列表进行操作,而sorted()方法会返回一个新列表,不再原来的基础上进行操作

sort()是应用在列表上的方法,而sorted()可以对所有可迭代对象进行排序操作

```python
# sort()
ls = [1, 2, 3, 4, 3, 2, 1]
# 倒序,默认升序
ls.sort(revrese=True)

print(a)

# sorted()
ls = [1, 2, 3, 4, 3, 2, 1]

pirnt(sorted(ls))

```

##### 1.9.7 遍历列表的索引和元素对

使用enumerate()函数可以同时输出索引和元素值

```python
ls = ['go', 'java', 'python']

for i,j in enumerate(ls):
    print(i, j)
    
# output
0 go
1 java
2 python
    
```

##### 1.9.8 查找列表中最频繁的元素

使用max()函数可以快速查找一个列表中出现频率最高的某个元素

```python
ls = [1, 1, 2, 2, 2, 3, 3]

print(max(set(ls), key=ls.count))

```

##### 1.9.9 将两个列表合并成字典

使用zip()函数,可以将两个列表合并成字典

```python
l1 = ['one', 'two', 'three']
l2 = [1, 2, 3]

print(dict(zip(l1, l2)))

```

##### 1.9.10 列表扁平化

使用列表推导式多层递归完成

```python
# 列表扁平化
nls = []

def flatlist(ls):
    for x in ls:
        if isinstance(x, list):
            flatlist(x)
        else:
            nls.append(x)
    return nls

print(flatlist([[1,2,3], 4, [5,[6,7],8]]))

output
[1, 2, 3, 4, 5, 6, 7, 8]

[flatlist(x) for x in ls if instance(x, list) else x]
```

##### 1.9.11 列表推导式

列表推导式的方括号内包含以下内容
==一个表达式后面为一个for子句,然后是零个或多个for或 if 子句,结果是由表达式依据 for和 if子句求值计算而得出一个新列表==

```python
import random

ls = [random.randint(-10,10) for x in range(10)]
# 筛选出ls中大于0的数,小于等于0的数置零
nls = [x if x>0 else 0 for x in ls]

print(nls)

```

#### 1.10 dict

##### 1.10.1 现有字典dic = {'a':5, 'b':4, 'c':3}请按字典中的value值进行排序?

```python
dic = {'a':5, 'b':4, 'c':3}

sorted(dic.items(),key = lambda x:x[1])
```

##### 1.10.2 字典和json的区别?

字典Python中重要的数据类型,字典是有键值对组成集合,通过使用键来访问数据,效率很高,和list一样支持对数据的增删改查

特点

​	不是序列类型,没有下标概念,是无序的键值集合,内置的高级数据类型
​	用{}来表示字典对象,每个键值对用逗号隔开
​	键必须是不可变的类型[数值,字符,元祖],值可以是任意的类型
​	每个键必定是唯一的,如果存在重复的键,后者会覆盖前者

字典是一种数据结构,json 是一种数据的表现形式,字典的 key 值只要是能 hash 的就行,json 的必须是字符串

##### 1.10.3 字典推导式

```python
dic = {key:value for (key, value) in iterable}
```

##### 1.10.4 输出一个字符串中每个字符的个数

###### 1)dict.get方法

```python
str = 'life is short I use python'

dic = dict()

for x in str:
    dic[x] = dic.get(x,0) + 1
    
print(dic)

# dict.get(Key,default=None),返回指定键的值,如果键不在字典中返回默认值为None或者设置的默认值

```

###### 2)dict属性

```python
str = 'life is short I use python'

dic = dict()

for x in str:
    if x not in dic.keys():
        dic[x] = 1
    else:
        dic[x] += 1
        
print(dic)

```

###### 3)collections模块

```python
from collections import Counter

str = 'life is short I use python'

dic = dict(Counter(str))
        
print(dic)

```

##### 1.10.5 字典由value获取key的方法

方法一 字典列表化

```python
stuinfo = {1:'小明', 2:'小红', 3:'小绿'}

def getKey(dict, value):
    return list(dict.keys())[list(dict.values()).index(value)]
    

print(getKey(stuinfo, '小明'))  #1

```

方法二 推导式

```python
stuinfo = {1:'小明', 2:'小红', 3:'小绿'}

def getKey(dict, value):
    return [x for x,y in dict.items() if y==value].pop()

print(getKey(stuinfo, '小红'))  #2

```

方法三 key,value值互换

```python
stuinfo = {1:'小明', 2:'小红', 3:'小绿'}

def getKey(dict, value):
    newdict = {v,k for k,v in dict.items()}
    return newdict[value]

pirnt(getKey(stuinfo, '小绿'))  #3

```

##### 1.10.6  写一个函数满足以下行为输出结果按照层级把同一层的属性放到一个子数组内

//输入对象
{"a":{"b":{"c":{"d":"h","j":"i","o":{"p":"q","r":"s"},"t":"u"}},"v":{"w":{"x":{"y":"z"}}}},"e":{"f":{"i":"k"},"m":"n"}}

//输出结果
[['a', 'e'], ['b', 'v', 'f', 'm'], ['c', 'w', 'i'], ['d', 'j', 'o', 't', 'x'], ['p', 'r', 'y']]

```python
def getDictKey(dictValue,answ = []):
    keys = []
    newdict = {}
    flag = False

    for key, value in dictValue.items():
        keys.append(key)
        if isinstance(value, dict):
            newdict.update(value)
            flag = True
        else:
            continue

    answ.append(keys)

    if flag:
        getDictKey(newdict, answ)

    return answ

```

##### 1.10.7 有一个下属-上级的映射表d:{1:2, 2:3, 4:3, 5:3, 6:5, 7:5, 8:5, 0:1}, 键代表下属id,值代表其所对应的上级,每个id代表不同的人,编写函数输出某个人的所有下属列表

```python
def myEmployees(num):
    dt = {1:2, 2:3, 4:3, 5:3, 6:5, 7:5, 8:5, 0:1}
    # newd = dict.fromkeys(dt.values(), [])
    newd = {key: [] for key in dt.values()}
    for i, j in dt.items():
        newd[j].append(i)
        
    return newd[num]
```

==使用dict.fromkeys() 创建的初始值[]指向同一个内存空间,类似于浅拷贝,所以使用字典生成式生成初始列表用以区分添加元素==

#### 1.11 set

set 集合,在 Python 中的书写方式的{},集合与之前列表、元组类似,可以存储多个数据,但是这些数据是不重复的
集合对象还支持 union(联合), intersection(交), difference(差)和sysmmetric_difference(对称差集)等数学运算

##### 1.11.1 集合常用操作

1)列表去重

```python
ls = [1, 1, 2, 2, 3, 3, 4, 4]

set(ls)

```

2)交集(共有部分)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a & b)

```

3)并集(总共部分)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a|b)

```

4)差集(另一个集合中没有部分)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a - b)
```

5)对称差集(在二者中,但不会同时出现在二者中)

```python
a = {1, 2, 3, 4, 5}
b = {1, 3, 5, 7, 9}

print(a ^ b)

```

#### 1.12 数据读写

##### 1.12.1 Python中读写json数据

json是一种数据交换格式,之前大家都是用xml传递数据,格式比较复杂,道格拉斯发明了json超轻量级数据交换格式

json规定字符集是utf-8,字符串必须使用双引号,数组或对象的最后一个成员不能加逗号

json语法规则

> 数据在名/值对中
> 数据由逗号分隔
> 方括号保存数组
> 花括号保存对象

json值

>数字  整数或浮点数
>字符  双引号中
>数组  方括号中
>对象  花括号中
>布尔值
>null

Python数据结构转换为json格式str对象	json.dumps()

```python
import json

data = {
    'name' : 'MIMI',
    'price' : 10
}

print(json.dumps(data))
print(type(json.dumps(data)))

output
{"name": "MIMI", "price": 10}
<class 'str'>

```

json格式str对象转换为Python数据结构	json.loads()

```python
import json

data = '{"name": "MIMI", "price": 10}'

print(json.loads(data))
print(type(json.loads(data)))

output
{'name': 'MIMI', 'price': 10}
<class 'dict'>

```

##### 1.12.2 with语句和上下文管理器

###### 1)with

with是python引入的一个新的语法,它是一种上下文管理协议,目的在于从流程图中把try,except和finally关键字和资源分配释放相关代码去除,简化try...except...finally处理流程

没有使用with

```python
try:
    file = open('sample.txt','r')
    file.write('ABC')
except Exception as e:
    print(e)
finally:
    file.close()
    
```

使用with

```python
with open('sample.txt', 'r') as f:
    f.write('ABC')
    
```

###### 2)上下文管理器

一个类只要实现了\_\_enter\_\_()和\_\_exit\_\_()这两个方法,通过该类创建的对象我们就称之为上下文管理器

```python
class File(object):

    def __init__(self, fileName, fileMode):
        self.fileName = fileName
        self.fileMode = fileMode

    # 上文方法,负责返回操作对象资源,比如文件对象、数据库连接对象
    def __enter__(self):
        self.file = open(self.fileName, self.fileMode)
        return self.file

    # with语句执行完成以后自动执行__exit__方法
    # 下文方法,负责释放对象资源,比如关闭文件、关闭数据库连接对象
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('over')
        self.file.close()
        
# with语句结合上下文管理器对象使用
with File('1.txt', 'w+') as f:
    fd = f.write('ABC')
    
```

#### 1.13 Poperty属性

##### 1.13.1 定义

定义property属性就是把一个方法当做属性进行使用,这样做可以简化代码使用

##### 1.13.2 实现方式

###### 1)装饰器方式

==使用装饰器方式的property属性那么方法名要保持一致==

一般调用方法

```python
class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    def age(self):
        print('获取属性')
        return self.__age


stud = Student()
age = stud.age()
print(age)

```

poperty属性

```python
class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    # 当对象调用age属性的时候就会执行下面的方法
    @property
    def age(self):
        print('获取属性')
        return self.__age

    @age.setter
    def age(self, newAge):
        print('设置属性')
        if 0 <= newAge <= 100:
            self.__age = newAge
        else:
            print('百岁')

stud = Student()
age = stud.age
print(age)

stud.age = 20
age = stud.age
print(age)

output:
获取属性
0
设置属性
获取属性
20

```

###### 2)类属性方式

```python
class Student(object):
    def __init__(self):
        # 私有属性
        self.__age = 0

    def getAge(self):
        print('获取属性')
        return self.__age

    def setAge(self, newAge):
        print('设置属性')
        if 0 <= newAge <= 100:
            self.__age = newAge
        else:
            print('百岁')

    # getAge 表示获取age属性时候执行方法
    # setAge 表示设置age属性时候执行方法
    age = property(getAge, setAge)


stud = Student()
age = stud.age
print(age)

stud.age = 20
age = stud.age
print(age)

output:
获取属性
0
设置属性
获取属性
20

```

### 二. Python高级

#### 2.1 Python中类方法、类实例方法、静态方法有何区别?

**类方法**
是类对象的方法,在定义时需要在上方使用@classmethod进行装饰,形参为 cls,表示类对象,类对象和实例对象都可调用 

**类实例方法**
是类实例化对象的方法,只有实例对象可以调用,形参为 self,指代对象本身

**静态方法**
是一个任意函数,在其上方使用@staticmethod进行装饰,可以用实例对象和类对象直接调用,静态方法实际上跟该类没有太大关系

#### 2.2 Python的内存管理机制及调优手段?

**内存管理机制:引用计数、垃圾回收、内存池**

**引用计数**

引用计数是一种非常高效的内存管理手段
当一个 Python 对象被引用时其引用计数增加 1,当其不再被一个变量引用时则计数减 1,当引用计数等于 0 时对象被删除

**垃圾回收**

+ 引用计数
  引用计数也是一种垃圾收集机制,而且也是一种最直观,最简单的垃圾收集技术
  当 Python 的某 个对象的引用计数降为 0 时,说明没有任何引用指向该对象,该对象就成为要被回收的垃圾了
  比如某个新建对象,它被分配给某个引用,对象的引用计数变为 1
  如果引用被删除,对象的引用计数为 0,那么该对象就可以被垃圾回收
  不过如果出现循环引用的话,引用计数机制就不再起有效的作用了
+ 标记清除
  如果两个对象的引用计数都为 1,但是仅仅存在他们之间的循环引用,那么这两个对象都是需要被回收的,也就是说,它们的引用计数虽然表现为非 0,但实际上有效的引用计数为 0,所以先将循环引用摘掉,就会得出这两个对象的有效计数
+ 分代回收
  从前面 标记-清除 这样的垃圾收集机制来看,这种垃圾收集机制所带来的额外操作实际上与系统中总的内存块的数量是相关的,当需要回收的内存块越多时,垃圾检测带来的额外操作就越多,而垃圾回收带来的额外操作就越少,反之,当需回收的内存块越少时,垃圾检测就将比垃圾回收带来更少的额外操作
  举个例子,当某些内存块 M 经过了 3 次垃圾收集的清洗之后还存活时,我们就将内存块 M 划到一个集合 A 中去,而新分配的内存都划分到集合 B 中去,当垃圾收集开始工作时,大多数情况都只对集合 B 进 行垃圾回收,而对集合 A 进行垃圾回收要隔相当长一段时间后才进行,这就使得垃圾收集机制需要处理的内存少了,效率自然就提高了,在这个过程中,集合 B 中的某些内存块由于存活时间长而会被转移到集合 A 中,当然集合 A 中实际上也存在一些垃圾,这些垃圾的回收会因为这种分代的机制而被延迟

#### 2.3 内存泄露是什么,如何避免?

内存泄露指由于疏忽或错误造成程序未能释放已经不再使用的内存的情况
内存泄漏并非指内存在物理上的 消失,而是应用程序分配某段内存后,由于设计错误,失去了对该段内存的控制,因而造成了内存的浪 费,导致程序运行速度减慢甚至系统崩溃等严重后果
有 __del__() 函数的对象间的循环引用是导致内存泄漏的主凶,不使用一个对象时使用:del object 来删除一个对象的引用计数就可以有效防止内存泄漏问题,通过 Python 扩展模块 gc 来查看不能回收的对象的详细信息,可以通过 sys.getrefcount(obj) 来获取对象的引用计数,并根据返回值是否为 0 来判断是否内存泄漏

#### 2.4 函数参数

##### 2.4.1 Python函数调用的时候参数的传递方式是值传递还是引用传递?

**Python 的参数传递有:位置参数、默认参数、可变参数、关键字参数**

函数的传值到底是值传递还是引用传递，要分情况

不可变参数用值传递
像整数和字符串这样的不可变对象,是通过拷贝进行传递的,因为你无论如何都不可能在原处改变不可变对象

可变参数引用传递
比如像列表,字典这样的对象是通过引用传递、和 C 语言里面的用指针传递数组很相似,可变对象能在函数内部改变

##### 2.4.2 对缺省参数的理解

缺省参数指在调用函数的时候没有传入参数的情况下,调用默认的参数,在调用函数的同时赋值时,所传入的参数会替代默认参数 *args 是不定长参数,他可以表示输入参数是不确定的,可以是任意多个
**kwargs 是关键字参数,赋值的时候是以键 = 值的方式,参数是可以任意多对在定义函数的时候不确定会有多少参数会传入时,就可以使用两个参数

##### 2.4.3 为什么函数名字可以当做参数用?

Python 中一切皆对象,函数名是函数在内存中的空间,也是一个对象

##### 2.4.4 Python中pass语句的作用是什么?

在编写代码时只写框架思路,具体实现还未编写就可以用 pass 进行占位,使程序不报错,不会进行任何操作

#### 2.5 内建函数

##### 2.5.1 filter、map函数和reduce函数?

1)从参数来讲
map()包含两个参数,第一个参数是一个函数,第二个(列表或元组),其中,函数(即 map 的第一个参数位置的函数)可以接收一个或多个参数
reduce()第一个参数是函数,第二个是序列(列表或元组),但是,其函数必须接收两个参数

2)从对传进来的数值作用来讲
map()是将传入的函数依次作用到序列的每个元素,每个元素都是独自被函数作用一次
reduce()是将传入的函数作用在序列的第一个元素得到结果后,把这个结果继续与下一个元素作用(累积计算)

```python
# 筛选列表中大于5的元素
ls = [1, 2, 3, 4, 5]

nls = filter(lambda x:x>3, ls)

print(list(nls))

```

```python
# 列表元素平方
ls = [1, 2, 3, 4, 5]

nls = map(lambda x:x**2, ls)

print(list(nls))

```

```python
# 求3阶乘
from functools import reduce

fact = reduce(lambda x,y:x*y,range(1,4))

print(fact)

```

##### 2.5.2 什么是lambda函数,有什么好处?

lambda 函数是一个可以接受任意多个参数(包括可选参数)并且返回单个表达式值函数,这种函数得名于省略了用 def 声明函数标准步骤 

1. lambda 函数比较轻便,即用即仍,适合需要完成一项功能,但此功能只在一处使用,连名字都很随意情况下
2. 匿名函数,一般用来给filter、map这样的函数式编程服务
3. 作为回调函数,传递给某些应用,比如消息处理

##### 2.5.3 all()和zip()

all()	函数用于判断给定的可迭代对象iterable中的所有元素是否都为TRUE,如果是返回TRUE,否则返回False

```python
# 判断注册参数
if not all([username, password, phone]):
    return '缺少必传参数'

```

zip()	函数用于将可迭代对象作为参数,将对象中对应的元素都打包成一个个元祖,然后由这些元祖组成的对象

#### 2.6 上下文管理器

with 是python引入的一个新的语法,是一种上下文管理协议,目的在于从流程图中把try....except....finally关键字和资源分配释放相关代码去除,简化处理流程

一个类只要实现了\_\_enter\_\_() 和\_\_exit\_\_()两个方法,通过该类创建的对象我们就称为上下文管理器

with 语句是由上下文管理器支撑,也就是说使用open函数创建的文件对象就是一个上下文管理器对象

#### 2.7 GIL(全局解释器锁)

Python为了利用多核,支持多线程,解决多线程之间数据完整性和状态同步的最简单方法自然是加锁,于是便有了GIL这把超级大锁,使得同一时刻只有一个线程在CPU单核上执行字节码

GIL会根据执行的字节码行数以及时间片释放GIL,GIL再遇到IO操作时会主动释放

[GIL代码演示](file/gil.ipynb ':include : type=code')

### 三. 设计模式

#### 3.1 单例模式

单例模式是一种常用的软件设计模式,在它的核心结构中只包含一个被称为单例类的特殊类
通过单例模式可以保证系统中一个类只有一个实例而且该实例易于外界访问,从而方便对实例个数的控制并节约系统资源
==如果希望在系统中某个类的对象只能存在一个,单例模式是最好的解决方案==

##### 3.1.1 手写单例

在 python 中,可以使用多种方法实现单例模式

###### 1)使用模块

Python的模块是天然单例模式,因为模块在第一次导入时,会生成 .pyc 文件,当第二次导入时,直接加载 .pyc 文件,不会再次执行模块代码

```python
# mysingle.py 
class MySingle: 
    def foo(self): 
        pass 

sinleton = MySingle() 

# 将上面的代码保存在文件 mysingle.py 中,然后

from mysingle import sinleton 

singleton.foo()

```

###### 2)使用\_\_new__()

为了使类只能出现一个实例,我们可以使用\_\_new__来控制实例的创建

```python
class Singleton(object):
    def __new__(cls):
    	# 每一次实例化的时候,我们都只会返回这同一个 instance 对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


obj1=Singleton()
obj2=Singleton()

obj1.attr='value'

print(obj1 is obj2)  #True
print(obj1.attr, obj2.attr) #value value

```

###### 3)使用装饰器

###### 4)使用metaclass(元类)

##### 3.1.2 单例模式应用场景

#### 3.2 装饰器

##### 3.2.1 什么是装饰器,手写一个计时器记录方法执行性能装饰器?

装饰器就是给已有函数增加额外功能的函数,它本质上就是一个闭包函数
==使用装饰器装饰已有函数的时候,内部函数的类型和要装饰的已有函数的类型保持一致==

特点

​	不修改已有函数的代码
​	不修改已有函数的调用方式
​	给已有函数增加额外的功能

###### 1)装饰无参无返回值函数

```python
import time

# 装饰器的定义
def runtime(func):
    def wrapper():
        sta = time.time()
        # 函数无参无返回值
        func()
        end = time.time()
        print('TIMECOST:%fS'%(end-sta))
    return wrapper

def isPrimeNumber(num):
    if num <= 1:
        return False
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
        return True

@runtime # 装饰器语法糖写法 primeNumber = runtime(primeNumber) == wrapper
def primeNumber():
    for i in range(1,1000):
        if isPrimeNumber(i):
            print(i)

primeNumber()

output:
..
..
971
977
983
991
997
TIMECOST:0.036900S
    
```

###### 2)装饰有参函数

**装饰有参无返回值函数**

```python
def decorator(func):
    def inner(x, y):
        print('正在执行加法运算')
        func(x, y)
    return inner

@decorator
def addNum(x, y):
    result = x+y
    print('rlt', result)

    
addNum(1, 2)

output:
正在执行加法运算
rlt 3

```

**装饰有参有返回值函数**

```python
def decorator(func):
    def inner(x, y):
        print('正在执行加法运算')
        rlt = func(x, y)
        return rlt
    return inner

@decorator
def addNum(x, y):
    return x+y


print(addNum(1, 2))

正在执行加法运算
3

```

**装饰带有不定长参数的返回值的函数**

```python
def decorator(func):
    def inner(*args,**kwargs):
        print('正在执行加法运算')
        # *args : 把元祖里面的每一个元素,按照位置参数进行传参
        # **kwargs : 把字典里面的每一个键值对,按照关键字的方式进行传参
        rlt = func(*args, **kwargs)
        return rlt
    return inner


@decorator # addNum = decorator(addNum) -> addNum = inner
def addNum(*args, **kwargs):
    result = 0

    # args : 元祖类型 -> 位置参数
    # kwargs : 字典类型 -> 关键字参数
    for val in args:
        result += val

    for val in kwargs.values():
        result += val

    return result

print(addNum(1, 2))

```

==该装饰器可以装饰所有通用函数,无参函数元祖和字典均为空==

##### 3.2.2 什么是闭包?

在函数嵌套的前提下,内部函数使用了外部函数的变量,并且外部函数返回了内部函数,我们把这个使用外部函数变量的内部函数称为闭包

**闭包构成条件**
	函数嵌套(函数里面再定义函数)的前提下
	内部函数使用了外部函数的变量(还包括外部函数的参数)
	外部函数返回了内部函数,这个使用了外部函数变量的内部函数称之为闭包

```python
def funcout():
    # 外部函数
    x = 10

    def funcinner(y):
        # 内部函数
        # 内部函数使用了外部函数的变量
        result = x + y
        print('rlt', result)

    # 外部函数返回内部函数,这个使用了外部函数变量的内部函数称为闭包
    return funcinner


# 获取闭包对象
# 这个newfunc就是闭包
# 这里的newfunc = funcinner
newfunc = funcout()
# 执行闭包
newfunc(10)

```

需求

根据配置信息使用闭包实现不同人的对话信息
例如:张三->到北京了没? 李四->已经到了放心吧

```python
# 外部函数接收姓名参数
def configName(name):
    # 内部函数保存外部函数参数,并且完成数据显示组成
    def inner(msg):
        print(name + ':' + msg)
# 外部函数返回内部函数
    return inner

# 创建mas闭包实例
mas = configName('mas')
# 创建zzs闭包实例
zzs = configName('zzs')

# 如果执行闭包,因为已经保存了name参数,以后在输入的时候都是name:XXXX
mas('你爱我吗?')
zzs('爱')

```

#### 3.3 迭代器、生成器

##### 3.3.1 迭代器、生成器区别？

**迭代器** 

**一个对象拥有\__iter__() 和 \_\_next\_\_() 方法,则这个对象就是迭代器(迭代器协议)**

可以用在 for...in... 语句中的都是可迭代的,比如 list, strings, files...因为这些可迭代的对象你可以随意的读取所以非常方便易用,
但是你必须把它们的值放到内存里,当它们有很多值时就会消耗太多的内存

```python
from collections import Iterable


ls = [1,2,3,4,5]
tu = (1,2,3,4,5)
dc = {1:2,3:4}
st = {1,2,3,4,5}

str = '12345'

# 判断一个对象是否可以迭代,上述都是可迭代的对象
print(isinstance(ls,Iterable))  #True
print(isinstance(tu,Iterable))  #True
print(isinstance(dc,Iterable))  #True
print(isinstance(st,Iterable))  #True

print(isinstance(str,Iterable))  #True

```

**生成器(generator)**

生成器也是迭代器的一种,但是只能迭代它们一次,因为它们不是全部存在内存里,它们只在要调用的时候在内存里生成,
生成器和迭代器的区别就是用()代替[],还有你不能用 for i in generator 第二次调用生成器,生成器会首先计算0,然后会在内存里丢掉0去计算1,直到计算完全

==根据制定规则生成循环数据,当条件不成立则生成数据结束,数据不是一次性全部生成处理,而是使用一个,生成一个,可以节约大量内存空间==

##### 3.3.2 将列表中的 [] 改成 () 之后数据结构是否发生改变?

数据结构从列表变为生成器

```python
ls = [x*x for x in range(10)]

print(ls,type(ls))  #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] <class 'list'>

en = (x*x for x in range(10))

print(en)  #<generator object <genexpr> at 0x000002A04FC21ED0>

```

通过列表生成式,可以直接创建一个列表,且创建一个包含百万元素的列表,不仅是占用很大的内存空间,
如:我们只需要访问前面的几个元素,后面大部分元素所占的空间都是浪费的
因此,没有必要创建完整的列表(节省大量内存空间)

在Python中,我们可以采用生成器:**边循环,边计算**的机制来应对这种需求

##### 3.1.3 生成器的创建

###### 1)生成器推导式

```python
myGenerator = (i*2 for i in range(3))

# while循环获取生成器中的值
while True:
    try:
        # 生成器取值使用next函数获取生成器中的下一个值
        value = next(myGenerator)
        print(value)
    except StopIteration:
        break

```

==生成器把所有数据生成完毕后,再次next会抛出一个StopIterration异常==
==for循环内部循环调用next()函数,获取生成器中的下一个值,当出现异常for循环内部自动进行了异常捕获==

###### 2)yield关键字

```python
def ownGenerator():
    for i in range(3):
        # 当程序执行到yield关键字的时候代码会暂停并把结果返回,再次启动生成器的时候会在暂停的位置继续向下执行
        yield i
        
rlt = ownGenerator()

for value in rlt:
    print(value)
    
```

##### 3.1.4 使用生成器生成斐波拉契数列

```python
# num 表示生成斐波那契数列个数
def fibonacci(num):
    # 初始化前两值
    a = 0
    b = 1

    # 记录每次生成个数的索引
    curindex = 0

    # 循环判断条件是否成立
    while curindex < num:
        rlt = a
        # 条件成立交换连个变量的值
        a, b = b, a+b
        curindex += 1
        # 当程序执行到yield关键字的时候代码会暂停并把结果返回,再次启动生成器的时候会在暂停的位置继续向下执行
        yield rlt


# 创建生成器
f = fibonacci(5)

for i in f:
    print(i)

```

#### 3.3 方法重载与方法重写?

##### 3.3.1 方法重载

是在一个类里面,方法名字相同,而参数不同,返回类型可以相同也可以不同
重载是让类以统一的方式处理不同类型数据的一种手段

##### 3.3.2 方法重写

子类不想原封不动地继承父类的方法,而是想作一定的修改,这就需要采用方法的重写,方法重写又称方法覆盖

#### 3.4 接口设计原则

**SRP 单一职责原则**

**里氏替换原则**
任何基类可以出现的地方,子类一定可以出现.
LSP 是继承复用的基石,只有当派生类可以替换掉基类,且软件单位功能不受到影响时,基类才能真正被复用,而派生类也能够在基类的基础上增加新的行为.
里氏代换原则是对开闭原则的补充.实现开闭原则的关键步骤就是抽象化,而基类与子类的继承关系就是抽象化的具体实现,所以里氏代换原则是对实现抽象化的具体步骤的规范

**DIP依赖倒置原则**
针对接口编程,依赖于抽象而不依赖于具体.

**接口隔离原则**

**迪米特法则**
一个实体应当尽量少地与其他实体之间发生相互作用,使得系统功能模块相对独立

**OCP开闭原则**
==开闭原则的意思是对扩展开放,对修改关闭.==
在程序需要进行拓展的时候,不能去修改原有的代码,实现一个热插拔的效果.
简言之,是为了使程序的扩展性好,易于维护和升级.

### 四. 面向对象

==类是对象的抽象,对象是类的实例==

#### 4.1 对象

##### 4.1.1 Python中的可变对象和不可变对象?

不可变对象,该对象所指向的内存中的值不能被改变
当改变某个变量时候,由于其所指的值不能被改变,相当于把原来的值复制一份后再改变,这会开辟一个新的地址,变量再指向这个新的地址
可变对象,该对象所指向的内存中的值可以被改变
变量(准确的说是引用)改变后,实际上是其所指的值直接发生改变,并没有发生复制行为,也没有开辟新的出地址,通俗点说就是原地改变

**Python 中,数值类型(int 和 float)、字符串 str、元组 tuple 都是不可变类型,而列表 list、字典 dict、集合 set 是可变类型**

##### 4.1.2 Python中is和==的区别?

is 判断的是 a 对象是否就是 b 对象,是通过 id 来判断的 
== 判断的是 a 对象的值是否和 b 对象的值相等,是通过 value 来判断的

##### 4.1.3 对面向对象的理解?

面向对象是相对于面向过程而言的,面向过程语言是一种基于功能分析的、以算法为中心的程序设计方法
而面向对象是一种基于结构分析的、以数据为中心的程序设计思想

**面向对象有三大特性:封装、继承、多态**

##### 4.1.4 OOP编程三大特征是什么?

**封装**
就是将一个类的使用和实现分开,只保留部分接口和方法与外部联系

**继承**
子类自动继承其父级类中的属性和方法,并可以添加新的属性和方法或者对部分属性和方法进行重写,增加代码可重用性

**多态**
多个子类中虽然都有同一个方法,但是这些子类实例化的对象调用这些相同方法后却可以获得不同的结果,多态增加了增加了应用灵活性(多态概念依赖继承)

##### 4.1.5 \_\_mro\_\_算法(深度优先-广度优先-C3算法)

当一个类有多个父类的时候,默认使用第一个父类的同名属性和方法
如果子类和父类拥有同名属性和方法,子类创建对象调用属性方法时,调用到的是子类里的同名属性方法

```python
class D:
    pass

class C(D):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)

# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
```

#### 4.2 一切皆对象

##### 4.2.1 Python中一切皆是对象

函数和类亦是对象

```python
def info(name='mas'):
    print(name)
    
class Person:
    def __init__(self, name):
        print(name)
# 可以赋值给个变量

# 可以添加到集合的对象

# 可以作为参数传递函数

# 可以作为函数的返回值
```

##### 4.2.2 type、object和class关系

##### 4.2.3 Python中常见数据类型

==对象三个属性:id、类型和值==

```python
a = None
b = None

id(a) == id(b)

```



| 类型             |                 举例                  |
| ---------------- | :-----------------------------------: |
| None             |             全局唯一对象              |
| 数值             |    int、float、complex(复数)、bool    |
| 迭代类型         |             迭代器生成器              |
| 序列类型         | list、bytes、range、tuple、str、array |
| 映射             |                 dict                  |
| 集合             |            set、frozenset             |
| 上下文管理器类型 |               with语句                |

#### 4.3 魔法函数

##### 4.3.1 什么是魔法函数

4.3.2 Python数据模型对Python的影响

### 五. 爬虫测试

#### 5.1 正则语法

##### 5.1.1 定义及常用语法

**定义**

正则表达式是一个特殊的字符序列,用以检查一个字符串是否与某种模式匹配

###### 1)re.match

```python
# re.match
#     re.match 尝试从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,match()就返回none
#     re.match(pattern,string,flags=0)
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     flags 标志位,用于控制正则表达式的匹配方式,如是否区分大小写
#     匹配成功re.match方法返回一个匹配的对象,否则返回None

import re

print(re.match('www', 'www.baidu.com'))  #<re.Match object; span=(0, 3), match='www'>
print(re.match('com', 'www.baidu.com'))  #None

```

###### 2)re.search

```python
# re.search
#     re.search 扫描整个字符串并返回第一个成功的匹配
#     re.search(pattern,string,flags=0)
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     flags 标志位,用于控制正则表达式的匹配方式,如是否区分大小写
#     匹配成功re.search方法返回一个匹配的对象,否则返回None

import re

print(re.match('www', 'www.baidu.com'))  #<re.Match object; span=(0, 3), match='www'>
print(re.match('com', 'www.baidu.com'))  #None

```

###### 3)re.sub

```python
# re.sub
#     re.sub用于替换字符串中的匹配项
#     re.sub(pattern, repl, string, count=0, flags=0)
#     pattern 正则中的模式字符串
#     repl 替换的字符串,也可为一个函数
#     string 要被查找替换的原始字符串
#     count 模式匹配后替换的最大次数,默认0表示替换所有的匹配

import re

# 去除#后面的字符
print(re.sub('#.+$', '', 'mm is a cute cat # mm是一直可爱的猫咪'))  #mm is a cute cat

```

###### 4)re.compile

```python
# re.compile
#     compile 函数用于编译正则表达式,生成一个正则表达式(Pattern)对象,供match()和search()这两个函数使用
#     re.compile(pattern[, flags])
#     pattern 一个字符串形式的正则表达式
#     flags 可选,表示匹配模式,比如忽略大小写,多行模式等,具体参数为
#         re.I 忽略大小写
#         re.X 为了增加可读性，忽略空格和 # 后面的注释

import re

pattern = re.compile(r'[a-z]+ [a-z]+', re.I)  #中有空格
print(pattern)  #re.compile('[a-z]+ [a-z]+', re.IGNORECASE)

```

###### 5)re.findall

```python
# re.findall
#     在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果没有找到匹配的,则返回空列表
#     re.findall(patter,string[,pos[,endpos]])
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     pos 可选参数,指定字符串的起始位置,默认为0
#     endpos 可选参数,指定字符串的结束位置,默认为字符串的长度

import re

print(re.findall('[0-9]+','1岁,2岁,3岁,4岁'))  #['1', '2', '3', '4']

```

###### 6)re.split

```python
# re.split
#     split方法按照能够匹配的子串将字符串分割后返回列表
#     re.split(pattern, string[, maxsplit=0, flags=0])
#     pattern 匹配的正则表达式
#     string 要匹配的字符串
#     maxsplit 分隔次数,maxsplit=1分隔一次,默认为0,不限制次数

# \W 匹配字母数字下划线
import re

print(re.split('\W+','love-will-disappear'))  #['love', 'will', 'disappear']

```

match() 函数监测 RE 是不是在 string 开始位置匹配
search() 函数会扫描整个 string 查找匹配

如果不是在开始位置匹配成功的话,match() 就返回 None

==re.match只匹配字符串的开始,如果字符串开始不符合正则表达式,则匹配失败,函数返回None,而re.search匹配整个字符串,直到找到一个匹配==

##### 5.1.2 常用正则字符简写

| 正则 |                             说明                             |
| ---- | :----------------------------------------------------------: |
| \d   |                      [0-9]任意一个数字                       |
| \D   |             [^0-9],跟\d相反表示除数字之外的字符              |
| \w   |          [a-zA-Z0-9_]匹配任意一个数字字母或者下划线          |
| \W   |                        [^a-zA-Z0-9_]                         |
| \s   | [\t\r\n\f]任意匹配一个空格、制表符、换行或者换页符,空白字符  |
| \S   |                  \s取反,匹配任何非空白字符                   |
| .    |                匹配出换行符\n之外的任何单字符                |
| *    |                  匹配前面子表达式零次或多次                  |
| +    |                  匹配前面子表达式一次或多次                  |
| ?    |      匹配前面子表达式零次或一次,或指明一个非贪婪限定符       |
| ()   | ==括号子表达式==开始和结束位置,提取匹配的字符串,(\s*)表示连续空白字符 |
| []   | ==中括号范围表达式==的开始和结束位置,定义匹配字符范围,[\s*]表示空白字符或者\* |
| {}   | ==大括号长度表达式==开始和结束位置,定义匹配长度,\s{3}表示匹配3个空白字符 |

可以用group()方法来提取匹配到的数据

```python
re.match('www', 'www.baidu.com').group
```

##### 5.1.3 常用正则表示

| 说明     | 表示 |
| -------- | ---- |
| IPv4     |      |
| 手机号码 |      |
| 身份证号 |      |

#### 5.2 Scrapy爬虫

##### 5.2.1 scrapy框架简介

scrapy框架是用纯python实现一个为了爬取网站数据、提取结构化数据而编写的应用框架

##### 5.2.2 scrapy架构图示

![image-20210405103349896](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210405103349896.png)

##### 5.2.3 安装使用

> pip install scrapy

新建scrapy项目

创建爬虫项目

> scrapy startproject 项目名称

创建爬虫文件

> scrapy genspider 文件名称 域名

启动爬虫项目

> scrapy crawl name

#### 5.3 软件测试

##### 5.3.1 概念

[常见概念](file/Python接口自动化.od ':include :type=code')

+ 黑盒测试

也称功能测试,黑盒测试着眼于程序外部结构,不考虑内部逻辑,主要针对软件界面和软件功能进行测试
在黑盒测试中,被测对象的内部结构和运作情况对测试人员是不可见的,测试人员检查程序功能是否按照规格说明书规定正常使用,是否能接收数据及产生正确的输出信息,并且满足数据库或者外部信息的完整性.也叫功能测试,市场上多数是手工测试,进阶的话就是自动化功能UI测试

+ 冒烟测试

对软件的基本功能进行测试,针对每个版本或每次需求变更后,在正式测试前对产品或系统的一次简单的验证性测试,通过后才进行后续的其他测试

+ 白盒测试

按照程序内部结构,逻辑驱动测试程序,用代码内部的分支,路径,条件,使程序设计的控制结构设计测试用例

+ 测试用例

是为了特定的目的而设计的一组有测试输入、执行条件、预期结果的输出文档
一般包含用例编号、用例标题、测试项目、用例级别、预置条件、测试输入、执行步骤、预期结果八个要素

+ 软件测试V模型

需求分析 - 概要设计 - 详细设计 - 软件编码 - 单元测试 - 集成测试 - 系统测试 - 验收测试

##### 5.3.2 常用测试点

+ 上传图片地方要用小写和大写后缀名进行测试

##### 5.3.2 图片内存大小设置

需求:最多添加3张图片,图片大小不超过12M

方法:windows命令行自带的copy命令

![image-20210428094704735](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210428094704735.png)

##### 5.3.3 web端和App端测试的不同?

单纯从功能测试的层面上来说,两端在流程和功能测试上是没有区别的

根据载体不一样,则区别如下

+ 系统结构方面
  + web项目B/S架构,基于浏览器的,web测试只要更新了服务端,客户端就会同步更新
  + App项目C/S架构,必须要有客户端,修改了服务端,则App所有核心版本都需要进行回归测试
+ 性能反面
  + web项目监测响应时间、CPU、Memory
  + App项目监测响应时间、CPU、Memory、流量、电量等

相对web项目,App有专项测试

+ 干扰测试:中断、来电、短信、关机、重启
+ 弱网测试、网络切换测试
+ 安装更新卸载

##### 5.3.4 印象最深的缺陷?

测试微信小程序中,安卓可以正常解析,IOS系统对js中的new Date()方法有格式要求,需要使用2020/02/20格式
而在实际应用日期格式大部分都为2020-02-20,所以在苹果开发过程中需要用正则对字符串进行预处理

```js
let ordt = '2020-02-20 19:00'
let nedt = new Date(ordt.replace(/-/g, '/')) // /g表示全局替换
```

##### 5.3.5 测试环境搭建步骤

```bash
cd /usr/program/script
echo "stop tomcat"
# 关闭tomcat服务
systemctl stop tomcat-fv-dev.service
mv FaceView_ZG-1.0-SNAPSHOT.war fv-test.war
# 移动war包到tomcat webapps目录下
mv fv-test.war /usr/program/tomcat-fv-dev/webapps
cd /usr/program/tomcat-fv-dev/webapps
rm -rf fv-test
echo "unzip war"
unzip -oq fv-test.war -d fv-test
rm fv-test.war
# 重启tomcat服务
echo "start tomcat"
systemctl start tomcat-fv-dev.service
echo "部署成功"

```

#### 5.4 jenkins + jmeter 集成压力测试

##### 5.4.1 安装

##### 5.4.2 jmeter

![image-20210712140508548](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210712140508548.png)

启动提示信息
不要使用GUI运行压力测试,GUI仅用于压力测试的创建和调试,执行压力测试请不要使用GUI,试用以下命令来执行测试

```
 jmeter -n -t [jmx file] -l [results file] -e -o [Path to web report folder]
 
 	-t : 执行测试文件所在的位置及文件名
　　-n : 非GUI 模式执行JMeter
　　-r : 远程将所有agent启动用在分布式测试场景下,不是分布式测试只是单点就不需要-r
　　-l : 指定生成测试结果的保存文件, jtl文件格式
　　-e : 测试结束后,生成测试报告
　　-o : 指定测试报告的存放位置
　　-o : 指定的文件及文件夹,必须不存在 ,否则执行会失败
```

配置

1. 创建线程组及设置参数
   ![image-20210712141304898](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210712141304898.png)

   > 线程数即模拟的用户数
   > Ramp-Up Period即每个线程的执行时间间隔,设置为0即为并发

2. 在线程组下创建HTTP请求

   ![image-20210712141723965](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210712141723965.png)

3. HTTP请求添加运行结果分析监听器(图形结果、聚合报告、查看结果树)

   > Samples	 	 本次场景中一共完成了多少事物
   > Averag	 	    平均响应时间
   > Median			统计响应时间中值
   > Troughput       吞吐量,单位 事物/sec ,服务器每秒钟处理的请求数目

##### 5.4.3 jenkins

启动

> java -jar jenkins.war

关闭

> localhost:8080/exit

![image-20210712114117951](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210712114117951.png)

重启

> localhost:8080/restart

重新加载jenkins配置信息

> localhost:8080/reload

配置

1. 创建一个自由风格的jenkins job任务

2. 参数构建过程配置,设置脚本运行参数和脚本信息
   ![image-20210712135430213](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210712135430213.png)

3. 构建脚本

   ```
   echo "删除历史日志目录"
   rd /s/q D:\Jmeter\result
   echo "执行脚本输出结果"
   jmeter -n -t D:\Jmeter\script\%fileName%.jmx -l D:\Jmeter\%fileName%.jtl -e -o D:\Jmeter\result\
   
   ```

4. HTML报告(安装Publish HTML Report)
   ![image-20210712135826716](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210712135826716.png)

### 六. 系统编程

#### 6.1 谈谈多线程、多进程以及协程理解?

==操作系统能够调度的最小单元就是线程==

###### 6.1.1 多线程编程的两种方式

1.  threading 类实例化

    [多线程实现购票](file/threading.ipynb ':include : type=code')

2.  通过继承Thread来实现多线程

    [多线程实现购票](file/threading.ipynb ':include : type=code')

<<<<<<< HEAD
```python
import time, random, threading

tickets = 100

class myThread(threading.Thread):
    
```



=======
>>>>>>> 047ea4b4850b83389fc953cc877af170b01fc8a7
> 关于thread.setDaemon()

若在主线程中创建了子线程,当主线程结束时根据子线程daemon(设置thread.setDaemon(True))属性值的不同可能会发生下面的两种情况之一:

- 如果某个子线程的daemon属性为False,主线程结束时会检测该子线程是否结束,如果该子线程还在运行,则主线程会等待它完成后再退出;
- 如果某个子线程的daemon属性为True,主线程运行结束时不对这个子线程进行检查而直接退出,同时所有daemon值为True的子线程将随主线程一起结束,而不论是否运行完成

属性daemon的值默认为False,如果需要修改,必须在调用start()方法启动线程之前进行设置

###### 6.1.2 线程间的通信

线程间的通信方式

1. 共享变量
2. queue方式(消息队列)

###### 6.1.3 线程间的同步



#### 6.2 Python虚拟环境使用?

##### 6.2.1 什么是Python虚拟环境

一种采用协作式隔离的运行时环境,允许 Python 用户和应用程序在安装和升级 Python 分发包时不会干扰到同一系统上运行的其他 Python 应用程序的行为

##### 6.2.2 venv基本使用和原理

查看 venv 命令参数

> python -m venv -h

![image-20210401215357140](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401215357140.png)

创建虚拟环境

> python -m venv venvdemo

![image-20210401215831406](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401215831406.png)

虚拟环境原理

> 修改环境变量,把虚拟环境的Python路径加入环境变量最前,环境变量使用原则近者优先.

![image-20210401220456638](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401220456638.png)

##### 6.2.3 保存和复制虚拟环境

虚拟环境依赖导出

> pip freeze > requirement.txt

![image-20210401220936652](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210401220936652.png)

#### 6.3 Git

##### 6.3.1 常用操作

###### 1)git clone

从git服务器拉取代码

> https://github.com/chanwanxiang/isMe.git

###### 2)git config

配置开发者用户名和邮箱

> 每次代码提交时候都会生成一条记录,其中会包含当前配置用户名和邮箱

###### 3)git branch

创建、重命名、查看、删除项目分支，通过 Git做项目开发时,一般都是在开发分支中进行,开发完成后合并分支到main

> git branch feature/dev-20210401
> 创建一个名为 dev-20210401
>
> git branch -m feature/dev-20210401 feature/dev-20210402
> 分支重命名 dev-20210402
>
> gitbranch
> 不带参数查看当前项目分支列表
>
> gitbranch -d feature/dev-20210402
> 分支已经完成可以通过-d参数将分支删除

###### 4)git checkout

切换分支

> git checkout feature/dev-20210403

###### 5)git status

查看文件变动状态

###### 6)git add

添加文件到暂存区

###### 7)git commit

提交文件变动到版本库

###### 8)git push

将本地改动推送到服务器

###### 9)git pull

将服务器最新资源拉取到本地

###### 10)git log

查看版本提交记录

###### 11) git tag

为项目标记里程碑

###### 12).gitignore

设置哪些内容被git忽略不需要推送服务器

##### 6.3.2 进阶知识

### 七. 网络编程

OSI 7层参考模型![image-20210729141016919](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210729141016919.png)

1. 物理层:提供数据原始比特流的传输通路
2. 链路层:进行逻辑链接硬件地址寻址
3. 网络层:IP地址寻址数据结点之间传输
4. 传输层:定义传输数据协议端口
5. 会话层:会话管理建立终止
6. 表示层:提供数据格式转换服务数据的安全与压缩
7. 应用层:为操作系统或者服务提供访问网络的接口

TCP/IP 协议族

| 定义                      |              协议               |
| ------------------------- | :-----------------------------: |
| 应用层(Application)       | TCP(HTTP、HTTPS、SMTP、DNS) UDP |
| 传输层(Transport)         |             TCP UDP             |
| 网络层(Internet)          |           IP ARP RARP           |
| 数据链路层(NetworkAccess) |    LANs MANs WANs(物理地址)     |

ARP:地址解析协议,是根据IP地址获取物理地址的一个TCP/IP协议

RARP:逆地址解析协议,是将局域网中某个主机的物理地址转换为IP地址

#### 7.1 UDP总结

==UDP是一种面向无连接的、不可靠的、基于数据报的传输层通信协议==,所谓`无连接`是指在通信前不必与对方先建立连接,不管对方状态如何都直接将数据发送过去,UDP虽然不能保证数据传输的可靠性,但数据传输效率较高

#### 7.2 TCP总结

==TCP是一种面向连接的、可靠的、基于字节流的传输层通信协议==,为两台主机提供高可靠的数据通信服务.它可以将源主机的数据无差别的传输到目标主机.当有数据要发送时,对应用进程送来的数据进行分片,以适合在网络层中传输;当接收到网络层传来的分组时,要对收到的分组进行确认,还要对丢失的分组设置超时重发等.为此TCP需要增加额外的开销,以便在数据传输过程中进行必要的控制,确保数据的可靠传输.因此TCP传输效率比较低

TCP主要特点

1)是面向连接的协议
2)端到端的通信,每个TCP连接只有两个端点,而且只能一对一通信
3)高可靠性,通过TCP连接传送的数据,能保证数据无差错、不丢失、不重复地准确到达接收方,并且保证各个数据的到达顺序与其发出的顺序形同
4)全双工方式传输
5)数据以字节流方式传输
6)传输的数据无消息边界

#### 7.3 简述TCP和UDP区别以及优缺点?

UDP可靠性不如TCP,UDP不能保证有序传输

UDP的速度比TCP快,由于UDP不需要先与对方建立连接,也不需要传输确认,因此其数据传输速度比TCP快得多.适用于强调传输性能而不是传输完整性的应用(如网络音频等)

UDP有消息边界,发送方UDP对应用程序程序送来的报文,在添加首部后就向下直接交付给IP层,既不拆分,也不合并,而是保留报文的边界.使用UDP不需要考虑消息边界问题,这一特征也说明了UDP是一种面向报文的传输协议

UDP可以一对多的传输,由于传输数据不建立连接,也就不需要维护连接状态,因此一台服务器可以同时向多个客户端传输相同的消息

==速度快是UDP的首要优势,由于抛弃了信息可靠传输机制,将安全和排序等功能移交上层应用完成,极大降低了执行时间,使速度得到保证==

#### 7.4 简述浏览器通过wsgi请求动态资源过程?
1).发送 http 请求动态资源给 web 服务器
2).web 服务器收到请求后通过 WSGI 调用一个属性给应用程序框架
3).应用程序框架通过引用 WSGI 调用 web 服务器的方法,设置返回的状态和头信息
4).调用后返回,此时 web 服务器保存了刚刚设置的信息
5).应用程序框架查询数据库,生成动态页面的 body 的信息
6).把生成的 body 信息返回给 web 服务器
7).web 服务器把数据返回给浏览器 

#### 7.5 简述浏览器访问 www.baidu.com 的过程?

1)根据域名到 DNS 中找到 IP
2)根据 IP 建立 TCP 连接(三次握手)
3)连接建立成功发起 http 请求
4)服务器响应 http 请求
5)浏览器解析 HTML 代码并请求 HTML 中的静态资源（js,css）
6)关闭 TCP 连接（四次挥手）
7)浏览器渲染页面

#### 7.7 GET和POST请求区别有哪一些?

GET是从服务器获取数据,POST是向服务器传送数据

GET请求,请求的数据会附加在URL之后,以?分割URL和传输数据,多个参数用&连接
URL的编码格式采用的是ASCII编码,而不是unicode,即是说所有的非 ASCII 字符都要编码之后再传输

POST 请求,POST请求会把请求的数据放置在HTTP请求包的包体中,因此,GET请求的数据会暴露在地址栏中,而POST请求则不会

传输数据大小,在开发中,浏览器或服务器对 URL 有长度限制,因此,使用 GET 请求时,传输的数据会受到 URL 长度限制
对于 POST,由于不是 URL 传值,理论上传输数据大小不受限制,实际上各个服务器会规定对 POST 提交数据大小进行限定

安全性,POST 的安全性比 GET 高

效率,GET 比 POST 效率高

+ GET 请求过程
  1.浏览器请求 TCP 连接(第一次握手)
  2.服务器答应进行 TCP 连接(第二次握手)
  3.浏览器确认,并发送 GET 请求头和数据(第三次握手,这个报文比较小,所以 HTTP 会在此时进行第一次数据发送)
  4.服务器返回 200 OK 响应
+ POST 请求过程
  1.浏览器请求 TCP 连接(第一次握手)
  2.服务器答应进行 TCP 连接(第二次握手)
  3.浏览器确认,并发送 POST 请求头(第三次握手,这个报文比较小,所以 HTTP 会在此时进行第一次数据发送)
  4.服务器返回 100 continue 响应
  5.浏览器开始发送数据
  6.服务器返回 200 OK 响应

根据HTTP规范,GET用于信息获取,应该是==安全的和幂等的==

+ 所谓安全的意味着该操作用于获取信息而非修改信息,不会影响资源状态
+ 所谓幂等的意味着统一URL多个请求应该返回同样的结果

#### 7.8 cookie和session

##### 7.8.1 cookie和session的区别?

1.cookie 数据存放在客户的浏览器上,session 数据放在服务器上
2.cookie 不是很安全,别人可以分析存放在本地的 cookie 并进行 cookie 欺骗,考虑到安全应当使用 session
3.session 会在一定时间内保存在服务器上,当访问增多,会比较占用服务器的性能考虑到减轻服务器性能方面,应当使用 cookie 
4.单个 cookie 保存的数据不能超过 4K,很多浏览器都限制一个站点最多保存 20 个 cookie
5.建议将登陆信息等重要信息存放为 session,其他信息如果需要保留,可以放在 cookie 中

##### 7.8.2 cookie和session的联系?

session 对 cookie 的依赖

cookie 采用客户端存储,session 采用的服务端存储的机制,session 是针对每个用户(浏览器端)的,session 值保存在服务器上,通过 sessionId 来区分哪个用户的 session,因此 sessionId 需要被绑定在浏览器端,sessionId 通常会默认通过 cookie 在浏览 器端绑定,当浏览器端禁用 cookie 时,可通过 URL 重写或者表单隐藏字段的方式将 sessionId 传回给服务器，以便服务通过 sessionId 获取客户端对应的 session

具体一次请求流程

当程序需要为客户端创建一个 session 的时候,服务器首先检测这个客户端请求里面是否已经包含了 session 的表示(sessionId),如果已经包含,则说明已经为客户端创建过一个 session,服务端根据 sessionId 检索出来 sesion 并使用,如果客户端请求不包含 sessionId,则为客户端创建一个 session,并生成一个 sessionId 返回给客户端保存

#### 7.9 简单描述TCP传输过程?

![image-20210419161819090](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210419161819090.png)

TCP通信过程的三个步骤:建立TCP连接通道-传输数据-断开TCP连接通道

##### 7.9.1 **三次握手**

1. 第一次握手:客户端请求建立连接,向服务端发送一个同步报文(SYN=1),同时选择一个随机数seq=x作为初始序列号,并进入SYN_SENT状态,等待服务器确认
2. 第二次握手:服务端收到连接请求后,如果同意建立连接,则向客户端发送同步确认报文(SYN=1, ACK=1),确认号为ack=x+1,同时选择一个随机数seq=y作为初始序列号,此时服务器进入SYN_RECV状态
3. 第三次握手:客户端收到服务端确认后,向服务端发送一个确认报文(ACK=1),确认号为ack=y+1,序列号为seq=y+1,客户端和服务器进入ESTABLISHED状态,完成三次握手

理想状态下,TCP一旦建立连接,在通信双方的任何一方主动关闭连接之前,TCP连接都将被一直保持下去

##### 7.9.2 为什么要三次握手而不是两次或者四次?

+ 为什么不是两次

  1. 防止已经过期的连接请求又传送到服务器,因而产生错误和资源浪费

  2. 至少三次握手才能让双方均确认对方有发送和接收数据的能力
  3. 告知对方自己的初始序列号,并确认收到对方的初始序列号值

  TCP实现了可靠的数据传输,原因之一就是TCP报文段中维护了序号字段和确认序号字段,通过这两个字段双方都可以知道在自己发出的数据中,哪些是已经被对方接收的.这两个字段的值会在初始序号值的基础递增,如果是两次握手,只有发起方的初始序号可以得到确认,而另一方的初始序号得不到确认

+ 为什么不是四次

  + 因为三次握手已经确认双方接收发送能力正常,双方都知道彼此已经准备好,而且也可以完成对双方出书序号值的确认,也就无需再第四次握手了

##### 7.9.3 数据传输

TCP数据传输设计概念包含超时重传、快速重传、流量控制、拥塞控制等等

a.超时重传是用来保证TCP传输的可靠性,每次发送数据包时,发送的数据包都有seq号,接收端收到数据后,会回复ack进行确认,表示某一seq号数据已经接收,发送方在发送某个seq包后,等待一段时间,如果没有收到对应的ack回复,就会认为报文丢失,会重传这个数据包

b.快速重传,接收数据一方发现有数据包丢了,就会发送ack报文告诉发送端重传丢失的报文,如果发送端连续收到标号相同的ack包,则会触发客户端的快速重传,比较超时 重传和快速重传,可以发现超时重传是发送端在傻等超时,然后触发重传;而快速重传是接收端主动告诉发送端数据没有收到,然后触发发送端重传

c.流量控制,TCP滑动窗口流量控制,TCP头字段里有一个windows字段,这个字段是接收端告诉发送端自己还有多少缓存区可以接收数据,发送端可以根据接收端的处理能力来发送数据,不会到至接收端处理不及,滑动窗口是提高TCP传输效率的一种机制

d.拥塞控制,滑动窗口流量控制只关注发送端和接收端自身的状况,而没有考虑整个网络的通信情况.拥塞控制则是基于整个网络来考虑的,应对某一时刻网络延迟突然增加,TCP应对重传数据,导致网络负担更重,引起更大的延迟以及更多的丢包.为此引入了拥塞控制策略,具体算法包括慢启动、拥塞避免、拥塞发生、快速恢复

##### 7.9.4 **四次挥手**

1.主动关闭方发送一个fin报文,用来关闭主动方到被动关闭方的数据传输,即主动关闭方告知被动关闭方,我不再给你发送数据
2.被动关闭方接收到fin报文后,发送一个ack报文给对方,确认序号为收到的序号+1
3.被动关闭方发送一个fin报文,用来关闭向对方的数据传送
4.主动关闭方接收端到fin报文,发送一个ack报文给被动关闭方,至此完成四次挥手

1. 第一次挥手:客户端向服务端发出连接释放报文(FIN=1, ACK=1),主动关闭连接,同时等待服务端确认
   + 序列号seq=x+2,及客户端上次发送报文的最后一个字节的序号+1
   + 确认号ack=y+1,及服务端上次发送报文的最后一个字节的序号+1
2. 第二次挥手:服务端收到连接释放报文后,立即发出确认报文(ACK=1),确认号为ack=x+3
   + 此时TCP连接处于半关闭状态,即客户端到服务端的连接已经关闭了,但是服务端到客户端的连接还未释放,这表示客户端已经没有数据发送,但是服务端可能还要给客户端发送数据
3. 第三次挥手:服务端向客户端发送连接释放报文(FIN=1, ACK=1),主动关闭连接,同时等待A的确认
4. 第四次挥手:客户端收到服务端的连接释放报文后,立即发出确认报文(ACK=1)

#### 7.10 说说HTTP和HTTPS区别?

HTTP超文本传输协议,是一个基于TCP的可靠性传输协议,是客户端和服务端请求和应答的标准,用于从www服务器传输超文本到本地浏览器的传输协议

HTTPS以安全为目标的HTTP通道,在HTTP层加入了SSL层.SSL依赖证书来验证服务器的身份,并为浏览器和服务器之间的通信加密,主要作用有两个,一是建立一个信息安全通道,保证数据传输安全,而是确认网站的真实性

主要区别

HTTP是超文本传输协议,信息是明文传输,https则是具有安全性的ssl加密传输协议
HTTP和HTTPS使用的是完全不相同的两种连接方式,HTTP是80端口,HTTPS是443端口
HTTPS更加安全,SEO更优,但HTTPS协议会使加载时间变得较长,增加数据开销损耗

#### 7.11 HTTP协议状态码作用及常见状态码?

通过状态码告诉客户端服务器的执行状态,以判断下一步执行操作

常见状态机器码
100-199	表示服务器成功接收部分请求,要求客户端继续提交其余请求才能完成整个处理流程
200-299	表示服务器成功接收请求并已完成处理过程,常用 200(OK 请求完成)
300-399	表示为完成请求,客户需要进一步细化请求,常用 302(搜索请求页面已经临时转移到新的URL)
400-499	表示客户端请求有错误,常用 404(服务器无法找到请求页面)、403(服务器拒绝访问,权限不够)
500-599	表示服务端出现错误,常用 500(请求未完成,服务器遇到不可预知情况)

#### 7.12 webSocket和HTTP的区别

websocket和http都是基于tcp的可靠性传输协议

http是半双工协议,也就是说在同一时间点只能处理一个方向的数据传输,属于单向传输,在客户端向服务器发起连接之前,服务器并不知道有这个连接,发起一个请求,得到一个响应

websocket协议是全双工的,服务器可以随时主动给客户端下发数据,可以双向发送或者接收信息,属于双向传输.websocket可以通过客户端和服务器握手建立连接,并且连接一直保持在打开状态,建立双向通信,直到客户端和服务端发送消息将其关闭

websocket优势

1)较少的资源浪费
在连接建立后,服务器和客户端之间交互时,传输的数据包头部相对较小.相对于http请求每次都要携带完整头部,资源浪费显著减少

2)更强的实时性
由于websocket协议是全双工的,所以服务器可以随时主动给客户端传输数据,相对于http请求需要等待客户端发起请求服务端才能响应,延迟明显更少

3)保持长连接
与http不同的是,websocket需要先创建连接,这就使得其成为了一种有状态的协议,而http请求可能徐亚在每个请求都携带状态信息(如身份认证等)

4)更好的二进制帧
websocket定制了二进制帧,相对http,可以更加轻松的处理二进制内容

5)更好的压缩效果
相对于http压缩,websocket在是适当扩展支持下,可以沿用之前内容的上下文,在传递类似数据时,显著提升压缩率

如果开发一个客户端和服务端持续交互的模块,websocket将是最佳选择,例如社交聊天、弹幕、在线教育、位置信息更新应用

#### 7.13 TCP网络应用开发流程

##### 7.13.1 TCP客户端程序开发

1. 创建客户端套接字对象		socket()
2. 和服务端建立连接               connect()
3. 发送数据                              send()
4. 接受数据                              recv()
5. 关闭客户端套接字                close()

##### 7.13.2 TCP服务端程序开发

1. 创建服务端套接字对象         socket()
2. 绑定端口号                           bind()
3. 设置监听                               listen()
4. 等待客户端的连接请求         accept()
5. 接收数据                               recv()
6. 发送数据                               send()
7. 关闭套接字                            close()

#### 7.14 DNS查询全过程

### 八. web开发

#### 8.1 django

##### 8.1.1 django创建项目的命令?

> django-admin startproject 项目名称
> python manage.py startapp 应用名称

##### 8.1.2 django创建项目后项目文件夹下的组成部分?

![image-20210416144220927](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210416144220927.png)

**项目文件夹的组成部分**

manage.py	  项目运行入口,指定配置文件路径

与项目同名的文件夹
	\__init.py__	一个空文件,作用是这个目录可以被当做包使用
	setting.py	项目整体配置文件
	urls.py 		项目的 URL 配置文件
	wsgi.py		项目与 WSGI 兼容的 web 服务器入口

##### 8.1.3 django框架的MVC流程?

用户 -> 发出访问请求 -> (Nginx|Apatch)服务器 -> Django(Router-View(Controller)-[Model]-Template(渲染所有代码)) --> 浏览器展示的内容 -> 用户

##### 8.1.4 django的models

###### 1)模型类的定义

**定义**

模型类被定义应用/models.py文件中
模型类必须继承自Model类,位于django.db.models中

**数据库表名**

模型类如果未指明表名,django默认以小写app应用名_小写模型类名作为数据库名
可以通过db_table指明数据库表名

**关于主键**

django会为表创建自动增长的主键列,每个模型只能有一个主键列,如果使用选项设置某属性为主键后django不会再创建自动增长主键列
默认创建的主键列属性为id,可以使用pk(primary key)代替

**属性命名限制**

不能是python的保留关键字
不允许使用连续的下划线,和django的查询方式有冲突
定义属性时徐亚指定字段类型,通过字段类型的参数指定选项,语法
属性=models.字段类型(选项)

**字段类型**

| 类型             |                             说明                             |
| :--------------- | :----------------------------------------------------------: |
| AutoField        | 自动增长的IntegerField,通常不用指定,不指定django会自动创建属性名为id的自动增长属性 |
| BooleanFiled     |                   布尔字段,值为True或False                   |
| NullBooleanFiled |                   支持Null,值为True或False                   |
| CharField        |            字符串,参数max_length表示最大字符个数             |
| TextField        |              大文本字段,一般超过4000个字符使用               |
| IntegerField     |                             整数                             |
| DateField        | 日期,参数auto_now表示每次保存对象时,自动设置该字段为当前时间 |
| TimeField        |                             时间                             |
| DateTimeField    |                   日期时间,参数同DateField                   |
| FileField        |                         上传文件字段                         |
| ImageField       |    继承自FileField,对上传的内容进行校验,确保是有效的图片     |

**字段选项**

| 选项        |                             说明                             |
| ----------- | :----------------------------------------------------------: |
| null        |              如True,表示允许为空,默认值为False               |
| blank       |           如True,表示字段允许为空白,默认值为False            |
| db_column   |            字段的名称,如果未指定,则使用属性的名称            |
| db_index    |        如True,则表中会为此字段创建索引,默认值为False         |
| default     |                             默认                             |
| primary_key | 如True,则该字段会成为模型的主键字段,默认值为False,一般作为AutoField的选项使用 |
| unique      |       如True,这个字段在表中必须有唯一值,默认值为False        |

> null是数据库范畴的概念,blank是表单验证范畴的

**外键**

设置外键时,需要通过on_delete选项指明主表删除数据时,对于外键引用表数据如何处理,在django.db.models中包含了可选常量

CASECADE           级联删除主表数据时连同一起删除外键表中数据
PROTECT			 保护通过抛出ProtectedError异常,来阻止删除主表中被外键应用的数据
SET_NULL			设置为NULL,仅在该字段null=True允许为null时可用

**迁移**

>生成迁移文件
>python manage.py makemigrations
>
>迁移文件
>python manage.py migrate

###### 2)数据库增删改操作

**增加数据**

```python
# 方法一 save
# 通过创建模型类对象,执行对象的save()方法保存到数据库中
from books.models import BookInfo,PeopleInfo

book = BookInfo(
    name='神雕侠侣',
    pubDate='1980-1-1',
    readCount=33,
    comentCount=45
)
book.save()

# 方法二 creat
# 通过模型类.objects.creat()保存
BookInfo.objects.creat(
    name='神雕侠侣',
    pubDate='1980-1-1',
    readCount=33,
    comentCount=45
)
```

**修改数据**

```python
# 方法一 save
# 通过修改模型类对象属性,然后执行save()方法
book = BookInfo.objects.get(name='神雕侠侣')
book.name = '神雕侠侣(精装版)'
book.save()

# 方法二 update
# 通过模型类.objects.filter().update(),返回受影响的行数
BookInfo.objects.filter(name='神雕侠侣').update(name='神雕侠侣(精装版)')

```

**删除数据**

```python
# 方法一 模型类对象delete
book = BookInfo.objects.get(name='神雕侠侣')
book.delete()

# 方法二 模型类.objects.filter().delete()
BookInfo.object.filter(name='神雕侠侣').delete()

```

###### 3)查询操作

**基本查询**

```python
# get          查询单一结果,如果不存在会抛出模型类.DoesNotExist异常
# all          查询多个结果
# count        查询结果数量

# 查询id为1的书籍
BookInfo.objects.get(id=1)

# 查询所有书籍信息
BookInfo.object.all()

# 查询书籍数量
BookInfo.objects.count()

```

**过滤查询**

```python
# 实现sql中的where功能,包括
# get     过滤单一结果
# filter  过滤多个结果
# exclude 排除掉符合条件剩下的结果

# 对于过滤条件使用,上述三个方法相同,以filter讲解
# 属性名称__比较运算符=值

# 相等查询

# exact       表示判等
# 查询编号为1的书籍
BookInfo.objects.get(id__exact=1)

# 模糊查询

# contains     是否包含
# 查询书名包含`湖`的书籍
BookInfo.objects.filter(name__contains='湖')

# startswith endswith     以指定值开头或结尾
# 查询书名以`部`结尾的书籍
BookInfo.objects.filter(name__endswith='部')

# 空查询

# isnull       是否为空
# 查询书名为空的书籍
BookInfo.objects.filter(name__isnull=True)

# 范围查询

# in           是否包含在范围
# 查询编号为1或3或5的书籍
BookInfo.objects.filter(id__in=[1,3,5])
# 比较查询

# gt      大于(greater then)
# gte     大于等于(greater then equal)
# lt      小于(less then)
# lte     小于等于(less then equal)
# 查询编号大于3的书籍
BookInfo.objects.filter(id__gt=3)
# 不等于的运算使用exclude()过滤器
# 查询编号不等于3的书籍
BookInfo.objects.exclude(id__exact=3)

# 日期查询
# year,month,day,week_day,hour,minute,second      对日期时间类型的属性进行运算
# 查询1980年发表的书籍
BookInfo.objects.filter(pubDate__year=1980)

# 查询1990年1月1日后发表的书籍
BookInfo.objects.filter(pubDate__gt='1990-1-1')

# F和Q对象
# F对象被定义在django.db.models,用于两个属性之间比较
# 语法
# Models.objects.filter(属性名称__比较运算符=F(属性名))

# 查询阅读量大于等于评论量的书籍
BookInfo.objects.filter(readCount__gt=F('commentCount'))

# 对于多个过滤器逐个调用表示逻辑与关系,同sql语句中的where部分的and关键字
# 查询阅读量大于20,并且编号小于3的图书
BookInfo.objects.filter(readCount__gt=20,id__lt=3)
# 或
BookInfo.objects.filter(readCount__gt=20).filter(id__lt=3)

# Q对象被定义在django.db.models,实现逻辑或or的查询,需要使用Q()对象结合|运算符
#语法
# Models.objects.filter(Q(属性名称__比较运算符=值)|Q(属性名称__比较运算符=值))
# 查询阅读量大于20或者编号小于3的书籍
BookInfo.objects.filter(Q(readCount__gt=20)|Q(id__lt=3))

# Q对象除了与或关系还可以加~表示非的关系

# 查询编号不等于3的书籍
BookInfo.objects.filter(~Q(id__exact=3))

# 聚合函数
# 使用aggregate()过滤器调用聚合函数
# 聚合函数包括Avg,Count,Max,Min,Sum,被定义在django.db.models
# 查询书籍总阅读量
BookInfo.objects.aggregrate(Sum('readCount'))

# 返回一个字典类型
# {'属性名__聚合函数小写':值}

# 排序函数
# 使用order_by对结果进行排序
# 对书籍的阅读量进行默认升序
BookInfo.objects.all().order_by('readCount')

# 降序
BookInfo.objects.all().order_by('-readCount')

```

**关联查询**

```python
# 由一到多的访问语法
# 一对应的模型类对象.多对应的模型类名小写_set
# 查询书籍id=1的所有人物信息
book = BookInfo.objects.get(id=1)
book.personinfo_set.all()

# 由多到一的访问语法
# 多对应的模型类对象.多对应的模型类中的关系类属性名

# 查询人物id=1的书籍信息
person = PersonInfo.objects.get(id=1)
person.book()

# 关联过滤查询
# 由多模型类条件查询一模型类数据
# 语法
# 关联模型类名小写__属性名__条件运算符=值

# 查询人物有`郭靖`的书籍
BookInfo.objects.filter(personinfo__name__exact='郭靖')

# 查询人物描述包含`八`的书籍
BookInfo.objects.filter(personinfo__descriptions__contains='八')

# 由一模型类条件查询多模型类数据
# 语法
# 一模型类关联属性名__一模型类属性名__条件运算符=值

# 查询书名为`天龙八部`所有人物
PersonInfo.objects.filter(book__name='天龙八部')

# 查询书籍阅读量大于30的所有书籍人物
PersonInfo.objects.filter(book__readCount__gt=30)

```

###### 4)查询集QuerySet()

```python
# django的ORM中存在查询集的概念
# 查询集亦称为查询结果集,QuerySet表示从数据库中获取的对象集合
# 当调用如下过滤器方法是,django会返回查询集(而不是简单的列表)
# all()           返回所有数据
# filter()        返回满足条件数据
# exclude()       返回满足条件之外数据
# order_by()      返回结果进行排序

# 对查询集可以再次调用过滤器进行过滤
books = BookInfo.objects.filter(readCount__gt=30).order_by('pubDate')

# 意味着查询集可以含有零个,一个或者多个过滤器,过滤器基于所给的参数限制查询结果
# 判断某一个查询集中是否有数据
# exists()        判断查询集中是否有数据,如果有则返回True,没有则返回False

# 两大特性

# 惰性执行
# 创建查询集不会访问数据库,直到调用数据才会进行访问,调用数据的情况包括迭代,序列化,与if合用
# 如当执行如下语句,并未进行数据库查询,只是创建了一个结果集books
books = BookInfo.objects.all()

for book in books:
    print(book.name)
    
# 缓存(性能优化)
# 同一个结果集,第一次使用时会发生数据库的查询,然后django会把结果缓存下来,再次使用这个结果集时会使用缓存的数据,减少了查询数据库的次数
# 情况一如下是两个查询集,无法重用缓存数据,每次查询都会与数据库进行一次交互,增加了数据库负载
[book.name for book in BookInfo.objects.all()]
[book.name for book in BookInfo.objects.all()]
# 情况二经过存储后,可以重用查询集,第二次使用缓存中的数据
books = BookInfo.objects.all()
[book.name for book in books]

# 限制查询集
# 可以对查询集进行取下标或切片操作,等同于sql中的limit和offset子句
# 不支持负数索引
# 对查询集进行切片后返回一个新的查询集,不会立即执行查询
# 如果获取一个对象,直接使用[0],等同于[0,1].get()
# 如果没有数据.[0]引发IndexError异常.[0:1].get如果没有数据引发DoesNotExist异常

# 获取第一,二项数据
BookInfo.objects.all()[0,2]

# 分页

# 导入分页模块
from django.core.paginator import Paginator

books = BookInfo.objects.all()

# 创建分页实例
p = Paginator(books,2)

# 获取指定页的数据
page = p.page(1)

# 获取分页数据
totalPage = paginator.num_pages

```

##### 8.1.5 django的views

###### 1)URLconf

**定义**

用户通过在浏览器的地址栏中输入网址请求网站
对于django开发的网站,由哪一个视图进行处理请求,是由url匹配完成

**配置**

项目中的setting.py

> 指定url配置
> ROOT_URLCONF = '项目.urls' 

项目中的urls.py

> 匹配成功后,包含到应用的urls.py
> url(正则,include('应用.urls'))

应用中的urls.py

> 匹配成功后,调用views.py对应函数
> url(正则,views.函数名)

提示

> 正则部分推荐使用r,表示字符串不转义,这样在正则表达式中使用\只写一个就可以
> 不能再开始加反斜杠,推荐在结束加反斜杠
> 正确  path/  或者 path
> 错误  /path/ 或者 path/
>
> ==请求的url被看做一个普通的python字符串,进行匹配时不包括域名,get或post参数==
>
> 如请求地址如下
> https:127.0.0.1:8000/index/?search=唐诗
>
> 去掉域名和参数部分之后,剩下如下部分进行正则匹配
> index/

###### 2)路由命名和反解析

**路由命名**

定义路由时,可以为路由命名,方便查找特定视图具体路径信息

> 使用include函数定义路由时,可以使用namespace参数定义路由的命名空间
> url(r'^',include('books.urls',namesapce='books'))
> 命名空间表示,凡是book.urls中定义的路由,均属于namespace指明的book名下
> 命名空间避免了不同应用中的路由使用了相同的名字发生冲突,使用命名空间区别开
>
> 在定义普通路由时,可以使用name参数指明路由名字

**reverse反解析**

使用reverse函数,可以根据路由名称,返回具体路径

```python
from django.urls import reverse

def index(request):
    url = reverse('books:index')
    
    print(url)

# 对于没有指明namespace的,reverse(路由name)
# 对于指明namespace的,reverse(命名空间namespace:路由name)

```

###### 3)HttpRequest对象

**HTTP协议向服务器传参途经**

+ 提取URL特定内容,可以在服务器端的路由中用正则表达式截取
+ 查询字符串(query string),形如key1=value1&key2=value2
+ 请求体(body)中发送数据,如表单数据、json、xml
+ 在http报文的头(header)中

**URL路径参数**

想从URL中获取值,需要在正则表达式中使用分组

+ 位置参数		参数位置不可错
+ 关键字参数	参数位置可以变,跟关键字保持一致即可

```python
from django.conf.urls import url
from books.views import index

urlpatterns = [
    # name给url起名,可以通过name找到这个路由
    url(r'^index/$',index,name='index'),
    
    # 分组获取正则数据,位置参数
    # http:127.0.0.1/categoryid/bookid/
    # url(r'^(\d+)/(\d+)/$',detail),
    
    # 分组获取正则数据,关键字参数
    # http:127.0.0.1/categoryid=?
    url(r'^(?P<categoryid>\d+)/(?P<bookid>\d+)/$',detail),

    # 参数一是正则,参数二是视图函数名称
    # BookView.as_view()返回的是一个视图函数名
    url(r'^login/$',BookView.as_view()),
]

```

**django的QueryDict()对象**

HttpRequest对象的属性GET,POST都是QueryDict类型对象
与python字典不同,QueryDict类型对象用来处理同一个键带有多个值的情况

> 方法get()      根据键获取值
>
> 如果一个键同时拥有多个值将获取最后一个值
> 如果键不存在则返回None,可以设置默认值进行后续处理
> get('键',默认值)
>
> 方法getlist()    根据键获取值,值以列表返回,可以获取指定键的所有值
>
> 如果键不存在则返回空列表[],可以设置默认值进行后续处理
> getlist('键',默认值)

**查询字符串query string**

获取请求路径中的查询字符串参数(形如?key1=value1&key2=value2),可以通过request.GET属性获取,返回QueryDict对象
==查询字符串不区分请求方式,即使使客户端进行POST方式请求,依然可以通过request.GET获取请求中的查询字符串数据==

**请求体**

请求数据格式不固定,可以是表单类型字符串,可以是JSON字符串,也可以是XML字符串,应区别对待
可以发送请求体数据的请求方式有POST,PUT,PATCH,DELETE

**表单类型Form Data**

获取前端发送的表单类型的请求体数据,可以通过request.POST属性获取,返回QueryDict对象

**非表单类型Non-Form Data**

非表单类型的请求体数据,django无法自动解析,可以通过request.body属性获取最原始的请求体数据,自己按照请求体格式(JSON,XML)进行解析
request.body返回bytes类型

**请求头**

可以通过request.META属性获取请求头headers中的数据,request.META为字典类型

###### 4)HttpResopnse对象

**定义**

视图在接收请求并处理后,必须返回HttpResponse对象或子对象
HttpRequest对象由django创建,HttpResponse对象由开发人员创建

**HttpResponse**

可以使用django.http.HttpResponse来构造响应对象

> HttpResponse(content=响应体,content_type=响应类型,status=状态码)

**HttpResponse子类**

django提供了一系列HttpResponse的子类,可以快速设置状态码

| 子类                          | 状态码 |
| ----------------------------- | ------ |
| HttpResponseRedirect          | 301    |
| HttpResponsePermanentRedirect | 302    |
| HttpResponseNotModified       | 304    |
| HttpResponseBadRequest        | 400    |
| HttpResponseNotFound          | 404    |
| HttpResponseForbidden         | 403    |
| HttpResponseNotAllowed        | 405    |
| HttpResponseGone              | 410    |
| HttpResponseServerError       | 500    |

**JsonResponse**

若要返回json数据,可以使用JsonRequest来构造响应对象

> 帮助我们将数据转换为json字符串
> 设置响应头content-type为application/json

###### 5)类视图

**定义**

在django中可以使用类来定义一个视图,称为类视图
使用类视图可以将视图对应的不同请求方式以类中的不同方法来区别定义

```python
from django.views.generic import View

# 类视图处理注册逻辑
class RegisterView(View):
    
    def get(self,request):
        # 处理GET请求,返回注册页面
        return reder(request,'register.html')

    def post(self,request):
        # 处理POST请求,实现注册逻辑
        return HttpResponse('实现注册逻辑')
    
```

**类视图的好处**

> 代码可读性好
> 类视图相对于函数视图有更高的复用性,如果其他地方需要用到某个类视图的某个特定逻辑,直接继承该类视图即可

**配置**

定义类视图需要继承自django提供的父类View,可使用

>from django.views.generic import View

配置路由时,使用类视图的as_view()方法来添加

**原理**

点击as_view函数查看django源码

######  6)中间件

**定义**

django中的中间件是一个轻量级底层的插件系统,可以介入django的请求和响应处理过程,修改django的输入和输出
中间件的设计为开发者提供了一种无侵入式的开发方式

##### 8.1.6 django的templates

###### 1)自带模板

**配置**

> 在工程创建目录templates
>
> 在settings.py配置文件中修改TEMPLATES配置项的DIRS值

###### 2)Jinja2模板

**安装**

> pip install jinja2

**配置**

> 项目文件中创建jinja2_env.py文件
> 在setting中TEMPLATES配置janja2环境

#### 8.2 flask

#### 8.3 通识

##### 8.3.1 对uWSGI和nginx的理解?

**uWSGI** 

是一个 Web 服务器,它实现了 WSGI 协议、uwsgi、http 等协议
nginx 中 HttpUwsgiModule 的作用是与 uWSGI 服务器进行交换
WSGI 是一种 web 服务器网关接口,它是一 个 web 服务器(如 nginx,uWSGI 等服务器)与 web 应用(如用 Flask 框架写的程序)通信的一种规范

**要注意 WSGI / uwsgi / uWSGI 这三个概念的区分**

WSGI 是一种通信协议

uwsgi 是一种线路协议而不是通信协议,在此常用于在 uWSGI 服务器与其他网络服务器的数据通信

uWSGI 是实现了 uwsgi 和 WSGI 两种协议的 web 服务器

**nginx**

是一个开源的高性能的 HTTP 服务器和反向代理

1)作为 web 服务器,它处理静态文件和索引文件效果非常高
2)它的设计非常注重效率,最大支持 5 万个并发连接,但只占用很少的内存空间
3)稳定性高，配置简洁
4)强大的反向代理和负载均衡功能,平衡集群中各个服务器的负载压力应用

##### 8.3.2 nginx和uWISG服务器之间如何配合工作?

浏览器发起 http 请求到 nginx 服务器,nginx 根据接收到请求包,进行 url 分析,判断访问的资源类型,如果是静态资源,直接读取静态资源返回给浏览器,如果请求的是动态资源就转交给 uWSGI 服务器,uWSGI 服务器根据自身的 uwsgi 和 WSGI 协议,找到对应的 django 框架,django 框架下的应用进行逻辑处理后,将返回值发送到 uWSGI 服务器,然后 uWSGI 服务器再返回给 nginx,最 nginx 将返回值返回给浏览器进行渲染显示给用户

##### 8.3.3 什么是CSRF攻击原理,如何解决?

CSRF(Cross Site Request Forgery),跨站请求伪造

图中 Browse 是浏览器,WebServerA 是受信任网站/被攻击网站 A,WebServerB 是恶意网站/点 击网站 B 

1)一开始用户打开浏览器,访问受信任网站 A,输入用户名和密码登陆请求登陆网站 A
2)网站 A 验证用户信息,用户信息通过验证后,网站 A 产生 Cookie 信息并返回给浏览器。 
3)用户登陆网站 A 成功后,可以正常请求网站 A
4)用户未退出网站 A 之前,在同一浏览器中,打开一个 TAB 访问网站 B。 
5)网站 B 看到有人访问后,他会返回一些攻击性代码。 
6)浏览器在接受到这些攻击性代码后,促使用户不知情的情况下浏览器携带 Cookie(包括 sessionId)信息,请求网站 A,这种请求有可能更新密码,带有恶意操作

解决方法

1)csrf_token
2)短信验证码

##### 8.3.4 代码优化从哪些方向考虑?

### **九. Ubantu**

#### 9.1 入门介绍

##### 9.1.1 linux是什么

linux是一款免费、开源、安全、高效、稳定的操作系统,处理高并发非常强悍,很多企业级的项目都部署到linux服务器中运行

##### 9.1.2 linux目录结构

linux的文件系统是采用级层式的树状结构,在此结构中最上层的是根目录'/',然后在此目录下再创建其他目录

> linux中一切皆文件

![image-20210423115234306](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210423115234306.png)

![image-20210412165942948](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210412165942948.png)

#### 9.2 用户管理

##### 9.2.1 基本介绍

linux系统是一个多用户多任务的操作系统,任何一个要使用系统资源的用户,都必须首先向系统管理员申请一个账号,然后以这个账号的身份进入系统
linux用户需要至少都属于一个组

##### 9.2.2 添加用户

+ 语法

  > useradd [add] 用户名

##### 9.2.3 给用户指定或修改密码

+ 语法

  > passwd 用户名

##### 9.2.4 删除用户

+ 语法

  > userdel 用户名

##### 9.2.5 查询用户信息

+ 语法

  > id 用户名

##### 9.2.6 切换用户

+ 语法

  > su - 切换到用户名

#### 9.3 实用指令

##### 9.3.1 指令知识

当我们对某个指令不熟悉时,可以使用linux提供的帮助命令来了解这个指令使用方法

+ man

  > man [命令或者配置文件] (功能描述:获取帮助信息)

+ help

  > help 命令 (功能描述:获取shell内置命令的帮助信息)

#### 9.4 文件目录

##### 9.4.1 pwd指令

+ 显示当前工作目录绝对路径

  > pwd

##### 9.4.2 ls指令

+ 查看当前目录下的所有内容信息

  > ls [选项] [文件或者目录]
  >
  > ls -a 显示当前目录包括隐藏所有文件目录
  >
  > ls -l 以列表形式显示信息

##### 9.4.3 cd指令

+ 切换到指定目录

  > cd [选项]
  >
  > 绝对路径从根目录开始定位
  >
  > 相对路径从当前的工作目录开始定位
  >
  > cd~ 或者 cd 回到自己/home目录
  >
  > cd..返回到当前目录上一级目录

##### 9.4.4 mkdir指令

+ 创建目录

  > mkdir [选项] 要创建的目录
  >
  > mkdir -p a/b/c 创建多级目录


##### 9.4.5 rmdir指令

+ 删除空目录

  > rmdir [选项] 要删除的空目录
  >
  > rmdir删除的是空目录如果目录下有内容无法删除
  >
  > rmdir -rf 要删除的目录

##### 9.4.6 touch指令

+ 创建空文件

  > touch 文件名称

##### 9.4.7 cp指令

+ 拷贝文件到指定目录

  > cp [选项] source dest
  >
  > cp -r source dest 递归复制整个文件夹

##### 9.4.8 rm指令

+ 移除删除文件或者目录

  > rm [选项] 要删除的文件或者文件夹
  >
  > rm -r 递归删除整个文件夹
  >
  > rm -f 强制删除不提示

##### 9.4.9 mv指令

+ 移动文件与目录或重命名

  > mv oldFileName newFileName (功能描述:重命名)
  >
  > mv /temp/movefile /targetFolder (功能描述:移动文件)

##### 9.4.10 cat指令

+ 查看文件内容,是以只读方式打开

  > cat [选项] 要查看的文件
  >
  > cat -n fileName (功能描述:显示行号查看FileName文件)
  >
  > cat只能浏览文件不能修改文件为了方便一般使用管道命令
  >
  > cat FileName | more [分页浏览]

##### 9.4.11 more指令

+ 基于vi编辑器的文本过滤器,它以全屏幕的方式按页显示文本文件内容

  > more 要查看的文件

##### 9.4.12 less指令

+ 用来分屏查看文件内容,功能与more类似,但是比more更加强大,支持各种显示终端,在显示文件内容时,并不是一次将整个文件加载之后显示,而是根据显示需要加载内容,对于显示大型文件具有较高效率

  > less 要查看的文件

##### 9.4.13 > 指令和 >> 指令

+ 输出的重定向

  > 输出的重定向 > 会将原来文件的内容覆盖 >> 不会覆盖原来的文件内容而是追加到文件的尾部
  >
  > ls -l > fileName.txt (功能描述:列表的内容写入文件fileName中)
  > 把一个文件复制到另外一个文件之中可以使用 >>

##### 9.4.14 echo指令

+ 输出内容到控制台

  > echo [选项] [输出内容]
  >
  > each $path (功能描述:输出环境变量)

##### 9.4.15 head指令

+ 显示文件的开头部分内容,默认情况下显示文件的前10行内容

  > head 文件 (功能描述:查看文件头10行内容)
  >
  > head -n 5 文件 (功能描述:查看文件头5行内容)

##### 9.4.16 tail指令

+ 输出文件尾部内容,默认情况下显示文件的后10行内容

  > tail 文件 (功能描述:查看文件后10行的内容)
  >
  > tail -n 5 文件 (功能描述:查看文件后5行的内容)
  >
  > tail -f 文件 (功能描述:实时跟踪改文档的所有更新内容)

##### 9.4.17 ln指令

+ 软连接也叫符号链接,类似windows里的快捷方式,主要存放了链接其他文件的路径

  >ln -s [原文件或目录] [软链接名] (功能描述:给原文件创建一个软链接)
  >
  >ln -s /root linkToRoot (功能描述:在当前目录下创建一个软链接linkToRoot链接到/root目录)

##### 9.4.18 history指令

+ 查看已经执行过的历史指令,也可以执行历史指令

  > history (功能描述:查看已经执行过历史命令)
  >
  > history 10 (功能描述:显示最近执行过的10个指令

##### 9.4.19 vim指令

![image-20210423115515090](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210423115515090.png)

+ Normal模式(上图命令模式)

| 指令                 |                             说明                             |
| -------------------- | :----------------------------------------------------------: |
| a \| A               |                append \| append after a line                 |
| i  \| I              |              insert     \| insert before a line              |
| o \| O               |            open a line below \| open a line above            |
| v  \|  V  \| ctrl +v |                  visual模式用例块状选择文本                  |
| gi                   |           跳转文件最后一次编辑的地方并进入编辑模式           |
| h \| j \| k \| l     |                  左 \| 下 \| 上 \| 右 移动                   |
| w \| W               |            移动下个word\| WORD开头(之间包含空格)             |
| e  \| E              |             移动下个word\|WORD结尾(之间包含空格)             |
| b  \| B              |             回到上个word\|WORD开头(之间包含空格)             |
| f{char} \| F{char}   | 同行搜索一个字符并且移动到该字符,F反向搜索前面字符(;下一个\|,上一个) |
| 0 \| $               |                     快速移动一行行首行尾                     |
| gg \| G              |         移动文件开开头结尾,可以使用ctrl + o 快速返回         |
| H \| M \| L          |                  跳转屏幕开头,中间结尾部分                   |
| ctru + u \| ctrl + f |                  上下翻页,zz把屏幕置位中间                   |

+ 编辑模式(上图输入模式)

| 指令                 |          说明           |
| -------------------- | :---------------------: |
| ctrl + h             |     删除上一个字符      |
| ctrl + w             |     删除上一个单词      |
| ctrl + u             |      删除当前的行       |
| ctrl + c \| ctrl + [ | 代替esc切换编辑普通模式 |
|                      |                         |



+ 底线命令模式

#### 9.5 时间日期

##### 9.5.1 date指令-显示当前日期

+ 显示当前时间

  > date
  >
  > date %Y (功能描述:显示当前年份)
  >
  > date %m (功能描述:显示当前月份)
  >
  > date %d (功能描述:显示当前是哪一天)

##### 9.5.2 date指令-设置日期

+ 设置系统当前时间

  > date -s 字符串时间

##### 9.5.3 cal指令

+ 查看日历

  > cal[选项] (功能描述:不加选项显示本月日历)

#### 9.6 搜索查找

##### 9.6.1 find指令

+ 将从目录详细递归地遍历其各个子目录将满足条件的文件或者目录显示在终端

  > find [搜索范围] [选项]
  >
  > find /home -name a.txt (功能描述:搜索在/home目录下按照名字搜索a.txt文件)
  >
  > find /home -size +20M (功能描述:搜索在/home目录下按照文件大小搜索20M以上文件)

##### 9.6.2 locate指令

+ 快速定位文件路径,利用事先简历的系统中的所有文件名称及路径的locate数据库事先快速定位给定的文件,locate指令无需遍历整个文件系统,查询速度较快

  > locate 搜索文件
  >
  > 由于locate指令基于数据库进行查询所以第一次运行前必须使用updatedb指令创建locate数据库

##### 9.6.3 grep指令和管道符号 | 

+ grep 过滤查找

+ 管道符 | 表示将前一个命令的处理结果输出传递给后面的命令处理

  > grep [选项] 查找内容 源文件
  >
  > cat a.txt | grep -n Yes (功能描述:在a.txt文件中查找Yes并显示行号)

##### 9.6.4 三剑客awk/grep/sed

#### 9.7 压缩解压

##### 9.7.1 gzip/gunzip指令

+ gzip 用于压缩文件

+ gunzip 用于解压

  > gzip fileName (功能描述:压缩fileName文件为*.gz文件)
  >
  > gunzip fileName.gz (功能描述:解压fileName.gz文件)
  >
  > 当我们使用gzip对文件进行压缩后不会保留原来的文件

##### 9.7.2 zip/unzip指令

+ zip 用于压缩文件

+ unzip 用于解压文件

  > zip [选项] xxx.zip 将要压缩的内容 (功能描述:压缩文件和目录的指令)
  >
  > unzip [选项] xxx.zip (功能描述:解压文件)
  >
  > zip常用选项
  >
  > ​	-r:递归压缩即是压缩目录
  >
  > unzip常用选项
  >
  > ​	-d <目录>:指定解压后文件的存放目录
  >
  > zip -r mypackage.zip /home (功能描述:将/home下面的所有文件进行压缩成mypackage.zip)
  >
  > unzip -d /opt/tmp/ mypackage.zip (功能描述:将mypackage.zip解压到/opt/tmp目录下)

##### 9.7.3 tar指令

+ 打包指令最后打包文件是.tar.gz文件

  > tar [选项] xxx.tar.gz 打包内容 (功能描述:打包目录压缩后的文件格式.tar.gz)
  >
  > tar -zcvf a.tar.gz a.txt b.txt (功能描述:将当前目录下的a.txt和b.txt压缩成a.tar.gz)
  >
  > tar -zcvf myhome.tar.gz /home/ (功能描述:将/home的文件夹压缩成myhome.tar.gz)
  >
  > tar -zxvf a.tar.gz (功能描述:将a.tar.gz解压到当前目录)
  >
  > tar -zxvf myhome.tar.gz -C /opt/ (功能描述:将myhome.tar.gz解压到/opt/目录下)

  | 选项 |        功能        |
  | ---- | :----------------: |
  | -z   |    打包同时压缩    |
  | -c   |  产生.tar打包文件  |
  | -x   |    解包.tar文件    |
  | -v   |    显示详细信息    |
  | -f   | 指定压缩后的文件名 |


#### 9.8 进程管理

##### 9.8.1 进程基本介绍

1) 在linux中,每个执行的程序都成为一个进程,每一个进程都分配一个id号
2) 每一个进程,都会对应一个父进程,而这个父进程可以复制多个子进程
3) 每个进程都可以以两种方式存在,前台和后台,前台进程就是用户目前屏幕上可以操作的,后台进程则是实际在操作,但是屏幕上无法看到的进程,通常使用后台方式执行
4) 一般系统的服务都是后台进程方式存在,而且都会常驻在系统中,直到关机才结束

##### 9.8.2 显示系统执行进程

+ 查看进程

  > ps -aux
  >
  > ps -a (功能描述:显示当前终端所有进程信息)
  >
  > ps -u (功能描述:以用户的格式显示进程信息)
  >
  > ps -x (功能描述:显示后台进程运行参数)

  | PS显示字段 |          说明          |
  | ---------- | :--------------------: |
  | PID        |       进程识别号       |
  | TTY        |        终端机号        |
  | TIME       |   此进程所消CPU时间    |
  | CMD        | 正在执行的命令或进程名 |

##### 9.8.3 终止进程kill and killall

若是某个进程执行一半需要停止时,或是已经消耗很大系统资源时,此时可以考虑停止该进程,使用kill命令来完成此项任务

+ 终止进程

  > kill [选项] 进程号 (功能描述:通过进程号杀死进程)
  >
  > 常用选项
  >
  > ​	-9	表示强迫进程立即停止
  >
  > killall 进程名称 (功能描述:通过进程名称杀死进程支持也通配符在系统因负载过大变得很慢时使用)

##### 9.8.4 查看进程树pstree

+ 以树结构查看进程信息

  >pstree [选项]
  >
  >常用选项
  >
  >​	-p	显示进程的PID
  >
  >​	-u	显示进程所属用户

##### 9.8.5 服务管理

+ 服务本质就是进程,但是运行在后台,通常会监听某个端口,等待其他程序的请求,因此又被称为守护进程

##### 9.8.6 动态监控进程

+ top与ps指令相似,都用来显示正在执行的进程,top与ps最大的不同之处在于top在执行一段时间可以更新正在运行的进程

  > top [选项]
  >
  > 常用选项
  >
  > ​	-d 秒数	 top指令每隔几秒更新默认是3秒
  >
  > ​	-i     	使top不显示任何闲置或者僵尸进程
  >
  > ​	-p	 	通过指定监控进程ID来仅仅监控某个进程状态

#### 9.9 Python定制篇开发平台Ubantu

##### 9.9.1 apt介绍

+ apt 是 Advanced Packaging Tool 简称,是一款安装包管理工具,在 ubantu 下可以使用 apt 指令用于软件包的安装、删除、清理等操作,类似于 windows 下的软件管理工具

##### 9.9.2  ubantu软件操作相关命令

+ 常用

  | 指令                                | 说明                                  |
  | ----------------------------------- | ------------------------------------- |
  | sudo apt-get update                 | 更新源                                |
  | sudo apt-get install package        | 安装包                                |
  | sudo apt-get remove package         | 删除包                                |
  | sudo apt-cache search package       | 搜索软件包                            |
  | sudo apt-cache show package         | 获取包的相关信息,如说明、大小、版本等 |
  | sudo apt-get -finstall              | 修复安装                              |
  | sudo apt-get remove package --purge | 删除包,包括配置文件等                 |
  | sudo apt-get upgrade                | 更新已安装的包                        |
  | sudo apt-get dist-upgrade           | 升级系统                              |

##### 9.9.3 ubantu软件安装卸载实例

+ 安装卸载vim软件

  > sudo apt-get remove vim (功能描述:卸载vim)
  >
  > sudo apt-get install vim (功能描述:安装vim)
  >
  > sudo apt-cache show package (功能描述:获取vim包信息)

##### 9.3.4 ubantu防火墙常用指令

+ 查看防火墙状态

  > sudo ufw status

+ 开启关闭防火墙

  > sudo ufw enable
  >
  > sudo ufw disable

+ 允许拒绝外来访问

  > ufw default allow/deny

+ 允许决绝访问 xx 端口

  > ufw allow/deny xx

#### 9.10 shell

shell是命令解释器,是Unix操作系统的用户接口,程序从用户接口得到输入信息,shell将用户程序及其输入翻译成操作系统内核能够识别的指令并将系统内核执行完成返回的输出通过shell再呈现给用户

##### 9.10.1 shell通识

shell广泛用于自动化批量系统初始化程序(update、软件安装、时区设置、安全策略)、自动化批量软件部署程序(LAMP、LNMP、Tomcat、LVS、Nginx)、自动化管理应用程序(KVM、集群管理扩容、Mysql)、日志分析处理(PV、UV、200、!200、top 100、grep/awk)、自动化备份恢复程序(Mysql完全备份/增量 + Crond)、自动化信息采集及监控程序(收集系统/应用状态、CPU、MEM、DISK、NET、TCP STATUS)

### 十. 数据库

#### 10.1 通识

##### 10.1.1 Python中操作Mysql步骤?

![image-20210419183934396](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210419183934396.png)

```python
import pymysql

# conn = pymysql.connect(host='127.0.0.1',port=3333,user='root',password='1234',database='sample')

# 操作cursor方法获取游标,得到一个可以执行的sql语句,并且将操作结果作为字典返回
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# try:
#     # 使用execute方法执行sql查询
#     cursor.execute('select * from `case`')
#     # 使用fetchall查询所有 fetchone查询单条
#     date = cursor.fetchall()
#     # date = cursor.fetchone()

#     print(date)

# except Exception as e:
#     print(e)

# finally:
#     conn.close()

from warnings import filterwarnings

# 忽略mysql告警信息
filterwarnings('ignore',category=pymysql.Warning)

class mysqlDB:

    def __init__(self):
        # 建立数据库连接
        self.conn = pymysql.connect(host='127.0.0.1',port=3333,user='root',password='1234',database='xdcls')
        # 使用cursor方法获取操作游标,得到一个可以执行的sql语句,并且操作结果作为字典返回的游标
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cur.close()
        # 关闭连接
        self.conn.close()

    def query(self,sql,state='all'):
        self.cur.execute(sql)
        if state == 'all':
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        return data

    def execute(self,sql):
        # 更新删除新增
        try:
            # 使用execute操作数据库
            rows = self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except Exception as e:
            print('数据库异常{0}'.format(e))
            self.conn.rollback()

if __name__ == "__main__":
    mydb = mysqlDB()
    # 查询
    rlt = mydb.query('select * from `case`')
    # 添加 必须使用双眼号,单眼号出错
    # rlt = mydb.execute("insert into `case`(app) values('xls')")
    print(rlt)
    
```

##### 10.1.2 SQL的SELECT语句完整执行顺序及常用语句?

**==SQL 对大小写不敏感==**

语法规范

> 不区分大小写但建议关键字大写、表名、列小写
> 每条命令使用分号结尾
> 每条命令根据需要可以缩进或者换行
>
> 注释
> 单行注释	#  文字
> 多行注释	/* 开头 */ 

```sql
SELECT *
FROM 表
WHERE 条件
GROUP BY 分组条件
HAVING 分组后的筛选条件
ORDER BY 排序字段
LIMIT 分页;

```

**执行顺序**

1)FROM / JOIN 和所有 ON条件 子句组装来自不同数据源的数据
2)WHERE 子句基于指定的条件对记录进行筛选
3)GROUP BY 子句将数据划分为多个分组
4)使用聚集函数进行计算
5)HAVING 子句筛选分组
6)计算所有的表达式
7)SELECT 子句查询字段
8)ORDER BY 子句对结果集进行排序
9)LIMIT 分页

![image-20210722092759313](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210722092759313.png)

常见DML语句

```sql
INSERT INTO 表名 VALUES(value1, value2, ......);
INSERT INTO 表名(列1, 列2 , ......) VALUES(value1, value2, ......);

UPDATE 表名 SET 列名1 = value1 WHERE 列名2 = value2;

DELETE FROM 表名 WHERE 列名 = 值;

```

常见DDL语句

```sql
# 查看当前所有数据库
SHOW DATABASES;

# 打开指定的库
USE 库名;

# 查看当前的库所在表
SHOW TABLES;

# 查看其他库表
SHOW TABLES FROM 库名;

# 创建表
CREATE TABLE 表名{
	列名 列类型,
	列名 列类型,
	列名 列类型
};

# 查看表结构
DESC 表名;

```

##### 10.1.3 Mysql数据库存储原理?

##### 10.1.4 事物的特性?

##### 10.1.5 数据库索引?

##### 10.1.6 数据库怎么优化查询效率?

##### 10.1.7 NoSQL和关系数据库的区别?

#### 10.2 Mysql

##### 10.2.1 引入

**数据库的好处**

1)持久化数据到本地
2)可以实现结构化查询,方便管理

**数据库的相关概念**

DB:数据库(database):存储数据的仓库,它保存了一系列有组织的数据
DBMS:数据库管理系统(Database Management System),数据库是通过DBMS创建和操作的容器
SQL:结构化查询语言(Structure Query Language),专门用来与数据库通信的语言

```sql
# 启动mysql服务(cmd管理员)
net start mysql

# 关闭mysql服务
net stop mysql

# 连接本地mysql服务
mysql -uroot -p

# 查看所有数据库名
SHOW DATABASES;

# 选择数据库名
USE dataName;

# 查看所有表名
SHOW TABLES;

# 解决中文乱码
SET NAMES GBK;

# 解决对齐
CHARSET GBK;

```

##### 10.2.2 DQL数据库查询语言

###### 1)基础查询

```sql
/*
语法:
select 查询列表 
from 表名;

特点:
1. 查询列表可以是:表中的字段,常量值,表达式,函数
2. 查询的结果是一个虚拟的表格
*/

USE myemployees;

#1. 查询单个字段
SELECT last_name FROM employees;

#2. 查询表中多个字段
SELECT last_name,salary,email FROM employees;

#3. 查询表中的所有字段
SELECT * FROM employees;

#4. 查询常量值
SELECT 100;
SELECT 'mars';

#5. 查询表达式
SELECT 100%98;

#6. 查询函数
SELECT VERSION();

#7. 起别名
# 方式一
SELECT 100%98 AS 结果;
SELECT last_name AS 姓,first_name AS 名 FROM employees;
# 方式二
SELECT last_name 姓,first_name 名 FROM employees;

# 案例: 查询salary,显示结果为out put
SELECT salary AS out put FROM employees;

#8. 去重
# 案例: 查询员工表中设计到所有的部门编号
SELECT DISTINCT department_id FROM employees;

#9. +号的使用 
/*
mysql中的+号仅仅只有一个功能:运算符
select 100+90;
select '123'+90;其中一个为字符型,视图将字符型转换为数值型,如果转换成功,则继续做加法运算
如果转换失败,则将字符型数值转换为0
*/

# 案例: 查询员工名和姓连接成一个字段,并显示为姓名
SELECT CONCAT(last_name,first_name) AS '姓名' FROM employees;

```

###### 2)条件查询

```sql
/*
语法:
select 查询列表 from 表名 where 筛选条件;

分类:
	1. 条件表达式筛选
	条件运算符:
		> < = != <> >= <= <=>安全等于
	2. 逻辑表达式筛选
	逻辑运算符:
		&& || !
		and or not
	3. 模糊查询
	like
	特点:
	1. 一般和通配字符搭配使用
		% 任意多个字符,包含0个字符
		_任意单个字符
	2. between and
		1. 提高sql简洁度
		2. 包含临界值
		3. 两个临界值不可调换顺序
	3. in
		1.提高sql简洁度
	4. is null
		1. 仅仅可以判断null值
		<=>:既可以判断null值又可以判断数值
*/
# 案例: 查询工资>12000的员工信息
SELECT * FROM employees WHERE salary > 12000;

# 案例:查询部门编号不等于90的员工和部门编号
SELECT * FROM employees WHERE department_id != 90;

# 案例: 查询工资在10000到20000之间的员工名,工资以及奖金
SELECT last_name,salary,commission_pct FROM employees WHERE salary >= 10000 AND salary <= 20000;

# 案例: 查询员工名字中包含字符a的员工信息
SELECT * FROM employees WHERE last_name LIKE '%a%';

# 案例: 查询员工名中第三个字符为n,第5个字符为l的员工名和工资
SELECT last_name,salary FROM employees WHERE last_name LIKE '__n_l%';

# 案例: 查询员工名第二个字符为_的员工名
SELECT last_name FROM employees WHERE last_name LIKE '_\_%';

# 案例: between and 查询员工编号在100到120之间的员工信息
SELECT * FROM employees WHERE employee_id BETWEEN 100 AND 120;

# 案例: 查询员工的工种编号是it_prog,ad_vp,ad_pres的员工名和工种编号
SELECT last_name,job_id FROM employees WHERE job_id IN ('IT_PROT','AD_VP','AD_PRES');

# 案例: 查询没有奖金的员工名和奖金率
SELECT last_name,commission_pct FROM employees WHERE commission_pct IS NULL;
SELECT last_name,commission_pct FROM employees WHERE commission_pct IS NOT NULL;

```

###### 3)排序查询

```sql
/*
select * from employees;

语法:
	select 查询列表
	from 表
	[where 筛选条件]
	order by 排序列表 [asc|desc]
特点:
	1. asc代表升序,desc代表降序
	2. order by子句中可以支持单个字段,多个字段,表达式,函数,别名
	3. order by子句一般放在最后,limit子句除外
*/

# 案例: 查询员工信息,要求工资从高到底排序
SELECT * FROM employees ORDER BY salary;

# 案例: 查询部门编号>=90的员工信息,按入职时间先后进行排序[添加筛选条件]
SELECT * 
FROM employees
WHERE department_id >= 90
ORDER BY hiredate;

# 案例: 按年薪高低显示员工的信息和年薪[按表达式排序]
SELECT *,salary*12*(1+IFNULL(commission_pct,0)) AS 年薪
FROM employees
ORDER BY salary*12*(1+IFNULL(commission_pct,0));

# 案例: 按年薪高低显示员工的信息和年薪[按别名排序]
SELECT *,salary*12*(1+IFNULL(commission_pct,0)) AS 年薪
FROM employees
ORDER BY 年薪;

# 案例: 按姓名的长度显示员工的姓名和工资[按函数排序]
SELECT LENGTH(last_name) AS 姓名长度,last_name,salary FROM employees ORDER BY LENGTH(last_name) DESC;

# 案例: 查询员工信息,要求先按工资排序,再按员工编号排序[按多个字段排序]
SELECT * FROM employees ORDER BY salary ASC,employee_id DESC;

```

###### 4)常见函数

```sql
/*

概念:类似java中的方法,将一组逻辑语句封装在方法体中,对外暴露方法名
好处:1. 隐藏了实现细节 2. 提高代码复用性

调用:select 函数名() form 表;

特点:
	1. 叫什么(函数名)
	2. 干什么(函数功能)
分类:
	1. 单行函数
	如:concat,length,ifnull等
	2. 分组函数
	功能:做统计使用,又称为统计函数,聚合函数,组函数

*/

# 字符函数

# length() 获取参数值的字节个数

SELECT LENGTH('mars');
SELECT LENGTH('张三s');

# concat 拼接字符串
SELECT CONCAT(last_name,'_',first_name) AS 姓名 FROM employees;

# upper,lower
SELECT UPPER('John');
SELECT CONCAT(UPPER(last_name),LOWER(first_name)) AS 'Name' FROM employees;

# substr,substring 索引从1开始
# 截取从指定索引处后面所有字符
SELECT SUBSTR('李莫愁爱上了陆展元',7) AS output;
# 截取从指定索引处指定字符长度的字符
SELECT SUBSTR('李莫愁爱上了陆展元',1,3) AS output;

# 案例:姓名中首字符大写,其他字符小写,然后拼接
SELECT CONCAT(UPPER(SUBSTR(last_name,1,1)),'_',LOWER(SUBSTR(last_name,2))) AS 'Nanme' FROM employees;

# instr 返回子串第一次出现的索引,如果找不到返回0
SELECT INSTR('杨不悔爱上了殷六侠','殷六侠') AS out_put;

# trim 去前后空格
SELECT TRIM('  张 珊  ') AS out_put;
SELECT TRIM('o' FROM 'oooo张oooo删oooo') AS out_put;

# lpad 用指定字符实现左填充指定长度
SELECT LPAD('殷素素',10,'*') AS out_put;

# rpad 用指定字符实现右填充指定长度
SELECT RPAD('殷素素',10,'*') AS out_put;
# replace 替换
SELECT REPLACE('张无忌爱上了周芷若','周芷若','西瓜') AS out_put;

# 数学函数

# round 四舍五入
SELECT ROUND(-1.55) AS out_put;
SELECT ROUND(1.427,2) AS out_put;

# ceil 向上取整
SELECT CEIL(-1.02);

# floor 向下取整
SELECT FLOOR(9.99);

# truncate 截断
SELECT TRUNCATE(1.65,1);

# mod 取余
SELECT MOD(10,3); a - a/b*b
SELECT MOD(-10,-3);

# 日期函数

# now 返回当前系统日期+时间
SELECT NOW();
# curdate 返回当前系统时间,不包含日期
SELECT CURDATE();
SELECT CURTIME();

# 可以获取指定的部分,年,月,日,时,分,秒
SELECT YEAR(NOW()) AS 年;
SELECT YEAR('1998-1-1') AS 年;
SELECT YEAR(hiredate) FROM employees;

SELECT MONTH(NOW()) AS 月; # 12
SELECT MONTHNAME(NOW()) AS 月; # December

# str_to_data 将字符通过指定格式转换成日期
SELECT STR_TO_DATE('1998-3-2','%Y-%c-%d') AS out_put;

# 查询入职日期为1992-4-3的员工信息
SELECT * FROM employees WHERE hiredate = '1992-4-3';

SELECT * FROM employees WHERE hiredate = STR_TO_DATE('4-3 1992','%c-%d %Y');

# date_format:将日期转换为字符
SELECT DATE_FORMAT(NOW(),'%y年%m月%d日') AS out_put;

# 查询所有奖金的员工名和入职日期(xx月/xx日 xx年)
SELECT last_name,DATE_FORMAT(hiredate,'%m月/%d日 %y年') AS 入职时间 FROM employees;

# 其他函数
SELECT VERSION();
SELECT DATABASE();
SELECT USER();
SELECT PASSWORD();

# 流程控制函数

# if函数 if else效果
SELECT IF(10>5,'大','小') AS 输出;
SELECT last_name,commission_pct,IF(commission_pct IS NULL,'没有奖金','拥有奖金') FROM employees;

# case函数的使用: switch case效果
/*
1
case 要判断的字段或表达式
when 常量1 then 要显示的值或语句
when 常量2 then 要显示的值或语句
................................
;
2
case 
when 条件1 then 要显示的值或语句
when 条件2 then 要显示的值或语句
................................
;
*/

# 案例: 查询员工的工资,要求
# 部门号=30,显示工资为1.1倍
# 部门号=40,显示工资为1.2倍

SELECT salary AS 原始工资,department_id,
CASE department_id
WHEN 30 THEN salary*1.1
WHEN 40 THEN salary*1.2
END AS 新的工资
FROM employees;

# 案例: 查询员工的工资情况
# 如果工资>20000,显示A级别
# 如果工资>15000,显示B级别
# 如果工资>10000,显示C级别
# 否则,显示B级别

SELECT salary,
CASE
WHEN salary>15000 THEN 'A'
WHEN salary>12000 THEN 'B'
WHEN salary>10000 THEN 'C'
ELSE 'D'
END AS '工资级别'
FROM employees;

# 分组函数

/*
功能:用作统计使用,又称为聚合函数或同级函数或组函数

分类: sum(),avg(),max(),min(),
count()返回非空值的个数

特点:
1. sum,avg一般用于处理数值型
	max,min,count可以处理任何类型
2. 以上函数都忽略null值

3. 可以和distinct搭配去重使用

4. conunt函数的单独介绍
	一般使用count(*)来统计结果集的行数
	
5. 和分组函数一同查询的字段要求是group by后的字段

*/

SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MAX(salary) 最大,MIN(salary) 最小,COUNT(salary) 计数 FROM employees;

# 和distinct搭配
SELECT SUM(DISTINCT salary),SUM(salary) FROM employees;
SELECT COUNT(DISTINCT salary),COUNT(salary) FROM employees;

# count函数的详细介绍 返回表中的所有行
SELECT COUNT(*) FROM employees;
SELECT COUNT(1) FROM employees;

# 和分组函数一通查询的字段有限制
SELECT AVG(salary),employee_id FROM employees;

# 案例:查询员工表中最大入职时间和最小入职时间的相差天数(diffrence)
SELECT MAX(hiredate)AS 最大入职时间,MIN(hiredate) AS 最小入职时间,DATEDIFF(MAX(hiredate),MIN(hiredate)) AS 入职相差时间 FROM employees;

```

###### 5)分组查询

```sql
/*

语法:
	SELECT 分组函数,列(要求出现在group by后面)
	from 表
	[where 筛选条件]
	group by 分组的列表
	[order by 子句]
	
注意:
	查询列表必须特殊,要求是分组函数和group by后出现的字段

特点:
	1. 分组查询中的筛选条件分为两类
		数据源:			位置			关键字
	分组前筛选:原始表		group by 语句之前	where
	分组后筛选:分组后的结果集	group by 语句之后	having

	1,分组函数做条件肯定放在having子句中
	2,能用分组前筛选的尽量使用分组前筛选
	
	2. group by子句支持单个字段分组,多个字段分组(多个字段使用逗号隔开)
	3. 添加排序放在整个分组查询之后
*/

# 案例: 查询每个组的平均工资
SELECT AVG(salary),department_id FROM employees GROUP BY department_id;

# 案例: 查询每个工种的最高工资
SELECT MAX(salary) AS 最高工资,job_id
FROM employees
GROUP BY job_id;

# 案例: 查询每个位置上的部门个数
SELECT COUNT(*),location_id
FROM departments
GROUP BY location_id;

# 案例: 查询邮箱中包含0字符的,每个部门的平均工资
SELECT AVG(salary),department_id,email
FROM employees
WHERE email LIKE '%a%'
GROUP BY department_id;

# 案例: 查询有奖金的每个领导下属员工最高工资
SELECT MAX(salary),manager_id
FROM employees
WHERE commission_pct IS NOT NULL
GROUP BY manager_id;

# 添加复杂筛选条件
# 案例:查询部门员工个数大于2(分组后的结果(having))
#	1. 查询每个部门员工个数
SELECT COUNT(*),department_id FROM employees GROUP BY department_id;
#	2. 根据1的结果进行筛选,查询那个部门员工个数大于2
SELECT COUNT(*),department_id FROM employees GROUP BY department_id HAVING COUNT(*)>2;

# 案例: 查询每个工种有奖金的员工的最高工资>12000的工种编号和最高工资
# 1. 查询每个工种有奖金的员工的最高工资
SELECT MAX(salary),job_id FROM employees WHERE commission_pct IS NOT NULL GROUP BY job_id HAVING MAX(salary)>12000;
# 2. 根据1的结果继续筛选,最高工资大于12000

# 案例: 查询领导编号>102的每个领导手下最低工资>5000的领导编号,以及其最低工资
SELECT manager_id,MIN(salary) FROM employees WHERE manager_id>102 GROUP BY manager_id HAVING MIN(salary)>5000;

# 按表达式分组
# 案例:按员工姓名的长度分组,查询每一组员工个数,筛选员工个数>5的
SELECT LENGTH(last_name),COUNT(*) FROM employees GROUP BY LENGTH(last_name) HAVING COUNT(*)>5;

# 按多个字段分组
# 案例: 查询每个部门,每个工种的平均工资
SELECT department_id,job_id,AVG(salary) FROM employees GROUP BY department_id,job_id;

# 添加排序
SELECT department_id,job_id,AVG(salary)
FROM employees 
WHERE department_id IS NOT NULL
GROUP BY department_id,job_id
HAVING AVG(salary) > 12000
ORDER BY AVG(salary);

```

###### 6)连接查询

![image-20210526170856822](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210526170856822.png)

```sql
/*
含义:多表查询

笛卡尔乘积的错误情况:当查询多个表时,没有添加有效的连接条件,表间完成完全连接.
表1有m行,表2有n行,结果=m*n行


发生原因:没有有效的连接条件
如何避免:添加有效的连接条件

分类:
	按年代分类
	sql92标准:仅仅支持内连接
		等值
		非等值
		自连接
		
	sql99标准[推荐]:
	按功能分类:
		内连接:
			等值连接
			非等值连接
			自连接
		外连接:
			左外连接
			右外连接
			全外连接
		交叉连接:

*/
SELECT * FROM beauty;
SELECT * FROM boys;
SELECT `name`,boyname FROM beauty,boys WHERE beauty.`boyfriend_id` = boys.`id`;

# 案例: 查询女生和对应的男生

# 1. 等值连接
/*

1. 多表等值连接结果为多表交集部分
2. n表连接至少需要n-1个连接条件
3. 多表的顺序没有要求
4. 一般需要为表起别名
5. 可以搭配前面介绍的所有子句

*/
SELECT name,boyname 
FROM beauty,boys 
WHERE beauty.`boyfriend_id` = boys.`id`;

# 案例: 查询员工名和对应部门名
SELECT last_name,department_name 
FROM employees,departments 
WHERE employees.`department_id` = departments.`department_id`;

# 案例: 为表取别名,提高语句简洁度
# 查询员工名,工种号,工种名
SELECT last_name,e.job_id,job_title 
FROM employees AS e,jobs
WHERE e.`job_id` = jobs.`job_id`;

# 案例: 添加筛选,查询有奖金的员工名,部门名
SELECT last_name,department_name FROM employees AS e,departments WHERE e.`department_id` = departments.`department_id` AND e.`commission_pct` IS NOT NULL;

#案例: 查询城市名中第二个字符为o的部门名和城市名
SELECT city,department_name 
FROM locations,departments 
WHERE locations.`location_id` = departments.`location_id` 
AND city LIKE '_o%';

# 添加分组
# 案例: 查询每个城市的部门个数
SELECT city,COUNT(*) AS 个数 
FROM locations,departments 
WHERE locations.`location_id` = departments.`location_id` 
GROUP BY city;

# 案例: 查询有奖金的每个部门的部门名称和领导编号和该部门的最低工资
SELECT department_name,departments.manager_id,MIN(salary) AS 最低工资
FROM departments,employees
WHERE departments.`department_id` = employees.`department_id`
AND commission_pct IS NOT NULL
GROUP BY department_name;

# 案例: 添加排序查询每个工种的工种名和员工个数,并且按员工个数降序
SELECT job_title,COUNT(*) AS 员工个数
FROM jobs,employees
WHERE jobs.`job_id` = employees.`job_id`
GROUP BY job_title
ORDER BY COUNT(*) DESC;

# 案列: 三表连接,查询员工名,部门名和所在的城市,且城市首字母为S
SELECT last_name,department_name,city
FROM employees,departments,locations
WHERE employees.`department_id` = departments.`department_id` 
AND departments.`location_id` = locations.`location_id`
AND city LIKE 'S%';

# 2. 非等值连接

# 案例: 查询员工的工资和工资级别

CREATE TABLE job_grades
(grade_level VARCHAR(3),
lowest_sal INT,
highest_sal INT);

INSERT INTO job_grades
VALUES ('A',1000,2999);

INSERT INTO job_grades
VALUES ('B',3000,5999);

INSERT INTO job_grades
VALUES ('C',6000,9999);

INSERT INTO job_grades
VALUES ('D',10000,14999);

INSERT INTO job_grades
VALUES ('E',15000,24999);

INSERT INTO job_grades
VALUES ('F',25000,40000);

SELECT last_name,salary,grade_level
FROM employees AS e,job_grades AS j
WHERE salary BETWEEN j.`lowest_sal` AND j.`highest_sal`;

# 3. 自连接
# 案例: 查询员工名和上级名称
SELECT e.employee_id,e.last_name,m.employee_id,m.last_name
FROM employees e,employees m
WHERE e.`manager_id` = m.`employee_id`;

# sql99语法
/*
语法:
	select 查询列表
	from 表1 别名 [连接类型]
	join 表2 别名
	on 连接条件
	[where 筛选条件]
	[group by 分组]
	[having 筛选条件]
	[order by 排序列表]

内连接(*):inner
外连接
	左外(*):left
	右外(*):right
	全外:full
交叉连接:cross

*/

# 内连接
/*
select 查询列表
form 表1 别名
inner join 表2 别名
on 连接条件

分类:
等值
非等值
自连接

*/

# 案例: 查询员工名,部门名
SELECT last_name,department_name
FROM employees e,departments d
WHERE e.`department_id` = d.`department_id`;

SELECT last_name,department_name
FROM employees e
INNER JOIN departments d
ON e.`department_id` = d.`department_id`;

# 案例: 查询名字中包含e的员工名和工种名(筛选)
SELECT last_name,job_title 
FROM employees e,jobs j
WHERE e.`job_id` = j.`job_id`
AND last_name LIKE '%e%';

SELECT last_name,job_title
FROM employees e
INNER JOIN jobs j
ON e.`job_id` = j.`job_id`
WHERE last_name LIKE '%e%';

# 案例: 查询部门个数>3的城市名和部门个数(分组+筛选)
SELECT city,COUNT(*) 部门个数
FROM locations l,departments d
WHERE l.`location_id` = d.`location_id`
GROUP BY city
HAVING 部门个数>3;

SELECT city,COUNT(*) 部门个数
FROM locations l
INNER JOIN departments d
ON l.`location_id` = d.`location_id`
GROUP BY city
HAVING 部门个数>3;

# 案例: 查询哪个部门的部门员工个数>3的部门名和员工个数,并按个数降序
SELECT department_name,COUNT(*) 员工个数
FROM departments d,employees e
WHERE d.`department_id` = e.`department_id`
GROUP BY d.department_name
HAVING 员工个数>3
ORDER BY 员工个数 DESC;

SELECT department_name,COUNT(*) 员工个数
FROM departments d
INNER JOIN employees e
ON d.`department_id` = e.`department_id`
GROUP BY department_name
HAVING 员工个数>3
ORDER BY 员工个数 DESC;

# 案例: 查询员工名,部门名,工种名,并按照部门名降序
SELECT last_name,department_name,job_title
FROM employees e,departments d,jobs j
WHERE e.`department_id` = d.`department_id`
AND e.`job_id` = j.`job_id`
ORDER BY department_name DESC;

SELECT last_name,department_name,job_title
FROM employees e
INNER JOIN departments d ON e.`department_id` = d.`department_id`
INNER JOIN jobs j ON e.`job_id` = j.`job_id`
ORDER BY department_name DESC;

# 非等值连接

# 案例: 查询员工的工资级别
SELECT last_name,salary,grade_level
FROM employees AS e
JOIN job_grades AS j
ON salary BETWEEN j.`lowest_sal` AND j.`highest_sal`;

SELECT grade_level,COUNT(*) 个数
FROM employees AS e
JOIN job_grades AS j
ON salary BETWEEN j.`lowest_sal` AND j.`highest_sal`
GROUP BY grade_level
HAVING 个数>15
ORDER BY 个数 DESC;


# 自连接
# 案例: 查询员工和上级的姓名
SELECT e.`last_name`,m.`last_name`
FROM employees AS e
JOIN employees AS m
ON e.`manager_id` = m.`employee_id`;

# 外连接
/*

应用场景:查询一个表中有一个表中没有的内容(主从关系)
特点:
1. 外连接的查询结果为主表中的所有记录
	如果从表中有和它匹配的,则显示匹配的值
	如果从表中没有和它匹配的,则显示null
	外连接查询结果=内连接结果+主表中有而从表中没有的记录
2. 左外连接,left join左边是从表
   右外连接,right join右边是从表
3. 左外和右外交换两个表的顺序可以实现相同效果
4. 全外连接=内连接+表1中有但表2没有+表2中有但表1中没有
5. 交叉连接:使用99语法实现笛卡尔乘积.
*/
# 引入: 查询男友不在男生表的女生
SELECT * FROM beauty;
SELECT * FROM boys;

SELECT be.name
FROM beauty be
LEFT OUTER JOIN boys bo ON be.`boyfriend_id` = bo.`id`
WHERE bo.id IS NULL;

# 案例: 查询哪个部门没有员工
SELECT department_name
FROM departments d
LEFT OUTER JOIN employees e
ON d.`department_id`=e.`department_id`
WHERE e.`employee_id` IS NULL;

# 全外连接
# mysql不支持
SELECT b.*,boys.*
FROM beauty b
FULL OUTER JOIN boys
ON b.`boyfriend_id` = boys.`id`;

# 交叉连接
SELECT b.*,bo.*
FROM beauty b
CROSS JOIN boys bo;

# sql92 sql99
# 功能:sql99支持较多
# 可读性:sql99实现连接条件的分离,可读性较高

# 案例: 查询编号>3的女生的男友信息,如果有则列出详细,没有用null填充
SELECT beauty.`name`,boys.*
FROM beauty
LEFT OUTER JOIN boys
ON beauty.`boyfriend_id` = boys.`id`
WHERE beauty.`id`>3;

# 案例: 查询哪个城市没有部门
SELECT city
FROM locations
LEFT OUTER JOIN departments
ON locations.`location_id` = departments.`department_id`
WHERE departments.`department_id` IS NULL;

# 案例: 查询部门名为SAL或IT的员工信息
SELECT department_name,employees.*
FROM employees
JOIN departments
ON employees.`department_id` = departments.`department_id`
WHERE departments.`department_name` = 'SAL' OR departments.`department_name` = 'IT';

```

###### 7)子查询

```sql
/*
定义:出现在其他语句中的select语句,称为子查询或内查询
外部的查询语句,称为主查询或外查询

分类:
按子查询出现的位置:
	select 后面:
		标量子查询
	from 后面:
		支持表子查询
	where 或 having后面:☆
		标量子查询(单行)
		列子查询(多行)
		行子查询
	exists后面(相关子查询):
		表子查询
按结果集的行列数不同:
	标量子查询(结果集只有一行一列)
	列子查询(结果集只有一列多行)
	行子查询(结果集有一行多列)
	表子查询(结果集一般多行多列)
*/


# 一. where或having后面
/*
1. 标量子查询(单行子查询)
2. 列子查询(多行子查询)
3. 行子查询(多列多行)

特点:
1. 子查询放在小括号内
2. 子查询一般放在条件右侧
3. 标量子查询一般搭配单行操作符使用(> < >= <= = <>)
   列子查询一般搭配多行操作符使用(in any/some all)
4. 子查询的执行顺序优先于主查询执行,主查询的条件依赖子查询的结果
*/

# 标量子查询
# 案例:谁的工资比Abel高?
# 1. 查询Abel的工资
SELECT salary
FROM employees
WHERE last_name = 'Abel';

# 2. 查询员工信息满足salary>1结果
SELECT *
FROM employees
WHERE salary > (
	SELECT salary
	FROM employees
	WHERE last_name = 'Abel'
);

# 案例: 返回job_id与141员工相同,salary比143号员工多的员工姓名,job_id和工资
# 1. 查询141号员工的job_id
SELECT job_id
FROM employees
WHERE employee_id = 141;

# 2. 查询143号员工的salary
SELECT	salary
FROM employees
WHERE employee_id = 143;

# 3. 查询员工姓名,job_id和工资,要求job_id=1并且salary>2
SELECT last_name,job_id,salary
FROM employees
WHERE job_id = (
	SELECT job_id
	FROM employees
	WHERE employee_id = 141
) AND salary > (
	SELECT	salary
	FROM employees
	WHERE employee_id = 143
);

# 案例: 返回工资最少员工的last_name,job_id和salary
# 1. 查询公司最低工资
SELECT MIN(salary)
FROM employees;

# 2. 查询last_name,job_id和salary,要求salary=1
SELECT last_name,job_id,salary
FROM employees
WHERE salary = (
	SELECT MIN(salary)
	FROM employees
);

# 案例: 查询最低工资大于50号部门最低工资的部门id和其最低工资
# 1. 查询50号部门的最低工资
SELECT MIN(salary)
FROM employees
WHERE department_id = 50;

# 2. 查询每个部门的最低工资
SELECT department_id,MIN(salary)
FROM employees
GROUP BY department_id; 

# 3. 筛选2,满足min(salary) > 1
SELECT department_id,MIN(salary)
FROM employees
GROUP BY department_id
HAVING salary > (
	SELECT MIN(salary)
	FROM employees
	WHERE department_id = 50
);

# 列子查询(多行子查询)
# 案例: 返回location_id是1400或1700的部门中的所有员工姓名
# 1. 查询location_id是1400或者1700的部门编号
SELECT DISTINCT department_id
FROM departments
WHERE location_id IN(1400,1700);

# 2. 查询员工姓名,要求部门号是1列表中的某一个
SELECT Last_name
FROM employees
WHERE department_id IN (
	SELECT DISTINCT department_id
	FROM departments
	WHERE location_id IN(1400,1700)
);

# 案例: 返回其他部门中比job_id为`IT_PROG`部门任一工资低的员工的员工号、姓名、job_id以及salary
# 1. 查询job_id为`IT_PROG`部门任一工资
SELECT DISTINCT salary
FROM employees
WHERE job_id = 'IT_PROG';

# 2. 查询员工号、姓名、job_id以及salary小于1中的任意一个
SELECT employee_id,last_name,job_id,salary
FROM employees
WHERE salary < ANY(
	SELECT DISTINCT salary
	FROM employees
	WHERE job_id = 'IT_PROG'
) AND job_id <> 'IT_PROG';
# 或
SELECT employee_id,last_name,job_id,salary
FROM employees
WHERE salary < (
	SELECT MAX(salary)
	FROM employees
	WHERE job_id = 'IT_PROG'
) AND job_id <> 'IT_PROG';

# 案例: 返回其他部门中比job_id为`IT_PROG`部门所有工资低的员工的员工号、姓名、job_id以及salary
SELECT employee_id,last_name,job_id,salary
FROM employees
WHERE salary < ALL(
	SELECT DISTINCT salary
	FROM employees
	WHERE job_id = 'IT_PROG'
) AND job_id <> 'IT_PROG';
# 或
SELECT employee_id,last_name,job_id,salary
FROM employees
WHERE salary < (
	SELECT MIN(salary)
	FROM employees
	WHERE job_id = 'IT_PROG'
) AND job_id <> 'IT_PROG';

# 行子查询(结果一行多列或者多行多列)
# 案例: 查询员工编号最小并且工资最高的员工信息

SELECT *
FROM employees
WHERE (employee_id,salary) = (
	SELECT MIN(employee_id),MAX(salary)
	FROM employees
);

# 1. 查询最小的员工编号
SELECT MIN(employee_id)
FROM employees;

# 2. 查询最高工资
SELECT MAX(salary)
FROM employees;

# 3. 查询员工信息
SELECT *
FROM employees
WHERE employee_id = (
	SELECT MIN(employee_id)
	FROM employees
) AND salary = (
	SELECT MAX(salary)
	FROM employees
);

# 二. SELECT后面的子查询
/*
仅支持标量子查询
*/

# 案例: 查询每个部门的员工个数
SELECT d.*,(
	SELECT COUNT(*)
	FROM employees e
	WHERE e.department_id = d.`department_id`
) number
FROM departments d;

# 案例: 查询员工号=102的部门名
SELECT (
	SELECT department_name
	FROM departments d
	INNER JOIN employees e
	ON d.department_id = e.department_id
	WHERE e.employee_id = 102
) 部门名;

# 三. FORM后面
# 案例: 查询每个部门的平均工资等级
# 1. 查询每个部门的平均工资
SELECT department_id,AVG(salary)
FROM employees
GROUP BY department_id;

# 2. 连接1的结果集合job_grade表,筛选条件平均工资
SELECT av_dep.department_id,av_salary,grade_level
FROM (
	SELECT department_id,AVG(salary) av_salary
	FROM employees
	GROUP BY department_id
) av_dep
INNER JOIN job_grades j
ON av_dep.av_salary BETWEEN j.lowest_sal AND j.highest_sal;

# 四. exists后面(相关子查询)
/*
语法:
exists(完整查询语句)
结果(0或者1)
*/

SELECT EXISTS(
	SELECT employee_id
	FROM employees
	WHERE salary = 30000
);

# 案例: 查询有员工的部门名
SELECT department_name
FROM departments d
WHERE EXISTS(
	SELECT *
	FROM employees e
	WHERE d.department_id = e.department_id
);

# 或in
SELECT 	department_name
FROM departments d
WHERE d.department_id IN (
	SELECT department_id
	FROM employees
);

# 案例: 查询没有女朋友的男神信息
SELECT bo.*
FROM boys bo
WHERE bo.id NOT IN (
	SELECT boyfriend_id
	FROM beauty
);

# 或exists
SELECT bo.*
FROM boys bo
WHERE NOT EXISTS(
	SELECT boyfriend_id
	FROM beauty b
	WHERE bo.id = b.boyfriend_id
);

```

###### 8)分页查询

```sql
/*
应用场景:要显示的数据需要分页提交sql请求
语法:
	SELECT 查询列表
	FROM 表
	[JOINTYPE JOIN 表2
	ON 连接条件
	WHERE 筛选条件
	GROUP BY 分组字段
	HAVING 分组后的筛选
	ORDER BY 排序字段]
	LIMIT offset,size;
	
	offset要显示条目的起始索引(起始索引从0开始)
	size要显示的条目个数
特点:
	1. limit语句放在查询语句的最后(执行上和语法上都是最后)
	2. 要显示的页数是page,每页条目数size
	SELECT *
	FORM 表
	LIMIT (page-1)*size,size;
*/
# 案例: 查询前五条员工信息
SELECT *
FROM employees
LIMIT 0,5;

# 案例: 查询第11条到第25条
SELECT *
FROM employees
LIMIT 10, 15;

# 案例: 有奖金的员工信息,并且工资较高的前10名
SELECT *
FROM employees
WHERE commission_pct IS NOT NULL
ORDER BY salary DESC
LIMIT 10;

```

###### 9)联合查询

```sql
/*
union 联合 合并:将多条查询语句合并成一个结果

语法:
查询语句1
UNION
查询语句2

应用场景:
要查询的结果来自于多个表,且多个表没有直接的连接关系,但查询的信息一致(全局搜索)

特点:
1. 要求多条查询语句查询列数一致
2. 要求多条查询语句查询每列类型和顺序要保持一致
3. UNION关键字默认去重,如果使用UNION ALL可以包含重复的项
*/

# 案例1:查询部门编号大于90或者邮箱中包含a的员工信息
SELECT *
FROM employees
WHERE email LIKE '%a%' OR department_id > 90;

# 或
SELECT *
FROM employees
WHERE email LIKE '%a%'
UNION
SELECT *
FROM employees
WHERE department_id > 90;

```

###### 10)查询总结

```mysql
# 语法
/*
SELECT 查询列表
FROM 表1 别名
连接类型 join 表2
ON 连接条件
WHERE 筛选
GOURP BY 分组列表
HAVING 筛选
ORDER BY 排序列表
LIMIT 起始条目索引, 条目数;
*/
```

##### 10.2.3 DML数据库操作语言

###### 1)插入语句

```sql
# 方式一:经典插入
/*
语法:
insert into 表名(列名,...)
values(值1,...); 

列名值名必须一一对应
可以省略列名,默认所有的列,且顺序和表中顺序一一对应
*/

# 1. 插入值的类型要与列的类型一致或兼容
INSERT INTO beauty(id,NAME,sex,borndate,phone,photo,boyfriend_id)
VALUES(13,'糖糖','女','1994-1-1','11111111111',NULL,2);

SELECT * FROM beauty;

# 2. 不可以为null的列必须插入值,可以为null的值如何插入值?

# 方式一:可以为空的写null
INSERT INTO beauty(id,NAME,sex,borndate,phone,photo,boyfriend_id)
VALUES(13,'糖糖','女','1994-1-1','11111111111',NULL,2);

# 方式二:可以为空的字段和值不写
INSERT INTO beauty(id,NAME,sex,borndate,phone,boyfriend_id)
VALUES(14,'方方','女','1990-2-2','11111111111',2);

# 3. 列的顺序是否可以调换--可以
INSERT INTO beauty(NAME,sex,id,phone) VALUES('江鲜','女',16,'110');

# 方式二:
/*
语法:
insert into 表名
set 列名=值,列名=值,...;
*/

INSERT INTO beauty
SET id=17,NAME='刘诗诗',sex='女',borndate='1991-3-3',phone='1818181818',boyfriend_id=2;

# 两种方式PK
# 1. 方式一支持多行插入,方式二不支持
INSERT INTO tableName(字段,....) VALUE(值,....),(值,....);
# 2. 方式一支持子查询,方式二不支持

```

###### 2)修改语句

```sql
/*
语法:
1. 修改单表记录
update 表名
set 列=新值,列=新值,...
where 筛选条件;

2. 修改多表记录[补充](级联修改)

sql92语法:
update 表1 别名,表2 别名
set 列=值,...
where 连接条件
and 筛选条件;

sql99语法:
update 表1 别名
inner|left|right join 表2 别名
on 连接条件
set 列=值,...
where 筛选条件;
*/

# 1. 修改单表记录
# 案例:修改beauty表中姓唐的电话为11111111
UPDATE beauty
SET phone='11111111'
WHERE NAME LIKE '糖%';

# 案例:修改boys表中id号为2的名称为张飞,魔力值10
UPDATE boys SET boyname='张飞',userCP=10
WHERE id=2;

# 2. 修改多表记录
# 案例:修改张无忌的女朋友的号码为114
UPDATE beauty be
INNER JOIN boys bo ON bo.`id`=be.`boyfriend_id`
SET phone='114'
WHERE bo.`boyName`='张无忌';

SELECT * FROM beauty;

# 案例:修改没有男朋友的女神男朋友编号为2
UPDATE beauty be
LEFT OUTER JOIN boys bo ON be.`boyfriend_id`=bo.`id`
SET be.`boyfriend_id`=2
WHERE bo.`id` IS NULL;

```

###### 3)删除语句

```sql
/*
方式一:delete
语法:
1. 单表删除[*]
delete from 表名 where 筛选条件

2. 多表删除[补充](级联删除)
语法:
sql92语法:
delete 表1的别名,表2的别名
from 表1 别名,表2 别名
where 连接条件
and 筛选条件;

sql99语法:
delete 表1的别名,表2的别名
from 表1 别名
inner|left|right join 表2 别名 on 连接条件
where 筛选条件;

truncate table 表名;
*/

# 方式一:delete

# 1.单表删除,删除手机号为9结尾女神信息
DELETE FROM beauty WHERE phone LIKE '%9';
SELECT * FROM beauty;

# 2.多表删除,删除张无忌女朋友的信息
DELETE be
FROM beauty be
INNER JOIN boys bo ON be.`boyfriend_id`=bo.`id`
WHERE bo.`boyName`='张无忌';

SELECT * FROM beauty;

# 案例:删除黄晓明的信息以及他女朋友的信息
DELETE be,bo
FROM beauty be
INNER JOIN boys bo ON be.`boyfriend_id`=bo.`id`
WHERE bo.`boyName`='黄晓明';

# 方式二:truncate语句 == delete from table;

# 案例:将魅力值>100的男神信息删除
TRUNCATE TABLE boys;

#delete PK truncate[面试题]
/*
1. delete可以加where条件[LIMIT 1],truncate不可
2. truncate删除,效率高些
3. 假如要删除的表中有自增长列,delete删除再插入数据,自增长的列从断点开始,truncate自增长列从1开始
4. truncate删除没有返回值,delete删除有返回值
5. truncate删除不能回滚,delete可以回滚
*/

```

##### 10.2.4 DDL数据库定义语言

###### 1)库的管理

```sql
/*
 1. 库的创建:
creat database [if not exists] 库名;
*/
CREATE DATABASE IF NOT EXISTS books;

# 2. 库的修改
RENAME DATABASE books TO 新库名;
# 更改库的字符集
ALTER DATABASE books CHARACTER SET gbk;

# 3. 库的删除
DROP DATABASE IF EXISTS books;

```

###### 2)表的管理

```sql
# 1. 表的创建
CREATE TABLE [IF NOT EXIST]表名(
	列名 列的类型[(长度) 约束],
	列名 列的类型[(长度) 约束],
	列名 列的类型[(长度) 约束]
);

CREATE TABLE book(
	id INT, # 编号
	bookName VARCHAR(20), # 书名
	authorid INT, # 作者
	price DOUBLE # 价格	
);

CREATE TABLE author(
	id INT,
	auName VARCHAR(20),
	nation VARCHAR(20)
);

# 2. 表的修改
/*
alter table 表名 add|drop|modify|change column 列名 [列类型 约束];
*/

# 修改列名
ALTER TABLE book CHANGE COLUMN authorid atorid INT;
# 修改列的类型或者约束
ALTER TABLE book MODIFY COLUMN atorid DOUBLE;
# 添加新列
ALTER TABLE book ADD COLUMN annual DOUBLE;
# 删除旧列
ALTER TABLE book DROP COLUMN annual;
# 修改表名
ALTER TABLE author RENAME TO authorinfo;

# 3. 表的删除
DROP TABLE IF EXISTS  authorinfo;
SHOW TABLES;

# 4. 表的复制

INSERT INTO authorinfo VALUES
(1,'村上','日本'),
(2,'莫言','中国'),
(3,'金庸','中国');

# 1. 仅仅复制表的结构
SELECT * FROM authorinfo;

CREATE TABLE copy1 LIKE authorinfo;

# 2. 复制表的结构+数据
CREATE TABLE copy2
SELECT * FROM authorinfo;

# 3. 仅复制部分数据
CREATE TABLE copy3
SELECT id,auName
FROM authorinfo
WHERE nation='中国';

# 4. 仅复制某些字段
CREATE TABLE copy4
SELECT id,auName
FROM authorinfo
WHERE 0;

SELECT * FROM copy4;

# 案例讲解

# 创建表 dept1.
NAME NULL? TYPE
id         INT(7)
NAME       VARCHAR(25)
# 
USE test;
CREATE TABLE dept1(
	id INT(7),
	NAME VARCHAR(25)
	);

# 将表departments中的数据茶树新表dept2中
CREATE TABLE dept2
SELECT * FROM myemployees.`departments`;

```

###### 3)数据类型

```mysql
# 常见数据类型

/*
数值型:
	整型
	小数
		定点数
		浮点数
字符型:
	短文本:char、varchar
	较长文本:text\blob(较长二进制的数据)
	
日期型:
*/

# 一. 整型
/*
分类:
tinyint、smallint、mediumint、int/integer、bigint
1        2         3         4            8

特点：
	如果不设置无符号还是有符号,默认是有符号,如果想要设置无符号,需要添加unsigned关键字
	如果插入的数值超过整型的范围,会报outofrange异常,并插入临界值
	如果不设置长度会有默认的长度,长度代表了显示的最大宽度,如果不够左边会用0填充需要搭配ZEROFILL使用,并且默认变为无符号的整型
*/

# 1. 如何设置无符号和有符号
DROP TABLE IF EXISTS intDemo;
CREATE TABLE intDemo(
	int1 INT(7) ZEROFILL,
	int2 INT(7) UNSIGNED
);

# 二. 小数
/*
1. 浮点型
float(M, D)
double(M, D)

2. 定点型
dec(M, D)
decimal(M, D)

特点:
	M:整数部位+小数部位
	D:小数部位
	如果超过范围,报OutOfRange异常,则插入临界值
	
	M和D都可省略,如果是decimal,默认dec(10, 0)
	如果是float或者double,则会根据插入的数值的精度来决定精度
	
	定点型的精度较高,如果要求插入的数值精度较高如货币可以使用decimal
	
原则:
	所选择的类型越简单越好,能保存数值的类型越小越好(节省空间)
*/

# 三. 字符型
/*
较短的文本
char
varchar

其他:
binary,varbinary用于保存较短的二进制文件
ENUM用于单个枚举
SET用于保存集合枚举

较长的文本
text
blob(较大的二进制)

特点:
	char(M)和varchar(M),M表示最大字符数,char的M可以不写,默认为1,varchar定义时必须写入M,char固定长度字符,varchar可变长度的字符,char相比varchar更加耗费空间,但效率较高
*/

CREATE TABLE charDemo(
	c1 ENUM('A', 'B', 'C')
);

# 四. 日期
/*
分类
date	只保存日期
time	只保存时间
year	只保存年月

datetime	保存日期+时间
timestamp	保存日期+时间	受时区影响
*/
CREATE TABLE dateDemo(
	d1 DATETIME,
    d2 TIMESTAMP
);
```

###### 4)常见约束

```mysql
/*
限制表中数据输入,保证表中数据的准确性和可靠性

六大约束:
	NOT NULL	非空,保证该字段的值不为空(姓名)
	DEFAULT		默认,保证该字段有默认值(性别默认为男)
	PRIMARY KEY	主键,用于保证该字段的值具有唯一性,并且非空(学号)
	UNIQUE		唯一,用于保证该字段的值具有唯一性,可以为空(座位号码)
	CHECK		检查约束(mysql中不支持)
	FOREIGN		外键,用于限制两个表的关系,用于保证该字段的值必须来源于主表关联列的值,在从表添加外键约束,用于主表中某列的值,比如学生表的专业编号,员工表的部门编号
	
添加约束时机:
	1. 创建表时
	2. 修改表时
	
约束添加分类:
	列级约束
		六大约束语法支持,但是外键约束无效
	表级约束
		除了非空以及默认,其他的都支持

主键约束唯一约束对比 PRIMERY KEY && UNIQUE
	主键保证唯一性,不能为空,一个表中最多只可设置一个主键,允许多列组合
	唯一保证唯一性,可以为空(只能一个null保证唯一),一个表中可以设置多个唯一,允许多列组合

外键
	1. 要求在从表设置外键关系
	2. 从表外键列的类型要和主表的关联列要求一致或者兼容, 名称没有要求
	3. 主表的关联列必须要是一个key(一般是主键或唯一)
	4. 插入数据先插入主表,再插入从表,删除数据时,先删除从表再删除主表
	
列级约束表级约束对比
	列级约束位置列的后面,语法全部支持,但是外键没有效果,不可以起约束名称
	表级约束在所有列后面,默认和非空不支持,其他支持,可以起约束名
*/
CREATE TABLE 表名(
	字段名	字段类型	约束
)

# 一. 创建表时添加约束

# 1. 添加列级约束
/*
语法:
	直接在字段名和类型后面追加约束类型即可(默认、非空、主键、唯一)
*/
CREATE TABLE studinfo(
	id INT PRIMARY KEY, # 主键
    studName VARCHAR(20) NOT NULL, # 非空
    gender CHAR(1) CHECK(gender = '男' or gender = '女'), # 检查
    seatNumb INT UNIQUE, # 唯一
    age INT DEFAULT 18, # 默认
    majorId INT FOREIGN KEY REFERENCES major(id) # 外键
);

CREATE TABLE major(
	id INT PRIMARY KEY, # 关联列必须是一个key(一般是主键或唯一)
    majorName VARCHAR(20)
);

DESC studinfo;

# 查看studinfo中所有的索引, 包括主键、外键、唯一
SHOW INDEX studinfo

# 2. 添加表级约束
/*
语法:
	在各个字段的最下
	[CONSTRAINT 约束名] 约束类型(列名)
*/
DROP TABLE IF EXISTS studinfo；

CREATE TABLE studinfo(
	id INT,
    studName VARCHAR(20),
    gender CHAR(1),
    seatNumb INT,
    age INT,
    majorId INT,
    
    CONSTRAINT pk PRIMARY KEY(id), # 主键
    CONSTRAINT uq UNIQUE(seatNumb), # 唯一
    CONSTRAINT ck CHECK(gender = '男' or gender = '女'), # 检查
    CONSTRAINT fk FOREIGN KEY(majorId) REFERENCES major(id)
);

SHOW INDEX studinfo;

# 通用写法

CREATE TABLE studinfo(
	id INT PRIMARY KEY,
    studName VARCHAR(20) NOT NULL,
    gender CHAR(1) CHECK(gender = '男' or gender = '女'),
    seatNumb INT UNIQUE,
    age INT DEFAULT 18,
    majorId INT,
    
    FOREIGN KEY(majorId) REFERENCES major(id)
);

# 二. 修改表时添加约束
/*
1. 添加列级约束
ALTER TABLE 表名 MODIFY COLUMN 字段名 字段类型 新的约束;
2. 添加表级约束
ATLERT TABLE 表名 ADD 新的约束(列名) [REFERENCES 表名(列名)];
*/
DROP TABLE IF EXISTS studinfo(
	id INT,
    studName VARCHAR(20),
    gender CHAR(1),
    seatNumb INT,
    age INT,
    majorId INT
);

DESC studinfo;

# 添加非空、默认约束
ALTER TABLE studinfo MODIFY COLUMN studName VARCHAR(20) NOT NULL;
ALTER TABLE studinfo MODIFY COLUMN age INT DEFAULT 18;

# 添加主键
ALTER TABLE studinfo MODIFY COLUMN id INT PRIMARY KEY;
ALTER TABLE studinfo ADD PRIMARY KEY(id);

# 添加唯一
ALTER TABLE studinfo MODIFY COLUMN seatNumb INT UNIQUE;
ALTER TABLE studinfo ADD UNIQUE(seatNumb);

# 添加外键
ALTER TABLE studinfo ADD FOREIGN KEY(majorid) REFERENCES major(id);

# 三. 删除表示删除约束
# 1. 删除非空、默认约束
ALTER TABLE studinfo MODIFY COLUMN studName VARCHAR(20) NULL;
ALTER TABLE studinfo MODIFY COLUMN age INT;

# 2. 删除主键
ALTER TABLE studinfo DROP PRIMARY KEY;

```

###### 5)自增长列

```mysql
/*
又称标识列,可以不用手动的插入值,系统提供默认的序列值

特点:
	1. 自增长列不必一定和主键搭配,但是要求和一个key搭配
	2. 一个表中只可以有一个自增长列
	3. 自增长列数据类型只能是数值型(一般INT)
	4. 自增长列可以通过 SET AUTO_INCREMENT_INCREMENT = 3设置步长
*/

# 一. 创建表示设置标识列
CREATE TABLE identity(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20)
);

SHOW VARIABLES LIKE %AUTO_INCREMENT%;

# 二. 修改表时设置自增长列
ALTER TABLE identity MODIFY COLUMN id INT PRIMARY KEY AUTO_INCREMENT;

# 三. 修改表时删除自增长列
ALTER TABLE identity MODIFY COLUMN id INT PRIMARY KEY;
```

##### 10.2.5 TCL 事物控制语言

Transaction Control Language

```mysql
# 事物
/*
概念:
	由单独单元的一个或一组SQL语句组成,在这个单元中,每个SQL语句是相互依赖的
	整个单独单元作为一个不可分割的整体,如果单元中某条SQL语句一旦执行失败或者产生错误,整个单元将会回滚,所有受到影响数据将返回事物开始以前的状态;如果单元中所有的SQL语句均执行成功,则事物顺利执行
	
案例 转账
A 1000
B 1000

UPDATE 表 SET A的余额 = 500;
UPDATE 表 SET B的余额 = 1500;

特点
	事物属性(ACID)属性
	1. 原子性(Atomicity)
	原子性是指事物是一个不可分割的工作单位,事物中的操作要么都发生,要么都不发生
	2. 一致性(Consistency)
	事物必须使数据库从一个一致性状态变换到另外一个一致性状态
	3. 隔离性(Isolation)
	事物的隔离性是指一个事物的执行不能被其他事物干扰,即一个事物内部操作及使用的数据对并发的其他事物是隔离的,并发执行的各个事物之间不能互相干扰
	4. 持久性(Durablity)
	持久性是指一个事物一旦被提交,它对数据库中的数据的改变就是永久性的,接下来的其他操作和数据库故障不应该对其有任何影响
	
创建
	隐式事物	事物没有明显的开启和结束标记(INSERT、UPDATE、DELETE语句)
	显式事物	事物具有明显的开启和结束标记(前提必须先设置自动提交功能为禁用SET ATUOCOMMIT = 0;)
	步骤1	开启事物
	SET AUTOCOMMIT = 0;
	START TRANSACTION; 可选
	步骤2	编写事物语句
	步骤3	结束事物
	COMMIT	提交事物
	ROLLBACK	回滚
	
	SAVEPOINT 设置保存点,搭配ROLLBACK使用
*/

# MySQL中的存储引擎
/*
概念
	在mysql中的数据用各种不同的计数存储在文件(或内存)中
	
通过 SHOW ENGINES 来查看mysql支持的存储引擎

在mysql中用的最多的存储引擎有: innodb、myisam、memory等,其中innodb支持事物,而myisam、memory等不支持事物
*/

# 演示事物使用步骤
DROP TABLE IF EXISTS account;
CREATE TABLE account(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(20),
    balance DOUBLE
);

INSERT INTO account(username, balance)
VALUES('A', 1000),('B', 1000)

# 开启事物
SET AUTOCOMMIT = 0;
START TRANSACTION;
# 编写一组事物的语句
UPDATE account SET balance = 500 where username = 'A';
UPDATE account SET balance = 1500 where username = 'B';
# 结束事物
COMMIT; # 提交
ROLLBACK; # 回滚

SELECT * FROM account;

# 演示SAVE POINT使用
SET AUTOCOMMIT = 0;
START TRANSACTION;
DELETE FROM account WHERE id = 25;
SAVEPOINT A; # 设置保存点
DELETE FROM account WHERE id = 28;
ROLLBACK TO A;

/*
数据库的隔离级别

定义
	一个事物与其他事物隔离的程度称为隔离级别,数据库规定了多种事物隔离级别,不同隔离级别对应不同的干扰程度,隔离级别越高,数据一致性就越好,但并发越弱

对于同时运行的多个事物,当这些事务访问数据库中相同的数据时,如果没有采用必要的隔离机制,就会导致各种并发问题
	脏读:对于两个事务T1,T2,T1读取了已经被T2更新但还没有被提交的字段之后,若T2回滚,T1读取的内容就是临时且无效的
	不可重复读取:对于两个事务T1,T2,T1读取了一个字段,然后T2更新了该字段,之后,T1再次读取同一个字段,值就不同了
	幻读:对于两个事务T1,T2,T1从一个表中读取了一个字段,然后T2在表中插入了一些新的行.之后,如果T1再次读取同一个表,就会多出几行

数据库提供4种事物隔离级别
 	READ UNCOMMITED: 出现脏读、不可重复读取、幻读
 	READ COMMITTED: 出现不可重复读取、幻读
 	REPEATABLE READ: 出现幻读
 	SERIALIZABLE: 不会出现脏读、不可重复读取、幻读
 	
 mysql中默认第三个隔离级别 REPEATABLE READ
*/

# 查看当前的隔离级别
SELECT @@TX_ISOLATION;

# 设置当前mysql连接的隔离级别
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

# 设置数据库系统的全局的隔离级别
SET GLOBAL TRANSACTION ISOLATION LEVEL READ COMMITTED;

# 视图
/*
定义
	一种虚拟存在的表,行和列的数据来自定义视图的查询中使用的表,并且是在使用视图时动态生成的,只保存了sql逻辑,不保存查询的结果
	
应用场景(封装)
	多个地方用到同样查询结果
	查询结果使用的sql语句比较复杂
*/
# 演示视图
CREATE VIEW myView
AS
SELECT studName, majorId
FROM studinfo
INNER JOIN major
ON studinfo.majorId = major.id
WHERE studinfo.majorId = 1;

# 一. 创建视图
/*
语法
	CREATE VIEW 视图名称
	AS
	查询语句;
*/
USE myemployees;

# 查询姓名包含a字符的员工名、部门名和工种信息
# 创建
CREATE VIEW myv1
AS
SELECT last_name, department_name, job_title
FROM employees e
JOIN departments d on e.department_id = d.department_id
JOIN jobs j on j.job_id = e.job_id;

# 使用
SELECT * FROM myv1 WHERE last_name LIKE %a%;

# 查询各部门的平均工资级别
# 创建视图查看每个部门平均工资
CREATE VIEW myv2
AS
SELECT AVG(salary) as ag, department_id
FROM employees
GROUP BY department_id;

# 使用
SELECT myv2.ag, g.grade_level
FROM myv2
JOIN job_grades g
ON myv2.ag BETWEEN g.lowest_sal AND g.heighest_sal;

# 查询平均工资最低的部门信息
SELECT * FROM myv2 ORDER BY ag LIMIT 1;

# 查询平均工资最低部门名和工资
CREATE myv3
SELECT * FROM myv2 ORDER BY ag LIMIT 1;

SELECT d.department_name, m.ag
FROM departments d
JOIN myv3 m
ON d.department_id = m.department_id;

# 二. 视图的修改
/*
方式一
	CREATE OR REPLACE VIEW myv3
	AS
	查询语句;
*/
CREATE OR REPLACE VIEW myv3
AS
SELECT AVG(salary), job_id
FROM employees
GROUP BY job_id;

/*
方式二
	ALTER VIEW 视图名称
	AS
	查询语句;
*/
ALTER VIEW myv3
AS
SELECT AVG(salary), job_id
FROM employees
GROUP BY job_id;

# 三. 查看视图
DESC myv3;
SHOW CREATE VIEW myv3;

# 四. 删除视图
/*
DROP VIEW 视图名称, 视图名称...;
*/
DROP VIEW myv1, myv2, myv3;

# 创建视图emp_v1,要求查询电话号码以'011'开头的员工姓名和工资、邮箱
CREATE OR REPLACE VIEW emp_v1
AS
SELECT last_name, salary, email
FROM employee
WHERE phone_number LIKE '011%';

# 创建视图emp_v2,要求查询部门最高工资高于12000的部门信息
CREATE OR REPLACE VIEW emp_v2
AS
SELECT MAX(salary) mx_dep, department_id
FROM employees
GROUP BY department_id
HAVING MAX(salary) > 12000;

SELECT d.* mx
```

##### 10.2.6 MySQL执行一条查询语句内部执行过程?

![image-20210519134854905](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210519134854905.png)

+ 客户端先通过连接器连接到MySQL服务器
+ 连接器通过数据库权限身份验证后,会先查询数据缓存是否存在(之前是否执行过相同的SQL查询),如果有会直接返回缓存中的数据,如果没有则会进入分析器
+ 进入分析器会对查询语法进行语法分析,判断该SQL是否存在语法错误,如果存在语法错误,会直接返回给客户端错误,如果正确则进入优化器
+ 优化器会对查询语句进行优化处理
+ 最终进入执行器,开始执行语句直到满足所有条件数据,进行返回

#### 10.3 redis

##### 10.3.1 常用redis语法

+ 查询键

  > keys *

### 十一. 数据结构算法

《数据结构与算法》裘宗燕	《算法图解》

#### 11.1 绪论

##### 11.1.1 前导课

###### 1)编程境界

写程序 - 高效地写程序 - 写高效的程序 - 设计算法 - 设计有用算法

算法常用设计模式

+ 枚举法
+ 贪心法 根据问题信息尽可能的做出部分的解
+ 分治法 复杂问题分解为相对简单的问题
+ 回溯法 采用试探方式根据实际情况选择一个可能方向当后面的求解动作无法继续时退回到前面的步骤
+ 动态规划 
+ 分支限界

###### 2)频繁查找词组

方法一 线性结构

​	线性结构,这些词按照默认顺序存放,查找一个词从头到尾顺序搜索

方法二 树状结构

​	树状结构,这些词条按照26个字符存放,查找一个词,首先查找第一个词的首字母,在查找第二个词的首字母

方法三 哈希结构

​	哈希结构,汉字在内存是有效二进制编码的,把这些词的二进制编码转换成对应十进制数,这个数作为词在顺序表中的存储位置组织并存放词条,那么查找某个词是否在词库中
​	1)首先计算该词的10进制值
​	2)然后对这个值所对应的存储下标去查找

##### 11.1.2 逻辑结构

在自然界中数据和数据之间可以归纳为四种逻辑关系

| 结构     |           说明            |
| -------- | :-----------------------: |
| 线性结构 | 一对一,如线性表、栈、队列 |
| 树形结构 |        一对多,如树        |
| 图状结构 |        多对多,如图        |
| 集合关系 |  没有关系的数据放在一起   |

##### 11.1.3 存储结构

数据在内存存放有两种基本形式

| 存储结构     |                            说明                            |
| ------------ | :--------------------------------------------------------: |
| 顺序存储结构 | 借助元素在存储器中的**相对位置**表示数据元素之间的逻辑关系 |
| 链式存储结构 |   借助指示元素存储地址的**指针**表示数据元素间的逻辑关系   |

##### 11.1.4 算法分析

###### 1)定义

解决某一特定问题的具体步骤的描述,它是指令的有限序列,每一个指令表示一个或多个操作,可以用自然语言,也可以使用计算机语言来描述

###### 2)算法特征

+ 有穷性,算法必须保证执行有限步骤之后结束
+ 确切性,算法的每一步必须有确切的定义
+ 可行性,算法原则上能够精确运行,用简单方法做有限次运算后即可完成
+ 输入,算法有0个或者多个输入,以刻画运算对象的初始情况,0个输入是指算法本身给定初始条件
+ 输出,算法有1个或者多个输出,以反应对输入数据加工后的结果,没有输出的算法是无意义的

###### 3)算法评价

+ 正确性
+ 可读性
+ 健壮性
+ 效率与低存储量

###### 4)算法性能分析与度量

引入**渐进时间复杂度**在数量上古迹一个算法的执行时间

> T(n) = O(f(n))

它表示随问题规模n的增大,算法执行时间的增长率和f(n)相同,并且只考虑数量级最高的语句执行频度,使用大O记号,O(f(n))称为算法渐进时间复杂度,简称时间复杂度

==算法时间复杂度取决于最深循环内包含基本操作的语句的重复执行次数,称语句重复执行次数为语句的频度==

5)算法好坏评价标准

+ 时间复杂度

  根据算法写成程序在执行时耗费时间的长度,这个长度往往也与输入数据的规模有关

+ 空间复杂度

  一般情况下,程序在机器上运行时,抛去需要存储程序本身的输入数据等之外,还需要存储对数据操作的存储单元,如果输入数据所占空间和算法无关,只取决于问题本身,那么只需要分析算法在实现过程中所占的辅助单元即可
  
  空间复杂度是对一个算法在运行过程中临时占用存储空间大小的量度,所谓的临时占用存储空间指的就是代码中**辅助变量所占用的空间**,它包括为参数表中**形参变量**分配的存储空间和为在函数体中定义的**局部变量**分配的存储空间两个部分,我们用 S(n)=O(f(n))来定义,其中n为问题的规模(或大小)。通常来说,只要算法不涉及到动态分配的空间,以及递归、栈所需的空间,空间复杂度通常为O(1),一个一维数组a[n],空间复杂度O(n),二维数组为O(n^2)

现阶段优化方向是**空间换时间**

#### 11.2 线性表

##### 11.2.1 概念和表抽象数据类型

###### 1)概念

线性表是相同数据类型的n个数据元素的有限序列

> A = (a1, a2, a3, a4, a5,......, an)
>
> 表头元素没有前驱
> 表尾元素没有后继
>
> n表示线性表A的长度,当n=0是,表A时空表

线性结构特点,在数据元素的非空有限集中

+ 存在唯一的一个被称作第一个的数据元素
+ 存在唯一的一个被称作最后一个的数据元素
+ 除第一个外,集合中的每个元素均只有一个前驱
+ 除最后一个外,集合中的每个数据元素均只有一个后继

###### 2)线性表的抽象数据类型

![image-20210503232358633](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210503232358633.png)

###### 3)线性表的实现

顺序存储 顺序表

+ 将表中元素顺序存放在一大块连续的存储区中,这样实现的线性结构称为顺序表,顺序表中元素类型相同,元素之间的顺序关系由它们的存储顺序体现

链式存储 链表

+ 将表元素存放在通过地址连接构造起来的一系列内存中,通过地址的指引来体现数据之间的顺序

##### 11.2.2 顺序表

###### 1)实现

定义

+ 用一组地址连续的存储单元存放一个线性表

线性表顺序存储的特点

+ 逻辑上相邻的数据元素,其物理地址也相邻,即用物理上的相邻表示逻辑上的相邻
+ 实现随机存取[知道一个元素的地址,可以知道其他元素地址],时间复杂度O(1)

###### 2)操作

| 操作           | 时间复杂度 |
| -------------- | :--------: |
| 按序号查找数据 |    O(1)    |
| 按值查找数据   |    O(n)    |
| 插入数据       |    O(n)    |
| 删除数据       |    O(n)    |

```python
# 按值查找
def search(sequ, elem):
    i = 0
    while i < len(sequ)-1:
        if self[i] == elem:
            return True
        else:
            i += 1
    else:
        return False
    
```

##### 11.2.3 Python中顺序表的实现

Python中的list和tuple两种类型采用了顺序表的实现技术

![image-20210503235929399](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210503232358633.png)

tuple 是不可变类型,即不变的顺序表,因此不支持改变其内部状态的任何操作,而其他方面,则与list的性质类型类似

list基本实现技术

Python标准类型 list 就是一种元素个数可变的线性表,可以加入和删除元素,并且在各种操作中维持已有元素的顺序(即保序),而且还具有以下特征:

| list                                       |                            顺序表                            |
| ------------------------------------------ | :----------------------------------------------------------: |
| 元素位置有下标,以索引可以直接获取元素      | 连续的存储空间,以偏移量计算取得元素,不必遍历所有元素,时间复杂度为O(1) |
| 元素无论如何改变,表对象不变,也就是其id不变 |                          分离式结构                          |
| 元素可以是任意类型                         |                           元素外置                           |
| 可以任意添加元素                           |                           动态扩充                           |

##### 11.2.4 顺序表的结构定义

###### 1)一个顺序表的完整信息包括两部分

+ 数据区域,表中元素集合
+ 表头区域,记录表中整体情况信息
  + 元素存储区的容量
  + 已有元素个数两项

###### 2)顺序表结构两种形式

![image-20210504001154707](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210504001154707.png)

###### 3)动态顺序表

当你执行添加数据操作时,Python中的列表自动的去扩容,即换一块更大的存储区域,这就是所谓的动态顺序表

列表就是动态顺序表,采用的是分离式结构

##### 11.2.5 顺序表特点

###### 1)优点

+ 逻辑相邻,物理相邻,存储空间紧凑,不必为结点间的逻辑关系而增加额外的存储开销
+ 可随机存储任一元素 O(1)

###### 2)缺点

+ 插入、删除操作需要移动大约表中一半元素,对n较大的顺序表效率低下

#### 11.3 链表

顺序表的构建需要预先知道数据大小来申请连续的存储空间,而在进行扩充时又需要进行数据的搬迁,所以使用起来并不是很灵活

##### 11.3.1 链表概述

链表(linkend list)是一种常见的基础数据结构,是一种线性表,但是不像顺序表一样连续存储数据,而是在每一个节点(数据存储单元)里存放下一个节点的位置信息(地址)

###### 1)结点结构

+ 数据区域,数据元素本身信息
+ 链接区域,直接后继或者直接前驱存储地址

![image-20210504003507580](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210504003507580.png)

###### 2)链表分类

+ 单向链表

  每个结点除包含数据域外,只设置一个链接域,用以指向其后继结点,最后一个节点的链接域则指向一个空值

+ 双向链表

  每个结点除包含数据域外,设置两个链接域,分别用于指向其前驱结点和后继结点

```python
# 单链表类定义

# 构造节点
class Node(object):
    # 初始化
    def __init__(self, elem):
        # data为自定义数据
        self.elem = elem
        # next为下一个结点的地址
        self.next = None
        
# 构造链表
class SingleLinkList():
    # 初始化链表,默认为空
    def __init__(self, node=None):
        self.head = node
        
```

##### 11.3.2 链表的变形和操作

![image-20210504010354390](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/image-20210504010354390.png)

###### 1)初始化化单链表

```python
class Node(object):
    # 初始化
    def __init__(self):
        # 表头head为空
        self.head = None
        
```

###### 2)判断单链表是否为空 O(1)

```python
def isEmpty(self):
    if self.head == None:
        return True
    else:
        return False
    
```

###### 3)头插法添加元素 O(1)

```python
# 创建新结点并存入数据
s = Node(5)

# 把原链接首结点链接存入新结点的链接域next
s.next = self.head

# 修改表头变量,使之指向新的结点
self.head = s

```

###### 4)扫描指针和遍历单链表 O(n)

单链表的特点是每个结点只保存其直接后继的地址,在已知单链表的head首地址情况下,如果要访问到单链表中的所有结点,需要一个扫描游标

```python
p = self.head
while p is not None:
    print(p.elem)
    p.next
    
```

###### 5)单链表表长 O(n)

```python
def length(self):
    p = self.head
    count = 0
    while p is not None:
        count += 1
        p = p.next
        
    return count

```

###### 6)按序号查找元素 O(n)

在链表中,即使知道被访问结点的序号i,也不能像顺序表中那样直接按序号i访问结点,而只能从链表的head出发,顺链接域逐个向下搜索,直到搜索到第i个结点为止

基本思路,借助扫描指针,从第一个结点开始扫描,判断当前结点是否是第i个,如果是,返回此节点地址,否则继续向后查找,知道找到或者链表结束

```python
def searchpos(self, pos):
    p = self.head
    count = 1
    if pos < i:
        return None
    else:
        while p is not None and count != pos:
            p = p.next
            count += 1
        # 查找成功返回p,查找失败返回空
        return p
    
```

###### 7)按值查找 O(n)

```python
def searchelem(self, elem):
    p = self.head
    while p is not None and p.elem != elem:
        p = p.next
    if p.elem == elem:
        reutrn p
    elif p is None:
        return None
    
```

###### 8)尾插法添加元素 O(n)

```python
def append(self, elem):
    p = self.head
    while p.next is not None:
        p = p.next
    # 生成结点,传值elem
    s = Node(elem)
    # 修改链接
    p.next = s
    
```

###### 9)在指定位置插入元素 O(n)

```python
def insert(self, pos, elem):
    p = self.head
    count = 0
    if pos >= self.length():
        return None
    while count < pos:
        p = p.next
        count += 1
    s = Node(elem)
    s.next = p.next
    p.next = s
       
```

###### 10)按值删除元素 O(n)

```Python
def remove(self, elem):
    p = self.head
    
    # 删除的是第一个结点需要单独处理
    if p.elem == elem:
        self.head = p.next
    else:   
    	while p is not None and p.elem != elem:
            # 记录p前驱结点
        	prep = p
            # p指针后移
        	p = p.next
        # 找到elem后,修改链接域
        pre.next = p.next
        
    return p
        
```

###### 11)合集

```python
# 定义结点
class Node(object):
    
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个结点的地址
        self.next = None

# 定义链表
class singleLinkList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        # 判断链表是否为空
        return self.head is None

    def length(self):
        # 链表长度
        curs = self.head
        coun = 0
        while curs is not None:
            coun += 1
            curs = curs.next
        return coun

    def items(self):
        # 遍历链表
        curs = self.head
        while curs is not None:
            yield curs.item
            curs = curs.next

    def add(self, item):
        # 向链表头部添加元素
        node = Node(item)
        # 新结点指针指向原头部的结点
        node.next = self.head
        # 头部结点指针修改为新的结点
        self.head = node

    def append(self, item):
        # 尾部添加元素
        node = Node(item)
        # 判断是否为空链表
        if self.isEmpty():
            self.head = node
        # 不是空链表则找到尾部,将next结点指向新的结点
        else:
            curs = self.head
            while curs.next is not None:
                curs = curs.next
            curs.next = node

    def insert(self, index, item):
        # 指定位置插入元素
        if index <= 0:
            self.add(item)
        # 指定位置超过尾部,尾部插入
        elif index > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            curs = self.head
            for i in range(index - 1):
                curs = curs.next
            node.next = curs.next
            curs.next = node

    def remove(self, item):
        # 删除结点
        curs = self.head
        pren = None
        while curs is not None:
            if curs.item == item:
                if not pren:
                    self.head = curs.next
                else:
                    pren.next = curs.next
                
                return True

            else:
                pren = curs
                curs = curs.next

    def find(self, item):
        # 查找元素是否存在
        return item in self.items()

if __name__ == '__main__':
    # 创建链表
    linklist = singleLinkList()
    # 创建结点
    node1 = Node(1)
    print(node1)  #<__main__.Node object at 0x00000258F5511BE0>
    node2 = Node(2)
    print(node2)  #<__main__.Node object at 0x00000258F5511C50>

    # 将结点添加到链表
    linklist.head = node1
    # 将第一个结点的next指针指向下一结点
    node1.next = node2

    # 访问第一个结点的数据
    print(linklist.head.item)       #1
    # 访问第二个结点的数据
    print(linklist.head.next.item)  #2
    
    # 向链表尾部添加数据
    for i in [3, 4, 5]:
        linklist.append(i)
    print(linklist.items())  #<generator object singleLinkList.items at 0x00000258F548B5E8>

    # 向头部添加数据
    linklist.add(0)
    print(linklist.items())  #<generator object singleLinkList.items at 0x00000258F548B5E8>

    # 遍历链表数据
    for i in linklist.items():
        print(i)  #0, 1, 2, 3, 4, 5

    # 链表数据插入数据
    linklist.insert(2, 1.5)
    print(linklist.items())  #<generator object singleLinkList.items at 0x00000258F548B5E8>
    for i in linklist.items():
        print(i)  #0, 1, 1.5, 2, 3, 4, 5

    # 删除链表数据
    linklist.remove(0)
    print(linklist.items())  #<generator object singleLinkList.items at 0x00000258F548B5E8>
    for i in linklist.items():
        print(i)  #1, 1.5, 2, 3, 4, 5
    
    # 查找链表数据
    print(linklist.find(3))  #True

```

##### 11.3.3 单链表特点

==它是一种动态结构,整个内存空间为多个链表共用(空间可以是连续或者不连续)==
不需要预先分配空间
链接域占用额外的存储空间
不能随机存取(不可通过地址运算计算某个元素位置),查找速度慢(必须从第一个元素开始查找)

##### 11.3.4 链表与顺序表的对比

链表失去了顺序表随机读取的优点,同时链表由于增加了节点的指针域,空间开销比较大,但对存储空间的使用要相对灵活

链表与顺序表的各种操作复杂度如下：

| 操作            | 链表 | 顺序表 |
| --------------- | :--: | :----: |
| 访问            | O(n) |  O(1)  |
| 在头部插入/删除 | O(1) |  O(n)  |
| 在尾部插入/删除 | O(n) |  O(1)  |
| 在中间插入/删除 | O(n) |  O(n)  |

注意:

虽然表面看起来复杂度都是O(n),但是链表和顺序表在插入和删除时都进行的是完全不同的操作
链表的主要耗时操作是遍历查找,删除和插入操作本身的复杂度是 O(1)
顺序表查找很快,主要耗时的操作是拷贝覆盖,因为除了目标元素在尾部的特殊情况,顺序表进行插入和删除时需要对操作位置之后的所有元素进行前后移位操作,只能通过拷贝和覆盖的方法进行

##### 11.3.5 双链表

一种更复杂的链表是双向链表或双面链表,每个节点有两个链接:一个指向前一个节点,当次节点为第一个节点时,指向空值;而另一个指向下一个节点,当次节点为最后一个节点时,指向空值

##### 11.3.6 双链表的实现和操作

```python
# 定义双向链表结点
class Node(object):
    
    def __init__(self, item):
        # 存放元素
        self.item = item
        # next指向下一个结点地址
        self.next = None
        # prev指向上一个结点地址
        self.prev = None
        
# 定义双向链表
class DoubbleLinkList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):

        return self.head is None

    def length(self):
        curs = self.head
        coun = 0
        while curs is not None:
            coun += 1
            curs = curs.next
        
        return coun

    def items(self):
        curs = self.head
        while curs is not None:
            yield curs.item
            curs = curs.next

    # 链表头部添加元素
    def add(self, item):
        node = Node(item)
        # 链表为空
        if self.isEmpty():
            self.head = node
        else:
            # 新结点指针指向原头部结点
            node.next = self.head
            # 原头部prev指向新结点
            self.head.prev = node
            # head指向新结点
            self.head = node

    # 链表尾部添加元素
    def append(self, item):
        node = Node(item)
        # 链表为空
        if self.isEmpty():
            self.head = node
        else:
            curs = self.head
            while curs.next is not None:
                curs = curs.next
            # 新结点上一级指针指向旧的尾部
            node.prev = curs
            # 旧的尾部指向新的结点
            curs.next = node

    # 指定位置插入元素
    def insert(self, index, item):
        if index <= 0:
            self.add(item)
        elif index > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            curs = self.head
            for i in range(index):
                curs = curs.next
            # 新的结点向下指针指向当前结点
            node.next = curs
            # 新的结点向上指针指向当前结点上一结点
            node.prev = curs.prev
            # 当前上一结点向下指针指向node
            curs.prev.next = node
            # 当前结点的向上指针指向新的结点
            curs.prev = node
       
```

#### 11.4 栈和队列

##### 11.4.1 栈

![image-20210508154657925](C:/Users/Admin/AppData/Roaming/Typora/typora-user-images/image-20210508154657925.png)

栈(stack),有些地方成为堆栈,是一种容器,可存入数据元素,访问元素,删除元素,他的特点在于只能允许在容器的一端(称为栈顶端指标top)进行加入数据(top)和输出数据(pop)的运算,没有了位置概念,保证任何时候可以访问、删除的元素都是此前最后存入的那个元素,确定了一种默认的访问顺序

由于栈数据结构只允许在一端就行操作,因而按照后进先出(LIFO，Last In First Out)的原理运作

##### 11.4.2 Python实现栈

```python
class Stack(object):
    
    def __init__(self):
        self.stack = []
    
    # 进栈函数
    def push(self, item):
        self.stack.append(item)
    
    # 出栈函数
    def pop(self):
        return self.stack.pop()
    
    # 取其栈顶
    def gettop(self):
        return self.stack[-1]
    
```

##### 11.4.3 队列

队列(queue)是只允许在一端进行插入操作,而在另一端进行删除操作的线性表

队列是一种先进先出的(First In First Out)的线性表,简称FIFO,允许插入的一端为队尾,允许删除的一端为队头,队列不允许在中间部位进行操作!

假设队列是 q=(a1, a2, ....... , an ),那么a1就是对头元素,而an是队尾元素,这样我们就可以在删除时,总是从a1开始,而插入时,总在队列最后,这也比较符合我们通常生活中的习惯,排在第一个的优先出列,最后来的排在队伍最后

#### 11.5 二叉树和树

#### 11.6 图

#### 11.7 查找

##### 11.7.1 线性查找

线性查找适合无序序列查找元素

```python
# 算法步骤
#   线性查找指按一定的顺序检查数组中每一个元素,直到找到所要寻找的特定值为止

def steepSearch(sequ, item):
    for i in range(len(sequ)):
        if sequ[i] == item:
            return f'元素在{i}号位'
    else:
        return '元素不在序列中'


print(search([1, 2, 3, 4, 5], 4))

```

##### 11.7.2 二分查找

```python
# 算法步骤
#     我们手里有一个长度为n的正序数列,当我们想查找一个数x是否在这个数列当中的时候
#     1)取数列正中间的数mid
#         如果mid和x相等,则找到结果,查找成功返回True
#         如果mid比x大,则x应该在mid的左侧,我们把mid左侧当作一个新的数列li
#         如果mid比x小,则x应该在mid的右侧,我们把mid右侧当作一个新的数列li
#     2)对于新的数列li,进行1的查找工作
#     3)一直重复上面查找,生成新的数列li为空的时候则数列当中没有数x返回False

# 代码实现

# 1)递归方法,每次传入一个新的序列无法确认元素索引位置

def halfSearch(sequ, item):
    # 传来序列每次都是新生成的,如果里面么有发现元素,则是查到尽头也没有找到
    if not sequ:
        return '不在序列之中'

    # 使用//向下取整取序列中间索引
    midinx = len(sequ)//2
    # 如果midinx比item大,则说明元素可能出现在midinx左边,对左边再进行二分查找
    if sequ[midinx] > item:
        return halfSearch(sequ[0:midinx-1], item)
    # 如果midinx比item大,则说明元素可能出现在midinx右边,对右边再进行二分查找
    elif sequ[midinx] < item:
        return halfSearch(sequ[midinx+1:-1], item)
    # 中间元素是要找的元素,返回真
    else:
        return True


print(halfSearch([1, 2, 3, 4, 5], 4))

# 2)非递归方法,对一个序列进行循环查找,可以方便确认元素索引位置

def binarySearch(sequ, item):
    # 最小索引位置的默认值
    mininx = 0
    # 最大索引位置的默认值
    maxinx = len(sequ)-1
    # 循环条件序列中有元素
    while mininx <= maxinx:
        # 使用//向下取整取序列中间索引
        midinx = (mininx+maxinx)//2
        # 如果midinx比item大,则说明元素可能出现在midinx左边,maxinx值为midinx-1
        if sequ[midinx] > item:
            maxinx = midinx - 1
        # 如果midinx比item小,则说明元素可能出现在midinx右边,mininx值为midinx+1
        elif sequ[midinx] < item:
            mininx = midinx + 1
        else:
            return f'元素在{midinx}号位'

    return '不在序列之中'


print(binarySearch([1, 2, 3, 4, 5], 4))

```

###### [二分查找变种](https://www.nowcoder.com/practice/4f470d1d3b734f8aaf2afb014185b395?tpId=188&&tqId=38588&rp=1&ru=/activity/oj&qru=/ta/job-code-high-week/question-ranking)

 给定一个元素有序的(升序)整型数组nums和一个目标值 target,写一个函数搜索nums中的第一个出现的target,如果目标值存在返回下标,否则返回 -1

```python
def search(nums, target):
    mininx = 0
    maxinx = len(nums) - 1
    answ = -1
    while mininx <= maxinx:
        midinx = (mininx + maxinx) // 2
        if nums[midinx] > target:
            maxinx = midinx - 1
        elif nums[midinx] < target:
            mininx = midinx + 1
        else:
            answ = midinx
            maxinx = midinx - 1
            
    return answ

```

#### 11.8 排序

##### 11.8.1 冒泡排序

![在这里插入图片描述](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/20200810193906338.gif)

```python
# 算法步骤
#     1)比较相邻的元素,如果第一个比第二个大,就交换他们两个
#     2)对每一对相邻元素作同样的工作,从开始第一对到结尾的最后一对这步做完后,最后的元素会是最大的数
#     3)针对所有的元素重复以上的步骤,除了最后一个
#     4)持续每次对越来越少的元素重复上面的步骤,直到没有任何一对数字需要比较

# 时间复杂度O(n2)
# 空间复杂度O(1)
# 稳定

# 代码实现

ls = [5, 4, 3, 2, 1]

def bubbleSort(sequ):
    # 每次冒泡确定一个最大值,n个数需要n-1次冒泡
    for i in range(len(sequ)-1):
        # 标志位初始值为False
        flag = False
        # 初始序列中有n个数,两两比较次数为n-1次,每次冒泡确认一个最大值,剩下前n-1个数比较
        for j in range(len(sequ)-1-i):
            # 判断前面的数是否大于后面
            if sequ[j] > sequ[j+1]:
                # 在单次冒泡排序中,如果需要任意两个数交换位置,标志位变文True
                flag = True
                # 大于则交换位置
                sequ[j], sequ[j+1] = sequ[j+1], sequ[j]
        # 在单词冒泡排序中,如果没有任意连个数交互位置,则说明不需要在进行下一轮冒泡排序,直接退出循环
        if flag == False:
            break

    return sequ


print(bubbleSort(ls))

# TODO:
#     sequ[j],sequ[j+1] = sequ[j+1],sequ[j]
#     等价于
#     temp = sequ[j]
#     sequ[j] = sequ[j+1]
#     sequ[j+1] = temp

```

##### 11.8.2 选择排序

![](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/20200811095713349.jpg)

```python
# 算法步骤
#     1)首先在未排序序列中找到最小(大)元素,存放到排序序列的起始位置
#     2)再从剩余未排序元素中继续寻找最小(大)元素,然后放到已排序序列的末尾
#     3)重复第二步,直到所有元素均排序完毕

# 时间复杂度O(n2)
# 空间复杂度O(log2N)-O(n)
# 不稳定

# 代码实现

ls = [5, 4, 3, 2, 1]

def selectSort(sequ):
    # 每次选择一个最小的数排到序列前面,n个数需要n-1次选择排序
    for i in range(len(sequ)-1):
        # 记录初始位,定义为最小数索引
        mininx = i
        # 一次选择排序,从第二个数开始与定义最小索引比较
        for j in range(i+1, len(sequ)):
            # 如果最小索引的值比索引j的值大则交换位置
            if sequ[mininx] > sequ[j]:
                mininx = j
        # i不是最小数是,将i和最小数进行交换
        if mininx != i:
            sequ[i], sequ[mininx] = sequ[mininx], sequ[i]

    return sequ


print(selectSort(ls))

```

##### 11.8.3 插入排序

![在这里插入图片描述](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/20200811114111139.jpg)

```python
# 算法步骤
#     1)从第一个元素开始,该元素可以认为已经被排序
#     2)取出下一个元素,在已经排序的元素序列中从后向前扫描
#     3)如果该元素(已排序)大于新元素,将该元素移到下一位置
#     4)重复步骤3,直到找到已排序的元素小于或者等于新元素的位置
#     5)将新元素插入到该位置后
#     6)重复步骤2-5

# 时间复杂度O(n2)
# 空间复杂度O(1)
# 稳定

# 代码实现

ls = [5, 4, 3, 2, 1]

def insertSort(sequ):
    # 第一个元素可以被认为已经被排序,遍历第一个元素之后的序列
    for i in range(1, len(sequ)):
        # 两数比较需要到sequ[0],即是sequ[i-1],i-1>0,i>=1
        while i > 0:
            # 取出未排序列的第一个元素,在已排元素序列中从后向前扫描
            if sequ[i] < sequ[i-1]:
                # 后面元素小于前面元素(第一次while循环前面元素即为有序序列的最后一位)则交换位置
                sequ[i], sequ[i-1] = sequ[i-1], sequ[i]
                i -= 1
            else:
                # 后面元素大于等于前面元素直接跳出本次循环
                break

    return sequ


print(insertSort(ls))

```

##### 11.8.4 希尔排序(缩小增量排序)

```python
def shellSort(sequ):
    
    step = len(sequ) // 2
    
    while step > 0:
        for i in range(step, len(sequ)):
            while i > 0:
                if sequ[i] < sequ[i-step]:
                    sequ[i], sequ[i-step] = sequ[i-step], sequ[i]
                else:
                    break
        step //= 2
        
    return sequ

```



##### 11.8.5 快速排序

![在这里插入图片描述](https://cdn.jsdelivr.net/gh/chanwanxiang/imageHosting/img/20200811152355953.gif)

```python
# 算法步骤
#     1)随机选取序列中一个值,挨个跟后面的数值作比较
#     2)比该数值小的将放在左序列中,反之则放在右序列
#     3)返回左序列+[随机值]+右序列,左右序列使用递归的方式继续进行排序

# 时间复杂度O(nlog2N)
# 空间复杂度O(nlog2N)
# 不稳定

def fastSort(sequ):
    # 序列元素不超过1个则返回该序列
    if len(sequ) < 2:
        return sequ
    # 随机取数
    base = sequ[0]
    # 比随机取数小的放在左序列
    leftSequ = [x for x in sequ[1:] if x <= base]
    # 比随机取数大的放在右序列
    rigtSequ = [x for x in sequ[1:] if x > base]

    # 左右序列递归方式继续排序
    return fastSort(leftSequ) + tempSequ + fastSort(rigtSequ)


print(fastSort([5, 4, 3, 2, 1]))

```

```python
def partiton(nums, l, r):
    i, j = l, r
    pivot = nums[l]
    while i != j:
        while i < j and nums[j] > pivot:
            j -= 1
        while i < j and nums[i] <= pivot:
            i += 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[i] = nums[i], nums[l]
    
    return i

def fastSort(nums, l, r):
    if l >= r:
        return
    
    base = partition(nums, l, r)
    fastSort(nums, l, base-1)
    fastSort(nums, base+1, r)
    
    
```

#### 11.9 力扣

##### 11.9.1 简单

###### 1)[两数之和](https://leetcode-cn.com/problems/two-sum/)

+ 双重for循环暴力求解 O(n**2)

```python
def twoSum(nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
```

+ for...if... O(n**2)

```python
def twoSum(nums, target):
    for i in nums:
        j = target - i

        stainx = nums.index(i)
        snapls = nums[stainx+1:]

        if j in snapls:
            return [stainx, stainx+snapls.index(j)+1]
        
```

+ dict O(n**n)

```python
def twoSum(nums, target):
    dt = {}
    for i, num in enumerate(nums):
        if target - num  not in dt:
            dt[num] = i
        else:
            return [dt[target-num], i]
            
```

###### 7)[整数反转](https://leetcode-cn.com/problems/reverse-integer/)

```python
def reverse(x):
    num = 0
    a = abs(x)
    
    while a != 0:
        temp = a%10
        num = num*10 + temp
        a = a//10
    
    if x > 0 and num < 2**31-1:
        return num
    if x < 0 and num < 2**31:
        return -num
    else:
        return 0
    
```

###### 9)[回文数](https://leetcode-cn.com/problems/palindrome-number/)

```python
def ispal(x):
    num = 0
    a = abs(x)
    
    while a != 0:
        temp = a%10
        num = num*10 + temp
        a = a//10
        
    if x > 0 and x == num:
        return True
    else:
        return False
    
```

###### 13)[罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

```python
def romantoint(s):
    # 字母数字映射
    numMap = {'I':1, 'V':5, 'X':10, 'L':50
              'C':100, 'D':500, 'M':1000}
    # 返回结果
    result = 0
    for i in range(len(s)):
        if i > 0 and numMap[s[i]] > numMap[s[i-1]]:
            result += numMap[s[i]] - 2*numMap[s[i-1]]
        else:
            result += numMap[s[i]]
            
    return result
    
```

###### 14)[最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

+ whileloop

```python
def maxpre(strs):
    answ = ''
    
    i = 0 
    while True:
        # 利用set去重判断各个字符同一索引是否相同
        sets = set(str[i] for str in strs)
        if len(sets) == 1:
            answ += sets.pop()
            i += 1
        else:
            break
            
    return answ
    
```

+ forloop

```python
def maxpre(strs):
    answ = ''
    
    for i in range(len(strs[0])):
        # 以strs第一个元素作为标杆比较
        for str in strs[1:]:
            if len(str) <= i or strs[0][i] != string[i]:
                break
            else:
                answ += strs[0][i]
    
    return answ

```

###### 20)[有效括号](https://leetcode-cn.com/problems/valid-parentheses/)

+ replace

```python
def isvalid(str):
    while '()' in str or '[]' in str or '{}' in str:
        str = str.replace('()', '')
        str = str.replace('[]', '')
        str = str.replace('{}', '')
        
    return str == ''

```

+ dict

```python
def isvalid(str):
    pile = []
    match = {'(':')', '[':']', '{','}'}
    
    for i in str:
        if i in match:
            pile.append(i)
        elif pile and i == match[pile[-1]]:
            pile.pop()
        else:
            return False
        
    return not pile
            
```

###### 21)[合并有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

```python
def mergeTwoList(l1, l2):
    base = ListNode(0)
    move = base
    while l1 and l2:
        if l1.val <= l2.val:
            move.next = l1
            l1 = l1.next
        else:
            move.next = l2
            l2 = l2.next
        move = move.next
    move.next = l1 if l1 else l2
    
    return base.next

```

###### 26)[删除有序数组重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

```python
def removedup(nums):
    # nums和nums[:]之间的区别,就是引用和副本之间的区别
    for i in nums[:]:
        if nums.count(i) != 1:
            nums.remove(i)
            
    return nums
        
```

###### 27)[移出元素](https://leetcode-cn.com/problems/remove-element/)

+ whileloop

```python
def removeelem(nums, elem):
    i = 0
    while i < len(nums):
        if nums[i] == elem:
            nums.pop(i)
        else:
            i += 1
    
    return nums
    
```

+ while...in...

```python
def removeelem(nums, elem):
    while elem in nums:
        nums.remove(elem)
        
    return nums

```

+ 快慢指针

```python
def removeelem(nums, elem):
    i = 0
    j = len(nums)
    
    while i <= j:
        if nums[i] == elem:
            # 赋值让慢指针继续前驱
            nums[i] = nums[j]
            j -= 1
        else:
            i += 1
            
    return i

```

###### 28) [strStr](https://leetcode-cn.com/problems/implement-strstr/)

+ 切片

```python
def strstr(strs, str):
    if strs == str:
        return 0
    i, j = len(strs), len(str)
    for x in range(i):
        if strs[x:x+j] == str:
            return x
        
    return -1

```

+ find

```python
def strstr(strs, str):
    return strs.find(str)

```

###### 35)[搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

+ 二分法

```python
def searchinsert(nums, elem):
    mininx = 0
    maxinx = len(sequ)-1
    
   	while mininx <= maxinx:
        midinx = (mininx+maxinx)//2
        if nums[midinx] > elem:
            maxinx = midinx-1
        elif nums[midinx] < elem:
            mininx = midinx + 1
        else:
            return midinx
        
    return mininx

```

###### 38)[外观数列](https://leetcode-cn.com/problems/count-and-say/)

```python
def countAndSay(n):
    pre = ''
    cur = '1'
    
    for i in range(1, n):
        pre = cur
        cur = ''
        start = 0
        end = 0
        while end < len(pre):
            while end < len(pre) and pre[start] == pre[end]:
                end += 1
            cur += str(end-start) + pre[start]
            start = end

    return cur

```

###### 66)[加一](https://leetcode-cn.com/problems/plus-one/)

```python
def plusone(nums):
    nums = int(''.join([str(x) for x in nums]))+1
    
    return [int(x) for x in str(nums)]

```

###### 67)[二进制求和](https://leetcode-cn.com/problems/add-binary/)

+ 内置函数

```python
def addbinary(a, b):
    
    return '{0:b}'.format(int(a,2)+int(b,2))

```

###### 69)[x的平方根](https://leetcode-cn.com/problems/sqrtx/)

```python
def mySqrt(x):
    left = 0
    rith = x
    while left <= righ:
        mid = (left + righ) // 2
        if mid**2 > x:
            
        
```



###### 70)[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

```python
def climbStairs(n):
    # 初始化前两个数的值
    a = 1
    b = 2
    
    cur = 0
    wheile cur < n:
        ans = a
        a, b = b, a+b
        cur += 1
        
    return ans

```

###### 206)[反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)

```python
def reverseList(head):
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    return prev

```

###### 345)反转字符串中的元音字母

```python
def reverseVowels(s):
    dt = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    ls = list(s)
    
    l, r = 0, len(s) - 1
    while l < r:
        if ls[l] in dt and ls[r] in dt:
            ls[l], ls[r] = ls[r], ls[l]
            l += 1
            r += 1
        elif ls[l] not in dt:
            l += 1
        elif ls[r] not in dt:
            r -= 1
            
    return ''.join(ls)

```

###### 551)[学生出勤记录I](https://leetcode-cn.com/problems/student-attendance-record-i/)

```python
def checkRecord(s):
    # 正则表达式
    return not re.match('^.*(A.*A|LLL).*$', s)
```

```python
# 模拟 三叶题解
def checkRecord(s):
    coun = 0
    for i in range(len(s)):
        if s[i] == 'A':
            count += 1
            if coun >= 2: return False
        elif s[i] == 'L':
            j = i
            while j < len(s) and s[j] == 'L': j += 1
            if j - i >= 3: return False
            
    return True
```

###### 1221)[分割平衡字符串](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings/)

```python
# 贪心:局部最优解到全局最优解
def banlanceStringSplit(s):
    i, j, answ = 0, 0, 0
    for x in s:
        if x == 'L':
            i += 1
        else:
            j += 1
        if i == j:
            answ += 1
            
    return answ

```

```python
# 数实现简易栈
def banlanceStringSplit(s):
    base, answ = 0, 0
    for x in s:
        if x == 'L':
            base += 1
        else:
            base -= 1
        if not base:
            answ += 1
            
    return answ

```

###### 1480)[一维数组的动态和](https://leetcode-cn.com/problems/running-sum-of-1d-array/)

```python
def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
        
    return nums

```

```python
def runningSum(nums):
    return list(accumulate(nums))

# accumulate函数功能是对传进来的iterable对象逐个进行某个操作,默认是累加,返回的是一个可迭代对象,需要强制类型转换成所需

```



###### 1646)[获取生成数组中的最大值](https://leetcode-cn.com/problems/get-maximum-in-generated-array/)

```python
def getMaxGenerated(n):
    if n < 2:
        return n
    nums = [0] * (n+1)
    nums[0], nums[1] = 0, 1
    answ = 1
    for i in range(2, n+1):
        nums[i] = nums[i//2] + (i%2)*nums[i//2 + 1]
    answ = max(answ, nums[i])
    
    return answ

```

##### 11.9.2 中等

###### 2)[两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
        
class Solution:
    def addTwoNumber(self, l1, l2):
        # 定义个空链表存储返回结果
        ans = ListNode()
        # 链表的连接域游标添加数据
        cur = ans
        # 进位
        carry = 0
        
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x +y
            carry = s//10
            car.next = ListNode(s%10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        #l1 l2都为空后判断是否有进位
        if carry:
                cur.next = ListNode(1)
                
        reutrn ans.next
            
```

###### 3)[无重复字符的最长子串](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/)

+ 利用字典

```python
def lengthOfLongestSubstring(s):
    charDict = dict()
    ini, ans = 0, 0
    
    for cur in range(len(s)):
        if s[cur] in charDict:
            ini = max(charDict[s[cur]], ini)
        else:
            ans = max(ans, cur -ini +1)
            charDict[s[cur]] = cur + 1
            
    return ans

```

+ 滑动窗口双指针

```python
def lengthOfLongestSubstring(s):
    if not s:
        return 0
    
    head = 0
    tail = 1
    answ = 1
    
    while tail < len(s):
        if s[tail] not in s[head:tail]:
            tail += 1
        else:
            answ = max(answ, tail - head)
            head += s[head:tail].index(s[tail]) + 1
        # 用于记录最长子串位于字符串最后一部分 
        answ = max(answ, tail - head)
        
    return answ
        
    
    
```

###### 5)[最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring/)

+ 暴力求解

```python
def longestPalindrome(s)
    if s == s[::-1]:
        return s

    maxl = 1
    answ = s[0]

    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if j - i + 1 > maxl and s[i:j+1] == s[i:j+1][::-1]:
                maxl = j - i + 1
                answ = s[i:j+1]

    return answ

```

+ 中心扩散

遍历每一个索引,以这个索引为中心,利用回文串中心对称的特点,往两边扩散,看最多能扩散多远
==注意回文串的长度可能是奇数,也可能是偶数==

```python
class Solution():
    def longestPalinadrome(self, s):
        if s == s[::-1]:
            return s

        maxl = 1
        answ = s[0]

        for i in range(len(s)):
            oddpal, odmaxl = self.centerSpread(s, i, i)
            evepal, evmaxl = self.centerSpread(s, i, i + 1)
            # 每次找到返回最长回文子串
            temp = oddpal if odmaxl >= evmaxl else evepal
            if len(temp) > len(answ):
                maxl = len(temp)
                answ = temp

        return answ

    def centerSpread(self, s, left, righ):
        # left = righ 时,此时回文中心是当前索引字符,回文字符长度是个奇数
        # left = righ - 1 时,此时回文中心是这两个字符中间的线,回文字符长度是个偶数
        while left >= 0 and righ < len(s) and s[left] == s[righ]:
            left -= 1
            righ += 1
            
        return s[left + 1:righ], righ - left - 1
    
```

###### 6)[Z字形变换](https://leetcode-cn.com/problems/zigzag-conversion/)

+ 遍历写入

```python
def convert(s, numRows): 
    if numRows <= 1:
        return s

    # rowlis存放二维数组
    rowlis = [[] for i in range(numRows)]
    # arrlis将字符写入每一行
    arrlis = [s for i in range(numRows)]

    # 标志用于判断返回和递增递减行数
    flag = 1
    # 行数
    rows = 0
    for i in range(len(s)):
        rowlis[i].append(arrlis[rows][i])
        rows += flag
        # 第一次遍历行数后,之后的第一行和最后一行flag值发生变化
        if rows == 0 or rows == numRows - 1:
            flag *= -1

    answ = []
    for elem in rowlis:
        answ.extend(elem)

    return ''.join(answ)

```

+ 遍历写入强化

```python
def convert(s, numRows):
    if numRows <= 1 or numRows > len(s):
        return s

    flag = 1
    rows = 0
    answ = ['']*numRows

    for i in s:
        answ[rows] += i
        rows += 1
        if rows in [0, numRows-1]:
            flag *= -1

    return ''.join(answ)
    
```

###### 8)[字符串转换整数](https://leetcode-cn.com/problems/string-to-integer-atoi/)

```python
def myAtoi(str):
    str = str.lstrip()
    if len(str):
        return 0

    rslt = 0
    i = 2 if str[0] in ['+', '-'] else 1
    while i < len(str):
        try:
            rslt = int(str[:i])
            i += 1
        except:
            break

    if rslt < -2147483648:
        return -2147483648
    elif rslt > 2147483647:
        return 2147483647
    else:
        return rslt

```

###### 11)[盛最多容量的水](https://leetcode-cn.com/problems/container-with-most-water/)

```python
def maxArea(height):
    lef = 0
    rig = len(height) - 1
    maxArea = 0

    # 底x高,底在减小,高需增加得最大值
    while lef < rig:
        bot = rig - lef
        if height[lef] < height[rig]:
            hgt = height[lef]
            lef += 1
        else:
            hgt = height[rig]
            rig -= 1
        maxArea = max(maxArea, hgt * bot)

    return maxArea
    
```

###### 12)[整数转罗马数字](https://leetcode-cn.com/problems/integer-to-roman/)

```python
def intToRoman(num):
    answ = ''
    mapp = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 
            'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

    para = num
    for k, v in mapp.items():
        flag = para // v
        if flag > 0:
            # 注意乘以flag个数
            answ += k * flag
            para -= v * flag

    return answ

```

###### 15)[三数之和](https://leetcode-cn.com/problems/3sum/)

```python
def threeSum(nums):

    answ = []
    if not nums or len(nums) < 3:
        return answ
    
    nums.sort()
    if nums[0] > 0:
        return answ

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                answ.append(nums[i], nums[j], nums[k])
                # 判断左界右界是否和下一位置重复,去除重复的解
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1
            else:
                k -= 1

        return answ
        
```

###### 16)[最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/)

```python
def threeSumCloseest(nums, target):
    nums.sort()
    # 初始化answ的值
    answ = nums[0] + nums[1] + nums[2]
    
    for i in range(len(nums)-2):
        # 剪枝
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = len(nums) - 1
        while j < k:
            snap = nums[i] + nums[j] + nums[k]
            if abs(target-answ) > abs(target-snap):
                answ = snap
                
            if target > sanp:
                j += 1
            elif target < snap:
                k -= 1
            else:
                return answ
                
    return answ
    
```

###### 17)[电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

```python
def letterCombinations(digits):
    mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    if digits == '':
        return []
    
    # 定义ans是一个空的字符列表,非空列表
    ans = ['']
    for num in digits:
        ans = [i+j for i in ans for j in mapping[num]]

    return ans

```

###### 18)[四数之和](https://leetcode-cn.com/problems/4sum/)

```python
def fourSum(nums, target):
    if not nums or len(nums) < 4:
        return []
    
    nums.sort()
    answ = []
    for a in range(len(nums)-3):
        if a > 0 and nums[a] == nums[a-1]:
            continue
        for b in range(a+1, len(nums)-2):
            if b > a+1 and nums[b] == nums[b-1]:
                continue
            c = b + 1
            d = len(nums) - 1
            while c < d:
                sum = nums[a] + nums[b] + nums[c] + nums[d]
                if sum == target:
                    answ.append([nums[a], nums[b], nums[c], nums[d]])
                    while c < d and nums[c] == nums[c+1]:
                        c += 1
                    while c < d and nums[d] == nums[d-1]:
                        d -= 1
                    c += 1
                    d -= 1
                elif sum < target:
                    c += 1
                else:
                    d -= 1
                    
    return answ

```

###### 165)[比较版本号](https://leetcode-cn.com/problems/compare-version-numbers/)

```python
def compareVersion(version1, version2):
    v1 = version1.split('.')
    v2 = version2.split('.')
    i, j = len(v1), len(v2)
    
    n = max(i, j)
    
    if i < n:
        v1.extend([0]*(n-i))
    if j < n:
        v2.extend([0]*(n-j))
        
    for i in range(n):
        if int(v1[i]) > int(v2[i]):
            return 1
        elif int(v1[i]) > int(v2[i]):
            return -1
        
    return 0

```

###### 394)[字符串解码](https://leetcode-cn.com/problems/decode-string/)

```python
def decodeString(str):
    answ, nums, stack = '', 0, []
    for i in str:
        if i.isdigit():
            nums = nums*10 + int(i)
        elif i =='[':
            stack.append((answ, nums))
            answ, nums = '', 0
        elif i == ']':
            top = stack.pop()
            answ = top[0] + answ*top[1]
        else:
            answ += i
            
    return answ
    
```

###### 692)[前K个高频单词](https://leetcode-cn.com/problems/top-k-frequent-words/)

```python
def topKFrequent(words, k):
    charDict = {}
    for i in words:
        charDict[i] = charDict.get(i, 0) + 1
    # 排序有多个key的话, 可以使用元祖
    answ = sorted(charDict.keys(), key = lambda x:(-charDict[x], x))
    return answ[:k]

```

###### 881)[救生艇](https://leetcode-cn.com/problems/boats-to-save-people/)

```python
def numRescueBoats(people, limit):
    people.sort()
    left, righ, answ = 0, len(people) - 1, 0
    while left <= righ:
        if people[left] + people[righ] <= limit:
            left += 1
        righ -= 1
        answ += 1
        
    return answ

```

###### 1442)[形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

```python
def countTriplets(arr):
    rslt = 0
    for i in range(len(arr)-1):
        answ = arr[i]
        # 找出数组里面连续i,j,k满足arr[i],arr[j],arr[k]异或和为0
        for j in range(i, len(arr)):
            answ ^= arr[j]
            if answ == 0:
                rslt += j -i

    return rslt

```

###### 1447)[找出第K大的异或坐标值](https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/)

```python
def kLargestValue(matrix, k):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i and j:
                matrix[i][j] ^= matrix[i][j-1] ^ matrix[i-1][j] ^ matrix[i-1][j-1]
            elif i:
                matrix[i][0] ^= matrix[i-1][0]
            elif j:
                matrix[0][j] ^= matrix[0][j-1]

    answ = sorted([j for i in matrix for j in i])
    return answ[-k]

```

##### 11.9.3 困难

##### 11.9.4 剑指offe

###### 22)[链表中倒数第k个结点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

```python
def getKthFromEnd(head, k):
    curr, leng = head, 0
    while curr:
        leng += 1
        curr = curr.next
    for i in range(leng - k):
        head = head.next
        
    return head

```

快慢指针

```python
def getKthFromEnd(head, k):
    slow, fast = head, head
    while k > 0:
        fast = fast.next
        k -= 1
    while fast != None:
        fast = fast.next
        slow = slow.next
        
    return slow

```

###### 45)[把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

```python
def minNumber(nums):
    strNum = [str[x] for x in nums]
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if int(strNum[j] + strNum[j+1]) > int(strNum[j+1] + strNum[j]):
                strNum[j], strNum[j+1] = strNum[j+1], strNum[j]
                
    return ''.join(strNum)

```

#### 11.10 算法面试

##### 11.10.1 德科OD

1. 给定一个整型数组,请从数组中选择3个元素组成最小数字并输出(如果数组长度小于三,则选择数组中所有元素来组成最小数字)

```
```

2. 服务之间交换的接口成功率作为服务调用关键质量特征,某个时间段内的接口失败率使用一个数组表示,数组中每个元素都是单位时间内失败率数值,数组中的数值为0-100的整数,给定一个数值(minAverageLost)表示某个时间段内平均失败率容忍值,即平均失败率小于等于minAverageLost,找出数组中最长时间段,如果未找到则直接返回NUL
3. 给定一个正整数序列,再给一个正整数n,求序列中的数相加的和等于n的最长子序列
4. 给定一个正整数数n,找出n=a*b,找出a,b.a,b为素数,没有返回-1

### 十二. 工作项目经历

#### 工作经历

##### 群音信息服务有限公司

智能汽车事业部担任资源开发工程师一职,该项目组的职责为人机交互语音转文字对文字的关键字赋语义操作,是车机开发过程中的一个环节,保证语义接口响应数据的正确性,开发流程为脚本编写,脚本部署,重启服务,BS端平台校验(http的get请求)
个人的工作主要包含两个方面
一是车机导航项目语义需求分析、资源制作、资源自测、缺陷修复
二是项目所有业务的缺陷统筹分发管理,包含与厂商测试部门对接缺陷修复计划、协助组员完成较难缺陷分析等

使用的技术栈包括:git、python、linux、mysql

##### 宇为科技有限公司

测试工程师
测试的目的是通过自动化或者手工测试找到产品与需求的差异性,直接目的是发现缺陷,最终目的是保证产品质量

###### 面签中心(toB)

是一款满足银行人员和贷款客户进行音视频通话及录制的产品,包含web端和App端
web端即是银行坐席,包含登录、面签受理、面签审核、订单详情、数据大屏等模块
App端即是业务员端,包含登录、订单基本信息录入、客户影像证件录入、订单列表、面签列表面签等模块

###### 发券系统(toC)

是一款向C端客户发放优惠券的产品,包含web端后台管理系统和小程序H5端活动页面
发券后台管理系统主要包含项目信息活动页面设置、优惠券管理模块
H5端包含单张领券、一键领券、我的优惠券等模块

在测试过程中首先保证产品和需求的一致性,即功能测试满足要求,同时借助mysql对数据进行增删改查完成测试中某一状态行为的转变以满足业务流程需要,根据查看Linux后台日志、postMan以及charles抓包分析接口以及http请求分析缺陷原因,在发券系统中jenkins + jmeter持续集成接口压力测试

#### 项目经历

##### 个人博客(django)

##### 接口自动化测试(python)

小滴课堂是一个web端教育商城,主要模块包含首页模块、视频列表、用户模块、收藏模块等.

- 编写测试用例脚本完成遍历用例、执行用例、发起请求、断言请求结果、更新结果存储到数据库、邮件发送测试报告.
- jmeter单机接口压力测试.
- 涉及库有json、datetime、openpyxl、pymysql、requests、smtplib、email.mine.multipar
