import os
import time
from util.tools import absp
from playwright.sync_api import sync_playwright, Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.url = ''
        # 初始化 playwright
        # self.playwright = sync_playwright().start()
        # 初始化浏览器
        # self.browser = self.playwright.chromium.launch(headless=False, channel='chrome')
        # 初始化上下文 viewport={'width': 1920, 'height': 1080}
        # self.context = self.browser.new_context(no_viewport=True)
        # 初始化页面
        # self.page = self.context.new_page()

    # cookie登录
    def loginCookies(self, page: Page, username: str, password: str):
        if os.path.exists(absp(f'auth/{username}.json')):
            # self.page.context.clear_cookies()
            # with open(absp(f'auth/{username}.json')) as f:
            #     cookies = f.read()
            # cookies = eval(cookies)
            # self.page.context.add_cookies(cookies)
            self.page.context.storage_state(path=absp(f'auth/{username}.json'))
            self.page.goto('/admin/index/index.html')
        else:
            self.page.context.clear_cookies()
            self.page.goto('/admin/index/index.html')
            self.page.get_by_placeholder("用户名").type(username, delay=300)
            self.page.get_by_placeholder("密码").fill(password)
            self.page.get_by_role("button", name="登录").click()
            cookies = self.page.context.cookies()
            with open(absp(f'auth/{username}.json'), 'w') as f:
                f.write(str(cookies))


    # 跳转 url 地址
    def navigate(self):
        self.page.goto(self.url)
        time.sleep(1)

    def close(self):
        time.sleep(1)
        self.page.close()
        self.playwright.stop()

    def clickEnter(self, elem):
        self.page.locator(elem).keyboard.press('Enter')

    def clickTab(self):
        self.page.keyboard('Tab')

    def fillinfolabel(self, elem:dict):
        if  not isinstance(elem, dict):
            return '类型错误'
        for key, value in elem.items():
            # 处理页面重复 label 值
            if len(key.split('-')) == 1:
                self.page.locator(f"//label[text()='{key}']/following::input[position()=1]").fill(value)
            else:
                self.page.locator(f"//label[text()='{key}']/following::input[position()=1]").nth(key.split('-')[-1]).fill(value)

    def edit(self):
        self.page.get_by_role('button:visible', name='编辑').click()

    def button(self, elem):
        self.page.get_by_role('button:visible', name=elem).click()

    def searchandclick(self):
        self.page.ger_by_role('button:visible', name='搜索').click()
        time.sleep(1)
    def scroll(self, elem):
        self.page.locator(elem).scroll_into_view_if_needed()
        time.sleep(1)

    def screenshot(self, elem, filename):
        self.page.locator(elem).screenshot(path=f'../ishot/{filename}.png')
