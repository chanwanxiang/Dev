
import os,sys
from time import sleep


sys.path.append('d:\\Dev\\atoTest')
# 导入页面
from pages.login import LoginPage

# 导入BaseCase
from cases.basecase import BaseCase


class TestNewApp(BaseCase):  # 继承BaseCase
	"""
	验证新建应用
	"""

	def test_new_app(self):
		"""
		新建应用
		"""
		# 登录
		user_login = LoginPage(self.driver)
		user_login.open(user_login)        # 跳转到登录页
		user_login.login("admin", "Yuwei@123456")
		sleep(1)

		# 新建应用
		# user_createApp = UdcAppsPage(self.driver)
		# user_createApp.open(user_createApp)  # 跳转到应用管理页
		# user_createApp.new_app_button()
		# user_createApp.new_app_name()
		# user_createApp.new_app_code()
		# user_createApp.new_app_sure()

