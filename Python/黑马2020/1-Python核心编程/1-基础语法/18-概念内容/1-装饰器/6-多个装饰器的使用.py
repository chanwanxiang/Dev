# 多个装饰器的使用

def makeDiv(func):
    print('makeDiv装饰器执行了')
    def inner():
        # 在内部函数对已有函数进行装饰
        result = '<div>' + func() + '</div>'
        return result
    return inner

def makeP(func):
    print('makeP装饰器执行了')
    def inner():
        # 在内部函数对已有函数进行装饰
        result = '<p>' + func() + '</p>'
        return result
    return inner

# 多个装饰器的过程:由内到外的一个装饰过程,先执行内部的装饰器,再执行外部的装饰器
@makeDiv
@makeP
def content():
    return '人生苦短,我用Pyhotn'


# <p>人生苦短,我用Python</p>
print(content())  

# TODO: 输出结果
# makeP装饰器执行了
# makeDiv装饰器执行了
# <div><p>人生苦短,我用Pyhotn</p></div>