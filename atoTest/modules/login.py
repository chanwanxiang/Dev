from modules.basepage import BasePage
from playwright.sync_api import expect, Page


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username = self.page.get_by_placeholder('用户名')
        self.password = self.page.get_by_placeholder('密码')

    def login(self, username, password):
        self.page.goto('admin/login/index.html')
        self.username.fill(username)
        self.password.fill(password)
        self.page.get_by_role('button', name='登录').click()
        expect(self.page.get_by_text('信息中心')).to_be_visible()
