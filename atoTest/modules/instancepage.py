from modules import login
from playwright.sync_api import Page

# page 集中实例
class InstancePage(Page):

    def __init__(self, page: Page):
        self.page = page
        self.loginpage = login.LoginPage(Page)
