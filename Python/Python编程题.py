## 编写一个程序，它将找到所有这些数字，可被7整除，但不是5的倍数，2000年至3200(包括在内)。得到的数字应按逗号分隔的顺序打印在一行上。

# ls = [str(x) for x in range(2000,3201) if x%5 != 0 and x%7 == 0]
# print(','.join(ls))

## 编写一个可以计算给定数的阶乘的程序。结果应该以逗号分隔的顺序打印在一行上。假设向程序提供以下输入:8,则输出为:40320

# def fact(x):
#     if x == 1:
#         return 1
#     return x*fact(x-1)

# print(fact(8))

## 使用给定的整数n，编写一个程序生成一个包含(i, i*i)的字典，该字典包含1到n之间的整数(两者都包含)。然后程序应该打印字典。假设向程序提供以下输入:8则输出为:{1:1，2:4，3:9，4:16，5:25，6:36，,7:49，8:64}

# def dct(x):
#     dt = {}
#     for x in range(1,x+1):
#         dt[x] = x*x
#     return dt

# print(dct(8))

## 问题:编写一个程序，该程序接受控制台以逗号分隔的数字序列，并生成包含每个数字的列表和元组。假设向程序提供以下输入:34岁,67年,55岁,33岁,12日,98年则输出为:['34'， '67'， '55'， '33'， '12'， '98']('34'， '67'， '55'， '33'， '12'， '98')

# import re

# str = input('请输入序列值->')
# ls = re.findall('[0-9]+',str)
# print(ls)
# print(tuple(ls))

## 问题:定义一个至少有两个方法的类: getString:从控制台输入获取字符串 printString:打印大写母的字符串。还请包含简单的测试函数来测试类方法。提示:使用_init__方法构造一些参数

# class InputString():
#     def __init__(self):
#         self.str = str

#     def getString(self):
#         self.str = input('请输入字符串->')

#     def printString(self):
#         print(self.str.upper())

# if __name__ == '__main__':
#     iS = InputString()
#     iS.getString()
#     iS.printString()

## 编写一个程序，根据给定的公式计算并打印值:Q=sqrt{[(2*C*D)/H]}。以下是C和H的固定值:C是50。H是30。D是一个变量，它的值应该以逗号分隔的序列输入到程序中。
## 例子假设程序的输入序列是逗号分隔的:100，150，180
## 程序输出为:18，22，24
## 提示:如果接收到的输出是小数，则应四舍五入到其最近的值(例如，如果接收到的输出是26.0，则应打印为26)。在为问题提供输入数据的情况下，应该假设它是控制台输入。

# import math

# seq = map(int,input('请输入序列值->').split(','))

# print(seq)

# for x in seq:
#     print(x)
#     print(round(math.sqrt((2*50*x)/30)))

## 编写一个程序，以2位数字，X,Y作为输入，生成一个二维数组。数组的第i行和第j列中的元素值应该是i*j。
## 注意:i= 0,1 . .,X - 1;    j = 0, 1,­Y-1。
## 例子假设程序有以下输入:3、5
## 则程序输出为:[[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]
## 提示:注意:如果要为问题提供输入数据，应该假设它是一个控制台输入，以逗号分隔。

# x,y = map(int,input('请输入两位数字->').split(','))

# for i in range(x):
#     ls = []
#     for j in range(y):
#         ls.append(i*j)
#     print(ls)

## 编写一个程序，接受逗号分隔的单词序列作为输入，按字母顺序排序后按逗号分隔的序列打印单词。假设向程序提供以下输入:
## without,hello,bag,world
## 则输出为:
## bag,hello,without,world
## 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

# seq = input('请输入字符串->').split(',')
# seq.sort()
# print(','.join(seq))

## 问题:编写一个程序，接受一行序列作为输入，并在将句子中的所有字符大写后打印行。
## 假设向程序提供以下输入:
## Hello world
## Practice makes perfect
## 则输出为:
## HELLO WORLD
## PRACTICE MAKES PERFECT
## 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。

# seqs = []

# while True:
#     seq = input('请输入序列->')
#     if seq:
#         seqs.append(seq.upper())
#     else:
#         break

# for seq in seqs:
#     print(seq)

