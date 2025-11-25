import allure
import pytest
from common.yamlUtil import YamlUtil
from common.logUtil import logs

yu = YamlUtil()


@allure.feature('用户相关接口')
class TestUserManger(object):

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/userManger/addUser.yaml'))
    @allure.story('新增用户')
    def test_addUser(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/userManger/queryUser.yaml'))
    @allure.story('查询用户')
    def test_queryUser(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/userManger/updateUser.yaml'))
    @allure.story('更新用户')
    def test_updateUser(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)

    @pytest.mark.parametrize('baseinfo, case', yu.rdYaml('/Users/ivi/Dev/apiTest/testcase/userManger/deleteUser.yaml'))
    @allure.story('删除用户')
    def test_deleteUser(self, baseinfo, case):
        yu.dealYaml(baseinfo, case)


if __name__ == '__main__':
    pytest.main(['--reruns=2', '-m "maoyan"'])
