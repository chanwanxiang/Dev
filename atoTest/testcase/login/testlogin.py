import allure
from pages import instancepage
from playwright.sync_api import Page, expect, Browser


@allure.step('登录测试')
def testlogin(page):
    mypage = instancepage.InstancePage(page)
    mypage.loginpage.login('haax', 'saas2020')
