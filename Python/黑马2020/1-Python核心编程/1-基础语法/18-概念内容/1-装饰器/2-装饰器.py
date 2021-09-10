# 装饰器

# 1. 定义
#     装饰器就是给已有函数增加额外功能的函数,它本质上就是一个闭包函数
#     装饰器的功能特点:
#         1. 不修改已有函数的代码
#         2. 不修改已有函数的调用方式
#         3. 给已有函数增加额外的功能

# 2. 示例代码

# 定义装饰器
def decorator(func):
    def inner():
        # 对已有的函数进行装饰
        print('登录验证完成')
        func()
    return inner

# 如果闭包函数的参数有且只有一个并且是函数类型,那么这个闭包函数称为装饰器


@decorator  # comment = decorator(comment) -> inner
# 装饰器的语法糖写法 @装饰器名称
def comment():
    print('发表评论')

# # 调用装饰器对已有函数进行装饰  comment == inner
# comment = decorator(comment)


# 调用方式不变
comment()
