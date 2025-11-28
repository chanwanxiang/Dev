import allure
import pytest
from common.yamlUtil import YamlUtil
from common.logUtil import logs
from util.tools import caseid

yu = YamlUtil()


@allure.feature('1. 登录接口')
class TestLogin(object):

    def setup(self):
        logs.info('在每个测试方式执行前都要执行我')

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/login/login.yaml'))
    @allure.story(next(caseid)+'用户名和密码正确登录')
    def test_login(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    # @pytest.mark.parametrize('params', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/login/login.yaml'))
    # @allure.story('用户名和密码错误登录')
    # def testCase02(self, params):
    #     yu.dealYaml(params)


if __name__ == '__main__':
    pytest.main(['--reruns=2', '-m "maoyan"'])
