from pages.basepage import BasePage
from playwright.sync_api import Page, expect


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
        expect(self.page.get_by_text('车贷管理系统')).to_be_visible(timeout=5000)
        self.page.screenshot(path='login.png')
