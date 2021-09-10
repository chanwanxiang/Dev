# self 指的是调用该函数的对象

class Animal():
    def sleep(self):
        print('sleep')
        print(self)

cat = Animal()  
print(cat)  #<__main__.Animal object at 0x00000242BC0D3E80>
cat.sleep()  #<__main__.Animal object at 0x00000242BC0D3E80>

# 由于打印对象和打印self得到的内存地址相同,所以self值得是调用该方法的对象