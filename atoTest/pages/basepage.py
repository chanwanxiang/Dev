class BasePage:

    def __init__(self, driver):
        self.driver = driver      # 驱动传入构造函数，继承页面类实例化需传入driver

    def open(self, page):         # 打开url：根据传入的page类名，跳转到该页面
        self.driver.get(page.url) # 该页面需要有url属性

    def find_element(self, locator):  # 查找元素简化方法
        return self.driver.find_element(*locator)
