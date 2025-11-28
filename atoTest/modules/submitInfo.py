import re
import random

from playwright.sync_api import Page
from modules import *
from util.tools import *

elem = {
    'fill': {
        '住宅(详细地址)': '这是测试环境住宅地址',
        '住宅邮编': '310000',
        '电子邮箱': '595366700@qq.com',
        '工作单位名称': '杭州宇为科技有限公司',
        '单位地址(详细地址)': '和瑞科技园T1幢1101',
        '单位电话区号': '0571',
        '单位电话': '85218521',
        '单位邮编': '310001',
        '姓名-1': '测试测试',
        '手机号': '15555308000',
        '联系电话区号': '0571',
        '联系电话': '12341234'
    },
    'select': {
        '自购车状况': '无',
        '单位地址(省) ': '',
        '单位地址(市)': '',
        '单位地址(县)': '',
        '职务': '',
        '与主贷人的关系': ''
    }
}

item = {
    'fill': {
        '车辆价格(元)': '109800',
        '还款人月均总收入(元)': '15000',
        '个人总资产(元)': '10000',
        '其他负债余额(元)': '1000',
        '其他月还款额(元)': '100',
        '贷款金额合计(元)': '30000'
    },
    'select': {
        '品牌名称': '比亚迪',
        '车系名称': '',
        '车型名称': '',
        '车辆类型': ''
    }
}

upload = {
    '车辆登记证书': 'testfile/分期补录/车辆登记证书.png',
    '车辆保险单':'testfile/分期补录/车辆保险单.png',
    '二手车评估报告':'testfile/分期补录/二手车评估报告.png',
    '房产证':'testfile/分期补录/房产证.png'
}


class SubmitInfo(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

    def submitinfo(self, page: Page, username, password, ordernum):
        self.loginPageSaveCookies(page, username, password)
        page.get_by_role("link", name="信息中心").click()
        page.locator(".menu-type").dblclick()
        page.wait_for_timeout(2000)
        page.get_by_role("link", name="订单操作信息").locator('visible=true').click()
        iframe = page.frame_locator("iframe >> nth=1")
        iframe.get_by_placeholder(
            "关键词").type(ordernum, delay=100)
        iframe.get_by_role(
            "button", name="搜索").click()
        page.wait_for_timeout(3000)
        iframe.get_by_role(
            "button", name="编辑").click()
        self.fillinfo(page, elem)
        iframe.get_by_title("进入单位时间").get_by_role("textbox").click()
        iframe.get_by_text("10", exact=True).first.click()
        iframe.get_by_role("button", name="保存").click()
        page.wait_for_timeout(1000)
        iframe.get_by_role(
            "tab", name="车辆分期信息").click()
        page.wait_for_timeout(2000)
        self.fillinfo(page, item)
        iframe.get_by_title(
            "车辆上牌地").get_by_placeholder("请选择").click()
        # page.pause()
        iframe.get_by_role(
            "menuitem", name="河北省").locator("span").click()
        iframe.get_by_role(
            "menuitem", name="石家庄市").locator("span").click()
        iframe.get_by_role(
            "button", name="保存").click()
        # page.pause()
        # page.frame_locator("iframe >> nth=1").get_by_role("button", name="上传影像材料").click()
        iframe.get_by_role('button', name='上传影像材料').click()

        for p, q in upload.items():
            iframe.get_by_role('treeitem', name=re.compile(rf'{p}$')).click()
            with page.expect_file_chooser() as chooser:
                iframe.get_by_role('button', name='点击上传').click()
            chooser.value.set_files(q)
        iframe.get_by_role('button', name='保存').last.click()
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
                q = [e for e in p if containsZh(e)]
                y = random.choices(q)[0]
            iframe.locator('li:visible').filter(has_text=re.compile(rf'^{y}$')).click()
            page.keyboard.press('Tab')
            page.wait_for_timeout(1000)
