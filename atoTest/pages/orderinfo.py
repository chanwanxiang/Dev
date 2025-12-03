from pages import *


class OrderInfoPage(BasePage):

    def __init__(self, page: Page):
        # 子类__init__接收page并传递给父类
        super().__init__(page)
        self.centerinfo = self.page.get_by_text('信息中心')
        self.menutype = self.page.locator('.menu-type')
        self.transorderinfo = self.page.get_by_text('订单操作信息')
        self.ifra = page.frame_locator('iframe >> nth=1')
        self.searchorder = self.ifra.get_by_placeholder('关键词')
        self.searchbutton = self.ifra.get_by_role('button', name='搜索')

    def orderinfo(self, orderno):
        self.centerinfo.click()
        self.menutype.dblclick()
        self.transorderinfo.click()
        self.searchorder.type(orderno, delay=100)
        self.searchbutton.click()
