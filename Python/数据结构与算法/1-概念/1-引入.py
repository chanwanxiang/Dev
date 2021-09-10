# 引入

# 如果 a+b+c=1000,且a^2+b^2=c^2(a,b,c为自然数),求出所有a,b,c可能得组合?

# 枚举法
import time

staTime = time.time()
ls = []
for a in range(1001):
    for b in range(1001):
        for c in range(1001):
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                print(a, b, c)

endTime = time.time()
print('spendTime', endTime-staTime)
print('Finished')

# 运行结果
#     0 500 500
#     200 375 425
#     375 200 425
#     500 0 500
#     spendTime 145.12375593185425
#     Finished

# 算法概念
#     算法是独立存在的一种解决问题的方法和思想

# 算法的五大特性
#     1. 输入:算法具有0个或者多个输入
#     2. 输出:算法至少有1个或多个输出
#     3. 有穷性:算法在有限的步骤之后会自动结束而不会无限循环,并且每一个步骤可以在可接受的时间完成
#     4. 确定性:算法中的每一步都有确定含义,不会出现二义性
#     5. 可行性:算法的每一步都是可行的,也就是说每一步都能够执行有限的次数完成
