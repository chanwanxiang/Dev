import os
import time
import pytest
from util.tools import absp
from common.logsUtil import logs


# conftest.py 中定义的夹具默认是局部的，只会自动引用到同一目录下的测试文件中


# session级别，全局仅运行一次，autouse=True 自动启用，它会在所有用例之前自动执行
# @pytest.fixture(scope="session", autouse=True)
# def startends():
#     logs.info('------UI测试开始------')
#     yield
#     logs.info('------UI测试结束------')
