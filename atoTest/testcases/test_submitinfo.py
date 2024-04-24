from playwright.sync_api import Page
from modules.submitInfo import SubmitInfo


def test_submitinfo(page: Page):
    si = SubmitInfo(page)
    si.submitinfo(page, 'haax', 'saas2020', 'rl001-240423-003')
