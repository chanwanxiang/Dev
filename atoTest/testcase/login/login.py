from common.rdwtUtil import YamlUtil
from palywright.sync_api import sync_playwright, Page



class Login():

    data = YamlUtil().rdYaml('../conf/config.yaml')

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, channel='chrome')
        self.context = self.browser.new_context(viewport={'width': 1920, 'height': 1080})
        self.page = self.context.new_page()


    def login(self, username, password):




