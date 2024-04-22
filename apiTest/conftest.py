import pytest
from common.yamlUtil import YamlUtil
from common.logUtil import logs

yu = YamlUtil()


@pytest.fixture(scope="session", autouse=True)
def clearextra():
    yu.clearextractYaml()


@pytest.fixture(scope="session", autouse=True)
def startends():
    logs.info('------接口测试开始------')
    yield
    logs.info('------接口测试结束------')