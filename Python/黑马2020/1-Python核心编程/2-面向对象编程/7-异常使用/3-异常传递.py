# 异常传递
#     异常try except写法
#     异常是从外往内传递的

# 需求:
#     1.尝试只读方式打开Test.txt文件,如果文件存在则读取文件内容,文件不存在则提示用户即可
#     2.读取内容要求,尝试循环读取内容,读取过程中如果检测到用户意外终止程序,则except捕获异常并提示用户

import time

try:
    f = open('Test.txt')
    try:
        while True:
            content = f.readline()

            # 如果读取完成退出循环
            if len(content) == 0:
                break

            time.sleep(2)
            print(content)
    except:
        # 如果在读取文件过程中,产生了异常,那么就会捕获到
        # 比如 命令提示符cmd中按下了ctrl+c
        print('程序意外终止读取数据')
    finally:
        f.close()
        print('关闭文件')
except:
    print('没有这个文件')