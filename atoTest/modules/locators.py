from playwright.sync_api import expect, Page

import re


class Locators:

    def __init__(self) -> None:
        pass

    def elemNextelem(self,  page: Page, elemtype):
        return self.page.locator(f'xpath=/following::{elemtype}[position()=1]')
    
    def elemAncestordiv(self, elem: Union[str, Locator]):
        if isinstance(elem, Locators):
            return  elem
        else:
            elemRex = re.compile(f"^\\s")
