# 斐波拉契数列的生成

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
        yield rlt


# 创建生成器
f = fibonacci(5)

for i in f:
    print(i)
