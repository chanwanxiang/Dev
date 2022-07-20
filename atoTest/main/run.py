import os
import time
import unittest

def suites():
    # 拼接用例路径
    casePath = os.path.join(os.getcwd(), 'cases')
    # 发现全部测试用例
    discover = unittest.defaultTestLoader.discover(
        casePath, pattern='deed.py')
    return discover


if __name__ == "__main__":
    # 指定测试日志级别
    runner = unittest.TextTestRunner(verbosity=0)
    runner.run(suites())