## 编写一个程序，接受一系列空格分隔的单词作为输入，并在删除所有重复的单词并按字母数字排序后打印这些单词。
## 假设向程序提供以下输入:
## hello world and practice makes perfect and hello world again
## 则输出为:
## again and hello makes perfect practice world
## 提示:在为问题提供输入数据的情况下，应该假设它是控制台输入。
## 我们使用set容器自动删除重复的数据，然后使用sort()对数据进行排序。

# seq = input('请输入序列->').split(' ')
# ls = list(dict.fromkeys(seq))
# ls.sort()
# print(','.join(ls))

## 编写一个程序，接受一系列逗号分隔的4位二进制数作为输入，然后检查它们是否可被5整除。 可被5整除的数字将以逗号分隔的顺序打印。
## 例：
## 0100,0011,1010,1001
## 那么输出应该是：
## 1010
## 注意：假设数据由控制台输入。

# seq = input('请输入序列->').split(',')

# ls = []
# for x in seq:
#     if int(x,2)%5 == 0:
#         ls.append(x)
    
# print(','.join(ls))

## 题：编写一个程序，它将找到1000到3000之间的所有这些数字（均包括在内），这样数字的每个数字都是偶数。
## 获得的数字应以逗号分隔的顺序打印在一行上。

# ls =map(str,[x for x in range(1000,3001) if int(str(x)[0])%2 == 0 and int(str(x)[1])%2 == 0 and int(str(x)[2])%2 == 0 and int(str(x)[3])%2 == 0])

# print(list(ls))

## 编写一个接受句子并计算字母和数字的程序。假设为程序提供了以下输入：
## Hello world! 123
## 然后，输出应该是：
## 字母10
## 数字3

# import re

# str = input('请输入字符串->')
# dt = dict.fromkeys(['char','number'],0)

# print(dt)

# for x in str:
#     if re.findall('[a-z]|[A-Z]',x):
#         dt['char'] += 1
#     elif re.findall('[0-9]',x):
#         dt['number'] += 1
# print('字母{}'.format(dt['char']))
# print('数字{}'.format(dt['number']))

## 编写一个接受句子的程序，并计算大写字母和小写字母的数量。
## 假设为程序提供了以下输入：
## Hello world!
## 然后，输出应该是：
## 大写实例 1
## 小写实例 9

# import re

# str = input('请输入字符串->')

# dt = dict.fromkeys(['Uchar','Lchar'],0)

# for i in str:
#     # 判断字母大小写也可使用方法 i.isupper() and i.islower()
#     if re.findall('[A-Z]',i):
#         dt['Uchar'] += 1
#     elif re.findall('[a-z]',i):
#         dt['Lchar'] += 1

# print('大写实例 {}'.format(dt['Uchar']))
# print('小写实例 {}'.format(dt['Lchar']))

## 编写一个程序，计算a + aa + aaa + aaaa的值，给定的数字作为a的值。假设为程序提供了以下输入：
## 9     然后，输出应该是： 11106

# i = input('请输入个数字->')

# sum = 0

# for j in range(1,5):
#     sum += int(i*j)

# print(sum)

## 使用列表推导来对列表中的每个奇数。 该列表由一系列逗号分隔的数字输入。
## 假设为程序提供了以下输入：
## 1,2,3,4,5,6,7,8,9
## 然后，输出应该是：
## 1,3,5,7,9

## 方法一 python函数式编程
# seq = map(int,input('请输入序列->').split(','))

# seqfil = map(str,filter(lambda x : x%2!=0,seq))

# print(','.join(seqfil))

## 方法二 列表推导式
# seq = input('请输入序列->').split(',')

# seqfil = [x for x in seq if int(x)%2 != 0]

# print(','.join(seqfil))

## 编写一个程序，根据控制台输入的事务日志计算银行帐户的净金额。 事务日志格式如下所示：
## D 100
## W 200

## D表示存款，而W表示提款。
## 假设为程序提供了以下输入：
## D 300
## D 300
## W 200
## D 100
## 然后，输出应该是：
## 500

# sum = 0

# while True:
#     seq = input('请输入序列->').split(' ')
#     if seq[0] == 'D':
#         sum += int(seq[1])
#     elif seq[0] == 'W':
#         sum -= int(seq[1])
#     else:
#         print(sum)
#         break

