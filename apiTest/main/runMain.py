import os
import unittest

# os.getcwd()
# 该函数不需要传递参数,它返回当前的目录.需要说明的是,当前目录并不是指脚本所在的目录,而是所运行脚本的目录.

# 定义加载全部测试用例方法


def loadAllTestCase():
    # 拼接用例路径
    casePath = os.path.join(os.getcwd(), 'case')
    # 发现全部测试用例
    discover = unittest.defaultTestLoader.discover(
        casePath, pattern='*Case.py')
    return discover


if __name__ == "__main__":
    # 指定测试日志级别
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(loadAllTestCase())
