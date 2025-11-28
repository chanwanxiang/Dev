import re
import random
from util.tools import absp
from playwright.sync_api import Page
from pages.basepage import BasePage


class SubmitInfo(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.centerinfo = page.get_by_role('link:visible', name="信息中心")
        self.menu = page.locator('.menu-type:visible')
        self.dealorder = page.get_by_role('link:visible', name="订单操作信息")

    def submitinfo(self, page: Page, username, password, ordernum):
        self.loginWithCookies(page, username, password)
        self.centerinfo.click()
        self.menu.dblclick()
        self.dealorder.click()
        ifra = page.frame_locator("iframe >> nth=1")
        ifra.get_by_placeholder('关键词').type(ordernum, delay=100)
        ifra.button('搜索')
        ifra.button('编辑')
        self.fillinfolabel(page, elem)
        iframe.get_by_role(
            "button", name="保存").click()
        page.wait_for_timeout(1000)
        iframe.get_by_role(
            "tab", name="车辆分期信息").click()
        page.wait_for_timeout(2000)
        self.fillinfo(page, item)
        iframe.get_by_title(
            "车辆上牌地").get_by_placeholder("请选择").click()
        iframe.get_by_role(
            "menuitem", name="北京市 ").locator("span").click()
        iframe.get_by_role(
            "menuitem", name="市辖区").locator("span").click()
        iframe.get_by_role(
            "button", name="保存").click()
        page.pause()
        page.wait_for_timeout(500)

    def fillinfo(self, page: Page, item: dict):
        iframe = page.frame_locator("iframe >> nth=1")
        for i, j in item['fill'].items():
            info = i.split('-')
            if len(info) == 1:
                iframe.locator(
                    f"//label[text()='{i}']/following::input[position()=1]").fill(j)
            else:
                iframe.locator(
                    f"//label[text()='{info[0]}']/following::input[position()=1]").nth(info[1]).fill(j)

        for x, y in item['select'].items():
            iframe.locator(
                f"//label[text()='{x}']/following::input[position()=1]").click()
            page.wait_for_timeout(1000)
            if not y:
                p = iframe.locator(
                    'li:visible').all_inner_texts()
                q = [e for e in p if containsChinese(e)]
                y = random.choices(q)[0]

            iframe.locator('li:visible').filter(has_text=re.compile(rf'^{y}$')).click()
            page.keyboard.press('Tab')
            page.wait_for_timeout(1000)
