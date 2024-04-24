import os, time
from util.tools import absp
from playwright.sync_api import expect, Page



# 类是对象的模板, 对象是类的实例
class BasePage:

    def __init__(self, page: Page) -> None:
        self.page = page
        settimeout = 10000
        self.page.set_default_timeout(settimeout)
        self.page.set_default_navigation_timeout(settimeout)

    def navigate(self, page: Page, path: str):
        if path[0] != '/':
            path = f'/{path}'
        self.page.goto(f'{page.url.split(".com")[0]}.com{path}')

    def loginPageSaveCookies(self, page: Page, username: str, password: str):
        if os.path.exists(absp(f'auth/{username}.txt')) and int(time.time() - os.path.getctime(absp(f'auth/{username}.txt'))) < 200:
            self.page.context.clear_cookies()
            with open(absp(f'auth/{username}.txt')) as f:
                cookies = f.read()
            cookies = eval(cookies)
            self.page.context.add_cookies(cookies)
            self.page.goto('/admin/index/index.html')
            self.page.wait_for_timeout(5000)
        else:
            self.page.context.clear_cookies()
            self.page.goto('/admin/index/index.html')
            self.page.get_by_placeholder("用户名").type(username, delay=300)
            self.page.get_by_placeholder("密码").fill(password)
            self.page.get_by_role("button", name="登录").click()
            # expect(page).to_have_title('车贷管理系统')
            # expect(self.page.get_by_text('车贷管理系统').nth(0)).to_be_visible(timeout=3000)
            # assert self.page.get_by_text('车贷管理系统').count()
            self.page.wait_for_timeout(3000)
            cookies = self.page.context.cookies()
            with open(absp(f'auth/{username}.txt'), 'w') as f:
                f.write(str(cookies))

    def switchtab(self, page: Page, tabname: str):
        self.page.locator("//div[@role='tab']").filter(has_text=tabname).click()


    # 关闭
    def close(self):
        time.sleep(3)
        self.page.close()
        self.playwright.stop()

    # 点击Enter键
    def clickEnter(self, elem):
        self.page.locator(elem).keyboard.press("Enter")