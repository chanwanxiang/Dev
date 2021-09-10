# 定义类

class 类名():
	代码
	......

# 类名要满足标识符命名规则,遵守大驼峰命名习惯

# sample
class Animal():
    def sleep(self):
        print('sleep')

# 创建对象,对象又名实例
cat = Animal()

# 输出结果该对象的内存地址<__main__.Animal object at 0x00000242BC0D3E80> 
print(cat)

# cat对象调用实例方法
cat.sleep()

# 创建对象的过程也叫作实例化对象