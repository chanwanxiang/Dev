import os
import time
import pytest
from util.tools import absp
from common.logsUtil import logs


# session级别，全局仅运行一次，autouse=True 自动启用，它会在所有用例之前自动执行
@pytest.fixture(scope="session", autouse=True)
def startends():
    logs.info('------UI测试开始------')
    yield
    logs.info('------UI测试结束------')


# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "viewport": {
#             "width": 1920,
#             "height": 1080,
#         }
#     }