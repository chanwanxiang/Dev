# 定义装饰器
def decorator(func):
    def inner():
        # 对已有的函数进行装饰
        print('登录验证完成')
        func()
    return inner

# 如果闭包函数的参数有且只有一个并且是函数类型,那么这个闭包函数称为装饰器


@decorator  # comment = decorator(comment)
# 装饰器的语法糖写法 @装饰器名称
def comment():
    print('发表评论')

# # 调用装饰器对已有函数进行装饰  comment == inner
# comment = decorator(comment)
