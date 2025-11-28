import allure
import pytest
from common.yamlUtil import YamlUtil
from common.logUtil import logs
from util.tools import caseid


yu = YamlUtil()


@allure.feature('2. 商品列表接口')
class TestOrderinfo(object):

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/orderinfo/goodlist.yaml'))
    @allure.story(next(caseid)+'商品列表')
    def test_goodlist(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)


if __name__ == '__main__':
    pytest.main(['--reruns=2', '-m "maoyan"'])
