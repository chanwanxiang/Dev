# 需求
#     存储数据位置:文件(student.data)
#         加载文件数据
#         修改数据后保存到文件
#     存储数据形式:列表存储学员对象

#     系统功能
#         添加学员
#         删除学员
#         修改学员
#         查询学员信息
#         显示保存所有学员信息
#         保存学员信息

# 管理系统框架
# 需求
#     系统功能循环使用,用户输入不同功能序号执行不同功能
# 步骤
#     定义程序入口函数
#         加载文件数据
#         显示功能菜单
#         用户输入不同功能序号
#         根据用户输入序号执行不同功能
#     定义系统功能函数,添加、删除学员等

from student import *

class mangerSystem():
    def __init__(self):
        # 存储学员数据所用列表
        self.stulist = []

    # 一. 程序入口函数,启动程序后执行的函数
    def run(self):
        # 1. 加载学员信息
        self.loadStu()

        while True:
            # 2. 显示功能菜单
            self.showMenu()

            # 3. 用户输入功能序号
            menuNum = int(input('输入您的功能序号->'))

            # 4. 根据用户输入执行不同功能
            if menuNum == 1:
                # 添加学员
                self.addStu()

            elif menuNum == 2:
                # 删除学员
                self.delStu()

            elif menuNum == 3:
                # 修改学员信息
                self.modifyStu()

            elif menuNum == 4:
                # 查询学员信息
                self.searchStu()

            elif menuNum == 5:
                # 显示所有学员信息
                self.showStu()

            elif menuNum == 6:
                # 保存学员信息
                self.saveStu()

            elif menuNum == 7:
                # 退出系统
                break

    # 二. 系统功能函数
    # 2.1 显示功能菜单
    @staticmethod
    def showMenu():
        print('请选择如下功能:')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')
        
    # 2.2 添加学员
    def addStu(self):
        print('addStu')
        # 1. 用户输入姓名,性别,手机号
        name = input('请输入您的姓名->')
        sex = input('请输入您的性别->')
        phone = input('请输入您的手机号码->')

        # 2. 创建学员对象
        newstu = Stundet(name,sex,phone)

        # 3. 将该对象添加到学员列表
        self.stulist.append(newstu)
        print(self.stulist)
        print(newstu)

    # 2.3 删除学员
    def delStu(self):
        print('delStu')
        # 1. 用户输入学员姓名
        delName = input('请您输入删除学员姓名->')
        
        # 2. 遍历学员信息列表
        for i in self.stulist:
            if i.name == delName:
                self.stulist.remove(i)
                break
        else:
            print('No Message')
        print(self.stulist)
            
    # 2.4 修改学员信息
    def modifyStu(self):
        print('modifystu')
        # 1. 用户输入需要修改用户姓名
        modifyName = input('请您输入需要修改学员姓名->')

        # 2. 遍历学员信息列表
        for i in self.stulist:
            if i.name == modifyName:
                i.name = input('请输入新的学员姓名->')
                i.sex = input('请输入新的学员性别->')
                i.phone = input('请输入新的学员手机号->')
                print(f'修改后的学员姓名为{i.name},性别为{i.sex},电话{i.phone}')
                break
        else:
            print('No Message')

    # 2.5 查询学员信息
    def searchStu(self):
        print('searchstu')
        # 1. 用户输入查询学员姓名
        searchName = input('请您输入需要查询学员姓名->')

        # 2. 遍历学员信息列表
        for i in self.stulist:
            if i.name == searchName:
                print(i)
        else:
            print('No Message')
            
    # 2.6 显示所有学员信息
    def showStu(self):
        print('showstu')
        # 1. 打印表头
        A,B,C = 'NAME','SEX','PHONE'
        print(f'{A:15} | {B:15} | {C:15}')
 
        # 2. 打印学员信息
        for i in self.stulist:
            print(f'{i.name:15} | {i.sex:15} | {i.phone:15}')
    
    # 2.7 保存学员信息
    def saveStu(self):
        print('savestu')
        # 1. 打开文件
        f = open('stuinfo.data','w')

        # 2. 写入数据
        # 注意1 文件写入的数据不能是学员对象的内存地址,需要把学员数据转换成列表字典数据在做存储
        newlist = [i.__dict__ for i in self.stulist]
        # [{'name': 'wxchans', 'sex': 'male', 'phone': '12345'}]
        print(newlist)
        # 注意2 文件内数据要求数据类型为字符串类型,故需要先转换数据类型为字符串才能文件写入数据
        f.write(str(newlist))

        # 3. 关闭文件
        f.close()

    # 2.8 加载学员信息
    def loadStu(self):
        print('loadstu')
        # 1. 打开文件
        # 尝试以'r'模式打开数据文件,文件存在(没有异常)则打开文件
        try:
            f = open('stuinfo.data','r')
        except:
            f = open('stuinfo.data','w')

        # 2. 读取数据,文件读取出的数据是字符串还原列表类型:[{}] 转换 [学员对象]
        else:
            data = f.read()  #返回从字符串中读取的字节,返回值类型是字符串
            print(data)
            print(type(data))  #<class 'str'>
            newlist = eval(data)  #eval() 函数用来执行一个字符串表达式,并返回表达式的值,此处是将字符串类型转换为list类型
            print(newlist)
            print(type(newlist))  #<class 'list'>
            self.stulist = [Stundet(i['name'],i['sex'],i['phone']) for i in newlist]

        # 3. 关闭文件
        finally:
            f.close()