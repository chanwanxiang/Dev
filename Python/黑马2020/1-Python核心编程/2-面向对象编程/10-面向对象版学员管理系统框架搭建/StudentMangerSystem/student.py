# 需求
    # 学员信息包含姓名,性别,手机号
    # 添加__str__方法,方便查看学员对象信息

class Stundet():
    def __init__(self,name,sex,phone):
        self.name = name
        self.sex = sex
        self.phone = phone

    def __str__(self):
        return f'学员姓名{self.name},性别{self.sex},手机号为{self.phone}'

if __name__ == '__main__':
    stu = Stundet('ms','男',12345678910)
    print(stu)