## 网站要求用户输入用户名和密码进行注册。编写程序以检查用户输入的密码的有效性。
## 以下是检查密码的标准：
## 1. [a-z]之间至少有1个字母
## 2. [0-9]之间至少有1个数字
## 1. [A-Z]之间至少有一个字母
## 3. [$＃@]中至少有1个字符
## 4.最短交易密码长度：6
## 5.交易密码的最大长度：12
## 您的程序应接受一系列逗号分隔的密码，并将根据上述标准进行检查。将打印符合条件的密码，每个密码用逗号分隔。
## 例：如果以下密码作为程序的输入：

## ABd1234@1,a F1#,2w3E*,2We3345
## 然后，程序的输出应该是：
## ABd1234@1

# import re

# pwd = input('请输入密码序列->').split(',')

# ls = []

# for i in pwd:
#     # break语句在循环结构中终止本层循环体,从而提前结束本层循环
#     # continue语句是跳过本次循环体中余下尚未执行的语句,立即进行下一次的循环条件判定,仅仅结束本次循环
#     if len(i) < 6 or len(i) >12:
#         continue
#     elif not re.search('[a-z]',i):
#         continue
#     elif not re.search('[A-Z]',i):
#         continue
#     elif not re.search('[0-9]',i):
#         continue
#     elif not re.search('[$＃@]',i):
#         continue
#     # \s表示空白,包括空格换行TAB缩进等所有的空白
#     elif re.search('\s',i):
#         continue
#     else:
#         pass
#     ls.append(i)

# print(','.join(ls))

## 您需要编写一个程序，按升序对（名称，年龄，高度）元组进行排序，其中name是字符串，age和height是数字。 元组由控制台输入。 排序标准是：
## 1：根据名称排序;
## 2：然后根据年龄排序;
## 3：然后按分数排序。
## 优先级是name> age>得分。
## 如果给出以下元组作为程序的输入：
## Tom,19,80
## John,20,90
## Jony,17,91
## Jony,17,93
## Json,21,85
## 然后，程序的输出应该是：
## [（'John'，'20'，'90'），（'Jony'，'17'，'91'），（'Jony'，'17'，'93'），（'Json'，'21 '，'85'），（'Tom'，'19'，'80'）]

# ls = []

# while True:
#     seq = input('请输入序列->')
#     if seq:
#         ls.append(tuple(seq.split(',')))
#     else:
#         break

# newls = sorted(ls,key=lambda x : x[0])
# print(newls)

# 使用生成器定义一个类，该生成器可以在给定范围0和n之间迭代可被7整除的数字。
# 提示：考虑使用yield。

# def getNum(n):
#     for i in range(n+1):
#         if i % 7 == 0:
#             yield i

# for j in getNum(100):
#     print(j)

## 机器人从原点（0,0）开始在平面中移动。 机器人可以通过给定的步骤向上，向下，向左和向右移动。 机器人运动的痕迹如下所示：
## UP 5
## DOWN 3
## LETF 3
## RIGHT 2
## 方向之后的数字是步骤。 请编写一个程序来计算一系列运动和原点之后距当前位置的距离。如果距离是浮点数，则只打印最接近的整数。
## 例：如果给出以下元组作为程序的输入：
## UP 5
## DOWN 3
## LETF 3
## RIGHT 2
## 然后，程序的输出应该是：2

# import math

# oriadr = [0,0]

# while True:
#     s = input('请输入轨迹->')

#     if not s:
#         break
    
#     x,y = s.split(' ')
#     dir = x  #方向
#     stp = int(y)  #位移
#     if dir == 'LEFT':
#         oriadr[0] -= stp
#     elif dir == 'RIGHT':
#         oriadr[0] += stp
#     elif dir == 'UP':
#         oriadr[1] += stp
#     elif dir == 'DOWN':
#         oriadr[1] -= stp

# print(round(math.sqrt(oriadr[0]**2+oriadr[1]**2)))

## 编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
## 假设为程序提供了以下输入：

## New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

## 然后，输出应该是：

## 2:2
## 3.:1
## 3?:1
## New:1
## Python:5
## Read:1
## and:1
## between:1
## choosing:1
## or:2
## to:1

# seq = input('请输入序列->').split(' ')

# dt = {}

# ## 方法一
# # for i in seq:
# #     if i not in dt.keys():
# #         dt[i] = 1
# #     else:
# #         dt[i] += 1

# ## 方法二
# for i in seq:
#     dt[i] = dt.get(i,0)+1

# ndt = sorted(dt.items(),key = lambda x:x[0])

# for x,y in ndt:
#     print(f'{x}:{y}')
