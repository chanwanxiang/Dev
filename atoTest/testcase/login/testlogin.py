import allure
from pages import instancepage
from playwright.sync_api import Page, expect



def testlogin(page: Page):
    mypage = instancepage.InstancePage(page)
    mypage.loginpage.login('haax', 'saas2020')
