from testcase import *


@allure.feature('1. 登录模块')
@allure.story('登录测试')
def testlogin(page):
    with allure.step('1. 初始化登录页'):
        mypage = instancepage.InstancePage(page)
    with allure.step('2. 输入用户名密码'):
        mypage.loginpage.login('haax', 'saas2020')
    with allure.step('3. 断言'):
        expect(page.get_by_text('车贷管理系统')).to_be_visible(timeout=5000)
    with allure.step('4. 保存storage_state复用'):
        page.context.storage_state(path=FILE_PATH['STORAGE_STATE_PATH'] + '/haax.json')
    with allure.step('5. 截图'):
        page.screenshot(path=absp('report/screenshot/login.png'))
        allure.attach.file(
            name='登录成功截图',
            attachment_type=allure.attachment_type.PNG,
            source=absp('report/screenshot/login.png'))
