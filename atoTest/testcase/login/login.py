from common.rdwtUtil import YamlUtil
from palywright.sync_api import sync_playwright, Page



class Login():

    data = YamlUtil().rdYaml('login')

    def __init__(self):
        self.page = Page

    def login(self, url, username, password):
        self.page.goto(data['url'])
        self.page.get_by_




