# 自定义异常

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