import os
import pytest
from common.logUtil import logs
from conf.setting import DIR_PATH
from common.yamlUtil import YamlUtil

yu = YamlUtil()


@pytest.fixture(scope="session", autouse=True)
def clearextra():
    yu.clearextractYaml()


@pytest.fixture(scope="session", autouse=True)
def startends():
    logs.info('------接口测试开始------')
    yield
    logs.info('------接口测试结束------')


@pytest.fixture(scope="session", autouse=True)
def login():
    params = yu.rdYaml(os.path.join(DIR_PATH, 'testcase', 'login', 'login.yaml'))
    yu.dealYaml(*params[0])