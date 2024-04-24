import time
from playwright.sync_api import sync_playwright


class BasePage:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False, channel='chrome')
        self.context = self.browser.new_context(viewport={'width': 1920, 'height': 1080})
        self.page = self.context.new_page()

    # 跳转 url 地址
    def navigate(self, url):
        self.page.goto(url)
        time.sleep(1)

    def close(self):
        time.sleep(1)
        self.page.close()
        self.playwright.stop()

    def clickEnter(self, elem):
        self.page.locator(elem).keyboard.press('Enter')

    def clickTab(self):
        self.page.keyboard('Tab')

    def scroll(self, elem):
        self.page.locator(elem).scroll_into_view_if_needed()
        time.sleep(1)

    def screenshot(self, elem, filename):
        self.page.locator(elem).screenshot(path=f'../ishot/{filename}.png')
