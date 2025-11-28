from common.rdwtUtil import YamlUtil
from pages.basepage import BasePage


class Login(BasePage):
    def login(self):
        data = YamlUtil().rdYaml('login')
        self.page.goto(data['url'])
        self.page.get_by_placeholder('用户名').fill(data['elem']['username'])
        self.page.get_by_placeholder('密码').fill(data['elem']['password'])
        self.page.get_by_role('button', name='登录').click()


lgin = Login().login()
