from playwright.sync_api import Page
from pages import login, orderinfo, submitinfo


# page 集中实例
class InstancePage:

    def __init__(self, page: Page):
        self.page = page
        self.loginpage = login.LoginPage(self.page)
        self.orderinfopage = orderinfo.OrderInfoPage(self.page)
        self.submitinfopage = submitinfo.SubmitInfoPage(self.page)
