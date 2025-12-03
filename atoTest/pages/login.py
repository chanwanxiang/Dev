from pages import *


class LoginPage(BasePage):

    def __init__(self, page: Page):
        # 子类__init__接收page并传递给父类
        super().__init__(page)
        self.username = self.page.get_by_placeholder('用户名')
        self.password = self.page.get_by_placeholder('密码')

    def login(self, username, password):
        self.page.goto('https://test104.yuuwei.com/admin/login/index.html')
        self.username.fill(username)
        self.password.fill(password)
        self.page.get_by_role('button', name='登录').click()
