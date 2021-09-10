# 语法:对象名.属性名

class Animal():
    def sleep(self):
        print('sleep')
        print(self)

cat = Animal()

# 类外面添加对象属性
cat.weight = 20

# 类外面获取对象属性
print(f'猫儿的体重是{cat.weight}')