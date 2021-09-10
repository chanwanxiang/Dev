# 通用的装饰器

# 1. 装饰带有参数函数

# def decorator(func):
#     # 使用装饰器装饰已有函数的时候,内部函数的类型和要装饰的已有函数的类型保持一致
#     def inner(x, y):
#         print('正在执行加法运算')
#         func(x, y)

#     return inner


# @decorator
# def addNum(x, y):
#     result = x+y
#     print('rlt', result)


# addNum(1, 2)


# 2. 装饰带有参数和返回值函数

# def decorator(func):
#     # 使用装饰器装饰已有函数的时候,内部函数的类型和要装饰的已有函数的类型保持一致
#     def inner(x, y):
#         print('正在执行加法运算')
#         rlt = func(x, y)
#         return rlt

#     return inner


# @decorator
# def addNum(x, y):
#     return x+y


# print(addNum(1, 2))


# 3. 装饰带有不定长参数的返回值的函数

# TODO:该装饰器可以装饰所有通用函数,无参函数元祖和字典均为空
def decorator(func):
    # 使用装饰器装饰已有函数的时候,内部函数的类型和要装饰的已有函数的类型保持一致
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


# TODO:
# if __name__ == '__main__':
#     x = (1,2)
#     print(*x)  # 1 2 *元祖表示对元祖进行拆包
#     y = {'name':'mars'}
#     print(**y) # TypeError: 'name' is an invalid keyword argument for print()