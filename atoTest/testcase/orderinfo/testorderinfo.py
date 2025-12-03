from testcase import *


@allure.feature('2. 订单模块')
@allure.story('搜索可录入的订单')
def testorderinfo(logginedpage: Page):
    with allure.step('1. 初始化订单页'):
        mypage = instancepage.InstancePage(logginedpage)
    with allure.step('2. 搜索订单编号'):
        mypage.orderinfopage.orderinfo('rl001-241224-001')
        mypage.page.wait_for_timeout(3000)
    with allure.step('3. 断言'):
        expect(mypage.page.get_by_text('车贷管理系统')).to_be_visible(timeout=5000)
        # 附加截图
        mypage.page.screenshot(path=absp('report/screenshot/orderinfo.png'))
        allure.attach.file(
            name='搜索成功截图',
            attachment_type=allure.attachment_type.PNG,
            source=absp('report/screenshot/orderinfo.png'))
