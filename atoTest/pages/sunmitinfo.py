import re
import random
from util.tools import absp
from playwright.sync_api import Page
from pages.basepage import BasePage

# 定义 containsChinese 函数，解决未定义名称问题
def containsChinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]')
    return bool(pattern.search(text))

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
                # 拆分长字符串，解决行过长问题
                xpath = (
                    f"//label[text()='{i}']"
                    "/following::input[position()=1]"
                )
                iframe.locator(xpath).fill(j)
            else:
                # 拆分长字符串，解决行过长问题
                xpath = (
                    f"//label[text()='{info[0]}']"
                    "/following::input[position()=1]"
                )
                iframe.locator(xpath).nth(info[1]).fill(j)

        for x, y in item['select'].items():
            # 拆分长字符串，解决行过长问题
            xpath = (
                f"//label[text()='{x}']"
                "/following::input[position()=1]"
            )
            iframe.locator(xpath).click()
            page.wait_for_timeout(1000)
            if not y:
                p = iframe.locator('li:visible').all_inner_texts()
                q = [e for e in p if containsChinese(e)]
                y = random.choices(q)[0]
            # 拆分长字符串，解决行过长问题
            regex = re.compile(rf'^{y}$')
            iframe.locator('li:visible').filter(has_text=regex).click()
            page.keyboard.press('Tab')
            page.wait_for_timeout(1000)
            