from pages.basepage import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.username = self.page.get_by_placeholder('用户名')
        self.password = self.page.get_by_placeholder('密码')

    def login(self, username, password):
        self.page.goto('https://test104.yuuwei.com/admin/login/index.html')
        self.username.fill(username)
        self.password.fill(password)
        self.page.get_by_role('button', name='登录').click()
        # expect(self.page.get_by_role('link', name='车贷流程')).to_be_visible()


if __name__ == '__main__':
    lgin = LoginPage().login('haax', 'saas2020')
