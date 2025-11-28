import allure
import pytest
from common.yamlUtil import YamlUtil
from common.logUtil import logs
from util.tools import caseid

yu = YamlUtil()


@allure.feature('3. 智慧物流')
class TestFlow(object):

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/transactionflow/materialinfo.yaml'))
    @allure.story(next(caseid) + '获取物料列表')
    def test_materialinfo(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/transactionflow/creatOrder.yaml'))
    @allure.story(next(caseid) + '创建订单')
    def test_creatOrder(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/transactionflow/receiveOrder.yaml'))
    @allure.story(next(caseid) + '接收订单')
    def test_receiveOrder(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/transactionflow/assign.yaml'))
    @allure.story(next(caseid) + '分配订单')
    def test_assign(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)


if __name__ == '__main__':
    pytest.main(['--reruns=2', '-m "maoyan"'])
