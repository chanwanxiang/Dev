from selenium.webdriver.common.by import By
from pages.basepage import BasePage

class LoginPage(BasePage):
	"""
	定义登录页面：
	- 页面地址
	- 页面元素定位器
	- 页面元素事件
	"""

	url = r"https://yuyinshi.yuuwei.com/#/fvpage/login"

	username_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/form/div[1]/div/div/input')
	password_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/form/div[2]/div/div/input')
	submit_locator = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/form/div[3]/div/button')  # ..表示父节点
	# agree_locator = (By.CSS_SELECTOR, "input[type=checkbox]")

	def submit(self):
	    """
	    点击登录按钮 
	    """
	    self.find_element(self.submit_locator).click()
		
	def username(self, username):
	    """
	    输入用户名
	    """
	    self.driver.find_element(*self.username_locator).send_keys(username)

	def password(self, password):
	    """
	    输入密码
	    """
	    self.driver.find_element(*self.password_locator).send_keys(password)

	def login(self, username, password):
	    """
	    输入用户名密码登录
	    """
	    self.username(username)
	    self.password(password)
	    self.submit()
