from pages import *

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

class SubmitInfoPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.ifra = page.frame_locator('iframe >> nth=1')
        self.save = self.ifra.get_by_role('button', name='保存')
        self.carloaninfo = self.ifra.get_by_role('tab', name='车辆分期信息')
        self.carplate = self.ifra.get_by_title('车辆上牌地').get_by_placeholder('请选择')
        self.city = self.ifra.get_by_role('menuitem', name='北京市').locator('span')
        self.area = self.ifra.get_by_role('menuitem', name='北京市').locator('span').last
        self.uploadinfo = self.ifra.get_by_role('button', name='上传影像材料')


    def submitinfo(self):
        self.fillinfo(elem)
        self.save.click()
        self.page.wait_for_timeout(1000)
        self.carloaninfo.click()
        self.page.wait_for_timeout(1000)
        self.fillinfo(item)
        self.carplate.click()
        # self.city.click()
        # self.area.click()
        self.save.click()
        self.page.wait_for_timeout(1000)
        self.uploadinfo.click()
        self.uploadfile(upload)
        self.page.wait_for_timeout(1000)

    def fillinfo(self, item: dict):
        for i, j in item['fill'].items():
            info = i.split('-')
            if len(info) == 1:
                # 拆分长字符串，解决行过长问题
                xpath = (
                    f"//label[text()='{i}']"
                    "/following::input[position()=1]"
                )
                self.ifra.locator(xpath).fill(j)
            else:
                # 拆分长字符串，解决行过长问题
                xpath = (
                    f"//label[text()='{info[0]}']"
                    "/following::input[position()=1]"
                )
                self.ifra.locator(xpath).nth(info[1]).fill(j)

        for x, y in item['select'].items():
            # 拆分长字符串，解决行过长问题
            xpath = (
                f"//label[text()='{x}']"
                "/following::input[position()=1]"
            )
            self.ifra.locator(xpath).click()
            self.page.wait_for_timeout(1000)
            if not y:
                p = self.ifra.locator('li:visible').all_inner_texts()
                q = [e for e in p if containsZh(e)]
                # 随机取出置空的下拉选择元素
                y = random.choices(q)[0]
            regex = re.compile(rf'^{y}$')
            self.ifra.locator('li:visible').filter(has_text=regex).click()
            self.page.keyboard.press('Tab')
            self.page.wait_for_timeout(1000)

    def uploadfile(self, item: dict):
        for k, v in upload.items():
            self.ifra.get_by_role('treeitem', name=re.compile(rf'{k}$')).click()
            with self.page.expect_file_chooser() as chooser:
                self.ifra.get_by_role('button', name='点击上传').click()
            chooser.value.set_files(v)
        self.ifra.get_by_role('button', name='保存').last.click()
        self.page.wait_for_timeout(500)
