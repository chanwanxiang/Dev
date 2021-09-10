# 一个类可以创建多个对象,多个对象都调用函数self地址是不相同的

class Animal():
    def sleep(self):
        print('sleep')
        print(self)

cat = Animal()
cat.sleep()  #<__main__.Animal object at 0x000001FB0FA91668>

dog = Animal()
dog.sleep()  #<__main__.Animal object at 0x000001FB0FA91710>