import os
import pytest
from common.logUtil import logs
from common.yamlUtil import YamlUtil

yu = YamlUtil()


@pytest.fixture(scope="session", autouse=True)
def clearextra():
    yu.clearextractYaml()
    yield
