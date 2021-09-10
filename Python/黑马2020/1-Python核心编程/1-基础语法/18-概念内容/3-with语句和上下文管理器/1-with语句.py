# with
#     是python引入的一个新的语法,它是一种上下文管理协议,目的在于从流程图中把try,except和finally关键字和资源分配释放相关代码去除,简化try...except...finally处理流程

# 开始
# try:
#     file = open('sample.txt','r')
#     file.write('ABC')
# except Exception as e:
#     print(e)
# finally:
#     file.close()

# 简化
with open('sample.txt', 'r') as f:
    f.write('ABC')
