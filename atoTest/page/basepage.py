class Basepage:
    def __init__(self, driver):
        self.driver = driver
    
    def open(self, page):
        self.driver.get(page.url)
    
    def find_element(self, locator):
        return self.driver.find_element(*locator)