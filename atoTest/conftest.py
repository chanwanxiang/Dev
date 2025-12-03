import os
import time
import pytest
from util.tools import absp
from conf.setting import FILE_PATH
from common.logsUtil import logs
from playwright.sync_api import Playwright, Browser, BrowserContext, Page


# session级别，全局仅运行一次，autouse=True 自动启用，它会在所有用例之前自动执行
@pytest.fixture(scope="session", autouse=True)
def startends():
    logs.info('------UI测试开始------')
    yield
    logs.info('------UI测试结束------')


# 会话级：整个测试会话启动一次
@pytest.fixture(scope="session")
def playwright():
    from playwright.sync_api import sync_playwright
    with sync_playwright() as sp:
        yield sp


@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright, pytestconfig):
    return {
        "no_viewport": True,
        # 忽略https报错
        "ignore_https_errors": True,
        **browser_context_args,
    }


# 会话级：登录状态复用创建已登录上下文
@pytest.fixture(scope="session")
def logginedcontext(browser: Browser) -> BrowserContext:
    # 检查是否已存在登录状态文件，存在则直接加载
    if os.path.exists(FILE_PATH['STORAGE_STATE_PATH'] + '/haax.json'):
        context = browser.new_context(
            storage_state=FILE_PATH['STORAGE_STATE_PATH'] + '/haax.json',
            no_viewport=True)
        yield context
        context.close()


# 函数级：每个用例运行前创建已登录的 Page 实例
@pytest.fixture(scope="function")
def logginedpage(logginedcontext: BrowserContext) -> Page:
    page = logginedcontext.new_page()
    page.goto('https://test104.yuuwei.com/')
    yield page
    page.close()
