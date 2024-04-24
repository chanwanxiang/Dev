import unittest
from time import sleep
from selenium import webdriver

class BaseCase(unittest.TestCase): 
    """
    1. BaseCase继承unittest,unittest的作用是只要执行该类,就会把类中的方法都执行一次
    2. 普通case继承BaseCase,也就有了unittest的执行方式
    3. 普通case继承BaseCase,也就继承了setUp和tearDown方法,所以也能执行
    4. setUp和tearDown主要放和一条用例相关的方法和属性
    """
    def setUp(self) -> None:
        chropath = 'D:\Dev\chromedriver.exe'
        driver1 = webdriver.Chrome(chropath)  # 打开浏览器
        driver1.maximize_window()
        driver1.implicitly_wait(5)
        self.driver = driver1         # 这里设置类属性driver

    def tearDown(self) -> None:
        sleep(1)
        self.driver.quit()            # 关闭浏览器
